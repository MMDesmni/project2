#Importing temporary libraries

import pandas as pd

#Read data from excel

df=pd.read_excel("kharid.xlsx")

#Save file as csv

df.to_csv('kharid.csv',index=False)

#Setting "User" coloumn as index

df.set_index("User",inplace=True)


#Simple recommendation system using function for loop and is and else statement

def recommend_items(user,df):
    user_purchases=df.loc[user]
    bought_items= []
    not_bought_items = []

#   adding items in bought_items and not_bought_items

    for item in df.coloumns:
        if user_purchases[item] == 1:
            bought_items.append(item)
        else:
            not_bought_items.append(item)
    
    recommendations = []


    #Recommendation base on same bought items or not having the same bought items

    for other_user in df.index:
        if other_user == user:
            continue

        other_purchases=df.loc[other_user]
        has_common_item= False

        for item in bought_items:
            if other_purchases[item] == 1:
                has_common_item=True
                break

        if has_common_item:
            for item in not_bought_items:
                if other_purchases[item] == 1 and item not in recommendations:
                    recommendations.append(item)
    
    return recommendations
