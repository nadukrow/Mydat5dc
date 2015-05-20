# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:30:53 2015

@author: nadukrow
"""
import csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv', index_col=0) #Read in the data

df.isnull() #Exploring the data
df.isnull().sum()
df.columns
df.head()

df.groupby(df.OpenStatus).describe()

feat_cols = ['ReputationAtPostCreation'] #Begin the Logistic Regression process
X = df[feat_cols]
y = df.OpenStatus

from sklearn.cross_validation import train_test_split #Code for train, test, split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

from sklearn.linear_model import LogisticRegression #Fitting the model with an import from scikit.learn for Logsitic Regression
logreg = LogisticRegression()                       #Instantiate
logreg.fit(X_train, y_train)                        

logreg.coef_ 

y_pred = logreg.predict(X_test) #Prediction line

from sklearn import metrics #Checking the results for accuracy
metrics.accuracy_score(y_test, y_pred)

metrics.confusion_matrix(y_test, y_pred)

y_prob = logreg.predict_proba(X_test)[:, 1] #Probability predictor
metrics.roc_auc_score(y_test, y_prob)
metrics.log_loss(y_test, y_prob)


testdf = pd.read_csv('test.csv', index_col=0) #Testing on the test set
testdf.head()

logreg.fit(X, y) 

#And then make our prediction on all of the test data
test_pred = logreg.predict_proba(testdf[feat_cols])[:,1]

#Creating the submission
sub = pd.DataFrame({'id':testdf.index, 'OpenStatus':test_pred}).set_index('id')
sub.to_csv('sub1.csv')