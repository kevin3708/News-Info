from flask import render_template
from app import app
from .request import get_news
@app.route('/')
def index():
    sports_news = get_news('sports')
    economy_news = get_news('economy')
    inter_news = get_news('international')
    title = 'Home -Welcome to the best News Website Online'
    return render_template('index.html',title = title, sports = sports_news, economy = economy_news, international = inter_news  )

@app.route('/news/<news_id>')
def news(news_id):
    title = f'You are viewing {news_id}'
    return render_template('news.html',title = title)