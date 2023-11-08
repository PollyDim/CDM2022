#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd
from zipfile import ZipFile
from io import BytesIO
import urllib.request as urllib2

data_url = "https://api.worldbank.org/v2/en/indicator/SP.DYN.CBRT.IN?downloadformat=csv"

r = urllib2.urlopen(data_url).read()
file = ZipFile(BytesIO(r))

endata_csv = file.open("API_SP.DYN.CBRT.IN_DS2_en_csv_v2_5730954.csv")
endata = pd.read_csv(endata_csv,skiprows=4)

#endata.drop([ '2022','Unnamed: 67'], axis='columns', inplace=True)
endata.head(10)


# In[32]:


metadata_Country_csv = file.open("Metadata_Country_API_SP.DYN.CBRT.IN_DS2_en_csv_v2_5730954.csv")
metadata_Country = pd.read_csv(metadata_Country_csv)
metadata_Country


# In[15]:


metadata_Indicator_csv = file.open("Metadata_Indicator_API_SP.DYN.CBRT.IN_DS2_en_csv_v2_5730954.csv")
metadata_Indicator = pd.read_csv(metadata_Indicator_csv)
metadata_Indicator


# In[18]:


for i in range(0, 10):
    print(F"{i} - {metadata_Country.SpecialNotes[i]}")


# In[19]:


metadata_Country[0:10].style.set_properties(subset=["SpecialNotes"], **{"width": "400px", "text-align": "left"})


# In[33]:


print(endata.columns)


# In[16]:


countries = endata['Country Name'].unique()
print(F"Number of Countries: {len(countries)}")
print(countries)


# In[41]:


endata.info()


# In[38]:


date_list = endata.columns.unique()
first_index = 4
last_index = 65
period = last_index-first_index
print(F"Starting on {endata.columns[first_index]}, ending on {endata.columns[last_index]}; with {period} periods.")


# In[51]:


data_slice = endata[[ "Country Name","1960", "2021"]]
#.sort_values("Attack Rate (per 1000)", ascending=False)
data_slice[0:6].style.set_properties(**{"width": "200px", "text-align": "left"})


# In[165]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

drawing = pd.pivot_table(data_slice[0:6], values=["1960","2021"], columns=["Country Name"])
drawing.plot(figsize=(20,10), grid=False)


# In[167]:


import seaborn as sns

sm = sns.FacetGrid(data_slice[0:6], col="Country Name", col_wrap=6, height=3, aspect=2, margin_titles=True) 
sm = sm.map(plt.plot,"1960","2021")



sm.set_titles("{col_name}", size=22).set_ylabels(size=20).set_yticklabels(size=15)\
                                    .set_xlabels(size=20).set_xticklabels(size=15, rotation=40)