# pie chart used for
'''
Percentages/shares dikhane hon
Parts ek whole ka hissa hon (sab milake 100%)
Categories 5-6 se zyada na hon
represent your data as slices of circle and show how each part contribute to the total
'''
import matplotlib.pyplot as plt
#syntax
# plt.pie(values), label=label_list,colors,autopercentage='1.1)
#1.1f%% mean format string start from here
# 1.1F MEAN one digit before the decimal and one digit after the decimal 

regions = ['North','South','East','West'] #its used as label_list
revenue = [3000,2000,1500,1000] #its used as values
plt.title('Revenue contribution by region')

plt.pie(revenue,labels=regions,autopct='%1.1f%%',colors=['gold','skyblue','green','coral',])
plt.show()