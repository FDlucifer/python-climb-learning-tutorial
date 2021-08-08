import matplotlib.pyplot as plt
import numpy as np

python = (85, 67, 23, 90)
java = (50, 67, 80, 14)
networking = (60, 20, 56, 22)
machine_learning = (88, 23, 40, 87)

people = ['Bob', 'Anna', 'John', 'Mark']

index = np.arange(4)
plt.bar(index, python, width=0.2, label="Python")
plt.bar(index + 0.2, java, width=0.2, label="Java")
plt.bar(index + 0.4, networking, width=0.2, label="Networking")
plt.bar(index + 0.6, machine_learning, width=0.2, label="Machine Learning")

plt.title("it skill levels")
plt.xlabel("person")
plt.ylabel("skill level")
plt.xticks(index + 0.2, people)
plt.legend(loc='upper left')
plt.ylim(0,120)

plt.show()