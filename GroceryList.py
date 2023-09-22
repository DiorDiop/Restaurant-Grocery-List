#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the libraries
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


# Sample data in multiple dictionaries
# Fresh_Produce

Fresh_Produce = {
    "Apples": {"weight": 2.5, "price_per_kg": 1.50},
    "Bananas": {"weight": 2.0, "price_per_kg": 2.50},
    "Strawberries": {"weight": 0.5, "price_per_kg": 1.50},
    "Avocados": {"weight": 1.5, "price_per_kg": 0.50},
    "Bell Peppers": {"weight": 4.5, "price_per_kg": 1.42},
    "Carrots": {"weight": 2.5, "price_per_kg": 1.57},
    "Potatoes": {"weight": 3.5, "price_per_kg": 2.50},
    "Spinach": {"weight": 1.5, "price_per_kg": 1.50},
    "Tomatoes": {"weight": 6.5, "price_per_kg": 4.50},
    "Mangoes": {"weight": 5.5, "price_per_kg": 5.50},
    "Kiwi": {"weight": 2.5, "price_per_kg": 5.50},
    "Papaya": {"weight": 5.5, "price_per_kg": 5.50},
    "Peaches": {"weight": 10.0, "price_per_kg": 7.51},
    "Pears": {"weight": 2.5, "price_per_kg": 5.50},
    "Watermelon": {"weight": 10.5, "price_per_kg": 10.50}
}


# In[3]:


# Grains

Grains = {
    "Breadcrumbs": {"weight": 1.5, "price_per_kg": 12.50},
    "Pasta": {"weight": 2.5, "price_per_kg": 5.50},
    "Quinoa": {"weight": 0.5, "price_per_kg": 1.50},
    "Rice": {"weight": 5.0, "price_per_kg": 1.50},
    "Sandwich Bread": {"weight": 1.5, "price_per_kg": 1.50},
    "Tortillas": {"weight": 1.5, "price_per_kg": 1.50},
    "Oatmeal": {"weight": 10.5, "price_per_kg": 2.50},
    "Barley": {"weight": 1.5, "price_per_kg": 3.50},
    "Bulgur": {"weight": 1.5, "price_per_kg": 1.50},
    "Couscous": {"weight": 1.5, "price_per_kg": 2.50},
    "Cornmeal": {"weight": 1.5, "price_per_kg": 3.50},
    "Whole wheat tortillas": {"weight": 0.5, "price_per_kg": 2.50},
    "Farro": {"weight": 0.5, "price_per_kg": 5.50},
    "Millet": {"weight": 0.5, "price_per_kg": 4.50},
    "Wild rice": {"weight": 12.5, "price_per_kg": 1.50}
}


# In[4]:


# Meat

Meat = {
    "Chicken breasts": {"weight": 2.5, "price_per_kg": 5.50},
    "Ground beef": {"weight": 5.5, "price_per_kg": 8.50},
    "Pork chops": {"weight": 0.5, "price_per_kg": 15.50},
    "Salmon fillets": {"weight": 12.5, "price_per_kg": 25.50},
    "Turkey": {"weight": 2.5, "price_per_kg": 5.50},
    "Bacon": {"weight": 10.5, "price_per_kg": 35.50},
    "Lamb chops": {"weight": 5.5, "price_per_kg": 15.50},
    "Shrimp": {"weight": 0.5, "price_per_kg": 5.50},
    "Tilapia fillets": {"weight": 0.5, "price_per_kg": 9.50},
    "Sausages": {"weight": 1.5, "price_per_kg": 7.50},
    "Beef steaks": {"weight": 2.5, "price_per_kg": 15.50},
    "Ground turkey": {"weight": 3.5, "price_per_kg": 12.50},
    "Pork tenderloin": {"weight": 1.5, "price_per_kg": 5.50},
    "Ham": {"weight": 3.5, "price_per_kg": 6.50},
    "Duck breast": {"weight": 7.5, "price_per_kg": 8.50}
}


# In[5]:


# Dairy

