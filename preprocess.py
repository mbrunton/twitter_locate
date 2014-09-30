# Preprocess raw twitter data

import re


line_re = re.compile(r'[0-9]+\t[0-9]+\t[^\t]+\t[0-9\-]{10} [0-9:]{8}')

