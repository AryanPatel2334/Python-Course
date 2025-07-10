#Bar chart

import matplotlib.pyplot as plt

x = ["A","B","C","D"]
y = [20,40,25,50]

plt.bar(x,y,color="green")
plt.title("Marks of students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
