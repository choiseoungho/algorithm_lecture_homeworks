# -*- coding: utf-8 -*-
import scipy.special
import numpy as np
np.random.seed(0)
import random
from time import time
'''
This is algorithm lecture 
1. Binomial Coefficient
2. Floyd's Shortest Path
3. Chained Matrix Multiplication
4. TSP
Args:
   Input: 2 list
   Output: Spend time
'''

def Binomial_Coefficient(arg1,arg2):
   return scipy.special.binom(arg1,arg2)

#E.g 1
numList_merge = [random.randint(1,100) for _ in range(2)]
t0= time()
print('first %d' %Binomial_Coefficient(numList_merge[0],numList_merge[1]))
print("Binomial_Coefficient spend time :%.2e"%(time()-t0))

numList_merge2 = [random.randint(1,100) for _ in range(2)]
t0 = time()
print ('second %d' %Binomial_Coefficient(numList_merge2[0],numList_merge2[1]))
print("Binomial_Coefficient spend time :%.2e"%(time()-t0))


def FloydsShortestPath(graph,V):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
INF = 9999
V=4
graph = [[0,5,INF,10],[INF,0,3,INF],[INF, INF, 0, 1],[INF, INF, INF, 0]]
t0 = time()
FloydsShortestPath(graph,V)
print("FloydsShortestPath spend time :%.2e"%(time()-t0))

def ChainedmMatrixMultiplicaiton(p):
    n = len(p) - 1
    m = [[0 for x in range(0, n)] for y in range(0, n)]
    s = [[0 for x in range(0, n)] for y in range(0, n)]
    for i in range(0,n):
        m[i][i] = 0
    # compute smallest matrix costs first
    # for chains of length 2 to n
    for l in range(2, n+1):
        for i in range(0, n - l + 1):
            j = i + l - 1 # j is the endpoint of the chain
            if i < j: # skip the i > j cases since we must multiply in order
                # cost values
                c = [m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1] for k in range(i, j)]
                # get minimum index and value from costs
                (s[i][j], m[i][j]) = min(enumerate(c), key=lambda x: x[1])
                #print (i, j, [x for x in enumerate(c)])
                s[i][j] = s[i][j] + i + 1 # correct our s value (count from 1, offset by i because. of enumerate)
    return m,s

def print_optimal_parens(s, i, j):
    if i == j:
        print ("parent_%d" % (i+1))
    else:
        print_optimal_parens(s, i, s[i][j]-1)
        print_optimal_parens(s, s[i][j], j)

numList_matrix = [random.randint(1,100) for _ in range(10)]
t0 = time()
m,s = ChainedmMatrixMultiplicaiton(numList_matrix)
print_optimal_parens(s,0,5)
print("First Chained Matrix Multiplicaiton spend time :%.2e"%(time()-t0))

numList_matrix2 = [random.randint(1,100) for _ in range(10)]
t0 = time()
m,s = ChainedmMatrixMultiplicaiton(numList_matrix2)
print_optimal_parens(s,0,5)
print("Second Chained Matrix Multiplicaiton spend time :%.2e"%(time()-t0))

import tsp

def TSP(r,dist):
   return tsp.tsp(r,dist)

mat = [[random.randint(1,100) for j in range(10)] for i in range(10)]
t0 = time()
r = range(len(mat))
dist = {(i,j):mat[i][j] for i in r for j in r}
result=TSP(r,dist)
print("First TSP spend time :%.2e"%(time()-t0))
print("First TSP result: "+str(result))

mat2 = [[random.randint(1,100) for j in range(30)] for i in range(30)]
t0 = time()
r = range(len(mat2))
dist = {(i,j):mat2[i][j] for i in r for j in r}
result2=TSP(r,dist)
print("Second TSP spend time :%.2e"%(time()-t0))
print("Second TSP result:"+str(result))

