import pandas as pd
import numpy as np
#Data Creation
df = pd.read_csv("students.csv")
print(df.to_string(index=False))
# Total, Average, Percentage nikalo
subjects = ["Math","Science","English","History","Computer"]
df["Total"] = df[subjects].sum(axis=1)

df["Average"] = df[subjects].mean(axis=1)

df["Percentage"] = np.round((df["Total"] / 500 * 100),2)


#3. Grade assign
conditions = [
    df["Percentage"] >=90,
    df["Percentage"] >=80,
    df["Percentage"] >=70,
    df["Percentage"] >=60,
    df["Percentage"] >=50,
]
Grades = ["A+","A","B","C","D"]
df["Grades"] = np.select(conditions,Grades,default = "F")

#Pass/Fail show
df["Status"] = np.where(df["Percentage"] > 50, "Pass","Fail")

#Rank
df["Rank"] = df["Percentage"].rank(ascending=False).astype(int)

#summary
df = df.sort_values("Rank")

grade_distrib = df["Grades"].value_counts()

top = df[["Rank", "Name", "Percentage", "Grades"]].head(3)
bott = df[["Rank", "Name", "Percentage", "Grades"]].tail(3)

summary = df[subjects].agg(["mean","max","min","std"])

print(summary)
print(grade_distrib)
print(top)
print(bott)

df.to_csv("student_results.csv",index=False)
print(df)