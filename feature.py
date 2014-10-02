
import mutual_info
import tweet_data
import csv

class Instance():
    def __init__(self, tweetid, attr_list, label=None):
        self.tweetid = tweetid
        self.attr_list = attr_list
        self.label = label


def create_instances_csv(numtweets, numwords):
    loc_to_tweets = tweet_data.get_loc_to_tweets_dict(numtweets)
    words = mutual_info.get_wordnum_restricted_word_list(numwords)
    loc_to_instances = get_loc_to_instances_dict(loc_to_tweets, words)
    filename = 'data/instances/'
    filename += str(numtweets*5) + 'twts_'
    filename += str(numwords) + 'maxmi_instances.csv'
    csv.create_csv(filename, loc_to_instances)




def get_loc_to_instances_dict(loc_to_tweets_dict, words):
    d = {}
    for loc in loc_to_tweets_dict:
        d[loc] = get_word_freq_instances(loc_to_tweets_dict[loc], words)
        for instance in d[loc]:
            instance.label = loc
    return d

# create vector instances from tweets
# returns python list of (tweet, [word1_freq, word2_freq, ...])
def get_word_freq_instances(tweets, words):
    instances = []
    for tweet in tweets:
        tweet_word_dict = {}
        for word in tweet_data.get_words_from_tweets([tweet]):
            if word not in tweet_word_dict:
                tweet_word_dict[word] = 1
            else:
                tweet_word_dict[word] += 1
        attr_list = []
        for word in words:
            if word in tweet_word_dict:
                attr_list.append(tweet_word_dict[word])
            else:
                attr_list.append(0)
        instances.append(Instance(tweet.tweetid, attr_list))
    return instances

# list of (tweet, [word_pair1_freq, word_pair2_freq, ...])
def get_word_pair_freq_instances(tweets, word_pairs):
    instances = []
    for tweet in tweets:
        tweet_word_pair_dict = {}
        tweet_words = tweet_data.get_words_from_tweets([tweet])
        tweet_word_pairs = mutual_info.get_word_pairs(tweet_words)
        for pair in tweet_word_pairs:
            if pair not in tweet_word_pair_dict:
                tweet_word_pair_dict[pair] = 1
            else:
                tweet_word_pair_dict[pair] += 1
        attr_list = []
        for pair in word_pairs:
            if pair in tweet_word_pair_dict:
                attr_list.append(tweet_word_dict[word])
            else:
                attr_list.append(0)
        instances.append(Instance(tweet.tweetid, attr_list))
    return instances






