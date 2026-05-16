## Gemma 4 E4B IT - Multimodal (Audio, Image, Video), Thinking, and Function Calling

import os
import json
import re
import torch
from io import BytesIO
from typing import Optional, Dict, List, Any, Union
from PIL import Image
from transformers import (
    AutoProcessor,
    AutoModelForMultimodalLM,
    BitsAndBytesConfig
)

MODEL_PATH = "/kaggle/input/models/google/gemma-4/transformers/gemma-4-e4b-it/1"

class GemmaClient:
    def __init__(self, model_path: str = MODEL_PATH):
        self.model_path      = model_path
        self._processor      = None
        self._model          = None
        self.max_context_length = 128000  # E4B has 128K context

    def _load(self):
        if self._model is not None:
            return self._processor, self._model

        processor = AutoProcessor.from_pretrained(self.model_path)

        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_use_double_quant=True,
        )

        model = AutoModelForMultimodalLM.from_pretrained(
            self.model_path,
            torch_dtype=torch.bfloat16,
            device_map="auto",
            quantization_config=bnb_config,
        )

        self._processor = processor
        self._model     = model

        return processor, model

    def _load_image(self, image_input) -> Image.Image:
        """
        Load a PIL Image from any supported input type:
        - PIL Image object (returned as-is after RGB conversion)
        - Streamlit UploadedFile or any file-like object with .read()
        - Local file path string
        - HTTP/HTTPS URL string
        """
        # ✅ Check PIL Image FIRST — before any hasattr checks
        if isinstance(image_input, Image.Image):
            return image_input.convert("RGB")

        # Local path or URL string
        if isinstance(image_input, str):
            if image_input.startswith("http://") or image_input.startswith("https://"):
                import requests
                r = requests.get(image_input, timeout=10)
                return Image.open(BytesIO(r.content)).convert("RGB")
            else:
                return Image.open(image_input).convert("RGB")

        # File-like object (Streamlit UploadedFile, BytesIO, etc.)
        if hasattr(image_input, "read"):
            return Image.open(BytesIO(image_input.read())).convert("RGB")

        raise ValueError(f"Unsupported image input type: {type(image_input)}")

    def _parse_response(self, response: str, processor) -> Dict[str, str]:
        """Parse response using processor.parse_response() for thinking mode."""
        try:
            parsed = processor.parse_response(response)
            return parsed
        except:
            return {"answer": response, "thinking": ""}

    def generate(self, system_prompt: str, user_prompt: str, max_new_tokens: int = 256,
                 enable_thinking: bool = False, force_json: bool = False) -> str:
        """Standard text generation with optional thinking mode and JSON output."""
        processor, model = self._load()

        messages = []

        if enable_thinking and system_prompt:
            system_prompt = f"<|think|>{system_prompt}"
        elif enable_thinking:
            system_prompt = "<|think|>You are a helpful assistant."

        if system_prompt and system_prompt.strip():
            messages.append({"role": "system", "content": system_prompt})
        if user_prompt and user_prompt.strip():
            messages.append({"role": "user", "content": user_prompt})
        if not messages:
            messages = [{"role": "user", "content": "Hello"}]

        if force_json:
            messages[-1]["content"] += "\n\nRespond with valid JSON only."

        full_prompt = processor.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )

        inputs = processor(
            text=full_prompt,
            return_tensors="pt"
        ).to(model.device)

        if enable_thinking:
            max_new_tokens = min(max_new_tokens * 3, 4000)

        with torch.no_grad():
            output = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=0.6,
                do_sample=True,
            )

        input_len = inputs["input_ids"].shape[1]
        return processor.decode(output[0][input_len:], skip_special_tokens=True)

    def generate_with_thinking(self, system_prompt: str, user_prompt: str,
                               max_new_tokens: int = 256) -> Dict[str, str]:
        """Generate with thinking mode, return both reasoning and answer."""
        response = self.generate(system_prompt, user_prompt, max_new_tokens, enable_thinking=True)

        think_pattern = r'<\|channel>thought\n(.*?)<channel\|>(.*)'
        match = re.search(think_pattern, response, re.DOTALL)

        if match:
            thinking = match.group(1).strip()
            answer = match.group(2).strip()
            return {"thinking": thinking, "answer": answer}

        return {"thinking": "", "answer": response}

    def generate_json(self, system_prompt: str, user_prompt: str) -> Dict[str, Any]:
        """Generate structured JSON output."""
        response = self.generate(system_prompt, user_prompt, max_new_tokens=512, force_json=True)

        try:
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                return json.loads(json_match.group(0))
            return json.loads(response)
        except:
            return {"error": "Failed to parse JSON", "raw": response}

    def generate_with_image(self,
                            image_path: Union[str, Image.Image],
                            prompt: str,
                            system_prompt: str = "",
                            max_new_tokens: int = 512,
                            enable_thinking: bool = False) -> str:
        """Generate response with image input.

        Args:
            image_path: PIL Image, local file path, URL, or Streamlit UploadedFile
            prompt: Text prompt for analysis
            system_prompt: System instructions
            max_new_tokens: Max tokens to generate
            enable_thinking: Enable thinking mode
        """
        processor, model = self._load()

        try:
            image = self._load_image(image_path)
        except Exception as e:
            return f"Image load failed: {e}"

        messages = []

        if system_prompt:
            content = f"<|think|>{system_prompt}" if enable_thinking else system_prompt
            messages.append({"role": "system", "content": content})

        messages.append({
            "role": "user",
            "content": [
                {"type": "image", "image": image},
                {"type": "text", "text": prompt}
            ]
        })

        # Use processor.apply_chat_template (image-aware, not tokenizer)
        inputs = processor.apply_chat_template(
            messages,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
            add_generation_prompt=True,
        ).to(model.device)

        # Fallback if pixel_values missing
        if "pixel_values" not in inputs:
            text_prompt = processor.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
            inputs = processor(
                text=text_prompt,
                images=image,
                return_tensors="pt"
            ).to(model.device)

        if "pixel_values" not in inputs:
            return "Error: image could not be embedded — pixel_values missing."

        input_len = inputs["input_ids"].shape[-1]

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=0.7,
                do_sample=True
            )

        if enable_thinking:
            response = processor.decode(outputs[0][input_len:], skip_special_tokens=False)
            parsed = self._parse_response(response, processor)
            return parsed.get("answer", response)
        else:
            return processor.decode(outputs[0][input_len:], skip_special_tokens=True)

    def generate_with_image_thinking(self,
                                     image_path: Union[str, Image.Image],
                                     prompt: str,
                                     system_prompt: str = "",
                                     max_new_tokens: int = 1024) -> Dict[str, str]:
        """Generate response with image AND thinking mode enabled."""
        processor, model = self._load()

        try:
            image = self._load_image(image_path)
        except Exception as e:
            return {"thinking": "", "answer": f"Image load failed: {e}"}

        if system_prompt:
            system_prompt = f"<|think|>{system_prompt}"
        else:
            system_prompt = "<|think|>You are a helpful assistant analyzing images."

        messages = [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": image},
                    {"type": "text", "text": prompt}
                ]
            }
        ]

        inputs = processor.apply_chat_template(
            messages,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
            add_generation_prompt=True,
        ).to(model.device)

        if "pixel_values" not in inputs:
            text_prompt = processor.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
            inputs = processor(
                text=text_prompt,
                images=image,
                return_tensors="pt"
            ).to(model.device)

        if "pixel_values" not in inputs:
            return {"thinking": "", "answer": "Error: image could not be embedded."}

        input_len = inputs["input_ids"].shape[-1]

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=0.7,
                do_sample=True
            )

        response = processor.decode(outputs[0][input_len:], skip_special_tokens=False)
        parsed = self._parse_response(response, processor)

        return {
            "thinking": parsed.get("thinking", ""),
            "answer": parsed.get("answer", response)
        }

    def generate_with_tools(self, user_prompt: str, tools: List[Dict], system_prompt: str = "") -> Dict:
        """Generate with function calling capability."""
        tool_prompt = f"{system_prompt}\n\nAvailable tools:\n{json.dumps(tools, indent=2)}\n\n"
        tool_prompt += "If you need to use a tool, respond with JSON: {\"tool\": \"tool_name\", \"parameters\": {...}}\n"
        tool_prompt += f"User request: {user_prompt}"

        response = self.generate_json("", tool_prompt)
        return response

    def generate_long_context(self, context: str, question: str, max_new_tokens: int = 512) -> str:
        """Handle long context (up to 128K tokens)."""
        full_prompt = f"Context (analyze all of this):\n\n{context}\n\n---\n\nQuestion: {question}"
        return self.generate("", full_prompt, max_new_tokens=max_new_tokens)

    def generate_with_video(self, video_path: str, prompt: str, system_prompt: str = "",
                            max_new_tokens: int = 512, enable_thinking: bool = False) -> str:
        """Generate response with video input (Official Gemma 4 format)."""
        processor, model = self._load()

        try:
            messages = []

            if system_prompt:
                content = f"<|think|>{system_prompt}" if enable_thinking else system_prompt
                messages.append({"role": "system", "content": content})

            messages.append({
                "role": "user",
                "content": [
                    {"type": "video", "video": video_path},
                    {"type": "text", "text": prompt}
                ]
            })

            text_prompt = processor.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )

            inputs = processor(
                text=text_prompt,
                videos=[video_path],
                return_tensors="pt",
                padding=True
            ).to(model.device)

            input_len = inputs["input_ids"].shape[-1]

            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    temperature=0.7,
                    do_sample=True
                )

            if enable_thinking:
                response = processor.decode(outputs[0][input_len:], skip_special_tokens=False)
                parsed = self._parse_response(response, processor)
                return parsed.get("answer", response)
            else:
                return processor.decode(outputs[0][input_len:], skip_special_tokens=True)

        except Exception as e:
            return f"Video processing failed: {e}"

    def generate_with_audio(self, audio_path: str, prompt: str, system_prompt: str = "",
                            max_new_tokens: int = 512, enable_thinking: bool = False) -> str:
        """Generate response with audio input (Official Gemma 4 E4B format)."""
        processor, model = self._load()

        try:
            messages = []

            if system_prompt:
                content = f"<|think|>{system_prompt}" if enable_thinking else system_prompt
                messages.append({"role": "system", "content": content})

            messages.append({
                "role": "user",
                "content": [
                    {"type": "audio", "audio": audio_path},
                    {"type": "text", "text": prompt}
                ]
            })

            text_prompt = processor.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )

            inputs = processor(
                text=text_prompt,
                audios=[audio_path],
                return_tensors="pt",
                padding=True
            ).to(model.device)

            input_len = inputs["input_ids"].shape[-1]

            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    temperature=0.7,
                    do_sample=True
                )

            if enable_thinking:
                response = processor.decode(outputs[0][input_len:], skip_special_tokens=False)
                parsed = self._parse_response(response, processor)
                return parsed.get("answer", response)
            else:
                return processor.decode(outputs[0][input_len:], skip_special_tokens=True)

        except Exception as e:
            return f"Audio processing failed: {e}"
