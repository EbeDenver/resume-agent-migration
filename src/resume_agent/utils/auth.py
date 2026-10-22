"""Google OAuth 2.0 authentication helper.

Manages the OAuth flow for Google Docs, Drive, Sheets, and Gmail APIs.
Stores refresh tokens locally in token.json for reuse across sessions.

Target Google account: ebeDenver@gmail.com
"""
import os.path
from typing import List

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build, Resource

SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive',  
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/gmail.send',
]


def get_credentials(token_path: str, credentials_path: str, scopes: List[str] = SCOPES) -> Credentials:
    """Load or create Google OAuth credentials.
    
    Flow:
    1. Try loading from token_path (cached refresh token)
    2. If expired, refresh automatically
    3. If no token, run interactive OAuth consent flow
    4. Save new token for reuse
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, scopes)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, scopes)
            # prompt="consent" ensures we get a refresh token
            creds = flow.run_local_server(port=0, prompt='consent')
            
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
            
    return creds


def build_service(service_name: str, version: str, credentials: Credentials) -> Resource:
    """Build a Google API service client."""
    return build(service_name, version, credentials=credentials)
