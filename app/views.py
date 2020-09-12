from flask import render_template
from app import app
from .request import get_sources, get_articles
#views

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_source = get_sources()
    
    return render_template('index.html', sources = news_source)

@app.route('/article/<id>')
def article(id):

    '''
    View news page function that returns the news source page and its data
    '''
    article = get_articles(id)

    return render_template('article.html',article = article)