from flask import Flask, request
from flask import render_template
from src.api import get_sports, get_personal_blog
from src.graphql import GraphQLClient
import json

app = Flask(__name__)
client = GraphQLClient("http://ec2-3-35-53-128.ap-northeast-2.compute.amazonaws.com:8000/graphql")

@app.route('/', methods=['GET', 'POST'])
def index():
    get_sport = get_sports()
    get_blog = get_personal_blog()
    epl_rank_url = "http://ec2-3-35-133-179.ap-northeast-2.compute.amazonaws.com:8001/"
    result = ""
    if request.method == 'POST':
        query = '''
            query GetToolByName($name: String!){
                toolByName(name: $name){
                    id
                    name
                    slug
                    title
                    description
                    imageUrl
                    ossRepo
                    canonicalUrl
                    websiteUrl
                }
            }
            '''
        tool = request.form['tool']
        if tool == "":
            result = ""
        else:
            variable = {
                'name': tool
            }
            result = client.execute(query=query, variables=variable)
            result = json.loads(result.encode().decode('unicode-escape'))
            if result['data']['toolByName'] == None:
                result = ""
        
    return render_template('index.html',
            title='컴홍설 - 컴퓨터 응용 설계 프로젝트',
            main_name='컴홍설',
            content_sports=get_sport,
            content_blog=get_blog,
            tool_value=result,
            epl_rank_url=epl_rank_url)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
    
