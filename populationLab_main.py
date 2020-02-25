import matplotlib.pyplot as plt

initialPopulation = 10
initialTime = 0.0
maxTime = 10.0
timeStep = 0.01
birthConstant = 3.0
deathConstant = 0.05

currentPopulation = initialPopulation
currentTime = initialTime

populationList = []
timeList = []

populationList.append(currentPopulation)
timeList.append(currentTime)
print("current population is: " + str(currentPopulation) + " currentTIme is: " + str(currentTime))

while currentTime <= maxTime:
    currentPopulation = currentPopulation + (((birthConstant * currentPopulation) - (deathConstant * currentPopulation**2)) * timeStep)
    currentTime = currentTime + timeStep
    populationList.append(currentPopulation)
    timeList.append(currentTime)
    print("current population is: " + str(currentPopulation) + " currentTIme is: " + str(currentTime))

plt.plot(timeList, populationList)
plt.show()