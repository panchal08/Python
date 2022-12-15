from unicodedata import category
import pandas as pd
import os

dataframe = pd.read_excel('TOND - IRD menu items.xlsx')

channel_name = dataframe['File Name'].tolist()

assets = "/home/shubhampanchal/Python-CORE/task/assets/"
cat = "/home/shubhampanchal/Python-CORE/task/assets/category/"
menu = "/home/shubhampanchal/Python-CORE/task/assets/menuitem/"


fileCount = 0
deleteCount = 0
for filename in os.listdir(assets):   
    try:
        
        fileCount +=1
        if filename not in channel_name:
            deleteCount +=1
            os.remove(assets+filename)

    except Exception as err:
        print(err)
print(fileCount, deleteCount , fileCount-deleteCount)


fileCount = 0
deleteCount = 0
for filename in os.listdir(cat):   
    try:
        fileCount +=1
        if filename not in channel_name:
            deleteCount +=1
            os.remove(cat+filename)

    except Exception as err:
        print(err)
print(fileCount, deleteCount , fileCount-deleteCount)



fileCount = 0
deleteCount = 0
for filename in os.listdir(menu):   
    try:
        fileCount +=1
        if filename not in channel_name:
            deleteCount +=1
            os.remove(menu+filename)

    except Exception as err:
        print(err)
print(fileCount, deleteCount , fileCount-deleteCount)