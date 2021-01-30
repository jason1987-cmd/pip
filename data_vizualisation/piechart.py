# Pie Chart

from matplotlib import pyplot
cities = ['London', 'Paris', 'New York', 'Angeles']
slices = [19, 20, 20, 36]
colors = ['c', 'r', 'b', 'y']
pyplot.pie(
    slices,
    labels=cities,
    colors=colors,
    startangle=90,
    shadow=True,
    explode=(0,0.1,0,0),
    autopct='%1.2f%%'
)
pyplot.title("Sales in different cities")
pyplot.show()