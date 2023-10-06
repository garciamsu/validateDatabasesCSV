import pandas as pd
from os import remove
import os

# Initialitation
password = "123456"
event = "ferialab-2-2023"
role = "visit"
rights = "any:any"


# Remove result'file
if os.path.isfile(event + ".csv"):
    remove(event + ".csv")

# Define the folder'route
root = os.getcwd()
pathname = os.path.join(root)

# Read the file source CSV
df_comma = pd.read_csv(pathname + "/source/origin.csv",
                       sep=",", encoding='latin1')
df_semi = pd.read_csv(pathname + "/source/origin.csv",
                      sep=";", encoding='latin1')
if df_comma.shape[1] > df_semi.shape[1]:
    origin = df_comma
else:
    origin = df_semi

df_comma = pd.read_csv(pathname + "/source/mirror.csv",
                       sep=";", encoding='latin1')
df_semi = pd.read_csv(pathname + "/source/mirror.csv",
                      sep=";", encoding='latin1')
if df_comma.shape[1] > df_semi.shape[1]:
    mirror = df_comma
else:
    mirror = df_semi

# Compare both CSV
print(origin.size/2)
origin = origin.drop_duplicates(['email'])
print(origin.size/2)

print("Processing information, please wait... ")
result = pd.DataFrame(
    columns=['name', 'email', 'password', 'event', 'role', 'rights'])
count = 0
for index1, row1 in origin.iterrows():
    # Get the email
    email1 = row1["email"]

    try:
        if (not (row1["email"].strip().lower() in mirror.email.values)):
            count = count + 1

            # https://es.stackoverflow.com/questions/525559/futurewarning-the-frame-append-method-is-deprecated-and-will-be-removed-from-pa
            result = pd.concat([result, pd.DataFrame({'name': row1["name"], 'email': row1["email"],
                               'password': password, 'event': event, 'role': role, 'rights': rights}, index=[0])], ignore_index=True)
    except Exception as e:
        print(row1["email"])


print(result)
print(result.size)
result.to_csv("Plantilla_usuarios.csv", encoding='latin1', index=False)
