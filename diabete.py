# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 07:32:00 2020

@author: Subhasmita Panda
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dia=pd.read_csv("D:\\Subhajit\\DataSet_Practice\\diabetes\\diabetes.csv")

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(path, names=names)
array = dia.values

X = array[:,0:8]
Y = array[:,8]

test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(X,Y)

set_printoptions(precission=2)

from sklearn.decomposition import PCA
pca=PCA(n_components=3)
fit=pca.fit(X)
print(fit.components_)

from sklearn.ensemble import ExtraTreesClassifier
model=ExtraTreesClassifier()
model.fit(X,Y)
print(model.feature_importances_)



