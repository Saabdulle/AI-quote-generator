from flask import Flask, jsonify
import json

server = Flask(__name__)

@server.route('/')
def home():
    return {"Home":
     "Welcome to AI Quotes Generator"    
    }


@server.route('/quotes')
def quotes():
    return {"Quotes": ["Quote 1", "Quote 2", "Quote 3"]}

