import os
import json
from typing import Any, Type, Optional
from pydantic import BaseModel
from . import LLMService


class GeminiLLMService(LLMService):
    def __init__(self, api_key: Optional[str] = None) -> None:
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if self.api_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                self.genai = genai
            except ImportError:
                self.genai = None
        else:
            self.genai = None

    def generate(self, prompt: str, system_prompt: str = '', temperature: float = 0.3, model: str | None = None) -> str:
        if not self.genai:
            return f"[Mock Response for Prompt]: {prompt[:100]}..."
            
        model_name = model or "gemini-1.5-flash"
        generative_model = self.genai.GenerativeModel(
            model_name=model_name,
            system_instruction=system_prompt if system_prompt else None
        )
        response = generative_model.generate_content(
            prompt,
            generation_config=self.genai.types.GenerationConfig(
                temperature=temperature,
            )
        )
        return response.text

    def generate_structured(self, prompt: str, response_model: Type[Any], system_prompt: str = '', temperature: float = 0.3, model: str | None = None) -> Any:
        if not self.genai:
            # Create mock dict based on model fields
            if issubclass(response_model, BaseModel):
                # Basic mock object instantiation for testing offline
                mock_data = {}
                for field_name, field_info in response_model.model_fields.items():
                    if field_info.annotation == str:
                        mock_data[field_name] = f"mock_{field_name}"
                    elif field_info.annotation == int:
                        mock_data[field_name] = 1
                    elif field_info.annotation == float:
                        mock_data[field_name] = 1.0
                    elif field_info.annotation == bool:
                        mock_data[field_name] = True
                    elif field_info.annotation == list[str]:
                        mock_data[field_name] = [f"mock_{field_name}_item"]
                    else:
                        mock_data[field_name] = None
                return response_model(**mock_data)
            return response_model()
            
        model_name = model or "gemini-1.5-flash"
        generative_model = self.genai.GenerativeModel(
            model_name=model_name,
            system_instruction=system_prompt if system_prompt else None
        )
        
        try:
            response = generative_model.generate_content(
                prompt,
                generation_config=self.genai.types.GenerationConfig(
                    temperature=temperature,
                    response_mime_type="application/json",
                    response_schema=response_model
                )
            )
            return response_model.model_validate_json(response.text)
        except Exception:
            # Fallback for parsing issues
            if issubclass(response_model, BaseModel):
                return response_model.model_construct()
            return response_model()
