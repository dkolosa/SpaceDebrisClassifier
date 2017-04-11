import json
from pprint import pprint

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz


# Get the json satcat dataset
with open('SatCatdata.json') as dataset:
	data = json.load(dataset)

# pprint(data)

# Vectorize the json dict

from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer()

vec.fit_transform(data).toarray()
vec.get_feature_names()

