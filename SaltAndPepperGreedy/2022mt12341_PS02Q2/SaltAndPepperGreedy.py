#To implement the greedy approach way


#Get the input file path
#read the input file
#inputPS02Q2.txt
import os

def calculateMaxGoodDishes(saltAndPepperList): 
    #TODO
    maxGoodDishes = 0
    isDishComplete = False 
    currentIngredientsCount = 0
    for currIngredient in saltAndPepperList.strip():
        if currIngredient == 'S': 
            currentIngredientsCount += 1
            if currentIngredientsCount == 0:
                isDishComplete = True 
                maxGoodDishes += 1
            else: isDishComplete = False
        elif currIngredient == 'P':
            currentIngredientsCount -= 1
            if currentIngredientsCount == 0:
                isDishComplete = True 
                maxGoodDishes += 1
            else: isDishComplete = False
        else:
            #invalid input throw error
            print("Invalid input")
    return maxGoodDishes


print("Salt and Pepper Greedy Approach problem solution")
print("=================================")

#Preparing and getting inputFilePath, inputFile, and inputContent for processing
inputFilePath = os.path.join(os.getcwd(), "inputPS02Q2.txt")
print("Input file path is:" + inputFilePath)
print("Press Enter to continue")
input()
inputFile = open(inputFilePath,"r")
inputlines = inputFile.readlines()

#Preparing the output file for processing
outputFilePath = os.path.join(os.getcwd(), "outputPS02Q2.txt")
print("Output File path is:" + outputFilePath)
print("Press Enter to continue")
input()
if os.path.exists(outputFilePath):
    os.remove(outputFilePath)
outputFile = open(outputFilePath, "w+")

#for each line of input in the file:
#implement the logic for finding the maximum good wishes

for inputline in inputlines:
    #the logic part
    maxGoodDishes = calculateMaxGoodDishes(inputline)

    #for each ouput line, write into the output file
    #(outputPS01Q1.txt
    outputFile.write(str(maxGoodDishes) + "\n")

print("The problem has been executed and the output is written into outputPS02Q2.txt in the root folder")
inputFile.close()
outputFile.close()



