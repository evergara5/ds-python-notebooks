from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask!"   # <-- must be indented (4 spaces or a tab)

if __name__ == '__main__':
    app.run(debug=True)
