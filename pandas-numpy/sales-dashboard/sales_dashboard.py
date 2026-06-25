import pandas as pd

df = pd.read_csv("sales_data.csv")

#to check what kind of dataset this and how much rows and see data type
# print(df.head(25))

'''
To check which one product sell more
print(df["Product"].value_counts())
print(df["City"].value_counts())'''

#calculate revenue and add this column inside sales dataset
df["Revenue"] = df["Quantity"] * df["Price"]

#calculate monthly revenue
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

monthly_revenue = df.groupby("Month")["Revenue"].sum()
# print(monthly_revenue)


#Top products
top_product = df.groupby("Product")["Revenue"].sum()
# print(top_product)

#for practice just check how much total headphone quantity sell
print(df.groupby("Product")["Quantity"].sum())

city_revenue = df.groupby("City")["Revenue"].sum()
# print(city_revenue)


print("=" * 40)
print("      SALES DASHBOARD SUMMARY")
print("=" * 40)
print(f"Total Revenue:   {df['Revenue'].sum():,}")
print(f"Total Orders:    {len(df):,}")
print(f"Best Month:      {monthly_revenue.idxmax()}")
print(f"Best Product:    {top_product.idxmax()}")
print(f"Best City:       {city_revenue.idxmax()}")
print("=" * 40)
