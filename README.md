Update the README file:
I am thrilled to anounce that the error with the sidebar has now been resolved.
To test the website, feel free to clone the repo: git clone

To clone the test bug: git clone -b

To create a requirement file:

 pip freeze | findstr "flask flask_login google gspread oauth2client requests" > requirements.txt

 pipreqs .

 manually write down the requirements.txt file is also a choice

Before running the main python file, remember to install all the dependencies:

 pip install -r requirements.txt