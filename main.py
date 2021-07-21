import pandas as pd
import os

# Define the folder'route
root = os.getcwd()
pathname = os.path.join(root)

# Read the file source CSV
df_comma = pd.read_csv(pathname + "/source/mirror.csv", sep=",")
df_semi = pd.read_csv(pathname + "/source/mirror.csv", sep=";")
if df_comma.shape[1] > df_semi.shape[1]:
    mirror = df_comma
else:
    mirror = df_semi

df_comma = pd.read_csv(pathname + "/source/origin.csv", sep=",")
df_semi = pd.read_csv(pathname + "/source/origin.csv", sep=";")
if df_comma.shape[1] > df_semi.shape[1]:
    origin = df_comma
else:
    origin = df_semi