Dairy = {
    "Milk": {"quantity": 2, "price_per_unit": 8.50},
    "Eggs": {"quantity": 2, "price_per_unit": 5.50},
    "Butter": {"quantity": 3, "price_per_unit": 7.50},
    "Yogurt": {"quantity": 25, "price_per_unit": 2.50},
    "Cheese": {"quantity": 7, "price_per_unit": 10.50},
    "Sour cream": {"quantity": 5, "price_per_unit": 18.50},
    "Cottage cheese": {"quantity": 1, "price_per_unit": 12.50},
    "Cream cheese": {"quantity": 5, "price_per_unit": 11.50},
    "Heavy cream": {"quantity": 2, "price_per_unit": 7.50},
    "Whipping cream": {"quantity": 3, "price_per_unit": 8.50},
    "Buttermilk": {"quantity": 4, "price_per_unit": 6.50},
    "Ricotta cheese": {"quantity": 1, "price_per_unit": 15.50},
    "Parmesan cheese": {"quantity": 2, "price_per_unit": 14.50},
    "Gouda cheese": {"quantity": 7, "price_per_unit": 18.50},
    "Goat cheese": {"quantity": 6, "price_per_unit": 28.50}
}


# In[6]:


# Baking_Goods

Baking_Goods = {
    "Baking powder": {"quantity": 2, "price_per_unit": 2.50},
    "Baking Soda": {"quantity": 6, "price_per_unit": 8.50},
    "Granulated Sugar": {"quantity": 10, "price_per_unit": 3.50},
    "Brown Sugar": {"quantity": 3, "price_per_unit": 5.50},
    "Flour": {"quantity": 2, "price_per_unit": 1.50},
    "Honey": {"quantity": 5, "price_per_unit": 2.50},
    "Vanilla Extract": {"quantity": 3, "price_per_unit": 2.50},
    "Dry Yeast": {"quantity": 6, "price_per_unit": 2.50},
    "Chocolate Chips": {"quantity": 10, "price_per_unit": 2.50},
    "Cocoa Powder": {"quantity": 5, "price_per_unit": 1.50},
    "Powdered Sugar": {"quantity": 5, "price_per_unit": 2.50},
    "Food coloring": {"quantity": 2, "price_per_unit": 3.50},
    "Sprinkles": {"quantity": 5, "price_per_unit": 1.50},
    "Powdered sugar": {"quantity": 6, "price_per_unit": 2.50},
    "Almond extract": {"quantity": 6, "price_per_unit": 8.50}
}


# In[7]:


# Freezer

Freezer = {
    "Berries": {"quantity": 5, "price_per_unit": 2.50},
    "Frozen Veggies": {"quantity": 2, "price_per_unit": 3.50},
    "Juice Concentrate": {"quantity": 3, "price_per_unit": 1.50},
    "Pizza": {"quantity": 10, "price_per_unit": 5.50},
    "Convenience Meals": {"quantity": 5, "price_per_unit": 8.50},
    "Pie Crust": {"quantity": 2, "price_per_unit": 6.50},
    "Cookie Dough": {"quantity": 3, "price_per_unit": 4.50},
    "Shrimp": {"quantity": 4, "price_per_unit": 1.50},
    "Ice cream": {"quantity": 2, "price_per_unit": 4.50},
    "dumplings": {"quantity": 1, "price_per_unit": 3.50},
    "appetizers": {"quantity": 4, "price_per_unit": 2.50},
    "seafood": {"quantity": 10, "price_per_unit": 9.50},
    "Waffles": {"quantity": 15, "price_per_unit": 7.50},
    "Pancakes": {"quantity": 7, "price_per_unit": 5.50},
    "Potstickers": {"quantity": 6, "price_per_unit": 2.50}
}


# In[8]:


# Canned

