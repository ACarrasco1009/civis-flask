from flask import Flask, render_template, redirect, url_for, request
import os
import civis
import hashlib
import uuid

app = Flask(__name__)

@app.route("/")
def home():
    return "Hi!"

@app.route('/welcome_series')
def welcome_series_trigger():
    pass


if __name__ == '__main__':
    app.run(port=3838)


