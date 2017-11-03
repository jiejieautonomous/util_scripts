import numpy as numpy
import matplotlib.pyplot as plt

with open("steering.txt") as file:
   steering_data = numpy.loadtxt(file)

fig = plt.figure()

ax1 = fig.add_subplot(311)

ax1.set_title("steering")

idx =  numpy.indices(steering_data.shape)
ax1.scatter(idx, steering_data, s=0.1,  c='r', label='collected steering angles')

leg = ax1.legend(loc="lower left")

plt.savefig("steering.png", dpi = 300)
plt.show()

