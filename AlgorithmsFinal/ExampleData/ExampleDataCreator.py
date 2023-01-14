import random
import geopy.distance
import json


# Creates example data set based in Austin, Texas
def createExPersonInfo():
    personInfoDict = {}
    for i in range(1, 501):
        personInfoDict[f"Person {i}"] = {
            'name': f'Example Person {i}',
            'address': f'Example Address {i}',
            'grade': random.randint(5,12),
            'lat': round(random.uniform(30.2672-.15, 30.2672+.15), 3),
            'long': round(random.uniform(-97.7431-.15, -97.7431+.15), 3),
        }
    with open("ExampleData/ExamplePersonInfo.json", "w") as outfile:
        print("doing")
        json.dump(personInfoDict, outfile)
    graph = {}
    nodes = {}
    usedAdresses = {}
    iIndex = 1
    for i in personInfoDict:
        if personInfoDict[i]['address'] not in usedAdresses:
            nodes[iIndex] = [i]
            usedAdresses[personInfoDict[i]['address']] = iIndex
            iIndex += 1
        else:
            nodes[usedAdresses[personInfoDict[i]['address']]].append(i)
    iIndex = 1
    for i in nodes:
        print(i)
        graph[int(iIndex)] = []
        iCoords = (personInfoDict[nodes[i][0]]['lat'], personInfoDict[nodes[i][0]]['long'])

        xIndex = 1
        for x in nodes:
            if personInfoDict[nodes[x][0]]['address'] != personInfoDict[nodes[i][0]]['address']:
                xCoords = (personInfoDict[nodes[x][0]]['lat'], personInfoDict[nodes[x][0]]['long'])
                dist = round(geopy.distance.geodesic(iCoords, xCoords).miles, 3)
                graph[iIndex].append([xIndex, dist])
            xIndex += 1
        iIndex += 1

    with open("ExampleData/ExampleMainGraph.json", "w") as outfile:
        json.dump([graph, nodes], outfile)

