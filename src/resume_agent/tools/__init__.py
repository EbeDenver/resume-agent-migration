"""Abstract service interfaces for external integrations.

All third-party connectors are defined as Protocols so they can be:
- Mocked in tests
- Swapped for local/offline implementations
- Run against real APIs in production
"""
from typing import Protocol, runtime_checkable


@runtime_checkable
class GoogleDocsService(Protocol):
    """Interface for Google Docs operations."""
    
    def create_document(self, title: str, content: str, folder_id: str | None = None, content_format: str = 'text') -> str:
        """Create a Google Doc. Returns the document URL."""
        ...
    
    def read_document(self, document_url_or_id: str) -> str:
        """Read the text content of a Google Doc."""
        ...
    
    def update_document(self, document_url_or_id: str, content: str, content_format: str = 'text') -> None:
        """Replace the content of a Google Doc."""
        ...


@runtime_checkable
class GoogleDriveService(Protocol):
    """Interface for Google Drive operations."""
    
    def create_file_in_folder(self, name: str, mime_type: str, folder_id: str, content: bytes | None = None) -> str:
        """Create a file in a Drive folder. Returns the file ID."""
        ...
    
    def move_to_folder(self, file_id: str, folder_id: str) -> None:
        """Move a file to a specific folder."""
        ...
    
    def get_file_content(self, file_id: str) -> bytes:
        """Download file content."""
        ...


@runtime_checkable
class GoogleSheetsService(Protocol):
    """Interface for Google Sheets operations."""
    
    def read_range(self, spreadsheet_id: str, range_str: str) -> list[list[str]]:
        """Read values from a sheet range."""
        ...
    
    def append_row(self, spreadsheet_id: str, tab_name: str, values: list[str], value_input_option: str = 'USER_ENTERED') -> None:
        """Append a row to a sheet tab."""
        ...


@runtime_checkable
class EmailService(Protocol):
    """Interface for email sending (Gmail or local)."""
    
    def send_email(self, to: str, subject: str, body_html: str) -> None:
        """Send an HTML email."""
        ...


@runtime_checkable
class JobScraperService(Protocol):
    """Interface for job posting scraping."""
    
    def scrape_url(self, url: str) -> dict:
        """Scrape a job posting URL. Returns {title, company, description, ...}."""
        ...
    
    def search_jobs(self, query: str, limit: int = 15) -> list[str]:
        """Search for job posting URLs. Returns list of URLs."""
        ...


@runtime_checkable
class WebSearchService(Protocol):
    """Interface for web search (company research etc)."""
    
    def search(self, query: str, num_results: int = 5) -> list[dict]:
        """Search the web. Returns list of {title, url, snippet}."""
        ...


@runtime_checkable  
class LLMService(Protocol):
    """Interface for LLM calls."""
    
    def generate(self, prompt: str, system_prompt: str = '', temperature: float = 0.3, model: str | None = None) -> str:
        """Generate text from a prompt."""
        ...
    
    def generate_structured(self, prompt: str, response_model: type, system_prompt: str = '', temperature: float = 0.3, model: str | None = None) -> object:
        """Generate structured output parsed into a Pydantic model."""
        ...
