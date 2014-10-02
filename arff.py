
# generate input files for weka


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
