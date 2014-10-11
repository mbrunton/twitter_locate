# Knowledge Technology Project 2
# Mitchell Brunton
# #537642
#
# create csv files for PyML
# can use csv string in arff creation also

import feature
import utils

def create_csv(numtweets, numwords, distr_skewed, include_userid):
    loc_to_instances = feature.get_loc_to_instances_dict(numtweets, numwords, distr_skewed, include_userid)[0]
    filename = 'data/instances/'
    filename += utils.get_title(numtweets, numwords, distr_skewed, include_userid)
    filename += '.csv'
    fd = open(filename, 'w')
    fd.write(get_csv_string(loc_to_instances))
    fd.close()

def get_csv_string(loc_to_instances):
    str_list = []
    for loc in loc_to_instances:
        instances = loc_to_instances[loc]
        for instance in instances:
            str_list.append(str(instance.tweetid) + ',')
            for att in instance.attr_list:
                str_list.append(str(att) + ',')
            if instance.label:
                str_list.append(str(instance.label) + '\n')
            else:
                str_list.append('?\n')
    return ''.join(str_list)

