from random import randrange
import numpy as np
from itertools import takewhile



class Evalution222:

    def __init__(self, valueStart, valueEnd):
        self.genotypeArray = []
        self.genotypeArrayNew = []
        self.valueStart = valueStart
        self.valueEnd = valueEnd

    def createGenotypePopulation(self):
        while len(self.genotypeArray) < 10:
            gen = randrange(self.valueEnd)
            self.genotypeArray.append(bin(gen))

    def printPopulation(self):
        print(self.genotypeArray)
        print(len(self.genotypeArray))

    def fitnessFunction(self, gen):
        phenotype = str(int(gen, 2))
        fit = 0
        for x in phenotype:
            if int(x) == 2:
                fit += 1
        return fit

    def crossover(self, genMale, genFemale):
        print("crossover")
        maleGenBody = []
        femaleGenBody = []
        maleLength = len(str(bin(genMale)))
        femaleLength = len(str(bin(genFemale)))

        print("Male Gen:")
        for i in range(1, maleLength):
            if i > 1:
                maleGenBody.append(str(bin(genMale))[i])

        print("Female Gen:")
        for i in range(1, femaleLength):
            if i > 1:
                femaleGenBody.append(str(bin(genFemale))[i])

        if len(maleGenBody) == len(femaleGenBody):
            splitPointMaleA = randrange(maleLength)
            splitPointFemaleA = splitPointMaleA

            splitPointMaleB = maleLength - splitPointMaleA
            splitPointFemaleB = femaleLength - splitPointFemaleA

            malePartA = np.array(maleGenBody[:splitPointMaleA])
            malePartB = np.array(maleGenBody[-splitPointMaleB:])

            femalePartB = np.array(femaleGenBody[:splitPointFemaleA])
            femalePartA = np.array(femaleGenBody[-splitPointFemaleB:])

            offspringA = ''.join(np.concatenate((malePartA, femalePartA), axis=None))
            offspringB = ''.join(np.concatenate((malePartB, femalePartB), axis=None))
            offspringAInt = int(offspringA, 2)
            offspringBInt = int(offspringB, 2)
            print("Child 1")
            print(offspringAInt)
            print("Child 2 ")
            print(offspringBInt)

    def take(n, iterable):
        "Return first n items of the iterable as a list"
        return list(islice(iterable, n))

    def evalution(self):
        self.createGenotypePopulation()
        genMap = {}
        genMapFilter = {}

        for gen in self.genotypeArray:
            genValue = self.fitnessFunction(gen)
            genMap[gen] = genValue
        genMapFilter = dict(sorted(genMap.items(),
                                  key=lambda item: item[1],
                                  reverse=True))
        genMapBest = dict(list(genMapFilter.items())[0: 5])

        print(genMapBest)


start = Evalution222(0, 255)
start.createGenotypePopulation()
start.printPopulation()
start.crossover(0b10100110, 0b11111010)
start.evalution()
