from app import app
import urllib.request,json
from .models import news

News = news.News

apiKey = app.config['NEWS_API_KEY']

base_url = app.config["NEWS_API_BASE_URL"]


def get_news(category):
    '''
    Function that gets the json responce to our url request
    '''
    get_news_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results

def process_news(news_list):
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        image = news_item.get('urlToImage')



        if image:
            news_object = News(id,name,title,description,url,image)
            news_results.append(news_object)