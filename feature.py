
import mutual_info
import tweet_data

class Instance():
    def __init__(self, tweetid, attr_list, label=None):
        self.tweetid = tweetid
        self.attr_list = attr_list
        self.label = label

def get_test_instances(test_tweets, numtweets, numwords, numwordpairs, distr_skewed, include_userid):
    loc_distr = tweet_data.get_loc_distribution('data/loc_to_tweets_contributed.txt')
    loc_word_distr = {}
    loc_pair_distr = {}
    for loc in loc_distr:
        loc_word_distr[loc] = int(loc_distr[loc] * numwords)
        loc_pair_distr[loc] = int(loc_distr[loc] * numwordpairs)

    if not distr_skewed:
        for loc in loc_distr:
            loc_word_distr[loc] = int(numwords / len(loc_distr))
            loc_pair_distr[loc] = int(numwordpairs / len(loc_distr))

    loc_to_tweets = tweet_data.get_loc_to_tweets_dict(numtweets)
    words = mutual_info.get_wordnum_restricted_word_list(loc_word_distr)
    wordpairs = mutual_info.get_word_pair_list(loc_pair_distr)
    instances = get_freq_instances(test_tweets, words, wordpairs, include_userid)
    return (instances, words, wordpairs)

def get_loc_to_instances_dict(numtweets, numwords, numwordpairs, distr_skewed, include_userid):
    loc_distr = tweet_data.get_loc_distribution('data/loc_to_tweets_contributed.txt')
    loc_word_distr = {}
    loc_pair_distr = {}
    for loc in loc_distr:
        loc_word_distr[loc] = int(loc_distr[loc] * numwords)
        loc_pair_distr[loc] = int(loc_distr[loc] * numwordpairs)

    if not distr_skewed:
        for loc in loc_distr:
            loc_word_distr[loc] = int(numwords / len(loc_distr))
            loc_pair_distr[loc] = int(numwordpairs / len(loc_distr))

    loc_to_tweets = tweet_data.get_loc_to_tweets_dict(numtweets)
    words = mutual_info.get_wordnum_restricted_word_list(loc_word_distr)
    wordpairs = mutual_info.get_word_pair_list(loc_pair_distr)
    loc_to_instances = get_loc_to_instances_dict_helper(loc_to_tweets, words, wordpairs, include_userid)
    return (loc_to_instances, words, wordpairs)

def get_loc_to_instances_from_attributes(numtweets, words, pairs):
    loc_to_tweets = tweet_data.get_loc_to_tweets_dict(numtweets)
    loc_to_instances = get_loc_to_instances_dict_helper(loc_to_tweets, words, pairs)
    return loc_to_instances




def get_loc_to_instances_dict_helper(loc_to_tweets_dict, words, wordpairs, include_userid):
    d = {}
    for loc in loc_to_tweets_dict:
        d[loc] = get_freq_instances(loc_to_tweets_dict[loc], words, wordpairs, include_userid)
        for instance in d[loc]:
            instance.label = loc
    return d

# create vector instances from tweets
# returns python list of 
# Instance(tweetid, attr_list=[word1_freq, word2_freq, ..., wordpair1_freq, wordpair2_freq, ...])
def get_freq_instances(tweets, words, wordpairs, include_userid):
    instances = []
    for tweet in tweets:
        tweet_word_dict = {}
        tweet_pair_dict = {}
        for word in tweet_data.get_words_from_tweets([tweet]):
            if word not in tweet_word_dict:
                tweet_word_dict[word] = 1
            else:
                tweet_word_dict[word] += 1
        for pair in tweet_data.get_word_pairs_from_tweets([tweet]):
            if pair not in tweet_pair_dict:
                tweet_pair_dict[pair] = 1
            else:
                tweet_pair_dict[pair] += 1
        attr_list = []
        if include_userid:
            attr_list.append(tweet.userid)
        for word in words:
            if word in tweet_word_dict:
                attr_list.append(tweet_word_dict[word])
            else:
                attr_list.append(0)
        for pair in wordpairs:
            if pair in tweet_pair_dict:
                attr_list.append(tweet_pair_dict[pair])
            else:
                attr_list.append(0)
        instances.append(Instance(tweet.tweetid, attr_list))
    return instances






