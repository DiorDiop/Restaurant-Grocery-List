#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the libraries
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


grocery_list = pd.read_csv(r"D:\DOCS\Downloads\Grocery_List.csv")


# In[3]:


grocery_list


# In[6]:


# Iterate through the DataFrame and add a "Priority" column
for index, row in grocery_list.iterrows():
    quantity = row["quantity"]
    if quantity > 15:
        grocery_list.loc[index, "Priority"] = "High"
    elif 5 < quantity <= 15:
        grocery_list.loc[index, "Priority"] = "Medium"
    else:
        grocery_list.loc[index, "Priority"] = "Low"

# Print the updated DataFrame
print(grocery_list)


# In[9]:


# Save the DataFrame to a CSV file
csv_filename = "D:\DOCS\Downloads\Priority_Tracker.csv"
grocery_list.to_csv(csv_filename, index=True)


# In[ ]:




