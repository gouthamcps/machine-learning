# -*- coding: utf-8 -*-
"""
Created on Wed May  9 17:39:21 2018

@author: laptop
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dataset=pd.read_csv('winemag-data-130k-v2.csv')
#To print the first 10 records
dataset.head(10)
#To display a bar chart
dataset['province'].value_counts().head(10).plot.bar()
#To display data in terms of percentage through a bar chart
(dataset['province'].value_counts().head(10)/len(dataset)).plot.bar()
print(dataset['province'].value_counts().head(10))
#To plot data as a line and area charts
dataset['points'].value_counts().sort_index().plot.bar()
dataset['points'].value_counts().sort_index().plot.line()
#Histogram is used for interval data
dataset[dataset['price']<200]['price'].value_counts().plot.hist()
#Main disadvantage of a histogram is that because they split data in to even intervals, they cannot work well with skewed data
dataset['points'].plot.hist()
dataset['points'].plot.bar()
#The above discussed problem can be seen by observing the bar chart and the histogram of province data
#In the bar chart, data is plotted per province whereas in a histogram, the data is divided into ranges and plotted per each interval rather than plkotiing per province making the visualization skewed
dataset['province'].value_counts().sort_index().plot.line()

