#Importing libraries that we need

import pandas as pd
import random

#Creating variables and list that we need

num_users=55
items=["Pencil","Book",'Notebook','Eraser']
data=[]

#A list that creates the list of our users
users=[f'user{i+1}'for i in range(num_users)]

#Creating shopping list using random choises

for user in users:
    purchases=[random.choice([0,1]) for _ in items]

#Chcecking that every person bought at least one thing from the shop

    if sum(purchases)==0:
        purchases[random.randint(0,3)]=1
    data.append([user]+purchases)

#Creating DataFrame
df=pd.DataFrame(data,columns=['User']+items)

#Saving as excel file
df.to_excel('kharid.xlsx',index=False)