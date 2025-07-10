##line chart

import matplotlib.pyplot as plt

x = ["Aryan","Manav","Jitesh","Abhishek","Keval"]
y = [20,30,15,40,35]

plt.plot(x,y,color="orange",marker="o")
plt.title("Simple line Graph")
plt.xlabel("Students Names")
plt.ylabel("Marks")
plt.grid(True)
plt.show()


