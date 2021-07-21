import pandas as pd
from os import remove
import os

#Remove result'file
remove("result.csv")

# Define the folder'route
root = os.getcwd()
pathname = os.path.join(root)

#pd.read_csv(gdp_path, sep='\t', engine='python')
#, encoding='utf-8'
#encoding='latin1'

# Read the file source CSV
df_comma = pd.read_csv(pathname + "/source/origin.csv", sep=",",encoding='latin1')
df_semi = pd.read_csv(pathname + "/source/origin.csv", sep=";",encoding='latin1')
if df_comma.shape[1] > df_semi.shape[1]:
    origin = df_comma
else:
    origin = df_semi

df_comma = pd.read_csv(pathname + "/source/mirror.csv", sep=",", encoding='latin1')
df_semi = pd.read_csv(pathname + "/source/mirror.csv", sep=";", encoding='latin1')
if df_comma.shape[1] > df_semi.shape[1]:
    mirror = df_comma
else:
    mirror = df_semi

#Compare both CSV
print(origin.size/2)
origin = origin.drop_duplicates(['email'])
print(origin.size/2)

print("Processing information, please wait... ")
result = pd.DataFrame(columns=['name', 'email'])
count = 0
for index1, row1 in origin.iterrows():
    # Get the email
    email1 = row1["email"]
    
    if (row1["email"] == "mayreebok@hotmail.com"):
        print(row1["name"] + " " + row1["email"])
        
    if (not (row1["email"] in mirror.email.values)):
        count = count + 1
        result.append(row1)
        result=result.append({'name' : row1["name"] , 'email' : row1["email"]} , ignore_index=True)
    
print(result)
print(result.size)
result.to_csv('result.csv', encoding ='latin1', index=False)