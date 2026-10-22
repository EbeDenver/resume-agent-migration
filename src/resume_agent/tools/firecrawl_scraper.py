import os
from typing import Any, Optional
import httpx
from bs4 import BeautifulSoup
from . import JobScraperService


class FirecrawlJobScraper(JobScraperService):
    def __init__(self, api_key: Optional[str] = None) -> None:
        self.api_key = api_key or os.environ.get("FIRECRAWL_API_KEY")
        if self.api_key:
            try:
                from firecrawl import FirecrawlApp
                self.app = FirecrawlApp(api_key=self.api_key)
            except ImportError:
                self.app = None
        else:
            self.app = None

    def scrape_url(self, url: str) -> dict[str, Any]:
        result: dict[str, Any] = {
            "title": "",
            "company": "",
            "description": "",
            "location": "",
            "employment_type": "",
            "raw_html": "",
            "error": None
        }
        
        if self.app:
            try:
                # Use Firecrawl
                scrape_result = self.app.scrape_url(url, params={'formats': ['markdown']})
                if isinstance(scrape_result, dict):
                    # Usually returns metadata + markdown
                    result["description"] = scrape_result.get("markdown", "")
                    metadata = scrape_result.get("metadata", {})
                    result["title"] = metadata.get("title", "")
                    result["company"] = metadata.get("og:site_name", "")
                    result["raw_html"] = scrape_result.get("html", "")
                return result
            except Exception as e:
                # Fallback on error
                result["error"] = f"Firecrawl error: {e}"

        # Fallback to httpx + bs4
        try:
            response = httpx.get(url, timeout=10.0, follow_redirects=True)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            result["raw_html"] = response.text
            result["title"] = soup.title.string if soup.title else ""
            # Extract basic text as description fallback
            for script in soup(["script", "style"]):
                script.extract()
            result["description"] = soup.get_text(separator="\n", strip=True)
            result["error"] = None # Reset error if fallback succeeds
        except Exception as e:
            result["error"] = f"Fallback error: {e}"
            
        return result

    def search_jobs(self, query: str, limit: int = 15) -> list[str]:
        # Provide basic mock/fallback for now. 
        # In a real implementation this might use SERP API or DuckDuckGo.
        return [f"https://example.com/job?q={query.replace(' ', '+')}&id={i}" for i in range(min(3, limit))]
