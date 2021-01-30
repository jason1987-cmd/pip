# Bar Chart

from matplotlib import pyplot
pyplot.bar([1,3,4,8],[28,40,76,65], label="Example One")
pyplot.bar([9,3,4,5],[15,65,90,78], label="Example Two")
pyplot.legend()
pyplot.title('Bar chart')
pyplot.xlabel('Horizontal')
pyplot.ylabel('Vertical')
pyplot.show()