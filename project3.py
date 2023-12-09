"""
Math 260
Final Project
Fall 2023

Partner 1: Jun Tan
Partner 2: Max Gorbarty
Date: 13th December 2023
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
INPUTS
adjList: Adjacency list for the currencies
adjMat: Adjacency matrix representing the exchange rates
tol: Tolerance, check after each update -- ignore if smaller than 1e-15
OUTPUTS

"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
   # Initialize distances and predecessors
    for vertex in adjList:
        vertex.dist = float('inf')
        vertex.prev = None
    
    # Relax edges |V| - 1 times
    for i in range(len(adjList) - 1):
        for vertex in adjList:
            for neighbor in vertex.neigh:
                if vertex.dist + adjMat[vertex.rank][neighbor.rank] < neighbor.dist:
                    neighbor.dist = vertex.dist + adjMat[vertex.rank][neighbor.rank]
                    neighbor.prev = vertex

    # Vertex distances after v-1 iterations 
    vertx_dist = [vertex.dist for vertex in adjList]

    # Check for negative cycles
    for vertex in adjList:
        for neighbor in vertex.neigh:
            if vertex.dist + adjMat[vertex.rank][neighbor.rank] < neighbor.dist - tol:
                 
    # Vertex distance after final iteratino 
    vertx_dist_final = [vertex.dist for vertex in adjList]

    # Changed distance index locator
    changed = None
    for i in range(len(adjList)):
        if vertex_dist[i] = vertex_dist_final[i]:
                changed = i 
                break 
    
    if changed is None:
        return []
    
    negCycle = []
    current = adjList[change
                

    # Negative cycle found, trace back to get the cycle
    cycle = []
    current = vertex
    while current not in cycle:
    cycle.append(current)
    current = current.prev
    cycle.reverse()  # To get the cycle in the correct order
    return cycle
                

    # No arbitrage opportunity found
    return []
    

################################################################################

"""
rates2mat
"""
def rates2mat(rates):
    # Using negative logarithm to transform the rates
    return [[-math.log(R) for R in row] for row in rates]
 
"""
Main function.
"""
if __name__ == "__main__":
    testRates()
