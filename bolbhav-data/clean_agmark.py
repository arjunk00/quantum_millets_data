#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_excel("Agmark crops.xlsx")


# In[3]:


df


# In[4]:


df = df.drop(['Crop Name (Hindi)','Agmark Crop Name (Raw)','Source','Crop Name (Marathi)','Variety Name (Hindi)','Variety Name - Cleaned'], axis=1)


# In[5]:


df


# In[6]:


df.drop(['Unnamed: 8'],axis=1,inplace=True)


# In[7]:


df


# In[8]:


df.isnull().sum()


# In[9]:


df = df.dropna(how='all')


# In[10]:


df.head(20)


# In[11]:


df2={'Crop Type':['दलहनी फसलें','फलियां','सब्ज़ी','फूल','फलदार फसलें','सूखे मेवे','तिलहनी फसलें','औषधीय','अनाज','मसाले','अन्य'],'Type Meanings':['Dal','Ignore','Vegetables','Flowers','Fruits','Dry Fruits','Seeds','Medicinal','Grains','Spices','Others']}


# In[12]:


df2=pd.DataFrame(df2)


# In[13]:


df2


# In[14]:


df.drop(['Crop Types','Type Meanings'],axis=1,inplace=True)


# In[15]:


df


# In[16]:


df['Crop Type']=df['Crop Type'].map(df2.set_index('Crop Type')['Type Meanings'])


# In[17]:


df


# In[18]:


df.isnull().sum()


# In[19]:


df.to_csv("Agmark_Crops_cleaned.csv")


# In[20]:


df


# In[24]:





# In[23]:


df_final=df.loc[df['Crop Type'] == 'Grains']


# In[24]:


df_final


# In[26]:


df_final.rename(columns={'Crop Name - Cleaned':'Crop_name','Crop Type':'Crop_type'},inplace=True)


# In[27]:


df_final


# In[28]:


df_final.to_csv("Agmark_grains_list.csv")


# In[ ]:




