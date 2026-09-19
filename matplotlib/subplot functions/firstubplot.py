import matplotlib.pyplot as plt

#syntax:
#plt.subplot(nrows,ncols,index) index should start with digit 1

x = [1,2,3,4]
y = [10,25,15,20]

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title('Line Chart')

plt.subplot(1,2,2)
plt.bar(x,y)
plt.title('Bar CHart')
plt.show()