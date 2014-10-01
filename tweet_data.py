# Knowledge Technology Project 2
# Feature Engineering for tweets

# attempt to recreate Jeremy's feature generation algorithm

tweets_filename = 'data/repaired_tweets.txt'
training_tweets_filename = 'data/training_tweets.txt'
dev_tweets_filename = 'data/dev_tweets.txt'

training_csv_filename = 'data/train.csv'
dev_csv_filename = 'data/dev.csv'

class Tweet():
    def __init__(self, userid, tweetid, text, date):
        self.userid = userid
        self.tweetid = tweetid
        self.text = text
        self.date = date

def get_tweets_from_file(filename):
    tweetfd = open(tweets_filename, 'r')
    tweets = []
    for line in tweetfd.readlines():
        fields = line.split('\t')
        userid = int(fields[0])
        tweetid = int(fields[1])
        text = fields[2]
        date = fields[3].strip()
        tweets.append(Tweet(userid, tweetid, text, date))
    return tweets

def get_all_tweets():
    return get_tweets_from_file(tweets_filename)

def get_training_tweets():
    return get_tweets_from_file(training_tweets_filename)

def get_dev_tweets():
    return get_tweets_from_file(dev_tweets_filename)

def get_labeled_tweets():
    tweets = get_training_tweets()
    tweets += get_dev_tweets()
    return tweets

def get_words_from_tweets(tweets):
    words = []
    for tweet in tweets:
        text = tweet.text
        for w in text.split():
            words.append(w)
    return words

# return the subset of tweets with an id in ids
def get_tweet_subset(tweets, ids):
    id_to_tweet = get_id_to_tweet_dict(tweets)
    subset = []
    for id in ids:
        if id in id_to_tweet:
            subset.append(id_to_tweet[id])
    return subset

# turns list of tweets into dict: tweetid => Tweet
def get_id_to_tweet_dict(tweets):
    d = {}
    for tweet in tweets:
        d[tweet.tweetid] = tweet
    return d

# opens a training/dev file and returns a dict: tweetid => loc
# assumes csv file
def get_id_to_loc_dict(filename):
    d = {}
    fd = open(filename, 'r')
    for line in fd.readlines():
        fields = line.split(',')
        tweetid = int(fields[0])
        loc = fields[-1].strip()
        d[tweetid] = loc
    return d

# dict: training_tweetid => loc
def get_training_id_to_loc_dict():
    return get_id_to_loc_dict(training_csv_filename)

# dict: dev_tweetid => loc
def get_dev_id_to_loc_dict():
    return get_id_to_loc_dict(dev_csv_filename)

# training and dev dicts combined
def get_labeled_id_to_loc_dict():
    d = get_training_id_to_loc_dict()
    for item in get_dev_id_to_loc_dict().items():
        d[item[0]] = item[1]
    return d

def get_loc_ids(loc):
    d = get_labeled_id_to_loc_dict()
    return [id for id in d if d[id] == loc]




