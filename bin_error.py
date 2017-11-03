"""Plotting error bars for labels vs predictions.
Input: labels and predictions in text files. 
Output: Plot of errorbars.
"""

import numpy as numpy
import matplotlib.pyplot as plt

#Reading data
with open("steering_head.txt") as label_file:
   labels = numpy.loadtxt(label_file)
with open("pred_steering_ext.txt") as prediction_file:
   predictions = numpy.loadtxt(prediction_file)

labels = numpy.reshape(labels, (-1,1))
predictions = numpy.reshape(predictions, (-1,1))

#errors is a 2dnumpy array [labels, errors]
errors = numpy.concatenate((labels, abs(labels-predictions)), axis=1)

#print errors

#Put errors into a number of bins and calc the mean/std per bin
num_of_bins = 10
# error_std is a 2d array with [mean, std] of errors
error_std = numpy.zeros((num_of_bins, 2))
idx = numpy.zeros((num_of_bins, 1))
for i in range(num_of_bins):
  error_bin = numpy.array(filter(lambda x: x[0]>-100/num_of_bins*(i+1) and x[0]<-100/num_of_bins*i, errors))
  error_std[i,0] = numpy.mean(error_bin[:,1], axis=0)
  error_std[i,1] = numpy.std(error_bin[:,1], axis=0)
  idx[i] = -100/num_of_bins*(i+1)

print error_std

fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.set_title("binned steering error bars")

#ax1.scatter(error_bin[:,0], error_bin[:,1], c='r', label='steering angle errors')
plt.errorbar(idx, error_std[:,0], yerr=error_std[:,1], fmt='o', label='steering angle prediction error mean/std')

leg = ax1.legend(loc="lower left")

plt.savefig("binned_steering_errors.png", dpi = 300)
plt.show()

