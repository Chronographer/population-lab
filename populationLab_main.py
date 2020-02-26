"""
Written by Daniel Isenberg in Intellij Idea using the Python community plugin.
Full project repository is available at https://github.com/Chronographer/population-lab (this is the only file though)

Simple program to model population over time using the Euler method given an initial population, a growth constant, a
decay constant, and a maximum time. In addition to the approximation provided by the Euler method, an analytical
solution is calculated at each time step to provide a sanity check for the computational solution. The analytical
solution does not account for population decay, and so the comparison between the analytical and computation results are
only valid when the decay constant is equal to zero.
"""
import matplotlib.pyplot as plt
import math

initialPopulation = 10
initialTime = 0.0
maxTime = 10.0
timeStep = 0.01
growthConstant = 0.1
decayConstant = 0.0

currentPopulation = initialPopulation
currentTime = initialTime

populationList = []
analyticalPopulationList = []
timeList = []

populationList.append(initialPopulation)  # this ensures that the initial population(s) are plotted on the graph
analyticalPopulationList.append(initialPopulation)
timeList.append(currentTime)

while currentTime <= maxTime:
    currentPopulation = currentPopulation + ((growthConstant * currentPopulation) - (decayConstant * currentPopulation ** 2)) * timeStep
    analyticalPopulation = initialPopulation * math.exp(growthConstant * currentTime)
    currentTime = currentTime + timeStep
    analyticalPopulationList.append(analyticalPopulation)
    populationList.append(currentPopulation)
    timeList.append(currentTime)
    print("current population is: " + str(currentPopulation) + " currentTIme is: " + str(currentTime))

plt.plot(timeList, populationList, label="computational")
plt.plot(timeList, analyticalPopulationList, label="analytical")
plt.legend()
plt.suptitle("Comparison of computational and analytical methods\nin unrestrained population growth")
plt.xlabel("Time")
plt.ylabel("Population")
plt.grid()
plt.show()
