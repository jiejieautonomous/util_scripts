import numpy as numpy
import matplotlib.pyplot as plt

with open("steering.txt") as file:
   data = numpy.loadtxt(file)

data = numpy.array(filter(lambda x: x>-5, data))

plt.hist(data)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.savefig("histogram.png", dpi = 300)
plt.show()
