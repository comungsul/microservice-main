from flask import Flask
from flask import render_template
from src.api import get_sports, get_personal_blog

app = Flask(__name__)


@app.route('/')
def index():
    # json_sports = get_sports()
    # json_personal_blog = get_personal_blog()
    # return render_template('index.html',
    #     content_sports=json_sports,
    #     content_blog=json_personal_blog)
    get_sport = get_sports()
    get_blog = get_personal_blog()
    return render_template('index.html',
        title='컴홍설 - 컴퓨터 응용 설계 프로젝트',
        main_name='컴홍설',
        content_sports=get_sport,
        content_blog=get_blog)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
