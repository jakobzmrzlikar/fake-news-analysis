import os
import json 


def load_tweets(dir, truth, lst):
    for tweet_file in os.list(dir):
        with open(tweet_file) as f:
            tweet = json.load(f)
            tweet["truth"] = truth
            lst.append(tweet)


def collect_tweets(rootdir, get_retweets=False):
    tweets = []

    for truth in ["real", "fake"]:
        dir = rootdir + '/' + truth
        for subdir in os.listdir(dir):
            
            tweets_dir = dir + "/" + subdir + "/tweets"
            tweets = load_tweets(tweets_dir, truth, tweets)

            if get_retweets:
                retweets_dir = dir + "/" + subdir + "/retweets"
                tweets = load_tweets(retweets_dir, truth, tweets)
    
    return json.dumps(tweets)

def collect_news(rootdir):
    news = []

    for truth in ["real", "fake"]:
        dir = rootdir + '/' + truth
        for subdir in os.listdir(dir):
            newsfile = dir + '/' + subdir + "/news content.json"
            try:
                with open(newsfile) as f:
                    article = json.load(f)
                    article["truth"] = truth
                    news.append(article)
            except:
                continue
    return json.dumps(news)
