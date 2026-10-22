import os
from typing import Optional
from . import GoogleDriveService


class GoogleDriveServiceImpl(GoogleDriveService):
    def __init__(self, credentials_path: str = "credentials.json") -> None:
        self.credentials_path = credentials_path
        self.has_credentials = os.path.exists(credentials_path)

    def create_file_in_folder(self, name: str, mime_type: str, folder_id: str, content: bytes | None = None) -> str:
        if not self.has_credentials:
            filename = f"mock_drive_{name}"
            if content:
                with open(filename, "wb") as f:
                    f.write(content)
            else:
                with open(filename, "w") as f:
                    f.write("")
            return f"mock_file_id_{name}"

        try:
            from google.oauth2.credentials import Credentials
            from googleapiclient.discovery import build
            from googleapiclient.http import MediaIoBaseUpload
            import io
            
            creds = Credentials.from_authorized_user_file(self.credentials_path)
            drive_service = build('drive', 'v3', credentials=creds)
            
            file_metadata = {
                'name': name,
                'mimeType': mime_type,
                'parents': [folder_id]
            }
            
            if content:
                media = MediaIoBaseUpload(io.BytesIO(content), mimetype=mime_type, resumable=True)
                file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            else:
                file = drive_service.files().create(body=file_metadata, fields='id').execute()
                
            return file.get('id')
        except Exception as e:
            print(f"Error creating file in drive: {e}")
            return ""

    def move_to_folder(self, file_id: str, folder_id: str) -> None:
        if not self.has_credentials:
            print(f"[Mock] Moved file {file_id} to folder {folder_id}.")
            return
            
        try:
            from google.oauth2.credentials import Credentials
            from googleapiclient.discovery import build
            
            creds = Credentials.from_authorized_user_file(self.credentials_path)
            drive_service = build('drive', 'v3', credentials=creds)
            
            file = drive_service.files().get(fileId=file_id, fields='parents').execute()
            previous_parents = ",".join(file.get('parents', []))
            drive_service.files().update(
                fileId=file_id,
                addParents=folder_id,
                removeParents=previous_parents,
                fields='id, parents'
            ).execute()
        except Exception as e:
            print(f"Error moving file: {e}")

    def get_file_content(self, file_id: str) -> bytes:
        if not self.has_credentials:
            return b"Mock file content"
            
        try:
            from google.oauth2.credentials import Credentials
            from googleapiclient.discovery import build
            import io
            from googleapiclient.http import MediaIoBaseDownload
            
            creds = Credentials.from_authorized_user_file(self.credentials_path)
            drive_service = build('drive', 'v3', credentials=creds)
            
            request = drive_service.files().get_media(fileId=file_id)
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            
            return fh.getvalue()
        except Exception as e:
            print(f"Error downloading file: {e}")
            return b""
