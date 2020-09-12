from app import app
import urllib.request, json
from .models import source, article
from datetime import datetime

Source = source.Source
Article = article.Article

#Get api key
api_key = app.config['NEWS_API_KEY']

#get base url
base_url = app.config["SOURCE_API_BASE_URL"]
article_url = app.config["ARTICLES_API_BASE_URL"]


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''

    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        
        name= source_item.get('name')
        
        source_object= Source(id,name)
        source_results.append(source_object)
        
    return source_results

def get_articles(id):
    get_article_url = article_url.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        
        if article_details_response['articles']:
            article_results_list = article_details_response['articles']

        article_results = []
        for article_item in article_results_list:
            name = article_item.get('source').get('name')
            author = article_item.get('author')
            title = article_item.get('title')
            description = article_item.get('description')
            url = article_item.get('url')
            urlToImage = article_item.get('urlToImage')
            pdate = article_item.get('publishedAt')
            
            publishedAt = datetime.strptime(pdate, '%Y-%m-%dT%H:%M:%SZ').date()

            if urlToImage != "null":
                article_object = Article(name,author,title,description,url,urlToImage,publishedAt)
                article_results.append(article_object)

    return article_results
