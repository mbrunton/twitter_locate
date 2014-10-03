
# create csv files for PyML

import feature
import utils

def create_csv(numtweets, numwords, distr_skewed):
    loc_to_instances = feature.get_loc_to_instances_dict(numtweets, numwords, distr_skewed)[0]
    filename = 'data/instances/'
    filename += utils.get_title(numtweets, numwords, distr_skewed)
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
    return ''.join(str_list)

