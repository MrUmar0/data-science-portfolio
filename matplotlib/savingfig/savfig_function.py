import matplotlib.pyplot as plt

#syntax:
#filename. extension like png/jpg or pdf, dpi mean dot per inches control image resolution
    #bbox_inches = tight => is used for like reduce whitespace arund plot or crop a plot
# savefig('filename.extension',dpi = value, bbox_inches = "tight")   [#used for save figure]

x = [1,2,3,4]
y = [10,20,15,25]

plt.plot(x,y,color='blue',marker='o')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('simple line chart')

#dpi=300 used when you do some reports or publish like research
plt.savefig('linechart.png', dpi = 300, bbox_inches='tight')

#also put foldername like this
#plt.savefig('savingfig/linechart.png', dpi = 300, bbox_inches='tight')
plt.show()