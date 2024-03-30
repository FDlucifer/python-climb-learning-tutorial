# pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "1KDxlGF2OBGnqWWY2Cw1ojvNUC5euOgEw_8Cuwt3UhkA"

def main():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())
    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        for row in range(2, 8):
            num1 = int(sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!A{row}").execute().get("values")[0][0])
            num2 = int(sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!B{row}").execute().get("values")[0][0])
            calculation_result = num1 + num2
            print(f"processing {num1} + {num2}")

            sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!C{row}",
                                   valueInputOption="USER_ENTERED", body={"values": [[f"{calculation_result}"]]}).execute()
            sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!D{row}",
                                   valueInputOption="USER_ENTERED", body={"values": [["done"]]}).execute()
        # result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Sheet1!A1:C6").execute()
        # values = result.get("values", [])
        # for row in values:
        #     print(row)
    except HttpError as error:
        print(error)

if __name__ == "__main__":
    main()
