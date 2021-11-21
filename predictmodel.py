#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
from sklearn import metrics
from sklearn.model_selection import train_test_split
import pickle


# In[7]:


data = pd.read_csv("blood_train.csv")

X = data.iloc[ : ,1:5]
y = data.iloc[ : ,-1]


# In[8]:


X_train, X_test, y_train, y_test = train_test_split(X,y , test_size = 0.3) 


# In[9]:


from sklearn.preprocessing import StandardScaler
Scaler = StandardScaler()
X_train = Scaler.fit_transform(X_train)
X_test = Scaler.fit_transform(X_test)


# In[10]:


from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=500, random_state=0)
rf.fit(X_train,y_train)


# In[11]:


y_pred = rf.predict(X_test)  


# In[13]:


pickle.dump(rf , open('predictmodel.pkl' , 'wb'))


# In[14]:


model = pickle.load(open('predictmodel.pkl' , 'rb'))


# In[ ]:




