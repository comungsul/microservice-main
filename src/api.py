from requests import get

def get_sports():
    response = get('http://localhost:8080/sports')
    return response.json()

def get_personal_blog():
    response = get('http://localhost:8080/personal-blog/simple-blog')
    return response.json()