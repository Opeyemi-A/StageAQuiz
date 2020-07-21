#!/usr/bin/env python
# coding: utf-8

# This data provided is from the Github link for ledsson 6 and is the fuel quality data from the Federal Energy Regulatory Commission provided by the United States Energy Information Administration. The data consists of the following columns:
# 'Record_id' : record id
# 'Utility_id_ferc1': Utility id assigned by the FERC
# 'Report_year': year of report
# 'Plant_name_ferc1': the name of the plant
# 'Fuel_type_code_pudl': the type of fuel
# 'Fuel_unit': the unit of fuel
# 'Fuel_qty_burned': the quantity of fuel burned
# 'Fuel_mmbtu_per_unit': the measure of energy per unit
# 'fuel_cost_per_unit_burned': the fuel cost per unit burned
# 'Fuel_cost_per_unit_delivered': the cost of fuel delivered per unit
# 'fuel_cost_per_mmbtu': the cost of fuel per mmbtu
# 
# Will be carrying out exploratory data analysis on this dataset.

# In[9]:


#ensure to import all necessary libraries before proceeding
import pandas as pd
import numpy as np

url='https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv'

ope_data = pd.read_csv(url, error_bad_lines=False)

ope_data


# In[82]:


ope_data.shape


# In[10]:


ope_data.describe()


# In[13]:


#check for missing values
ope_data.isnull()


# In[23]:


ope_data.isnull().sum()


# In[83]:


#dropping missing data
ope_data.dropna()


# In[26]:


#merging
fuel_df1=ope_data.iloc[0:19000].reset_index(drop=True)
fuel_df2=ope_data.iloc[19000:].reset_index(drop=True)
fuel_df1


# In[27]:


fuel_df2


# In[29]:


#check that the length of both dataframes sum to the expected length
assert len(ope_data) == len(fuel_df1) + len(fuel_df2)
len(ope_data)


# In[30]:


#inner merge
pd.merge(fuel_df1, fuel_df2, how='inner')


# In[31]:


pd.merge(fuel_df1, fuel_df2, how='outer')


# In[32]:


pd.merge(fuel_df1, fuel_df2, how='left')


# In[84]:


pd.merge(fuel_df1, fuel_df2, how='right')


# In[34]:


#check for duplicate rows
ope_data.duplicated().any()


# In[85]:


#fuel type with lowest average fuel cost per unit burned
ope_data.groupby(["fuel_type_code_pudl"])["fuel_cost_per_unit_burned"].mean()


# In[56]:


#to find the 75th percentile and standard deviation
print("75th percentile:  ", np.percentile(fuel_mmbtu, 75))
print("standard deviation: ", fuel_mmbtu.std())


# In[58]:


#skewness and kurtosis for the fuel quantity burned
print(ope_data['fuel_qty_burned'].skew())
print(ope_data['fuel_qty_burned'].kurt())


# In[86]:


#how to find correlation using the pearson method
ope_data.corr(method='pearson')


# In[49]:


#the two years with the lowest and second to lowest average fuel cost per unit burned
ope_data.groupby("report_year")["fuel_cost_per_unit_burned"].mean().sort_values()[:2]


# In[110]:


#percentage of missing values
ope_data.isna().mean() * 100





# In[113]:


ope_data['pct_change'] = ope_data.groupby(['report_year'])['fuel_cost_per_unit_burned'].pct_change()
ope_data['pct_change']


# In[68]:


#average fuel cost per unit delivered
answer = ['report_year', 'fuel_cost_per_unit_delivered']
count_1997 = 0
count_2018 = 0
count_1996 = 0
count_2004 = 0
count_2009 = 0
ope_data[answer].head()
for i in zip(ope_data[answer]['report_year'],ope_data[answer]['fuel_cost_per_unit_delivered']):
  if i[0] == 1997:
   count_1997 += i[1]
  if i[0] == 2018:
   count_2018 += i[1]
  if i[0] == 1996:
   count_1996 += i[1]
  if i[0] == 2004:
   count_2004 += i[1]
  if i[0] == 2009:
   count_2009 += i[1]

print('The average of 1997 fuel cost per unit delivered is ', count_1997 // len(ope_data))
print('The average of 2018 fuel cost per unit delivered is ', count_2018 // len(ope_data))
print('The average of 1996 fuel cost per unit delivered is ',count_1996 // len(ope_data))
print('The average of 2004 fuel cost per unit delivered is ',count_2004 // len(ope_data))
print('The average of 2018 fuel cost per unit delivered is ',count_2018 // len(ope_data))


# In[35]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#select a sample dataset
sample_df=ope_data.sample(n=100, random_state=4)
sns.regplot(x=sample_df["utility_id_ferc1"], y=sample_df["fuel_cost_per_mmbtu"], fit_reg=False)


# In[36]:


#box plot
sns.boxplot(x="fuel_type_code_pudl", y="utility_id_ferc1", palette=['r','b'], data=ope_data)


# In[ ]:




