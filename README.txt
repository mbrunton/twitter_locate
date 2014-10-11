Readme for Knowledge Technologies Project 2
Mitchell Brunton
#537642

There are two prediction files for the the supplied reduced test data:
    OneR_predictions.txt - predictions using a one-R model
    NBmn_predictions.txt - predictions using a naive bayes multinomial model
Each was generated using Weka.

My included source code files are as follows:
    preprocess.py - convert raw twitter data (with newlines, tabs, non-alpha chars etc) into cleaned twitter data
    tweet_data.py - get/manipulate cleaned twitter data
    mutual_info.py - generate/retrieve mutual information lists by location (words/word pairs)
    feature.py - generate instances from tweets, given a set of features
    csv.py - generate csv files from instances
    arff.py - generate arff files from instances
    utils.py - helper functions

A high-level overlook of my procedure in solving this task is as follows
- preprocess tweet data so it's in a nice form
- write functions for selecting features
- choose the most effective subset of features
- write functions for turning tweets into instances
- write functions for creating output files of tweet instances (arff ended up being my preferred format)
- build models from tweet instances using Weka
- use models to predict location of test tweets, using Weka

Final set of features:
- 30 words from all words which appeared in any labeled (training/dev) tweet which maximised mutual information
  with locations, chosen from each location in proportion to how many tweets that location outputs each year.
- 500 pairs of words, chosen in a similar fashion to the 30 individual words.
- user id of tweet

Final learning algorithm:
(I cheated and chose two)
One-R - this selected the user id attribute, and had a ridiculously high accuracy on the training/dev data
        (73% when model build on 66% of training/dev tweets, and tested on the rest)
Naive bayes multinomial
(output included for both models)

