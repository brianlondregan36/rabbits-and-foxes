import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    global CURRENTRABBITPOP
    
    newRabbits = 0    
    for i in range(CURRENTRABBITPOP):  #for every rabbit in the forest
        if (CURRENTRABBITPOP + newRabbits) < MAXRABBITPOP:  #rule: rabbit population has upper limit
            pRabbitRepro = 1 - (float(CURRENTRABBITPOP + newRabbits) / float(MAXRABBITPOP))
            if random.random() < pRabbitRepro:   #chances of rabbit reproducing
                newRabbits += 1
        else:
            break
    
    CURRENTRABBITPOP = CURRENTRABBITPOP + newRabbits   #new head count
            
def foxGrowth():
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    
    foxChanges = 0    
    for i in range(CURRENTFOXPOP):    #for every fox in the forest    
            pFoxEats = (float(CURRENTRABBITPOP) / float(MAXRABBITPOP))
            if random.random() < pFoxEats:  #caught a rabbit
                if CURRENTRABBITPOP > 10:  #rule: must be at least 10 rabbits
                    CURRENTRABBITPOP = CURRENTRABBITPOP - 1  #kill that rabbit
                    if random.random() < (1.0/3.0):  #chances of fox reproducing given that it ate
                        foxChanges += 1
                else:
                    break
            else: #did not catch a rabbit
                if (CURRENTFOXPOP + foxChanges) > 10: #rule: must be at least 10 foxes
                    if (random.random() < 0.9):  #chances of fox dying of hunger
                        foxChanges -= 1    #kill that fox

    CURRENTFOXPOP = CURRENTFOXPOP + foxChanges  #new head count
            
def runSimulation(numSteps):
    #run through x time steps and see what the model does to the populations over time
    #add current counts to these lists every time step to watch population rise or fall
    rabbit_populations = []
    fox_populations = []

    for n in range(numSteps):       
        if n == 0:
            if (CURRENTRABBITPOP < 10) or (CURRENTFOXPOP < 10):
                break   #rule: again, must be at least 10 rabbits and 10 foxes
                
        rabbitGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        foxGrowth()
        fox_populations.append(CURRENTFOXPOP)
      
    stateOfTheForest = (rabbit_populations, fox_populations)
    return stateOfTheForest
        





#START TEST THEN PLOT

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
