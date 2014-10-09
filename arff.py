
# generate input files for weka

import feature
import csv
import utils

def generate_arff_header(relation, numeric_attributes):
    s = '@RELATION ' + relation + '\n'
    s += '@ATTRIBUTE id NUMERIC\n'
    for att in numeric_attributes:
        s += '@ATTRIBUTE ' + att + ' NUMERIC\n'
    s += '@ATTRIBUTE location {LA,NY,C,At,SF}\n'
    s += '@DATA\n'
    return s

def create_arff_from_csv(csv_file, arff_file, relation, numeric_attributes):
    body = open(csv_file, 'r').read()
    header = generate_arff_header(relation, numeric_attributes)
    open(arff_file, 'w').write(header + body)

def generate_arff_body(instances):
    str_list = []
    for ins in instances:
        str_list.append(str(ins.tweetid) + ',')
        attr_list = ins.attr_list
        for att in attr_list:
            str_list.append(str(att) + ',')
        if ins.label:
            str_list.append(ins.label)
        else:
            str_list[-1] = str_list[-1][:-1]
        str_list.append('\n')
    return ''.join(str_list)

def create_arff(numtweets, numwords, numpairs, distr_skewed, include_userid):
    loc_to_instances, words, pairs = feature.get_loc_to_instances_dict(numtweets, numwords, 
                                                    numpairs, distr_skewed, include_userid)
    filename = 'data/instances/'
    title = utils.get_title(numtweets, numwords, numpairs, distr_skewed, include_userid)
    filename += title
    filename += '.arff'
    fd = open(filename, 'w')
    if include_userid:
        numeric_attributes = ['userid']
    else:
        numeric_attributes = []
    numeric_attributes += words[:]
    for (w1, w2) in pairs:
        numeric_attributes.append( w1 + '_' + w2 )
    head = generate_arff_header(title, numeric_attributes)
    body = csv.get_csv_string(loc_to_instances)
    fd.write(head + body)

def create_arff_using_attributes(numtweets, attributes):
    words = [att for att in attributes if '_' not in att]
    pairs = [tuple(att.split('_')) for att in attributes if '_' in att]
    loc_to_instances = feature.get_loc_to_instances_from_attributes(numtweets, words, pairs)
    filename = 'data/selected_attributes/' 
    title = str(numtweets) + 'twts_' + 'custom_attributes_instances'
    filename += title + '.arff'
    fd = open(filename, 'w')
    numeric_attributes = words[:]
    for (w1, w2) in pairs:
        numeric_attributes.append( w1 + '_' + w2 )
    head = generate_arff_header(title, numeric_attributes)
    body = csv.get_csv_string(loc_to_instances)
    fd.write(head + body)










