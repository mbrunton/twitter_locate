# Knowledge Technologies Project 2
# Mitchell Brunton
# #537642
#
# Preprocess raw twitter data

import re

tweet_filename = 'data/original_tweet_data.txt'

# convert raw tweets into nice tweets (lowercase, alphabetic, collapse whitespace into spaces)
def generate_repaired_tweets():
    lines = open(tweet_filename, 'r').readlines()
    lines = concat_split_lines(lines)
    lines = remove_tabs(lines)
    lines = reduce(lines)
    lines = remove_empty(lines)
    return lines

def concat_split_lines(lines):
    r = re.compile(r'^[0-9]+\t[0-9]+\t')
    prevline = ''
    goodlines = []
    for line in lines:
        m = r.match(line)
        justappended = False
        if not m:
            prevline = prevline.strip() + line
        else:
            if prevline != '':
                goodlines.append(prevline)
                justappended = True
            prevline = line
    if not justappended:
        goodlines.append(prevline)
    return goodlines

def remove_tabs(lines):
    goodlines = []
    for line in lines:
        fields = line.split('\t')
        goodline = fields[0] + '\t' + fields[1] + '\t'
        tweet = ' '.join(fields[2:-1])
        goodline += tweet + '\t' + fields[-1]
        goodlines.append(goodline.strip())
    return goodlines

def reduce(lines): 
    goodlines = []
    for line in lines:
        fields = line.split('\t')
        tweet = fields[2]
        tweet = ''.join(c.lower() for c in tweet if c.isalpha() or c.isspace())
        tweet = re.sub(r'[ \t\r\f\n]+', ' ', tweet)
        fields[2] = tweet
        goodlines.append('\t'.join(fields))
    return goodlines

def remove_empty(lines):
    goodlines = []
    for line in lines:
        if line.split('\t')[2] != '':
            goodlines.append(line)
    return goodlines


