import numpy # import mean() and median() 
from scipy import stats # import mode()



# measured the speed of 13 cars

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = numpy.mean(speed)
median = numpy.median(speed)
mode = stats.mode(speed) # will show the repeating number and how many times it occurred

print(mean)
print(median)
print(mode)