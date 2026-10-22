"""Tests for service Protocol interface compliance.

Verifies that mock implementations satisfy the Protocol contracts.
"""
import pytest
from typing import runtime_checkable

from resume_agent.services.protocols import (
    GoogleDocsService,
    GoogleDriveService,
    GoogleSheetsService,
    EmailService,
    JobScraperService,
    WebSearchService,
    LLMService
)

class MockGoogleDocsService:
    def create_document(self, title: str, folder_id: str) -> str:
        return "mock_doc_id"
    def get_document_text(self, doc_id: str) -> str:
        return "mock text"
    def append_text(self, doc_id: str, text: str) -> None:
        pass

class MockGoogleDriveService:
    def copy_file(self, file_id: str, new_title: str, folder_id: str) -> str:
        return "mock_file_id"
    def move_file(self, file_id: str, folder_id: str) -> None:
        pass

class MockGoogleSheetsService:
    def append_row(self, spreadsheet_id: str, range_name: str, values: list) -> None:
        pass
    def get_values(self, spreadsheet_id: str, range_name: str) -> list:
        return [[]]

class MockEmailService:
    def send_email(self, to: str, subject: str, body: str) -> None:
        pass

class MockJobScraperService:
    def scrape_job(self, url: str) -> str:
        return "mock job description"

class MockWebSearchService:
    def search(self, query: str) -> list:
        return ["mock result"]

class MockLLMService:
    def generate_text(self, prompt: str) -> str:
        return "mock response"
    def analyze_job(self, description: str) -> dict:
        return {}

def test_google_docs_service_mock():
    """Test GoogleDocsService mock"""
    mock = MockGoogleDocsService()
    assert isinstance(mock, GoogleDocsService)

def test_google_drive_service_mock():
    """Test GoogleDriveService mock"""
    mock = MockGoogleDriveService()
    assert isinstance(mock, GoogleDriveService)

def test_google_sheets_service_mock():
    """Test GoogleSheetsService mock"""
    mock = MockGoogleSheetsService()
    assert isinstance(mock, GoogleSheetsService)

def test_email_service_mock():
    """Test EmailService mock"""
    mock = MockEmailService()
    assert isinstance(mock, EmailService)

def test_job_scraper_service_mock():
    """Test JobScraperService mock"""
    mock = MockJobScraperService()
    assert isinstance(mock, JobScraperService)

def test_web_search_service_mock():
    """Test WebSearchService mock"""
    mock = MockWebSearchService()
    assert isinstance(mock, WebSearchService)

def test_llm_service_mock():
    """Test LLMService mock"""
    mock = MockLLMService()
    assert isinstance(mock, LLMService)
