from flask import Flask, request, jsonify
from flask import render_template
from flask_cors import CORS
from src.api import get_sports, get_personal_blog

app = Flask(__name__)


@app.route('/')
def index():
    json_sports = get_sports()
    json_personal_blog = get_personal_blog()
    return render_template('index.html',
        content_sports=json_sports,
        content_blog=json_personal_blog)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
