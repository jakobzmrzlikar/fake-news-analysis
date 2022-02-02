import os
import json 


def load_tweets(path, truth, mode):
    tweet_file = path + '/' + mode + '.json'
    if not os.path.exists(tweet_file):
        return []

    with open(tweet_file) as f:
        tweets = json.load(f)
        for tweet in tweets:
            tweet["truth"] = truth
    return tweets


def collect_tweets(rootdir, get_retweets=False):
    tweets = []

    for truth in ["real", "fake"]:
        dir = rootdir + '/' + truth
        for subdir in os.listdir(dir):
            
            tweets_dir = dir + "/" + subdir
            tweets += load_tweets(tweets_dir, truth, "tweets")

            if get_retweets:
                retweets_dir = dir + "/" + subdir
                tweets += load_tweets(retweets_dir, truth, "retweets")
    
    return tweets


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