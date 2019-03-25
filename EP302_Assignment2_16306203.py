#!/usr/bin/env
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:04:39 2019

@author: BenGfoyle
"""

import matplotlib.pyplot as plt #plot graphs
from scipy import constants as con #constants
from numpy import sqrt
from numpy import exp #exponential e function
from numpy import mean
#import XlsxWriter

#define constants
PI = con.pi
HBAR = con.hbar
#dfined such that a = 1
K = HBAR ** 2
M = 1
w = HBAR
a = 1

#array of constants,in array for conviniet import to excel
constants = [PI,HBAR,K,M,w,a]
conNames = ["Pi","Hbar","K","M","w","a"]

# =============================================================================
# #define excel workbooks
# wb = XlsxWriter.Workbook('probability.xlsx')
# worksheet = wb.add_worksheet()
# =============================================================================

#==============================================================================
def makeGraph(yAxis,xAxis,name): #standard plotting using numpy
    plt.scatter(xAxis,yAxis, label = name) #scatter plot
    plt.plot(xAxis,yAxis) #scatter plot
    plt.legend(name)
    plt.legend(loc='upper right')
    plt.xlabel("Displacement")
    plt.ylabel("Probability")
    plt.title("Plot of Probability versus Displacement")
    plt.grid(True)
    plt.show()
    return plt
#==============================================================================

#==============================================================================
def psi(k1,k2,k3,x): #calculate shroedinger equation for a given state
    schro = abs(k1 * k3 * ((k2 * a / PI)**0.25) * exp(-0.5 * a * x * x))
    return schro
#==============================================================================

#==============================================================================
# =============================================================================
# def toExcel(head, data, location):
#     worksheet.write(location, head)
#     worksheet.write(location, data)
# =============================================================================
#==============================================================================

#==============================================================================
# =============================================================================
# def excelHeaders(headings):
#     for i in range(0,len(headings)):
#         worksheet.write(0,i,headings[i])
# =============================================================================
#==============================================================================

#==============================================================================
def average():

    p1 = [0.751125544464943,0.455580672011333]
    p2 = [0.531125966013598,0.322144182556738]
    
    dist = [-4,-3,-2,-1,0,1,2,3,4]
    
    avgProb = []
    
    for i in range(0,len(p1)):
        avgProb.append((p1[i] + p2[i])/2)
        
    print(avgProb)
    makeGraph(avgProb,dist,"Average")
#==============================================================================

#==============================================================================
def main():
    #headings = ["Names","Constants","Unit Distance","Lvl 0","Lvl 1","Lvl 2"]
    #excelHeaders(headings)
    dist = [-4,-3,-2,-1,0,1,2,3,4]
    prob = []
    for i in range(0,3):
        for j in range(-4,5):
            energy = [(1,1,1),(1,4 * a * a ,j),(1/sqrt(2),1,(2 * a * j * j) - 1)]
            c_pro = psi(energy[i][0],energy[i][1],energy[i][2],j)
            prob.append(c_pro)
            print(j,c_pro)
        makeGraph(prob,dist,"Energy Level:" + str(i))
        prob.clear()
    #average()
        
    
#==============================================================================

#==============================================================================
if __name__ == "__main__":
    main()
#==============================================================================