from flask import render_template,request,redirect,url_for
from app.request import get_news
from . import main


# Views
@main.route('/')
def index():
    business_news = get_news('business')
    

   #sasa=get_news()
   # title = 'THE NEWS APP'
    return render_template('index.html', business = business_news)

@main.route('/news/<id>')
def articles(id):

    '''
    View news page function that returns the news details page and its data
    '''
    articles = get_reviews(id)
    return render_template('news-articles',id = news_id)
   
#     # Getting popular News
#     popular_News = get_news('popular')
#     upcoming_news = get_news

# @main.route('/news/<int:news_id>')
# def news(news_id):

#     '''
#     View news page function that returns the news details page and its data
#     '''
#     return render_template('news.html',id = news_id)

