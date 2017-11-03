import os

with open('pred_steering.txt', 'r') as searchfile:
    for line in searchfile:
        if 'Steering_angle' in line:
            print float(line.split(" ")[1])

