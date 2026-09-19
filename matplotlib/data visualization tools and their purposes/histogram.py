import matplotlib.pyplot as plt

#when it is used 
'''
Ek numeric column ka spread dekhna ho
Average ke aas paas kitna data hai
Outliers hain ya nahi dekhna ho
'''
#used to show distribution of continuous data by dividing into ranges(mean bins) 
#group your continuous data into bins mean interval and show frequencey of each data in each range

#syntax 
# plt.hist(data, bins=numnber_of_bins, color=colorname, edgecolor='' edge mean border)

#what does mean bins
'''
Quantity 1-25 hai — bins=5 karo toh:
[1-5] [6-10] [11-15] [16-20] [21-25]
har range mein kitne orders hain woh bar dikhata hai'''

scores = [45,67,89,56,78,69,92,19,45,95,77,46,94,25,66,94,11,43,99,55,16,73,47]
plt.hist(scores,bins=5,color='purple',edgecolor='black')
plt.xlabel('score range')
plt.ylabel('number of students')
plt.title('score distribution of student')

plt.show()