

def get_title(numtweets, numwords, numpairs, distr_skewed):
    title = str(numtweets) + 'twts_'
    title += str(numwords)
    if distr_skewed:
        title += 'distr_skewed_'
    title += 'maxmi'
    if numpairs > 0:
        title += str(numpairs)
        if distr_skewed:
            title += 'distr_skewed_'
        title += 'maxmipairs'
    title += '_instances'
    return title



