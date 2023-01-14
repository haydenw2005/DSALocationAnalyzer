from Algorithms.MSTAlgorithm import *
from Algorithms.ClusteringAlgorithm import *
from ExampleData.ExampleDataCreator import *


# Prints intro information
def startingInfo():
    print("  _____        _           _____ _                   _                                        _            _"
          "                  _ _   _                   ")
    print(" |  __ \\      | |         / ____| |                 | |                                      | |     /\\   "
          "| |                (_| | | |                  ")
    print(" | |  | | __ _| |_ __ _  | (___ | |_ _ __ _   _  ___| |_ _   _ _ __ ___ ___    __ _ _ __   __| |    /  \\  |"
          " | __ _  ___  _ __ _| |_| |__  _ __ ___  ___ ")
    print(" | |  | |/ _` | __/ _` |  \\___ \\| __| '__| | | |/ __| __| | | | '__/ _ / __|  / _` | '_ \\ / _` |   / /\\ "
          "\\ | |/ _` |/ _ \\| '__| | __| '_ \\| '_ ` _ \\/ __|")
    print(" | |__| | (_| | || (_| |  ____) | |_| |  | |_| | (__| |_| |_| | | |  __\\__ \\ | (_| | | | | (_| |  / ____ "
          "\\| | (_| | (_) | |  | | |_| | | | | | | | \\__ \\")
    print(" |_____/ \\__,_|\\__\\__,_| |_____/ \\__|_|   \\__,_|\\___|\\__|\\__,_|_|  \\___|___/  \\__,_|_| |_|\\__,_| "
          "/_/    \\_|_|\\__, |\\___/|_|  |_|\\__|_| |_|_| |_| |_|___/")
    print(" ______________   ________           _____  ______ _____ __________________________                         "
          "  __/ |                                     ")
    print(" |______  |  | \\  ||_____||         |_____]|_____/|     |  |  |______|         |                           "
          " |___/                                      ")
    print(" |      __|__|  \\_||     ||_____    |      |    \_|_____|__|  |______|_____    |   ")
    print()
    print()
    print("Welcome to the final project of my data structures and algorithms independent study.")
    print("Using data scraped from Veracross, Lakeside now has the opportunity to visualize household location data.")
    print("With a series of algorithms, users can manipulate a graph of every (disclosed) student household.")
    print()


# Prints user options
def userOptions():
    print("\tOPTIONS")
    print("\t1 ~ Change sample size")
    print("\t2 ~ Execute algorithm")
    print("\t3 ~ Quit")
    print()


# Main loop for program
def mainLoop():
    startingInfo()
    grades = []
    graphDict = {}
    while True:
        userOptions()
        if grades:
            graphDict = getSampleSize(grades)
        usrInput = getUserInt(1, 3)
        if usrInput == 1:
            grades = changeGrades()
        if usrInput == 2:
            runAlgorithm(graphDict)
        if usrInput == 3:
            print("Bye!")
            quit()


# Helper function to get valid int
def getUserInt(minOpt, maxOpt):
    usrInput = 0
    while not minOpt <= usrInput <= maxOpt:
        try:
            usrInput = int(input(f"What would you like to do? (Input {minOpt}-{maxOpt}) "))
            if not minOpt <= usrInput <= maxOpt:
                print(f"Invalid input: Please enter an number from {minOpt} to {maxOpt}.")
        except ValueError:
            print(f"Invalid input: Please enter an integer.")
        print()
    return usrInput


# Helper function to get valid float
def getUserFloat():
    usrInput = 0
    while not usrInput:
        try:
            usrInput = float(input("Please enter the maximum edge length (miles): "))
        except ValueError:
            print(f"Invalid input: Please enter a float.")
        print()
    return usrInput


# Changes the grades used in the dataset
def changeGrades():
    grades = []
    while not grades:
        usrInput = input("Please enter the grades (5-12) you would like to use in the data set (EX. 5,8,12): ")
        if usrInput == 'all':
            grades = [5, 6, 7, 8, 9, 10, 11, 12]
            break
        try:
            grades = [int(x) for x in usrInput.split(",")]
            for grade in grades:
                if 5 > grade or grade > 12:
                    grades = []
                    raise ValueError
        except ValueError:
            print("Invalid input. Please enter the values as integers (range 5-12) separated by commas.")
    print()
    print(f"SUCCESS ~ Graph data set updated to {grades}")
    print()
    return grades


# Loads the graph and person data from json files
def getSampleSize(grades):
    f1 = open("ExampleData/ExampleMainGraph.json")
    graphData = json.load(f1)
    f2 = open("ExampleData/ExamplePersonInfo.json")
    personInfo = json.load(f2)

    newGraphDict = {}
    idx = 1
    for household in graphData[1]:
        for person in graphData[1][household]:
            if personInfo[person]['grade'] in grades:
                newGraphDict[str(idx)] = []
        idx += 1
    for person in newGraphDict:
        for edge in graphData[0][person]:
            if str(edge[0]) in newGraphDict:
                newGraphDict[person].append(edge)
    return [newGraphDict, graphData[1]]


# Function that allows for user to choose what algorithms they would like to use
def runAlgorithm(graphData):
    if not graphData:
        print("Please enter a sample size (option 1).")
        return
    print("\tALGORITHM MENU")
    print("\t1 ~ Prim's MST")
    print("\t2 ~ BFS clustering")
    print("\t3 ~ Back")
    print()
    usrInput = getUserInt(1, 3)
    if usrInput == 1:
        print("Running Prim's MST algorithm...")
        mst(graphData[0])
        print("Complete!")
    if usrInput == 2:
        thresholdLength = getUserFloat()
        print("Running BFS clustering algorithm...")
        clusteringAlgorithm(thresholdLength, graphData[0])
        print("Complete!")
    if usrInput == 3:
        pass
    print()


# Main
if __name__ == '__main__':
    mainLoop()



