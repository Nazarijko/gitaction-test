from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    time.sleep(5)