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

initialPopulation = 1.0
initialTime = 0.0
maxTime = 2.5
timeStep = 0.01
growthConstant = 5.0
decayConstant = 0.05

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

plt.plot(timeList, populationList, label="Initial population: " + str(initialPopulation) + "\ngrowth constant: " + str(growthConstant) + "\ndecay constant: " + str(decayConstant) + "\ntime step: " + str(timeStep))  # this automatically populates the legend with the parameters used to create the plot
# plt.plot(timeList, analyticalPopulationList, label="analytical")  # uncomment this to plot the analytical solution
plt.legend()
plt.suptitle("Computational model of population growth\nwith small decay constant")
plt.xlabel("Time")
plt.ylabel("Population")
plt.grid()
plt.show()
