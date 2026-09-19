import matplotlib.pyplot as plt
x = ['Mon','Tues','Wed','Thrus','Frid'] # x-axis
y = [10,15,7,20,12] # y-axix
plt.plot(x,y)

plt.title('Bakery sales this week: ') #graph title

plt.xlabel('Day of the week') #set label
plt.ylabel('sales per day in this week')  #set label

plt.show()