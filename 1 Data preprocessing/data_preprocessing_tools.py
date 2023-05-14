# -*- coding: utf-8 -*-
"""Data_preprocessing_tools.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QxbVZFaOpKr80pxdnpxp7_0_a-rjubIW

# Data Preprocessing Tools

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

data = pd.read_csv('Data.csv')

# iloc takes the indexes of both the rows and columns, the rows and columns are
# separated by ','
X = data.iloc[:, :-1].values # features, all the columns except the last one
Y = data.iloc[:, -1].values # dependent variables, only the last column

print(X)

print(Y)

"""## Taking care of missing data"""

# The SimpleImputer class is used for handling missing values in a dataset
from sklearn.impute import SimpleImputer

# creates an instance of SimpleImputer with the missing_values parameter set to 
# np.nan and the strategy parameter set to 'mean'
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# fits the SimpleImputer instance imputer to the columns 1 and 2 
# (indexing starts from 0) of the array X
imputer.fit(X[:, 1:3])
# applies the transformation using the fitted SimpleImputer instance imputer to 
# the columns 1 and 2 (indexing starts from 0) of the array X
X[:, 1:3] = imputer.transform(X[:, 1:3])

print(X)

"""## Encoding categorical data

### Encoding the Independent Variable
"""

# The ColumnTransformer class is part of scikit-learn and is used for applying 
# different transformations to different columns of a dataset
from sklearn.compose import ColumnTransformer

# The OneHotEncoder class is used for converting categorical features into a 
# one-hot encoded representation. It transforms categorical variables into a 
# binary vector format where each category is represented by a binary feature column
from sklearn.preprocessing import OneHotEncoder

#  creates a ColumnTransformer named ct with a single transformation
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')

# The code x = np.array(ct.fit_transform(x)) applies the ColumnTransformer 
# transformation specified by ct to the array x, and then converts the 
# transformed result into a NumPy array.
X = np.array(ct.fit_transform(X))

print(X)

"""### Encoding the Dependent Variable"""

# The LabelEncoder class is used for encoding categorical labels (i.e., target 
# variables or class labels) with numerical values
from sklearn.preprocessing import LabelEncoder

# creates an instance of the LabelEncoder class and assigns it to the variable le
le = LabelEncoder()

# fits the LabelEncoder instance le to the array y and transforms the labels 
# into their encoded numerical representation
Y = le.fit_transform(Y)

print(Y)

"""## Splitting the dataset into the Training set and Test set"""

# The train_test_split function is commonly used for splitting a dataset into 
# training and testing subsets
from sklearn.model_selection import train_test_split

# splits the arrays X and Y into training and testing sets using the 
# train_test_split function. The resulting splits are assigned to the 
# variables X_train, X_test, Y_train, and Y_test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1) # The random_state parameter in the train_test_split function is used to set the random seed for the random number generator. By setting the random seed to a specific value, such as 1 in your example, you ensure that the random shuffling and splitting of the data will be reproducible

print(X_train)

print(X_test)

print(Y_train)

print(Y_test)

"""## Feature Scaling"""

# The StandardScaler class is used for standardizing features by removing the 
# mean and scaling to unit variance
from sklearn.preprocessing import StandardScaler

# creates an StandardScaler object
sc = StandardScaler()

# uses the fit_transform method of a StandardScaler instance to standardize a 
# subset of features in the X_train array
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])

# applies the transformation learned from the StandardScaler instance (sc) 
# to standardize a subset of features in the X_test array
X_test[:, 3:] = sc.transform(X_test[:, 3:])

print(X_train)

print(X_test)