import numpy
import matplotlib.pyplot as plt 

normalData = numpy.random.normal(5.0, 0.0, 10000)

#visualize data

plt.hist(normalData, 100)
plt.show()