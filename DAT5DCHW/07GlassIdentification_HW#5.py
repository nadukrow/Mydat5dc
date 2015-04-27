# -*- coding: utf-8 -*-
"""

@author: nadukrow
"""

# 1) Read data into a DataFrame
import pandas as pd
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data',
                 names=['id','ri','na','mg','al','si','k','ca','ba','fe','glass_type'],
                 index_col='id')

# 2) Briefly explore the data
df.shape
df.head()
df.tail()
df.glass_type.value_counts()

# 3) Convert to binary classification problem (1/2/3/4 maps to 0, 5/6/7 maps to 1)
import numpy as np
df['binary'] = np.where(df.glass_type < 5, 0, 1)

# 4) Create a feature matrix (X)
features = ['ri','na','mg','al','si','k','ca','ba','fe']    # create a list of features
X = df[features]                # create DataFrame X by only selecting features

# 5) Create a response vector (y)
y = df.binary

# 6) Split X and y into training and testing sets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=99)

# 7) Fit a KNN model on the training set using K=5
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 8) Take predictions on the testing set and calculate accuracy
y_pred = knn.predict(X_test)
from sklearn import metrics
print metrics.accuracy_score(y_test, y_pred)    # 90.7% accuracy

# 9) Calculate null accuracy
1 - y.mean()                                    # 76.2% null accuracy
