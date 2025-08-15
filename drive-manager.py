import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]


def authenticate_user():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def is_valid_folder_id(folder_id, service):
    try:
        service.files().get(fileId=folder_id, fields="id").execute()
        return True
    except HttpError as error:
        if error.resp.status == 404:
            return False
        else:
            raise


def list_files_in_folder(folder_id, service):
    try:
        results = (
            service.files()
            .list(
                pageSize=10,
                fields="nextPageToken, files(id, name)",
                q=f"'{folder_id}' in parents",
            )
            .execute()
        )
        items = results.get("files", [])

        if not items:
            print("No files found.")
            return
        print("Files:")
        for item in items:
            print(f"{item['name']} ({item['id']})")
    except HttpError as error:
        print(f"An error occurred: {error}")


def upload():
    print("Upload functionality is not implemented yet.")


def main():
    creds = authenticate_user()
    if not creds:
        print("Failed to authenticate user.")
        return

    service = build("drive", "v3", credentials=creds)
    folder_id = input("Enter the folder ID: ")

    if not is_valid_folder_id(folder_id, service):
        print("Invalid folder ID.")
        return

    action_option = input("Do you want to View or Upload? ").lower()
    if action_option == "view":
        list_files_in_folder(folder_id, service)
    elif action_option == "upload":
        upload()
    else:
        print("Invalid option. Please choose 'View' or 'Upload'.")


if __name__ == "__main__":
    main()
