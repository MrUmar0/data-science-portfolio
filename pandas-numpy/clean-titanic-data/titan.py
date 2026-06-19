import seaborn as sns
import pandas as pd
df = sns.load_dataset('titanic')

print(df.info())
print(df.head())
print(df.tail())
print("\n ")
print(f'shape : {df.shape}')
print(f'Column Name: {df.columns}')
print("\n ")
# print(df.isnull())
print(df.isnull().sum())
df['age'] = df['age'].fillna(df['age'].mean()).round().astype(int)
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
df['embark_town'] = df['embark_town'].fillna(df['embark_town'].mode()[0])
df.drop(columns=['deck'], inplace=True)
print(df['age'].dtype,df['embarked'].dtype,df['embark_town'].dtype) 
print("\n ")
print(df.isnull().sum())

df.to_csv("clean_titanic_data_panda.csv",index=False)
print(df)


