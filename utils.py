

def get_title(numtweets, numwords, distr_skewed):
    title = str(numtweets) + 'twts_'
    title += str(numwords)
    if distr_skewed:
        title += 'distr_skewed_'
    title += 'maxmi_instances'
    return title



