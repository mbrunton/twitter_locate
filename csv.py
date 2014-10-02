
# create csv files for PyML

def create_csv(filename, loc_to_instances_dict):
    fd = open(filename, 'w')
    for loc in loc_to_instances_dict:
        instances = loc_to_instances_dict[loc]
        for instance in instances:
            fd.write(str(instance.tweetid) + ',')
            for att in instance.attr_list:
                fd.write(str(att) + ',')
            if instance.label:
                fd.write(str(instance.label) + '\n')
    fd.close()

