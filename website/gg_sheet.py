import gspread
from google.oauth2.service_account import Credentials

class GoogleSheetClient:
    """
    This class is for connecting with the gg spreadsheet and writing down data
    in an object-oriented programing style. This should be a more effective way for scalability"""
    def __init__(self, credentials_file, sheet_name):
        """Initializing everything"""
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
                       'https://www.googleapis.com/auth/drive']
        self.credentials_file = credentials_file
        self.sheet_name = sheet_name
        self.client = self.authenticate()
    def authenticate(self):
        """Authenticate and return a gspread client"""
        credentials = Credentials.from_service_account_file(self.credentials_file, scopes = self.SCOPES)
        return gspread.authorize(credentials)
    def write_in4_to_spreadsheet(self, email, username, datetime):
        try:
            sheet = self.client.open(self.sheet_name).sheet1

            # this is running much faster and more efficiently
            sheet.append_row([email, username, datetime])

            # the method of calculating manually which row the data should be written on is so inefficient 
            # email_column = sheet.col_values(1)
            # next_line = len(email_column) + 1
            # sheet.update_cell(next_line, 1, email)
            # sheet.update_cell(next_line, 2, username)
            # sheet.update_cell(next_line, 3, datetime)

        except Exception as e:
            # print out the exception in here for debugging
            print(e)