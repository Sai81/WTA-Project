from flask import Flask, render_template
from newsapi import NewsApiClient


app = Flask(__name__)


@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key = "57c0fcb51bc74ebbb71643ef42293cdd")
    topheadlines = newsapi.get_top_headlines(country="in")
    
    articles = topheadlines['articles']
    
    desc =[]
    news = []
    img = []
    link = []
    
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])
        
        
    mylist = zip(news, desc, img, link)
    
    return render_template('NewsFeed.html', context = mylist)

if __name__=="__main__":
    
    app.run(debug=True)