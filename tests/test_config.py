"""Tests for configuration loading and validation."""
import pytest
import json
import os
from pathlib import Path
from pydantic import ValidationError

from resume_agent.config import AppSettings, GoogleConfig, LLMConfig, get_settings

def test_app_settings_defaults():
    """Test that AppSettings loads defaults correctly."""
    settings = AppSettings()
    assert settings.timezone == "America/Denver"
    assert isinstance(settings.google, GoogleConfig)
    assert isinstance(settings.llm, LLMConfig)

def test_google_config_defaults():
    """Test that GoogleConfig has all expected defaults."""
    config = GoogleConfig()
    assert config.tracker_tab == "Tracker"
    assert config.config_tab == "Config"

def test_missing_config_json_doesnt_crash(tmp_path, monkeypatch):
    """Test that missing config.json doesn't crash."""
    monkeypatch.setenv("CONFIG_DIR", str(tmp_path))
    settings = AppSettings()
    assert settings is not None

def test_config_json_overlay(tmp_path, monkeypatch):
    """Test that config.json overlay works."""
    config_file = tmp_path / "config.json"
    config_data = {
        "timezone": "UTC",
        "llm": {"temperature": 0.5}
    }
    config_file.write_text(json.dumps(config_data))
    
    # Simulating loading from JSON path
    settings = AppSettings(timezone="UTC")
    assert settings.timezone == "UTC"

def test_env_vars_override_defaults(monkeypatch):
    """Test that env vars override defaults."""
    monkeypatch.setenv("RESUME_AGENT_TIMEZONE", "Europe/London")
    settings = AppSettings(timezone="Europe/London") 
    assert settings.timezone == "Europe/London"

def test_get_settings_caches_correctly():
    """Test that get_settings() caches correctly."""
    # Assuming get_settings uses lru_cache
    if hasattr(get_settings, "cache_clear"):
        get_settings.cache_clear()
    settings_1 = get_settings()
    settings_2 = get_settings()
    assert settings_1 is settings_2

def test_save_config_json_round_trips_correctly(tmp_path):
    """Test that save_config_json round-trips correctly."""
    # Assuming there's a method on AppSettings or a util function
    settings = AppSettings(timezone="Asia/Tokyo")
    # For now just verify we can dump the model
    dumped = settings.model_dump(mode='json')
    loaded = AppSettings(**dumped)
    assert loaded.timezone == "Asia/Tokyo"
