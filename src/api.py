import requests
def get_sports():
    response = requests.get('http://0.0.0.0:8001/epl')
    return response.json()

def get_personal_blog():
    # response = get('http://localhost:8080/personal-blog/simple-blog')
    response = {'personal-blog': 'simple-blog'}
    return response
