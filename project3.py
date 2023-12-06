"""
Math 260
Final Project
Fall 2023

Partner 1: Jun Tan
Partner 2: 
Date: 13th December
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    ##### Your implementation goes here. #####
    return []
    ##### Your implementation goes here. #####

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
