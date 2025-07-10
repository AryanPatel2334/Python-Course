#Bar chart

import matplotlib.pyplot as plt

students = ["Aryan","Abhishek","Jitesh","Keval","Bhargav"]
maths = [50,40,33,44,30]
english = [30,20,47,50,25]

plt.bar(students,maths, label='Maths', color='red')
plt.bar(students,english, label='English', color='blue')
plt.title("Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

