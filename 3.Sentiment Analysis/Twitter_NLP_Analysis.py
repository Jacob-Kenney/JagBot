'''
NLP is used to conduct analyis on text. We will be using NLP to classify whether tweets about stocks are positive or negative.

'''

# Import the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Change the dataset location in your own implementation
dataset = pd.read_csv("/Users/gaurishlakhanpal/downloads/stock_data.csv")

# Makes the corpus 
corpus = dataset.iloc[:, 0].values
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = len(corpus[0]))
x = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Shapes y into 2D array
y1 = []
for i in y:
    y0 = []
    y0.append(i)
    y1.append(y0)
y = y1

# Splits data into train and test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .20, random_state = 0)

# Build Random Forest and predicts
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 102, criterion = "entropy", random_state = 0)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

# Returns accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score(y_pred, y_test))





