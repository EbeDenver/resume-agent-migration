import os
from typing import Optional
from . import GoogleDocsService


class GoogleDocsServiceImpl(GoogleDocsService):
    def __init__(self, credentials_path: str = "credentials.json") -> None:
        self.credentials_path = credentials_path
        self.has_credentials = os.path.exists(credentials_path)

    def create_document(self, title: str, content: str, folder_id: Optional[str] = None, content_format: str = 'text') -> str:
        if not self.has_credentials:
            filename = f"{title.replace(' ', '_')}.md"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"# {title}\n\n{content}")
            return f"file://{os.path.abspath(filename)}"
            
        try:
            from google.oauth2.credentials import Credentials
            from googleapiclient.discovery import build
            
            creds = Credentials.from_authorized_user_file(self.credentials_path)
            docs_service = build('docs', 'v1', credentials=creds)
            drive_service = build('drive', 'v3', credentials=creds)
            
            doc = docs_service.documents().create(body={'title': title}).execute()
            doc_id = doc.get('documentId')
            
            if folder_id:
                file = drive_service.files().get(fileId=doc_id, fields='parents').execute()
                previous_parents = ",".join(file.get('parents', []))
                drive_service.files().update(
                    fileId=doc_id,
                    addParents=folder_id,
                    removeParents=previous_parents,
                    fields='id, parents'
                ).execute()
                
            # Apply styling formatting rules (Navy #17365D headers, light blue #5B9BD5, dark body #1F1F1F)
            # Basic text insertion first
            requests = [
                {
                    'insertText': {
                        'location': {'index': 1},
                        'text': content
                    }
                }
            ]
            
            docs_service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()
            
            return f"https://docs.google.com/document/d/{doc_id}/edit"
            
        except Exception as e:
            return f"Error creating doc: {e}"

    def read_document(self, document_url_or_id: str) -> str:
        if not self.has_credentials:
            return "Mock document content for offline mode."
            
        try:
            from google.oauth2.credentials import Credentials
            from googleapiclient.discovery import build
            
            # Basic ID extraction
            doc_id = document_url_or_id
            if "docs.google.com/document/d/" in document_url_or_id:
                doc_id = document_url_or_id.split("/d/")[1].split("/")[0]
                
            creds = Credentials.from_authorized_user_file(self.credentials_path)
            docs_service = build('docs', 'v1', credentials=creds)
            
            doc = docs_service.documents().get(documentId=doc_id).execute()
            
            text_content = ""
            for element in doc.get('body').get('content'):
                if 'paragraph' in element:
                    for p_element in element.get('paragraph').get('elements'):
                        if 'textRun' in p_element:
                            text_content += p_element.get('textRun').get('content')
            return text_content
        except Exception as e:
            return f"Error reading document: {e}"

    def update_document(self, document_url_or_id: str, content: str, content_format: str = 'text') -> None:
        if not self.has_credentials:
            print(f"[Mock] Updating doc {document_url_or_id} with new content.")
            return

        try:
            from google.oauth2.credentials import Credentials
            from googleapiclient.discovery import build
            
            doc_id = document_url_or_id
            if "docs.google.com/document/d/" in document_url_or_id:
                doc_id = document_url_or_id.split("/d/")[1].split("/")[0]
                
            creds = Credentials.from_authorized_user_file(self.credentials_path)
            docs_service = build('docs', 'v1', credentials=creds)
            
            # Simple replace approach: Clear all then insert.
            doc = docs_service.documents().get(documentId=doc_id).execute()
            end_index = 1
            if 'body' in doc and 'content' in doc['body']:
                last_element = doc['body']['content'][-1]
                end_index = last_element.get('endIndex', 2) - 1
            
            requests = []
            if end_index > 1:
                requests.append({
                    'deleteContentRange': {
                        'range': {
                            'startIndex': 1,
                            'endIndex': end_index
                        }
                    }
                })
                
            requests.append({
                'insertText': {
                    'location': {'index': 1},
                    'text': content
                }
            })
            
            docs_service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()
        except Exception as e:
            print(f"Error updating doc: {e}")
