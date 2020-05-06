# Application for webpage 

from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
	return render_template('user.html')
	
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
	app.run()