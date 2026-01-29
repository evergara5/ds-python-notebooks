python-Copy

from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():

return "Hello from Flask!"

if name == '__main__': app.run(opens in a new tab)(debug=True)