Canned = {
    "Chicken stock": {"quantity": 4, "price_per_unit": 7.50},
    "Broth": {"quantity": 2, "price_per_unit": 1.50},
    "Salsa": {"quantity": 6, "price_per_unit": 2.50},
    "Diced Tomatoes": {"quantity": 5, "price_per_unit": 3.50},
    "Jam": {"quantity": 2, "price_per_unit": 2.50},
    "Jelly": {"quantity": 6, "price_per_unit": 1.50},
    "Peanut Butter": {"quantity": 4, "price_per_unit": 4.50},
    "Pasta Sauce": {"quantity": 10, "price_per_unit": 3.50},
    "Beans": {"quantity": 3, "price_per_unit": 2.50},
    "Soups": {"quantity": 5, "price_per_unit": 1.50},
    "Tuna": {"quantity": 6, "price_per_unit": 2.50},
    "Green Chiles": {"quantity": 6, "price_per_unit": 2.50},
    "Canned Veggies": {"quantity": 5, "price_per_unit": 2.50},
    "Coffee": {"quantity": 10, "price_per_unit": 2.50},
    "Tea": {"quantity": 15, "price_per_unit": 2.50}
}


# In[9]:


# Condiments

Condiments = {
    "Black Pepper": {"quantity": 1, "price_per_unit": 1.50},
    "Chili Powder": {"quantity": 2, "price_per_unit": 2.50},
    "Cinnamon": {"quantity": 3, "price_per_unit": 3.50},
    "Crushed Red Pepper": {"quantity": 5, "price_per_unit": 0.50},
    "Cumin": {"quantity": 4, "price_per_unit": 2.50},
    "Garlic Powder": {"quantity": 5, "price_per_unit": 5.50},
    "Ketchup": {"quantity": 15, "price_per_unit": 2.50},
    "Mustard": {"quantity": 10, "price_per_unit": 2.50},
    "Mayo": {"quantity": 25, "price_per_unit": 3.50},
    "Nutmeg": {"quantity": 5, "price_per_unit": 2.50},
    "Paprika": {"quantity": 3, "price_per_unit": 2.50},
    "Salt": {"quantity": 5, "price_per_unit": 1.50},
    "Soy Sauce": {"quantity": 5, "price_per_unit": 4.50},
    "Steak Sauce": {"quantity": 15, "price_per_unit": 3.50},
    "Buffalo Sauce": {"quantity": 15, "price_per_unit": 4.50}
}


# In[10]:


# Oils_Vinegars

Oils_Vinegars = {
    "Coconut Oil": {"quantity": 5, "price_per_unit": 15.50},
    "Olive Oil": {"quantity": 5, "price_per_unit": 25.50},
    "Vegetable": {"quantity": 15, "price_per_unit": 4.50},
    "Canola Oil": {"quantity": 1, "price_per_unit": 14.50},
    "Peanut oil": {"quantity": 1, "price_per_unit": 24.50},
    "Avocado oil": {"quantity": 5, "price_per_unit": 34.50},
    "Sesame oil": {"quantity": 5, "price_per_unit": 24.50},
    "Grapeseed oil": {"quantity": 5, "price_per_unit": 34.50},
    "Walnut oil": {"quantity": 5, "price_per_unit": 24.50},
    "Apple cider vinegar": {"quantity": 10, "price_per_unit": 14.50},
    "Balsamic vinegar": {"quantity": 5, "price_per_unit": 25.50},
    "Red Wine Vinegar": {"quantity": 10, "price_per_unit": 30.50},
    "White Vinegar": {"quantity": 15, "price_per_unit": 25.50},
    "Cooking Wine": {"quantity": 15, "price_per_unit": 25.50},
    "White Wine Vinegar": {"quantity": 5, "price_per_unit": 34.50}
}


# In[11]:


# List of dictionaries to update
dictionaries_to_update = [Fresh_Produce, Grains, Meat, Dairy, Baking_Goods, Freezer, Canned, Condiments, Oils_Vinegars]


# In[12]:


# Iterate through each dictionary and update key names
for dictionary in dictionaries_to_update:
    for item, data in dictionary.items():
        if "weight" in data:
            data["quantity"] = data.pop("weight")
        if "price_per_kg" in data:
            data["price_per_unit"] = data.pop("price_per_kg")


# In[13]:


# Display one of the updated dictionaries as an example
print("Updated_Fresh_Produce:")
print(Fresh_Produce)
print("Updated_Grains:")
print(Grains)
print("Updated_Meat:")
print(Meat)


# In[14]:


