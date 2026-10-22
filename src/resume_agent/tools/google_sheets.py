import os
from typing import Optional
from . import GoogleSheetsService


class GoogleSheetsServiceImpl(GoogleSheetsService):
    def __init__(self, credentials_path: str = "credentials.json") -> None:
        self.credentials_path = credentials_path
        self.has_credentials = os.path.exists(credentials_path)

    def read_range(self, spreadsheet_id: str, range_str: str) -> list[list[str]]:
        if not self.has_credentials:
            print(f"[Mock] Reading from sheet {spreadsheet_id} range {range_str}")
            return [["Mock Header 1", "Mock Header 2"], ["Value 1", "Value 2"]]

        try:
            from google.oauth2.credentials import Credentials
            from googleapiclient.discovery import build
            
            creds = Credentials.from_authorized_user_file(self.credentials_path)
            sheets_service = build('sheets', 'v4', credentials=creds)
            
            result = sheets_service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id, range=range_str).execute()
            
            return result.get('values', [])
        except Exception as e:
            print(f"Error reading sheets range: {e}")
            return []

    def append_row(self, spreadsheet_id: str, tab_name: str, values: list[str], value_input_option: str = 'USER_ENTERED') -> None:
        if not self.has_credentials:
            print(f"[Mock] Appending to sheet {spreadsheet_id} tab {tab_name}: {values}")
            return
            
        try:
            from google.oauth2.credentials import Credentials
            from googleapiclient.discovery import build
            
            creds = Credentials.from_authorized_user_file(self.credentials_path)
            sheets_service = build('sheets', 'v4', credentials=creds)
            
            body = {
                'values': [values]
            }
            range_name = f"{tab_name}!A:A"
            
            sheets_service.spreadsheets().values().append(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                insertDataOption='INSERT_ROWS',
                body=body
            ).execute()
        except Exception as e:
            print(f"Error appending row: {e}")
