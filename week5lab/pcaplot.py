#!/usr/bin/env python


from matplotlib.mlab import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
import numpy as np

data = np.array("plink.eigenvec")

try:
    results = PCA(data)
except:
    raise

    #this will return an array of variance percentages for each component
    print results.fracs

    #
    print results.Wt

    #this will return a 2d array of the data projected into PCA space
    print results.Y 

    x = []
    y = []
    z = []
    for item in results.Y:
        x.append(item[0])
        y.append(item[1])
        z.append(item[2])

    fig1 = plt.figure() # Make a plotting figure
    ax = Axes3D(fig1) # use the plotting figure to create a Axis3D object.
    pltData = [x,y,z] 
    ax.scatter(pltData[0], pltData[1], pltData[2], 'bo') # make a scatter plot of blue dots from the data

    # make simple, bare axis lines through space:
    xAxisLine = ((min(pltData[0]), max(pltData[0])), (0, 0), (0,0)) # 2 points make the x-axis line at the data extrema along x-axis 
    ax.plot(xAxisLine[0], xAxisLine[1], xAxisLine[2], 'r') # make a red line for the x-axis.
    yAxisLine = ((0, 0), (min(pltData[1]), max(pltData[1])), (0,0)) # 2 points make the y-axis line at the data extrema along y-axis
    ax.plot(yAxisLine[0], yAxisLine[1], yAxisLine[2], 'r') # make a red line for the y-axis.
    zAxisLine = ((0, 0), (0,0), (min(pltData[2]), max(pltData[2]))) # 2 points make the z-axis line at the data extrema along z-axis
    ax.plot(zAxisLine[0], zAxisLine[1], zAxisLine[2], 'r') # make a red line for the z-axis.

    # label the axes 
    ax.set_xlabel("x-axis label") 
    ax.set_ylabel("y-axis label")
    ax.set_zlabel("y-axis label")
    ax.set_title("The title of the plot")

    plt.show() # show the plot