# Create DataFrames from the dictionaries
df_fresh_produce = pd.DataFrame.from_dict(Fresh_Produce, orient='index')
df_grains = pd.DataFrame.from_dict(Grains, orient='index')
df_meat = pd.DataFrame.from_dict(Meat, orient='index')
df_dairy = pd.DataFrame.from_dict(Dairy, orient='index')
df_baking_goods = pd.DataFrame.from_dict(Baking_Goods, orient='index')
df_freezer = pd.DataFrame.from_dict(Freezer, orient='index')
df_canned = pd.DataFrame.from_dict(Canned, orient='index')
df_condiments = pd.DataFrame.from_dict(Condiments, orient='index')
df_oils_vinegars = pd.DataFrame.from_dict(Oils_Vinegars, orient='index')


# In[15]:


# Define the conversion function
def convert_to_dollars(price):
    return f"${price:.2f}"

# Sample data in multiple dictionaries

# Convert prices to dollars in all DataFrames
df_fresh_produce['price_per_unit'] = df_fresh_produce['price_per_unit'].apply(convert_to_dollars)
df_grains['price_per_unit'] = df_grains['price_per_unit'].apply(convert_to_dollars)
df_meat['price_per_unit'] = df_meat['price_per_unit'].apply(convert_to_dollars)
df_dairy['price_per_unit'] = df_dairy['price_per_unit'].apply(convert_to_dollars)
df_baking_goods['price_per_unit'] = df_baking_goods['price_per_unit'].apply(convert_to_dollars)
df_freezer['price_per_unit'] = df_freezer['price_per_unit'].apply(convert_to_dollars)
df_canned['price_per_unit'] = df_canned['price_per_unit'].apply(convert_to_dollars)
df_condiments['price_per_unit'] = df_condiments['price_per_unit'].apply(convert_to_dollars)
df_oils_vinegars['price_per_unit'] = df_oils_vinegars['price_per_unit'].apply(convert_to_dollars)


# In[16]:


# Add a column 'Category' to each DataFrame to identify the category
df_fresh_produce['Category'] = 'Fresh_Produce'
df_grains['Category'] = 'Grains'
df_meat['Category'] = 'Meat'
df_dairy['Category'] = 'Dairy'
df_baking_goods['Category'] = 'Baking_Goods'
df_freezer['Category'] = 'Freezer'
df_canned['Category'] = 'Canned'
df_condiments['Category'] = 'Condiments'
df_oils_vinegars['Category'] = 'Oils_Vinegars'


# In[17]:


# Display the tables
print("Fresh Produce:")
print(df_fresh_produce)

print("\nGrains:")
print(df_grains)

print("\nMeat:")
print(df_meat)

print("\nDairy:")
print(df_dairy)


# In[18]:


# Join all the tables
Grocery_List = pd.concat([df_fresh_produce, df_grains, df_meat, df_dairy, df_baking_goods, df_freezer, df_canned, df_condiments, df_oils_vinegars])


# In[19]:


# Display all the tables
print("Grocery_List:")
print(Grocery_List)


# In[20]:


# Save the DataFrame to a CSV file
csv_filename = "D:\DOCS\Downloads\Grocery_List.csv"
Grocery_List.to_csv(csv_filename, index=True)


# In[21]:


# Convert 'price_per_unit' to a numeric format (float)
Grocery_List["price_per_unit"] = Grocery_List["price_per_unit"].str.replace("$", "", regex=True).astype(float)


# In[22]:


Grocery_List = Grocery_List.sort_values(by='price_per_unit')

# Display the sorted DataFrame
print(Grocery_List)


# In[24]:


# Count the number of products in each category
category_price_sum = Grocery_List.groupby('Category')['price_per_unit'].sum().sort_values()

# Create a bar chart
plt.figure(figsize=(10, 6))
category_price_sum.plot(kind='bar', color='black')
plt.title('Total Price per Category')
plt.xlabel('Category')
plt.ylabel('Total Price per Category in Dollar')

# Display the bar chart
plt.xticks(rotation=45)  # Rotate the category labels for better readability
plt.tight_layout()
plt.show()


# In[ ]:




