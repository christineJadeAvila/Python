import numpy
import matplotlib.pyplot as plt

#generate 250 set of float number from 0.0 to 5.0 using the numpy lib function random.uniform
floatsy = numpy.random.uniform(0.0, 5.0, 250)


'''HISTOGRAM'''

#Visualizing Data 

plt.hist(floatsy, 5)
plt.show()


