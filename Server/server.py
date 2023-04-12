from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"Welcome to AI Quotes Generator"})


@app.route('/quotes')
def quotes():
    return {"Quotes": ["Quote 1", "Quote 2", "Quote 3"]}

if __name__ == "__main__":
    app.run(debug=True)
