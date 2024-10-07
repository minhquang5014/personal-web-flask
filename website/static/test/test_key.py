import gspread
from google.oauth2.service_account import Credentials

# Define the scope
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 
          'https://www.googleapis.com/auth/drive']

# Path to your credentials JSON file
CREDENTIALS_FILE = 'website/key.json'

# Authenticate and create a service account client
credentials = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
client = gspread.authorize(credentials)

# Open the Google Sheet by name
sheet_name = 'database'  # Replace with your sheet's name
try:
    sheet = client.open(sheet_name).sheet1
    print(f"Successfully connected to {sheet_name}")
    
    # Test reading a value
    cell_value = sheet.cell(1, 1).value 
    print(f"The value in A1 is: {cell_value}")

except Exception as e:
    print(f"Unable to connect to the Google Sheet: {e}")
