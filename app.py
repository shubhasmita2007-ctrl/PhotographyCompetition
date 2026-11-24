from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Photography Competition! Please submit your entry below. "   
@app.route('/submit', methods=['POST'])
def submit():
    # Handle form submission logic here
    # For example, you can save the submitted data to a database or perform other actions
    return form("participant name: " + request.form['name'] + ", photo title: " + request.form['title'])
    return form("email id: " + request.form['email'] + ", photo file: " + request.form['photo']
    return form("photography title: " + request.form['title'] + ", photo file: " + request.form['photo']))
    return form("description: " + request.form['description'])  
def form(message):
    return "thank you for your submission! " + message
if __name__ == '__main__':
    app.run(debug=True)