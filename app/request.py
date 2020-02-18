
import urllib.request,json
from .models import News

# Getting api key
api_key = None
# Getting the news base url
#base_url=None

articles_url =None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    # articles_url = app.config['ARTICLES_BASE_URL']
    
    
def process_news(news_list):
     
    news_results = []
     
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        category = news_item.get('category')
        language = news_item.get('language')
        
        if description:
            news_object = News(id,name,description,url,category,language,title)
            news_results.append(news_object)
            
    return news_results


def get_news(category):
    '''
    this  function will get the json response to the url request
    '''
    get_news_url = base_url.format(category,api_key)

    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_news(news_results_list)
            
    return news_results


def get_reviews(id):
    
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    
    get_reviews_url = reviews_url.format(id,api_key)
    
    
    with urllib.request.urlopen(get_reviews_url) as url:
        reviews_results = json.loads(url.read())
        reviews_object = None
        if reviews_results['reviews']:
            reviews_object = process_reviews(reviews_results['reviews'])
    return reviews_object

def process_reviews(reviews_list):
    reviews_object = []
    for review_item in reviews_list:
        id = review_item.get('id')
        author = review_item.get('author')
        title = review_item.get('title')
        description = review_item.get('description')
        url = review_item.get('url')
        urlToImage = review_item.get('urlToImage')
        publishedAt = review_item.get('publishedAt')
        if urlToImage:
            reviews_result = Review(id,author,title,description,url,urlToImage,publishedAt)
            reviews_object.append(reviews_result)
            
    return news_results
 
 

        
            
