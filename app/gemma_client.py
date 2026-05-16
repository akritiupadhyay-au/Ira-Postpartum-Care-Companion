## Gemma 4 E4B IT - Multimodal (Audio, Image, Video), Thinking, and Function Calling

import os
import json
import re
import torch
from typing import Optional, Dict, List, Any
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

    def _parse_response(self, response: str, processor) -> Dict[str, str]:
        """Parse response using processor.parse_response() for thinking mode."""
        try:
            parsed = processor.parse_response(response)
            return parsed
        except:
            # Fallback if parse fails
            return {"answer": response, "thinking": ""}

    def generate(self, system_prompt: str, user_prompt: str, max_new_tokens: int = 256,
                 enable_thinking: bool = False, force_json: bool = False) -> str:
        """Standard text generation with optional thinking mode and JSON output."""
        processor, model = self._load()

        messages = []

        # To enable thinking, add <|think|> token at start of system prompt
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

        # Add JSON instruction if enabled
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

        # Increase tokens for thinking mode
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

        # Parse Gemma 4 thinking format: <|channel>thought\n[reasoning]<channel|>[answer]
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
            # Extract JSON from response
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                return json.loads(json_match.group(0))
            return json.loads(response)
        except:
            return {"error": "Failed to parse JSON", "raw": response}

    def generate_with_image(self, image_path: str, prompt: str, system_prompt: str = "",
                           max_new_tokens: int = 512, enable_thinking: bool = False) -> str:
        """Generate response with image input (Official Gemma 4 format).

        Args:
            image_path: Path to image file or URL
            prompt: Text prompt for analysis
            system_prompt: System instructions
            max_new_tokens: Max tokens to generate
            enable_thinking: Enable thinking mode with <|think|> token
        """
        processor, model = self._load()

        try:
            # Support both local files and URLs
            if image_path.startswith("http://") or image_path.startswith("https://"):
                image_content = {"type": "image", "url": image_path}
            else:
                # For local files, we need to load and the processor handles it
                image_content = {"type": "image", "image": pil_image}
                image = Image.open(image_path).convert("RGB")
        except Exception as e:
            return f"Image load failed: {e}"

        # Build messages in official Gemma 4 format
        messages = []

        # Add system prompt with thinking token if enabled
        if system_prompt:
            if enable_thinking:
                messages.append({"role": "system", "content": f"<|think|>{system_prompt}"})
            else:
                messages.append({"role": "system", "content": system_prompt})

        # Add user message with image before text (official format)
        messages.append({
            "role": "user",
            "content": [
                image_content,
                {"type": "text", "text": prompt}
            ]
        })

        # Process input using official method
        inputs = processor.apply_chat_template(
            messages,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
            add_generation_prompt=True,
            images=[pil_image] if pil_image is not None else None,
        ).to(model.device)

        input_len = inputs["input_ids"].shape[-1]

        # Generate output
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=0.7,
                do_sample=True
            )

        # Decode with skip_special_tokens=False to keep thinking tokens
        response = processor.decode(outputs[0][input_len:], skip_special_tokens=False)

        # Parse response (extracts thinking if enabled)
        if enable_thinking:
            parsed = self._parse_response(response, processor)
            return parsed.get("answer", response)
        else:
            # Clean response for non-thinking mode
            return processor.decode(outputs[0][input_len:], skip_special_tokens=True)

    def generate_with_image_thinking(self, image_path: str, prompt: str, system_prompt: str = "",
                                     max_new_tokens: int = 1024) -> Dict[str, str]:
        """Generate response with image AND thinking mode enabled (Official format)."""
        processor, model = self._load()

        try:
            # Support both local files and URLs
            if image_path.startswith("http://") or image_path.startswith("https://"):
                image_content = {"type": "image", "url": image_path}
            else:
                image_content = {"type": "image"}
                image = Image.open(image_path).convert("RGB")
        except Exception as e:
            return {"thinking": "", "answer": f"Image load failed: {e}"}

        # Enable thinking by adding <|think|> token to system prompt
        if system_prompt:
            system_prompt = f"<|think|>{system_prompt}"
        else:
            system_prompt = "<|think|>You are a helpful assistant analyzing images."

        messages = []
        messages.append({"role": "system", "content": system_prompt})
        messages.append({
            "role": "user",
            "content": [
                image_content,
                {"type": "text", "text": prompt}
            ]
        })

        # Process input using official method
        inputs = processor.apply_chat_template(
            messages,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
            add_generation_prompt=True,
        ).to(model.device)

        input_len = inputs["input_ids"].shape[-1]

        # Generate output
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=0.7,
                do_sample=True
            )

        # Decode with skip_special_tokens=False to preserve thinking tokens
        response = processor.decode(outputs[0][input_len:], skip_special_tokens=False)

        # Parse response using processor's parse_response method
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
        # Context can be entire health history
        full_prompt = f"Context (analyze all of this):\n\n{context}\n\n---\n\nQuestion: {question}"

        return self.generate("", full_prompt, max_new_tokens=max_new_tokens)

    def generate_with_video(self, video_path: str, prompt: str, system_prompt: str = "",
                           max_new_tokens: int = 512, enable_thinking: bool = False) -> str:
        """Generate response with video input (Official Gemma 4 format).

        Args:
            video_path: Path to video file or URL
            prompt: Text prompt for analysis
            system_prompt: System instructions
            max_new_tokens: Max tokens to generate
            enable_thinking: Enable thinking mode

        Note: Videos up to 60 seconds supported at ~1 fps (60 frames max)
        """
        processor, model = self._load()

        try:
            # Build messages in official Gemma 4 format
            messages = []

            # Add system prompt with thinking token if enabled
            if system_prompt:
                if enable_thinking:
                    messages.append({"role": "system", "content": f"<|think|>{system_prompt}"})
                else:
                    messages.append({"role": "system", "content": system_prompt})

            # Support both local files and URLs
            if video_path.startswith("http://") or video_path.startswith("https://"):
                video_content = {"type": "video", "video": video_path}
            else:
                video_content = {"type": "video", "video": video_path}

            # Add video before text (official format)
            messages.append({
                "role": "user",
                "content": [
                    video_content,
                    {"type": "text", "text": prompt}
                ]
            })

            # Process input using official method
            inputs = processor.apply_chat_template(
                messages,
                tokenize=True,
                return_dict=True,
                return_tensors="pt",
                add_generation_prompt=True,
            ).to(model.device)

            input_len = inputs["input_ids"].shape[-1]

            # Generate output
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    temperature=0.7,
                    do_sample=True
                )

            # Decode response
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
        """Generate response with audio input (Official Gemma 4 E4B format).

        Args:
            audio_path: Path to audio file or URL (.wav format)
            prompt: Text prompt (e.g., transcription instructions)
            system_prompt: System instructions
            max_new_tokens: Max tokens to generate
            enable_thinking: Enable thinking mode

        Note: Audio up to 30 seconds supported

        Example prompts:
        - "Transcribe the following speech segment in Hindi into Hindi text."
        - "Transcribe the following speech in English, then translate to Hindi."
        """
        processor, model = self._load()

        try:
            # Build messages in official Gemma 4 format
            messages = []

            # Add system prompt with thinking token if enabled
            if system_prompt:
                if enable_thinking:
                    messages.append({"role": "system", "content": f"<|think|>{system_prompt}"})
                else:
                    messages.append({"role": "system", "content": system_prompt})

            # Support both local files and URLs
            if audio_path.startswith("http://") or audio_path.startswith("https://"):
                audio_content = {"type": "audio", "audio": audio_path}
            else:
                audio_content = {"type": "audio", "audio": audio_path}

            # Add audio before text (official format)
            messages.append({
                "role": "user",
                "content": [
                    audio_content,
                    {"type": "text", "text": prompt}
                ]
            })

            # Process input using official method
            inputs = processor.apply_chat_template(
                messages,
                tokenize=True,
                return_dict=True,
                return_tensors="pt",
                add_generation_prompt=True,
            ).to(model.device)

            input_len = inputs["input_ids"].shape[-1]

            # Generate output
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    temperature=0.7,
                    do_sample=True
                )

            # Decode response
            if enable_thinking:
                response = processor.decode(outputs[0][input_len:], skip_special_tokens=False)
                parsed = self._parse_response(response, processor)
                return parsed.get("answer", response)
            else:
                return processor.decode(outputs[0][input_len:], skip_special_tokens=True)

        except Exception as e:
            return f"Audio processing failed: {e}"
