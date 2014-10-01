
import mutual_info
import tweet_data

"""
# TODO: finish
def generate_mutual_info_pair_list(loc, all_word_pairs, wp_fd, all_loc_word_pairs, lp_fd):
    mi_pair_list = []
    num_word_pairs = len(all_word_pairs)
    num_loc_word_pairs = len(all_loc_word_pairs)
    word_pairs = set(all_word_pairs)
    for pair in word_pairs:
        # p(pair, loc), intersection
        if pair not in lp_fd:
            p_pair_loc = 0
            mi = 0
        else:
            p_pair_loc = float(lp_fd[pair]) / num_word_pairs
            # p(pair)
            p_pair = float(wp_fd[pair]) / num_word_pairs
            # p(loc)
            p_loc = float(num_loc_word_pairs) / num_word_pairs
            if p_w == 0 or p_loc == 0:
                mi = 0
            else:
                mi = p_w_loc * math.log(float(p_w_loc) / (p_w * p_loc), 2)
        mi_list.append( (w, mi) )
    return list(reversed(sorted(mi_list, key=lambda t : t[1])))
    """

