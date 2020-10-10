'''
NLP is used to conduct analyis on text. We will be using NLP to classify whether stock news is positive or negative.
'''

# Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Change the dataset location in your own implementation
dataset = pd.read_excel("/Users/gaurishlakhanpal/downloads/archive (1)/Project6500.xlsx", quoting = 3)

# Makes the corpus 
corpus = dataset.iloc[:, 1].values
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = len(corpus[0]))
x = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 3:].values

# Splits data into train and test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)


# Build Random Forest and predicts
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 101, criterion = "entropy", random_state = 0)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

# Returns accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score(y_pred, y_test))





