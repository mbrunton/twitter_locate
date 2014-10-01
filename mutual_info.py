
import tweet_data
from nltk import FreqDist
import math

get_mi_list(loc):
    filename = loc + '_mi_list.txt'
    fd = open(filename, 'r')
    mi_list = []
    for line in fd.readline():
        split_line = line.split('\t')
        w = split_line[0]
        mi = float(split_line[1])
        mi_list.append( (w, mi) )
    return mi_list






# THESE FUNCTIONS GENERATE mutual information word lists and take a long time
# to complete. I ran them once, then wrote the output to files of form
# name:     <State code>_mi_list.txt
# formate:  word1 <mutual information of word1 for <state>>
#           word2 <mutual information of word2 for <state>>

# return sorted list of (word, mutual_info) for set of words
# sorted in decreasing order by mutual_info
def generate_mutual_info_list(loc, tweets):
    # all_words has repeats. it's all words from all tweets
    all_words = tweet_data.get_words_from_tweets(tweets)
    num_words = len(all_words)
    words_fd = FreqDist(all_words)
    # all words from tweets marked as in location 'loc'
    all_loc_words = get_loc_words(loc, tweets)
    num_loc_words = len(all_loc_words)
    loc_words_fd = FreqDist(all_loc_words)

    mi_list = []
    words = set(all_words)
    for w in words:
        # p(w, loc), intersection
        if w not in loc_words_fd:
            p_w_loc = 0
            mi = 0
        else:
            p_w_loc = float(loc_words_fd[w]) / num_words
            # p(w)
            p_w = float(words_fd[w]) / num_words
            # p(loc)
            p_loc = float(num_loc_words) / num_words
            if p_w == 0 or p_loc == 0:
                mi = 0
            else:
                mi = p_w_loc * math.log(float(p_w_loc) / (p_w * p_loc), 2)
        mi_list.append( (w, mi) )
    return list(reversed(sorted(mi_list, key=lambda t : t[1])))

# has repeat words
def get_loc_words(loc, tweets):
    ids = tweet_data.get_loc_ids(loc)
    loc_tweets = tweet_data.get_tweet_subset(tweets, ids)
    all_loc_words = tweet_data.get_words_from_tweets(loc_tweets)
    return all_loc_words

def generate_mutual_info_lists():
    locs = ['At', 'SF', 'C', 'NY', 'LA']
    tweets = tweet_data.get_labeled_tweets()
    # debugging
    # tweets = tweets[:100]
    mi_lists = []
    for loc in locs:
        mi_lists.append( (loc, generate_mutual_info_list(loc, tweets)) )
    return mi_lists


