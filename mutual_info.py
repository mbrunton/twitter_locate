
import tweet_data
import math

supplied_mi_filename = 'data/supplied_mi_list.txt'

locs = tweet_data.locs

def get_mi_list_dict():
    d = {}
    for loc in locs:
        d[loc] = get_mi_list(loc)
    return d

def get_mi_list(loc):
    filename = 'data/' + loc + '_mi_list.txt'
    fd = open(filename, 'r')
    mi_list = []
    for line in fd.readlines():
        split_line = line.split('\t')
        w = split_line[0]
        mi = float(split_line[1])
        mi_list.append( (w, mi) )
    return mi_list

def get_supplied_mi_list():
    fd = open(supplied_mi_filename, 'r')
    mi_list = [line.strip() for line in fd.readlines()]
    return mi_list


# THESE FUNCTIONS GENERATE mutual information word lists and take a long time
# to complete. I ran them once, then wrote the output to files of form
# filename:     <state code>_mi_list.txt
# format:   word1 <mutual information of word1 for <state>>
#           word2 <mutual information of word2 for <state>>

# return sorted list of (word, mutual_info) for set of words
# sorted in decreasing order by mutual_info
def generate_mutual_info_list(loc, all_words, words_fd, all_loc_words, loc_words_fd):
    mi_list = []
    num_words = len(all_words)
    num_loc_words = len(all_loc_words)
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

def generate_mutual_info_lists():
    tweets = tweet_data.get_labeled_tweets()
    # all_words has repeats. it's all words from all tweets in training+dev sets
    all_words = tweet_data.get_words_from_tweets(tweets)
    num_words = len(all_words)
    words_fd = get_freq_dist(all_words)

    mi_lists = []
    for loc in locs:
        # all words from tweets marked as in location 'loc'
        all_loc_words = tweet_data.get_loc_words(loc, tweets)
        num_loc_words = len(all_loc_words)
        loc_words_fd = get_freq_dist(all_loc_words)
        mi_list = generate_mutual_info_list(loc, all_words, words_fd, all_loc_words, loc_words_fd)
        mi_lists.append( (loc, mi_list) )
    return mi_lists


def get_freq_dist(words):
    d = {}
    for w in words:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1
    return d


def generate_mutual_info_pair_lists():
    tweets = tweet_data.get_labeled_tweets()
    # all_words has repeats. it's all words from all tweets in training+dev sets
    all_words = tweet_data.get_words_from_tweets(tweets)
    all_word_pairs = get_word_pairs(all_words)
    num_word_pairs = len(all_word_pairs)
    word_pairs_fd = get_freq_dist(all_words)

    mi_pair_lists = []
    for loc in locs:
        # all words from tweets marked as in location 'loc'
        all_loc_words = tweet_data.get_loc_words(loc, tweets)
        all_loc_word_pairs = get_word_pairs(all_loc_words)
        num_loc_word_pairs = len(all_loc_word_pairs)
        loc_word_pairs_fd = get_freq_dist(all_loc_word_pairs)

        mi_pair_list = generate_mutual_info_list(loc, all_word_pairs, word_pairs_fd, 
                                                    all_loc_word_pairs, loc_word_pairs_fd)
        mi_lists.append( (loc, mi_pair_list) )
    return mi_pair_lists

def get_word_pairs(words):
    pairs = []
    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[i+1]
        pairs.append( (w1, w2) )
    return pairs






