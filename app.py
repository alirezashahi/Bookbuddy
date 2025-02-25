from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/form', methods=['GET','POST'])
def form():
    return render_template('form.html')

@app.route('/my library', methods=['GET'])
def my_library():
    return render_template('my_library.html')

@app.route('/sign-up', methods=['POST','GET'])
def signup():
    if request.method == "POST":
    # Handle form submission
    username = request.form.get("username")
    password = request.form.get("password")

    # Validate input (basic example)
    if not username or not password:
        return "Username and password are required!", 400

    # Store user data (in-memory for this example)
    users.append({"username": username, "password": password})
    return render_template('homepage.html', message="User created successfully!")

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
    # Handle form submission
        username = request.form.get("username")
        password = request.form.get("password")

    # Validate input (basic example)
    if not username or not password:
        return "Username and password are required!", 400

    # Check if user exists
    for user in users:
        if user["username"] == username and user["password"] == password:
            return render_template('form.html', message="Login successful!")

    return "Invalid username or password", 400

if __name__ == "__main__":
    app.run(debug=True)