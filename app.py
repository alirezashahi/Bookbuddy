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
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        email = request.form['email']
        return render_template('homepage.html')
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)