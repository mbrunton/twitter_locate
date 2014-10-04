
import tweet_data
import math

# TODO: remove from mi_lists and mi_pair_lists any words/pairs
#       which appear in multiple lists!!

supplied_mi_filename = 'data/supplied_mi_list.txt'
LA_mi_filename = 'data/LA_mi_list_reduced.txt'
NY_mi_filename = 'data/NY_mi_list_reduced.txt'
At_mi_filename = 'data/At_mi_list_reduced.txt'
C_mi_filename = 'data/C_mi_list_reduced.txt'
SF_mi_filename = 'data/SF_mi_list_reduced.txt'

LA_mi_pair_filename = 'data/LA_mi_pair_list_reduced.txt'
NY_mi_pair_filename = 'data/NY_mi_pair_list_reduced.txt'
At_mi_pair_filename = 'data/At_mi_pair_list_reduced.txt'
C_mi_pair_filename = 'data/C_mi_pair_list_reduced.txt'
SF_mi_pair_filename = 'data/SF_mi_pair_list_reduced.txt'

locs = tweet_data.locs

def get_mi_list_dict():
    d = {}
    for loc in locs:
        d[loc] = get_mi_list(loc)
    return d

def get_mi_pair_list_dict():
    d = {}
    for loc in locs:
        d[loc] = get_mi_pair_list(loc)
    return d

"""
def get_mi_restricted_word_list(mi_min):
    d = get_mi_list_dict()
    words = set()
    for loc in d:
        mi_list = d[loc]
        locwords = [w for (w, mi) in mi_list if mi >= mi_min]
        for w in locwords:
            words.add(w)
    return words
"""

def get_wordnum_restricted_word_list(loc_distr):
    d = get_mi_list_dict()
    words = set()
    for loc in d:
        if loc_distr[loc] == 0:
            continue
        mi_list = d[loc]
        locwords = [w for (w, mi) in mi_list]
        words_added = 0
        for w in locwords:
            if w not in words:
                words.add(w)
                words_added += 1
                if words_added >= loc_distr[loc]:
                    break
    return list(words)

def get_word_pair_list(loc_distr):
    d = get_mi_pair_list_dict()
    pairs = set()
    for loc in d:
        if loc_distr[loc] == 0:
            continue
        mi_pair_list = d[loc]
        locpairs = [(w1, w2) for (w1, w2, mi) in mi_pair_list]
        pairs_added = 0
        for p in locpairs:
            if p not in pairs:
                pairs.add(p)
                pairs_added += 1
                if pairs_added >= loc_distr[loc]:
                    break
    return list(pairs)

def get_mi_list(loc):
    filename = get_mi_filename_from_loc(loc)
    fd = open(filename, 'r')
    mi_list = []
    for line in fd.readlines():
        split_line = line.split('\t')
        w = split_line[0]
        mi = float(split_line[1])
        mi_list.append( (w, mi) )
    return mi_list

def get_mi_pair_list(loc):
    filename = get_mi_pair_filename_from_loc(loc)
    fd = open(filename, 'r')
    mi_pair_list = []
    for line in fd.readlines():
        split_line = line.split('\t')
        w1 = split_line[0]
        w2 = split_line[1]
        mi = float(split_line[2])
        mi_pair_list.append( (w1, w2, mi) )
    return mi_pair_list

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
def generate_mutual_info_list(loc, all_words, words_fd, all_loc_words, loc_words_fd, scale=None):
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
            if w not in loc_words_fd:
                p_w_loc = 0
            else:
                p_w_loc = float(loc_words_fd[w]) / num_words
            # p(w)
            if w not in words_fd:
                p_w = 0
            else:
                p_w = float(words_fd[w]) / num_words
            # p(loc)
            p_loc = float(num_loc_words) / num_words
            if p_w == 0 or p_loc == 0:
                mi = 0
            else:
                if scale:
                    mi = scale * p_w_loc * math.log(float(p_w_loc) / (p_w * p_loc), 2)
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
        all_loc_words = tweet_data.get_loc_words(loc)
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
    # DEBUGGING
    #all_words = all_words[:100000]
    all_word_pairs = tweet_data.get_word_pairs(all_words)
    num_word_pairs = len(all_word_pairs)
    word_pairs_fd = get_freq_dist(all_word_pairs)

    mi_pair_lists = []
    for loc in locs:
        # all words from tweets marked as in location 'loc'
        all_loc_words = tweet_data.get_loc_words(loc)
        all_loc_word_pairs = tweet_data.get_word_pairs(all_loc_words)
        num_loc_word_pairs = len(all_loc_word_pairs)
        loc_word_pairs_fd = get_freq_dist(all_loc_word_pairs)
        #scale = 1000*1000
        scale = None
        mi_pair_list = generate_mutual_info_list(loc, all_word_pairs, word_pairs_fd, 
                                        all_loc_word_pairs, loc_word_pairs_fd, scale)
        mi_pair_lists.append( (loc, mi_pair_list) )
    return mi_pair_lists

def get_mi_filename_from_loc(loc):
    if loc == 'LA':
        filename = LA_mi_filename
    elif loc == 'NY':
        filename = NY_mi_filename
    elif loc == 'At':
        filename = At_mi_filename
    elif loc == 'C':
        filename = C_mi_filename
    elif loc == 'SF':
        filename = SF_mi_filename
    else:
        raise Exception('Invalid location name: ' + loc)
    return filename


def get_mi_pair_filename_from_loc(loc):
    if loc == 'LA':
        filename = LA_mi_pair_filename
    elif loc == 'NY':
        filename = NY_mi_pair_filename
    elif loc == 'At':
        filename = At_mi_pair_filename
    elif loc == 'C':
        filename = C_mi_pair_filename
    elif loc == 'SF':
        filename = SF_mi_pair_filename
    else:
        raise Exception('Invalid location name: ' + loc)
    return filename

if __name__ == '__main__':
    generate_mutual_info_pair_lists()




