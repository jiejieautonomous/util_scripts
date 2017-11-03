import numpy as numpy
import matplotlib.pyplot as plt

with open("camera1newdelta.txt") as f_camera:
   camera_data = numpy.loadtxt(f_camera)
with open("camera2newdelta.txt") as f_camera1:
   camera_data1 = numpy.loadtxt(f_camera1)
with open("camera3newdelta.txt") as f_camera2:
   camera_data2 = numpy.loadtxt(f_camera2)

fig = plt.figure()

ax1 = fig.add_subplot(311)

ax1.set_title("camera timestamp delta")   

ax1.scatter(camera_data[165:1920:10], numpy.zeros_like(camera_data[165:1920:10]) + 1, s = 1, c='r', label='camera0 time delta')
ax1.scatter(camera_data1[165:1920:10], numpy.zeros_like(camera_data1[165:1920:10]) + 1.1, s = 1, c='g', label='camera1 time delta')
ax1.scatter(camera_data2[165:1920:10], numpy.zeros_like(camera_data2[165:1920:10]) + 1.2, s = 1, c='b', label='camera2 time delta')

leg = ax1.legend()

plt.xlim((0.096,0.104))

plt.savefig("cameranewdelta.png", dpi = 300)
plt.show()
