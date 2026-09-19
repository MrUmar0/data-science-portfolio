import matplotlib.pyplot as plt

#professtion recommended way
#syntax:                                          
# figure, axess=    no. of rows, no. of columns,figuresize put as tuple (you can put both height,width)
# fig, ax = plt.subplots(nrows, ncol, figsize=(width,height))  [figsize is optional ]


fig, ax = plt.subplots(1,2, figsize= (10,5))


x = [1,2,3,4]
y = [10,25,15,20]

ax[0].plot(x,y,color='blue')
ax[0].set_title('line plot')

ax[1].bar(x,y,color='green')
ax[1].set_title('bar Chart')

fig.suptitle('comparision between line and bar charts')

#titht_layput also adjust those things like title cross chart or chats overlap
plt.tight_layout() #provide perfect and fit visual image
plt.show()