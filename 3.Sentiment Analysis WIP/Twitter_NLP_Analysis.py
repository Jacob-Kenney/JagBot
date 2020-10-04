#!/usr/bin/env python
# coding: utf-8

# In[287]:


# Same old drill, just a diff dataset this time so some of the algos might also be diff

# Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[288]:


# Then we do dataset

dataset = pd.read_csv("/Users/gaurishlakhanpal/downloads/stock_data.csv")


# In[289]:


print(dataset)


# In[290]:


# Now that we have our dataset

corpus = dataset.iloc[:, 0].values


# In[291]:


print(corpus)


# In[292]:


# Lets get our max features
print(len(corpus[0]))


# In[293]:


# Now we transform the phrases into the matrix

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 95)
x = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values


# In[294]:


print(x)


# In[295]:


# We have to do this little trick to keep the shapes the same
# We probably could have also used reshape... but this works fine
y1 = []
for i in y:
    y0 = []
    y0.append(i)
    y1.append(y0)
print(np.array(y1))
y = y1


# In[296]:


# Now its the easy part we just split it and start training

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .20, random_state = 0)


# In[297]:


print(x_train)


# In[298]:


print(x_test)


# In[299]:


print(y_train)


# In[300]:


print(y_test)


# In[301]:


# Now we test some models

from sklearn.svm import SVC
classifier = SVC(kernel = "rbf", random_state = 0)
classifier.fit(x_train, y_train)


# In[302]:


y_pred = classifier.predict(x_test)


# In[303]:


# Now we test accuracy the exciting part

from sklearn.metrics import accuracy_score
accuracy_score(y_pred, y_test)


# In[304]:


# Oof that accuracy is absolute garbage
# Lets try some tweaking?
# 72.8% is the highest we get 


# In[305]:


# Lets try logistic regression lol

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(x_train, y_train)


# In[306]:


y_pred = classifier.predict(x_test)


# In[307]:


accuracy_score(y_pred, y_test)


# In[308]:


# The accuracy is decent.... its not horrendous but it could be better


# In[309]:


# Lets try something else

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train, y_train)


# In[310]:


y_pred = classifier.predict(x_test)


# In[311]:


accuracy_score(y_pred, y_test)


# In[312]:


# Accuracy wasn't too good here


# In[313]:


# Ok, time to use the one and only.... RandomForestClassification

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 102, criterion = "entropy", random_state = 0)
classifier.fit(x_train, y_train)


# In[314]:


y_pred = classifier.predict(x_test)


# In[315]:


accuracy_score(y_pred, y_test)


# In[316]:


# This hasn't been the most succesful, but do note that the dataset isn't very large either
# Looks like svc beat out our random forest... but we have some tricks left, the fight shall go on
# Lets try changing the sample size to 20% or 25% lets see what this does
# Changing the sample size didn't have a considerable impact


# In[317]:


# It seems that the highest accuracy we can get is 72.8%...


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




