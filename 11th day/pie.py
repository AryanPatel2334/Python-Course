#Pie chart
import matplotlib.pyplot as plt

label = ["Whatsapp","YouTube","Instagram","LinkedIn","Snapchat"]
usage = [20,40,10,20,10]
color = ["Green","Red","Pink","Blue","Yellow"]

plt.pie(usage,labels = label, autopct='%1.1f%%',startangle=90,colors = color)
plt.title("Usage of SocialMedia")
plt.show()
