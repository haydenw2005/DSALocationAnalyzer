from matplotlib import colors as mcolors
import random
from DataCompilation.GraphVisualizer import visualizeGraph
from . import MSTAlgorithm


# Function that deletes all edges longer than threshold
# Calls dfs to sort node by respective cluster
def clusteringAlgorithm(lengthThresh, edgeDict):
    clusterEdgeDict = {}
    nodeDict = {}
    for node in edgeDict:
        clusterEdgeDict[node] = []
        nodeDict[node] = False
        for edge in edgeDict[node]:
            if edge[1] < lengthThresh:
                clusterEdgeDict[node].append(edge)
    colorDict = dfsLoop(clusterEdgeDict, nodeDict)
    edgeSet = MSTAlgorithm.primsAlgo(clusterEdgeDict)
    visualizeGraph(colorDict, edgeSet)


# Return Dict with color coded nodes by cluster
# Recursive depths search
def dfsLoop(edgeDict, nodeDict):
    colorDict = {}
    clusterIdx = 0
    colors = list(mcolors.TABLEAU_COLORS)

    for i in nodeDict:
        if not nodeDict[i]:
            randColor = random.choice(colors)
            colorDict[clusterIdx] = [[i, randColor]]
            dfs(edgeDict, nodeDict, i, colorDict[clusterIdx], randColor)
            if len(colorDict[clusterIdx]) == 1:
                colorDict[clusterIdx][0][1] = 'black'
            clusterIdx += 1

    return colorDict


# Function called by dfsLoop recursively to search through set of edges
def dfs(edgeDict, nodeDict, i, cluster, randColor):
    nodeDict[i] = True
    if i in edgeDict:
        for j in edgeDict[i]:
            if not nodeDict[str(j[0])]:
                cluster.append([str(j[0]), randColor])
                dfs(edgeDict, nodeDict, str(j[0]), cluster, randColor)
