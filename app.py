from flask import Flask  # Example if using Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! hi i am rajan  i want to learn more  "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # ← Must use port 80!
