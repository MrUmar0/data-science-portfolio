import matplotlib.pyplot as plt

#scatter plot is used 
#to find corelation between two variables 
#one is input variable which is independent
#second one is dependent variable which os output variable

#syntax
# plt.scatter(x,y,color=colorname,marker='name symbol',label= 'label name')

study_hours = [1,2,3,4,5,6,7,8]
exam_score = [40,49,60,68,75,83,89,95]
plt.scatter(study_hours,exam_score,color='green',marker='o',label='student score data')
plt.xlabel('hours studied')
plt.ylabel('exam score')
plt.title('Relationship between study hours and exam score')
plt.legend()
plt.grid(True)
plt.show()


'''
scatter plot is used in ML for visualize prediction values or actual values and also check
        is this model fit perfectly under this circumstances or not
'''