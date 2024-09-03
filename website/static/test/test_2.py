from flask import Flask, render_template, request, redirect, url_for
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Setup Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('path_to_your_credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Your Google Sheet Name").sheet1

@app.route('/')
def index():
    if 'signed_up' in request.cookies:
        return render_template('main.html')
    return redirect(url_for('sign_up'))

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        sheet.append_row([name, email, password])
        resp = redirect(url_for('index'))
        resp.set_cookie('signed_up', 'true')
        return resp
    return render_template('sign_up.html')

if __name__ == '__main__':
    app.run(debug=True)
