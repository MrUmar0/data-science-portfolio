import matplotlib.pyplot as plt

#bar chat is used for categories not used for continuous level data
'''
used for
Categories compare karni hon
Ranking dikhani ho (kon pehle, kon doosra)
Ek specific time ka snapshot ho
'''


#syntax
# plt.bar(x-axis,value like height,colorname,width=value, labelname)

product = ['A','B','C','D']
sales = [1000,1500,800,1200]
plt.xlabel('product')
plt.ylabel('sales')

plt.bar(product,sales,color='orange',label='sales 2026')
plt.title('product sales 2026')
plt.legend()
# plt.xlim('A','D')
# plt.ylim(0,2000)

plt.show()