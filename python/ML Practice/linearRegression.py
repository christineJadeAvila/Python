import matplotlib.pyplot as plt
from scipy import stats

# draw SCATTER plot of data, and draw the LINE of linear regression

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myFunc(x):
    return slope * x + intercept

mymodel = list(map(myFunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

