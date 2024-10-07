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

# def check_available_row():
#     """Filtering out the rows that return None to find out the next empty row
#     Once an empty row has been determined, we can write down the new info, without overwriting the already existing rows"""
#     pass

def write_in4_to_sheet(email, username, datetime):
    try:
        sheet = client.open(sheet_name).sheet1

        # This might be very slow as it will loop through every row and column of the spreadsheet
        # ugly code here as get_all_records will make you loop through the entire spreadsheet, Idk, O(n2) for the runtime complexity
        # list_of_hashes = sheet.get_all_records()

        # instead, we should loop the one column only
        # get the list of value in the first column
        email_column = sheet.col_values(1)
        next_line = len(email_column) + 1  

        # Test reading a value
        # cell_value = sheet.cell(1, 1).value 
        # print(f"The value in A1 is: {cell_value}")

        # # this is for writing
        sheet.update_cell(next_line, 1, email)
        sheet.update_cell(next_line, 2, username)
        sheet.update_cell(next_line, 3, datetime)
    except Exception as e:
        print(e)

