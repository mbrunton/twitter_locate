
# generate input files for weka


def generate_arff_header(relation, numeric_attributes):
    s = '@RELATION ' + relation + '\n'
    for att in numeric_attributes:
        s += '@ATTRIBUTE' + att + 'NUMERIC\n'
    s += '@ATTRIBUTE location {LA,NY,C,At,SF}\n'
    s += '@DATA\n'
    return s

def generate_arff_instances(instances):
    pass
