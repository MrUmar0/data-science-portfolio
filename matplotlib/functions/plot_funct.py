import matplotlib.pyplot as plt

#parameter
# plt.plot(z,y,color='red or FF15SF',linestyle='line_style',
#                                       linewidth=value, marker= 'symbol', label='label name)

months = [1,2,3,4]
sales = [15000,9000,69000,40005]
#---------------------------
plt.title('Total four months sales data')
plt.xlabel('months')
plt.ylabel('sales per month')
#---------------------------
#---------------------------
plt.plot(months,sales,color='blue',linestyle='--',linewidth = 2,marker = 'o',label='2026 sales data')
#---------------------------

#---------------------------
plt.legend() #present what marker represent in graph 

#OR below is optional
#plt.legend(loc='pass two location like => upper left or lower right', fontsize= value) 
#---------------------------

#---------------------------
# plt.grid() #used to show horizontal and verticale background lines
#its also customize like this
plt.grid(color='gray',linestyle=':',linewidth=1)
#---------------------------

#---------------------------
#plt.xlim() & plt.ylim()  lim mean limit
#its used to limit data according to your ranges
plt.xlim(1,4)
plt.ylim(0,75000)
#---------------------------

#---------------------------
#plt.xticks() & plt.yticks() is used to convert default numerics like 1.2 2.0 2.5 into meaningful
#used to convert default numerics like 1.2 2.0 2.5 into meaningful label like quater 1 quater2 month1
plt.xticks([1,2,3,4],['M1','M2','M3','M4'])

plt.show() #its used to show final design
