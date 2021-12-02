import requests
def get_sports():
    response = requests.get('http://localhost:8001/epl')
    print(response.text)
    return response.json()

def get_personal_blog():
    # response = get('http://localhost:8080/personal-blog/simple-blog')
    response = {'personal-blog': 'simple-blog'}
    return response
