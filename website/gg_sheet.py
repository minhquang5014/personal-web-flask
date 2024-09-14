import gspread
from google.oauth2.service_account import Credentials
import os
from oauth2client.service_account import ServiceAccountCredentials
# Define the scope
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 
#           'https://www.googleapis.com/auth/drive']

# # Path to your credentials JSON file
# CREDENTIALS_FILE = os.getenv('DATABASE')

# # Authenticate and create a service account client
# credentials = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
# client = gspread.authorize(credentials)

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']

# Reading Credentails from ServiceAccount Keys file
credentials = ServiceAccountCredentials.from_json_keyfile_name("/website/key.json", scope)
# print(CREDENTIALS_FILE)
# intitialize the authorization object            
client = gspread.authorize(credentials)

# Open the Google Sheet by name
sheet_name = 'database'  # Replace with your sheet's name
try:
    sheet = client.open(sheet_name).sheet1
    # print(f"Successfully connected to {sheet_name}")
    
    # Test reading a value
    # cell_value = sheet.cell(1, 1).value  # Reads the value of the first cell (A1)
    # print(f"The value in A1 is: {cell_value}")

    sheet_info = sheet.get_worksheet(0)
    #Get and print all records
    print(sheet_info.get_all_records())

except Exception as e:
    print(f"Unable to connect to the Google Sheet: {e}")

