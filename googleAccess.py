import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("/Users/changbeankang/Claw_For_Humanity/THSS/thss-scanner-703290cce285.json", scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Spreadsheet by title
spreadsheet = client.open('My New Spreadsheet')

# Select a specific worksheet by index (0-based) or by title
worksheet = spreadsheet.get_worksheet(0)  # Replace 0 with the index of your desired worksheet

# Read data from the worksheet
data = worksheet.get_all_values()
for row in data:
    print(row)

# Update data in the worksheet
worksheet.update('A1', 'New Value')  # Replace 'A1' with the cell you want to update

# Append data to the worksheet
new_row = ['New Data', 'More Data']
worksheet.append_row(new_row)

# Add more operations as needed


# from google.oauth2 import service_account
# from googleapiclient.discovery import build

# # Load credentials from the JSON file you downloaded from the Cloud Console
# credentials = service_account.Credentials.from_service_account_file('/Users/changbeankang/Claw_For_Humanity/THSS/thss-scanner-703290cce285.json', scopes=['https://www.googleapis.com/auth/drive'])

# # Create a Google Drive API service
# drive_service = build('drive', 'v3', credentials=credentials)

# # Define the metadata for the new Google Spreadsheet
# file_metadata = {
#     'name': 'My New Spreadsheet',
#     'mimeType': 'application/vnd.google-apps.spreadsheet'
# }

# # Create the new Google Spreadsheet on Google Drive
# spreadsheet = drive_service.files().create(body=file_metadata).execute()

# # Print the link to the newly created spreadsheet
# print(f"New Spreadsheet created: {spreadsheet['name']} ({spreadsheet['id']})")
