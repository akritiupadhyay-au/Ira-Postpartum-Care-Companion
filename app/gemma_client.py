## Gemma 4 with Multimodal, Thinking, and Function Calling

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

    def generate(self, system_prompt: str, user_prompt: str, max_new_tokens: int = 256,
                 enable_thinking: bool = False, force_json: bool = False) -> str:
        """Standard text generation with optional thinking mode and JSON output."""
        processor, model = self._load()

        messages = []
        if system_prompt and system_prompt.strip():
            messages.append({"role": "system", "content": system_prompt})
        if user_prompt and user_prompt.strip():
            messages.append({"role": "user", "content": user_prompt})
        if not messages:
            messages = [{"role": "user", "content": "Hello"}]

        # Add thinking instruction if enabled
        if enable_thinking:
            messages[-1]["content"] += "\n\nThink step-by-step before answering. Use <think>...</think> tags for your reasoning."

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

        # Extract thinking and answer
        think_pattern = r'<think>(.*?)</think>'
        match = re.search(think_pattern, response, re.DOTALL)

        if match:
            thinking = match.group(1).strip()
            answer = re.sub(think_pattern, '', response, flags=re.DOTALL).strip()
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
                           max_new_tokens: int = 512) -> str:
        """Generate response with image input."""
        processor, model = self._load()

        try:
            image = Image.open(image_path).convert("RGB")
        except Exception as e:
            return f"Image load failed: {e}"

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})

        messages.append({
            "role": "user",
            "content": [
                {"type": "image", "image": image},
                {"type": "text", "text": prompt}
            ]
        })

        full_prompt = processor.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = processor(
            text=full_prompt,
            images=image,
            return_tensors="pt"
        ).to(model.device)

        with torch.no_grad():
            output = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False)

        input_len = inputs["input_ids"].shape[1]
        return processor.decode(output[0][input_len:], skip_special_tokens=True)

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
