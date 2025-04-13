##DATAFRAME FİLTRELEME
import pandas as pd
"""
student=[
    {"name":"Aylin","surname":"Gelmez","email":"aylin@gmail.com"},
     {"name":"Ahmet","surname":"Mattia","email":"ahmet@gmail.com"}
]
 
df=pd.DataFrame(student)
print(df)
"""

df= pd.read_csv("3.hafta/1day/Salary_Data.csv")

"""
print(df)
gender_filter=df['Gender']=='Male'
print(gender_filter)
"""
"""print(df[df["Job Title"]=="Software Engineer"])"""

"""print(df[(df["Job Title"]=="Software Engineer") & (df["Gender"]=="Female")])"""
pd.set_option('display.max_columns', None)

print(df[(df["Job Title"] == "Software Engineer") & (df["Gender"] == "Female")])
print(df[~(df["Job Title"]=="Software Engineer")])
print(df[df["Age"] >=30])
print(df[(df["Age"] >=30)& (df["Age"]<40)])