def get_sports():
    # response = get('http://localhost:8080/sports')
    response = {'sports': ['football', 'basketball', 'baseball']}
    return response

def get_personal_blog():
    # response = get('http://localhost:8080/personal-blog/simple-blog')
    response = {'personal-blog': 'simple-blog'}
    return response
