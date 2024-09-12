#!/usr/bin/env python
# coding: utf-8

# ## Welcome to your notebook.
# 

# #### Run this cell to connect to your GIS and get started:

# In[1]:


#Script created by Donald Maruta - NCL ICB Senior Geospatial Manager - 21 Feb 24
from arcgis.gis import GIS
gis = GIS("home")


# #### Now you are ready to start!

# In[2]:


#Import Required Modules
import requests, csv, shutil
import pandas as pd
from datetime import datetime


# In[3]:


#Copy current metadata file to backup metadata file
shutil.copy2('/arcgis/home/CancerDashboard/Metadata.csv', '/arcgis/home/CancerDashboard/OldMetadata.csv')


# In[4]:


#Import Updated Metadata from FingerTips
csv = "https://fingertips.phe.org.uk/api/indicator_metadata/csv/all"
selected_columns = ['Indicator ID', 'Date updated']
new_csv_path = '/arcgis/home/CancerDashboard/Metadata.csv'


# In[5]:


#Open the URL Request
response = requests.get(csv)
response.raise_for_status()


# In[6]:


#Write to the CSV file
with open(new_csv_path, 'wb') as file:
    file.write(response.content)


# In[7]:


#Create Pandas dataframe
df_original = pd.read_csv(new_csv_path)


# In[8]:


#Rejig dataframe columns
df_selected_columns = df_original[selected_columns]
df_selected_columns.columns = ['IndicatorId', 'LastUpdatedDate']


# In[9]:


# Write the resulting DataFrame to a new CSV file
df_selected_columns.to_csv(new_csv_path, index=False)

