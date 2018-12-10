import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

source = 'C:/Users\Dell\Downloads\ml-20m\ml-20m/'
rating = pd.read_csv(source + 'ratings.csv', sep=',')

rating.head()

