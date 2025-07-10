#Plot chart

# popular libraries like Matplotlib, Seaborn, and Plotly
##
import matplotlib.pyplot as plt
##
##x = [1,2,3,4]
##y = [20,40,60,80]
##
##plt.plot(x,y,color="red",marker="*")
##plt.grid(True)
##plt.show()


#bar chart

##x = ['A','B','C','D']
##y = [10,20,30,40]
##
##plt.bar(x,y,color='blue')
##plt.xlabel("Names")
##plt.ylabel("Marks")
##plt.grid(True)
##plt.title("Marks of students")
##plt.show()

#pie chart

##labels = ["Insta","Facebook","Whatsapp"]
##per = [30,30,40]
##color=['red','green','blue']
##
##plt.pie(per,labels=labels,autopct='%1.1f%%',startangle=120,colors=color)
##plt.title("Ratio of socialmedia")
##plt.show()


#scatter chart

##x = [5,10,15,20]
##y = [10,20,30,40]
##
##plt.scatter(x,y,color='red')
##plt.title("Value of chart")
##plt.xlabel("v1")
##plt.ylabel("v2")
##plt.grid(True)
##plt.show()


#subplot

x = [1,2,3,4]
y1 = [10,20,30,40]
plt.subplot(1,2,1)
plt.plot(x,y1)
plt.title("Square")
plt.show()



y2 = [5,10,15,20]
plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title("Reverse Square")
plt.show()









