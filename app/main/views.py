from flask import render_template
from . import main
from ..request import get_sources, get_articles, topheadlines
#views

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_source = get_sources()
    top = topheadlines()
    return render_template('index.html',sources = news_source, top = top)

@main.route('/article/<id>')
def article(id):

    '''
    View news page function that returns the news source page and its data
    '''
    news_source = get_sources()
    article = get_articles(id)
    if article:
        for i in article:
            name = i.name
    else:
        for source in news_source:
            if source.id == id :
                name = source.name
        
    return render_template('article.html',sources = news_source,article = article,name = name)