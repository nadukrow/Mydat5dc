# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:30:53 2015

@author: nadukrow
"""
import csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv', index_col=0)

#Changing the column names
df.columns
df.rename(columns={'ReputationAtPostCreation':'Reputation', 'BodyMarkdown':'Body', 'PostCreationDate':'PostDate', 'OwnerCreationDate':'OwnerDate', 'OwnerUndeletedAnswerCountAtPostTime':'Answers', 'OpenStatus':'Status'}, inplace=True)

df.isnull().sum() #To check the column names


df['PostDate'] = pd.to_datetime(df.PostDate)
df['OwnerDate'] = pd.to_datetime(df.OwnerDate)
df['PostClosedDate'] = pd.to_datetime(df.PostClosedDate)
#Standardizing Dates...

#This is where we would create new features.
df['BodyLength'] = df.Body.apply(len)
df['TitleLength'] = df.Title.apply(len)

df['PostCount'] = 0
for item in df.sort('OwnerUserId'):


df.groupby(df.Status).PostId.describe()
df.groupby(df.Status).Answers.describe()
df.groupby(df.Status).OwnerDate.describe()
df.sort('OwnerDate')

pd.scatter_matrix(df)


dates = pd.date_range(df.PostDate.min(), df.PostDate.max(), freq='D')

print dates
print dates.shape

ts = pd.Series(df.Reputation.sum(), index=dates)
ts = ts.cumsum()
ts.plot()




#Fitting the model
feat_cols = ['PostId', 'Answers', 'OwnerUserId']
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df[feat_cols], df.Status)

#Logistic regression
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
from sklearn import metrics
metrics.accuracy_score(y_pred, y_test)


feat_cols = ['Reputation', 'Answers', 'OwnerUserId', 'BodyLength', 'TitleLength']
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df[feat_cols], df.Status)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_prob = logreg.predict_proba(X_test)

from sklearn import metrics
metrics.log_loss(y_test, y_prob)



sub = pd.DataFrame({'id':test.index, 'OpenStatus':y_prob}).set_index('id')
sub.to_csv('sub1.csv')