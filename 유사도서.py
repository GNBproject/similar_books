#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import sys


# In[2]:


from ast import literal_eval


# In[3]:


from sklearn.metrics.pairwise import cosine_similarity


# In[33]:


try:
    df = pd.read_csv(argv[1],index_col=None,converters = {"embedding":literal_eval})
except:
    printf("read_csv failed. check file name and format")


# In[34]:


try:
    embeddings = df['embedding'].values.tolist()
except:
    printf("embedding column does not exist")


# In[36]:


embeddings = pd.DataFrame(embeddings)


# In[38]:


embeddings = embeddings.astype(np.float32) #float 32 로 바꾸어서 속도와 메모리 공간을 줄였다. -> 정확도는 절반정도로 낮춤


# In[12]:


# isbn 기준 -> 다른키 기준으로 하려면 밑에 3개의 isbn 을 column 이름으로 대체


# In[45]:


similar_df = pd.DataFrame(columns = ['isbn','similar_books']) #유사 책들을 저장할 Dataframe


# In[47]:


for cut in range(int((embeddings.index.stop)/10)): # macbook pro 기준 100개 20초: 만개에 2000초-> 30분: 10만개에 300분 -> 5시간
    if(cut%10==0):
        print(cut,'....')
    embeddings_cut = embeddings[(cut)*10:(cut+1)*10]
    similarity = pd.DataFrame(cosine_similarity(embeddings_cut,embeddings))
    similarity = similarity.set_index(embeddings_cut.index)
    for index in similarity.index:
        sim_list = similarity.loc[index].sort_values(ascending=False).index.tolist()[1:11]
        similar_isbn = df['isbn'][sim_list].values.tolist()
        similar_books = ' '.join(map(str,similar_isbn))
        similar_df.loc[index] = [df['isbn'][index],similar_books]


# In[ ]:


try:
    similar_df.to_csv(argv[2],index=False)
except:
    print("pd.to_csv failed. check file name")


# In[ ]:




