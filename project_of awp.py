#!/usr/bin/env python
# coding: utf-8

# In[1]:


#load libraries
import pandas as pd
import numpy as np
import warnings 
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#load data 
df=pd.read_csv("matches.csv")
df


# In[3]:


#load a first 5 data in dataset
df.head()


# In[4]:


##check datatypes in dataset
df.dtypes


# In[5]:


#load last 5 data in dataset
df.tail()


# In[6]:


#shape of  dataset
df.shape


# In[7]:


#to count of dataset
df.count()


# In[8]:


#total season in dataset
df["season"].unique()


# In[9]:


#total team in dataset
a=df["team1"].unique()
print(a)


# In[10]:


#which city play match in given dataset
b=df["city"].unique()
print(b)


# In[11]:


#show result 
s=df["result"].unique()
S=df["result"].value_counts()
print(s)
print(S)


# In[12]:


#show venue of dataset
df["venue"].value_counts()


# In[13]:


#how many matches wegot in the dataset?
df["id"].max()


# In[14]:


#palyer of match in dataset
df["player_of_match"].value_counts()


# In[15]:


#To show the toss decision of teams?
df["toss_decision"].value_counts()


# In[16]:


#which team win most match in ipl?
df["winner"].value_counts()


# In[17]:


#differnt type of data in dataset
df.info()


# In[18]:


#find empty in dataset
df.empty


# In[19]:


#size of dataset
df.size


# In[20]:


#find columns in data set
df.columns


# In[21]:


#find dimension
df.ndim


# In[22]:


#memiry usage by dataset
df.memory_usage()


# In[23]:


#use pop function
df["date"].pop


# In[24]:


#show null
df.isnull()
#fill null values by 0
df.fillna(0)


# In[25]:


#show in row format
for i,j in df.iterrows():
    print(i, j)
    print()


# In[26]:


# use of len function 
len(df["city"].unique())


# In[27]:


#which team hod won by maximum runs?
df.iloc[df["win_by_runs"].idxmax()]


# In[28]:


#which teams had won by maximum wikets?
df.iloc[df["win_by_wickets"].idxmax()]["winner"]


# In[29]:


#which season had most number of matches?
sns.countplot(x="season",data=df)
plt.show()


# In[30]:


#the most successful ipl team
sns.countplot(y="winner",data=df)
plt.show()


# In[31]:


d=df.winner.value_counts()
sns.barplot(y=d.index,x=d,orient="h");


# In[32]:


#toss winning helped in match winning?
s=df["toss_winner"]==df["winner"]
s.groupby(s).size()


# In[33]:


sns.countplot(df["toss_winner"]==df["winner"])
plt.show()


# In[34]:


#which teams has win most matches
df["winner"].value_counts()


# In[35]:


#show in cross table of all teams 
pd.crosstab(df["winner"],df["season"])


# In[36]:


#who have beenthe most experienced umpires?
(df.umpire1.value_counts()+df.umpire2.value_counts()).sort_values(ascending=False).head(10)


# In[37]:


#total team1 and team2 play match  
(df.team1.value_counts()+df.team2.value_counts()).sort_values(ascending=False).head(10)


# In[38]:


#team proformance
df[df["win_by_runs"]>0].groupby(["winner"])["win_by_runs"].apply(np.median).sort_values(ascending=False)


# In[39]:


#boxplot of team proformance
sns.boxplot(y="winner",x="win_by_runs",data=df[df["win_by_runs"]>0],orient="h")
plt.show()


# In[40]:


df[df["win_by_wickets"]>0].groupby(["winner"])["win_by_wickets"].apply(np.median).sort_values(ascending=False)


# In[41]:


sns.boxplot(y="winner",x="win_by_wickets",data=df[df["win_by_wickets"]>0],orient="h")
plt.show()


# In[ ]:





# In[ ]:




