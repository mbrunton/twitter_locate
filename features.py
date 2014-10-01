# Knowledge Technology Project 2
# Feature Engineering for tweets

# attempt to recreate Jeremy's feature generation algorithm

tweets_filename = 'data/repaired_tweets.txt'
training_filename = 'data/train.csv'
dev_filename = 'data/dev.csv'

class Tweet():
    def __init__(self, userid, tweetid, text):
        self.userid = userid
        self.tweetid = tweetid
        self.text = text

def get_tweets():
    tweetfd = open(tweets_filename, 'r')
    tweets = []
    for line in tweetfd.readlines():
        fields = line.split('\t')
        userid = int(fields[0])
        tweetid = int(fields[1])
        text = fields[2]
        tweets.append(Tweet(userid, tweetid, text))
    return tweets

def get_words_from_tweets(tweets):
    words = []
    for tweet in tweets:
        text = tweet.text
        for w in text.split():
            words.append(w)
    return words

def get_tweet_subset(tweets, ids):
    id_to_tweet = get_id_to_tweet_dict(tweets)
    subset = [id_to_tweet[id].text for id in ids]
    return subset

def get_id_to_tweet_dict(tweets):
    d = {}
    for tweet in tweets:
        d[tweet.tweetid] = tweet
    return d

# assumes csv file
def get_id_to_loc_dict(filename):
    d = {}
    fd = open(filename, 'r')
    for line in fd.readlines():
        fields = line.split(',')
        tweetid = int(fields[0])
        loc = fields[-1]
        d[tweetid] = loc
    return d

def get_training_id_to_loc_dict():
    return get_id_to_loc_dict(training_filename)

def get_dev_id_to_loc_dict():
    return get_id_to_loc_dict(dev_filename)

def get_training_tweets():
    tweets = get_tweets()
    training_id_to_loc = get_training_id_to_loc_dict()
    training_ids = training_id_to_loc.keys()
    training_tweets = get_tweet_subset(tweets, training_ids)

def get_dev_tweets():
    tweets = get_tweets()
    dev_id_to_loc = get_dev_id_to_loc_dict()
    dev_ids = dev_id_to_loc.keys()
    dev_tweets = get_tweet_subset(tweets, dev_ids)

def get_training_id_to_tweet_dict():
    training = get_training_tweets()
    return get_id_to_tweet_dict(training)

def get_dev_id_to_tweet_dict():
    dev = get_dev_tweets()
    return get_id_to_tweet_dict(dev)




