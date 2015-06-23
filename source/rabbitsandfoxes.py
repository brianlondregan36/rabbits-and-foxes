import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    global CURRENTRABBITPOP
    
    newRabbits = 0    
    for i in range(CURRENTRABBITPOP):
        if (CURRENTRABBITPOP + newRabbits) < MAXRABBITPOP:
            pRabbitRepro = 1 - (float(CURRENTRABBITPOP + newRabbits) / float(MAXRABBITPOP))
            if random.random() < pRabbitRepro:
                newRabbits += 1
        else:
            break
    
    CURRENTRABBITPOP = CURRENTRABBITPOP + newRabbits
            
def foxGrowth():
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    
    foxChanges = 0    
    for i in range(CURRENTFOXPOP):        
            pFoxEats = (float(CURRENTRABBITPOP) / float(MAXRABBITPOP))
            if random.random() < pFoxEats:  #caught one
                if CURRENTRABBITPOP > 10:
                    CURRENTRABBITPOP = CURRENTRABBITPOP - 1
                    if random.random() < (1.0/3.0):
                        foxChanges += 1
                else:
                    break
            else: #did not catch one
                if (CURRENTFOXPOP + foxChanges) > 10:
                    if (random.random() < 0.9):
                        foxChanges -= 1

    CURRENTFOXPOP = CURRENTFOXPOP + foxChanges
            
def runSimulation(numSteps):
    rabbit_populations = []
    fox_populations = []

    for n in range(numSteps):       
        if n == 0:
            if (CURRENTRABBITPOP < 10) or (CURRENTFOXPOP < 10):
                break
                
        rabbitGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        foxGrowth()
        fox_populations.append(CURRENTFOXPOP)
      
    stateOfTheForest = (rabbit_populations, fox_populations)
    return stateOfTheForest
        



numTrials = 200
tup = runSimulation(numTrials)

rabbitPopulationOverTime = tup[0]
foxPopulationOverTime = tup[1]
xVals = range(len(rabbitPopulationOverTime))

pylab.plot(xVals, rabbitPopulationOverTime)
pylab.plot(xVals, foxPopulationOverTime)
coeff1 = pylab.polyfit(xVals, rabbitPopulationOverTime, 2)
pylab.plot(pylab.polyval(coeff1, xVals))
coeff2 = pylab.polyfit(xVals, foxPopulationOverTime, 2)
pylab.plot(pylab.polyval(coeff2, xVals))

pylab.title('State of the Forrest')
pylab.xlabel('Number of Time Steps')
pylab.ylabel('Population')
pylab.legend(('Rabbit Population', 'Fox Population', 'Rfit', 'Ffit'))

pylab.show()
