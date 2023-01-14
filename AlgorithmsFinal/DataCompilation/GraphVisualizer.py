import json
import matplotlib.pyplot as plt
import numpy as np
import requests


# Draws graph using matplotlib
# Edge must be in this form: [place_1_ID, place_2_ID, distance]
# Node must be in this form: [nodeIdx, node_color]
def visualizeGraph(clusterGraph, edges=False):
    f1 = open("ExampleData/ExamplePersonInfo.json")
    personData = json.load(f1)
    f2 = open("ExampleData/ExampleMainGraph.json")
    personKey = json.load(f2)[1]
    minLat = 200
    maxLat = -200
    minLong = 200
    maxLong = -200
    for person in personData:
        lat = personData[person]['lat']
        long = personData[person]['long']

        if lat < minLat:
            minLat = lat
        if lat > maxLat:
            maxLat = lat
        if long < minLong:
            minLong = long
        if long > maxLong:
            maxLong = long

    # Draw edges
    if edges:
        for edge in edges:
            loc1 = personData[personKey[str(edge[0])][0]]
            loc2 = personData[personKey[str(edge[1])][0]]
            x, y = [loc1['long'], loc2['long']], [loc1['lat'], loc2['lat']]
            plt.plot(x, y, color="black")

    # Draw addresses by lat long
    lats = np.array([])
    longs = np.array([])
    colors = []
    for graph in clusterGraph:
        for person in clusterGraph[graph]:
            lat = personData[personKey[str(person[0])][0]]['lat']
            long = personData[personKey[str(person[0])][0]]['long']
            colors.append(person[1])
            lats = np.append(lats, lat)
            longs = np.append(longs, long)
        plt.scatter(longs, lats, c=colors)

    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')

    # See createMap below
    # createMap(minLong, maxLong, minLat, maxLat)
    img = plt.imread("ExampleData/map.png")

    plt.imshow(img, extent=[minLong, maxLong, minLat, maxLat])
    plt.show()
    plt.close()


# Use this code if you want to create new map for new dataset
"""
def createMap(minLong, maxLong, minLat, maxLat):
    meanLat = (maxLat + minLat) / 2
    meanLong = (maxLong + minLong) / 2
    ySize = int((maxLat - minLat)*800)  # Vertical
    xSize = int((maxLong - minLong)*800)  # Horizontal
    key = '' #Enter staticmaps key here
    https = "https://maps.googleapis.com/maps/api/staticmap?center=" + str(meanLat) + "," + str(meanLong) + "&zoom=11&size=" + str(xSize) + "x" + str(ySize) + "&scale=2&key=" + key
    response = requests.get(https)
    with open('ExampleData/map.png', 'wb') as file:
        file.write(response.content)
"""