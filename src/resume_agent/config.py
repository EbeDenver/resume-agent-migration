"""Configuration management for the Automated Resume Generator.

Loads settings from .env / environment variables (secrets/API keys) and
config.json (persistent resource URLs and preferences). The config.json
mirrors the Gumloop agent's config.json + Google Sheet Config tab.
"""
from functools import lru_cache
from pathlib import Path
import json

from pydantic import BaseModel, Field, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class GoogleConfig(BaseModel):
    """Google Workspace resource configuration."""
    account_email: str = 'ebeDenver@gmail.com'
    job_tracker_url: str = 'https://docs.google.com/spreadsheets/d/1fXSxbi49_JY2HzKXTdPXpAOpJkNqwEcDuK8qp-uh12Y/edit'
    tracker_tab: str = 'Tracker'
    config_tab: str = 'Config'
    drive_root_folder_id: str = '1qUGsgipiDwuwMY-7oyUCtWuWH-GYu1H5'
    generated_resumes_folder_id: str = '1H_yfsR7r86NcuyL0x67ES7X44dSy549h'
    cover_letters_folder_id: str = '1Q4Rkxbw3UYlzGZRUAMYplvNaoM6RgvYA'
    job_analyses_folder_id: str = '1cRIpOeBAjk1P9RPn6Vn6rvvLiycEtln7'
    master_resume_folder_id: str = '1n7TzAJ7aFQsxL2cKKGz4kRQVKpRZJq52'
    resume_instructions_url: str = 'https://docs.google.com/document/d/1csBfzkxUor6K-oHX24_rKcI159BaTahHn3wULBZSIS8/edit'
    cover_letter_instructions_url: str = 'https://docs.google.com/document/d/10bl0RrenXocRyCzGkXh_qNtySJ-JOWWJjpXFO6QzFaE/edit'
    master_resume_url: str | None = None
    job_listings_url: str = 'https://docs.google.com/document/d/1SSn9tpakNaZZL70Z01XX-aYhlmRotS4_muAFET1Tjbo/edit'
    notification_email: str = 'eberolston@yahoo.com'


class LLMConfig(BaseModel):
    """LLM provider configuration."""
    model: str = 'gemini-2.5-pro'
    model_fast: str = 'gemini-2.0-flash'
    temperature: float = 0.3
    max_retries: int = 3


class AppSettings(BaseSettings):
    """Root application settings — merges env vars + config.json."""
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_prefix='',
        extra='ignore',
    )
    
    # API Keys (from .env / env vars)
    google_client_id: str = ''
    google_client_secret: str = ''
    firecrawl_api_key: str = ''
    gemini_api_key: str = ''
    
    # Nested config (from config.json)
    google: GoogleConfig = Field(default_factory=GoogleConfig)
    llm: LLMConfig = Field(default_factory=LLMConfig)
    timezone: str = 'America/Denver'
    
    # Config file path
    config_json_path: Path = Path('config.json')

    @classmethod
    def load(cls, config_json_path: Path | None = None) -> 'AppSettings':
        """Load settings from env + config.json overlay."""
        settings = cls()
        json_path = config_json_path or settings.config_json_path
        if json_path.exists():
            with open(json_path) as f:
                overrides = json.load(f)
            # Apply google config overrides
            if 'google' in overrides:
                settings.google = GoogleConfig(**{**settings.google.model_dump(), **overrides['google']})
            if 'llm' in overrides:
                settings.llm = LLMConfig(**{**settings.llm.model_dump(), **overrides['llm']})
            if 'timezone' in overrides:
                settings.timezone = overrides['timezone']
        return settings

    def save_config_json(self) -> None:
        """Persist current google + llm config to config.json."""
        data = {
            'google': self.google.model_dump(),
            'llm': self.llm.model_dump(),
            'timezone': self.timezone,
        }
        with open(self.config_json_path, 'w') as f:
            json.dump(data, f, indent=2)


@lru_cache()
def get_settings() -> AppSettings:
    """Get cached application settings."""
    return AppSettings.load()
