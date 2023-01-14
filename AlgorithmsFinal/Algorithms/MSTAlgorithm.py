import heapq
from DataCompilation.GraphVisualizer import visualizeGraph


# Calls prims, returns MST
def mst(edgeDict):
    # Initialize a dictionary of colored vertices, with all vertices colored blue
    coloredVertices = {'0': []}
    for i in edgeDict:
        coloredVertices['0'].append([i, 'b'])

    # Call the primsAlgo function to find the MST edges
    mstEdges = primsAlgo(edgeDict)

    # visualize the graph using the colored vertices and MST edges
    visualizeGraph(coloredVertices, mstEdges)


# Prims algo, returns MST edges
def primsAlgo(edgeDict):
    # initialize all vertices as not in the spanning tree
    vertices = {}
    for i in edgeDict:
        if edgeDict[i]:
            vertices[i] = False
    vertices['0'] = True

    # initialize the starting vertex as in the spanning tree
    spanningVx = {'0': True}
    mstEdges = []
    total = 0
    currentV = next(iter(edgeDict))
    minHeap = []

    # repeat until all vertices are in the spanning tree
    while vertices != spanningVx:
        found = False

        # add all edges of the current vertex to the min heap
        for item in edgeDict[str(currentV)]:
            heapq.heappush(minHeap, (item[1], item))

        # pops the edges from the heap until it finds one that points to a new vertex
        while minHeap:
            minItem = heapq.heappop(minHeap)
            if str(minItem[1][0]) not in spanningVx:
                found = True
                break

        # Allows prims algo to work on disconnected cluster graphs
        if not minHeap:
            for i in edgeDict:
                if i and i not in spanningVx and edgeDict[str(i)]:
                    currentV = int(i)
                    break

        # Update items
        if found:
            vertices[str(minItem[1][0])] = True
            total += minItem[1][1]
            spanningVx[str(minItem[1][0])] = True
            minItem[1].insert(0, int(currentV))
            mstEdges.append(minItem[1])
            currentV = minItem[1][1]

    print("MST total length in miles:", round(total, 2))
    return mstEdges
