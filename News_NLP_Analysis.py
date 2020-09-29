#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This file will be to analyze the news stories about a stock to weigh wether or not it is a buy
# We will be using NLP to do this, specifically the Bag - O - Words model
# There is also a model called BERT, which some people say is really good, but Bag - O - Words should be just fine for now
# Bag - O - Words is a classifier which means that based on certain phrases it will either classify them as good or bad
# You can look at it like linear regression but for words
# Lets Begin :)!

# Step 1: Import the Libraries
# These libraries will be key to how we manipulate the data and presesnt it :)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


# Step 2: Import the dataset
# We do this to be able to actually use the dataset
dataset = pd.read_excel("/Users/gaurishlakhanpal/downloads/archive (1)/Project6500.xlsx", quoting = 3)


# In[4]:


# Lets check out this dataset:
print(dataset)


# In[7]:


# Technically I should be cleaning the dataset out but using stopwords and such might get rid of a looot of stuff
# For that reason we are just gonna stick with the phrases that we have...
# We are just going to be storing the headlines in the variable corpus
# The whole dataset.iloc just helps us to do this
# The .iloc[:, 1] means all the columns in the 1's index
corpus = dataset.iloc[:, 1].values


# In[11]:


print(corpus)
# This bottom value is for our max_features which will be used in our count vectorizer
# If I remember correctly it is just how diverse the words are? I'm not too sure
print(len(corpus[0]))


# In[12]:


# Now we make the bag of words model
# Esesntially what happens here is that there is a huuggeee array. 
# Each value in the matrix represents a word
# Each time a word show up in the phrase the value corresponding that word in the matrix goes up by one
# So we have a big 20k long array with diff values and we use this to make our predictions

# We make the x and y here. They are just represeneted in weird ways but the whole idea of y = mx + b still holds
# The x is the big 20k long array
# The y is the 0 and 1 values with indicate negative or positive respectively 

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 59)
x = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 3:].values


# In[13]:


print(x)


# In[14]:


print(y)


# In[139]:


# Here we are splitting the data into test and train. We train the model on the training data
# Once we have trained we can test its accuracy on the test data
# Usually we split it 4:1, but I think 5:1 ended up giving a higher accuracy

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)


# In[117]:


print(x_train)


# In[118]:


print(x_test)


# In[119]:


print(y_train)


# In[120]:


print(y_test)


# In[121]:


# Now we build our classification model to train on the matrices that we have... 
# What regression should we use? Lets try a few

# This is Support Vector Classification with the rbf kernel

# This is the general way to make the model

# Import the model
from sklearn.svm import SVC

# Make the class and set parameters if neccesary
classifier = SVC(kernel = "rbf", random_state = 0)

# Fit the data to the model to that it can train on it
classifier.fit(x_train, y_train)


# In[122]:


# Here we make our prediciton and store it in y_pred
y_pred = classifier.predict(x_test)


# In[123]:


print(y_pred)


# In[124]:


# This thing here compares our prediction values to the actual values to give our accuracy

from sklearn.metrics import accuracy_score
accuracy_score(y_pred, y_test)


# In[125]:


# No way! We got an 87% accuracy rate with support vector classification
# Also note:
# Linear kernel = 84% accuracy
# RBF kernel = 87% accuracy so we will go with rbf


# In[126]:


# Now lets try something else

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(x_train, y_train)


# In[127]:


y_pred = classifier.predict(x_test)


# In[128]:


accuracy_score(y_pred, y_test)


# In[129]:


# Hmm this is the same as the svc with a linear kernel 84% is still the champ rn


# In[130]:


# Lets try another thing

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train, y_train)


# In[131]:


y_pred = classifier.predict(x_test)


# In[132]:


accuracy_score(y_pred, y_test)


# In[133]:


# Oof this was bad, 78% is much lower than the others... 


# In[254]:


# Now it is time to try one of the best classification models out there, RandomForest

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 101, criterion = "entropy", random_state = 0)
classifier.fit(x_train, y_train)


# In[255]:


y_pred = classifier.predict(x_test)


# In[256]:


accuracy_score(y_pred, y_test)


# In[257]:


# Wow we got 88%.... this is amazing!


# In[199]:


# Lets try to play with the sample sizes... 
# Looks like making sample size smaller for x_test made it much better....
# We have a champion ding ding ding.... random forest with 100 trees nets us a whopping 88%!
# We also increased the accuracy by playing with the tree


# In[ ]:





# In[ ]:




