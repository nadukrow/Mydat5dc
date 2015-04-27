# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 22:28:52 2015

@author: nadukrow
"""

'''
Part 1
Produce a plot that compares the mean mpg for the different numbers of cylinders.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
auto = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt', sep='|')

auto.groupby('cylinders').mpg.mean() # This will give us the data grouped by cylinders and the resulting mean.

auto.groupby('cylinders').mpg.mean().plot(kind='bar') # Here we choose a bar graph to plot the data.
plt.title("Comparing Mean MPG for Different Numbers of Cylinders") # Here is how we title our graph.
plt.xlabel("Number of Cylinders") # X label
plt.ylabel("Average MPG") # Y label
plt.show() # Finally this produces the plot.

'''
Part 2
Use a scatter matrix to explore relationships between different numeric variables.
'''
pd.scatter_matrix(auto) # Choose a scatter plot to represent the data.
plt.show() # Returns the plot.

'''
Part 3
Use a plot to answer the following questions:
'''

'''
-Do heavier or lighter cars get better mpg?
'''
auto.plot(kind='scatter', x='weight', y='mpg', alpha=0.5) # Choose to use a scatter plot.
plt.title('Car MPG by Weight')
plt.xlabel('Car weight')
plt.ylabel('MPG')
plt.show() #You can see as you increase in weight that the car gets lowers miles per gallon.

'''
-How are horsepower and displacement related?
'''

auto.plot(kind='scatter', x='displacement', y='horsepower', alpha=0.5) 
plt.title('Horsepower by Engine Displacement')
plt.xlabel('Engine Displacement')
plt.ylabel('Horsepower ')
plt.show() #The higher the horsepower, the higher the displacement.

'''
-What does the distribution of acceleration look like?
'''

auto.acceleration.hist()
plt.title('Distribution of Acceleration')
plt.xlabel('Acceleration')
plt.ylabel('Frequency')
plt.show()


'''
-How is mpg spread for cars with different numbers of cylinders?
'''

auto.boxplot('mpg', by='cylinders')
plt.title('Car MPG by Number of Cylinders')
plt.xlabel('Number of Cylinders')
plt.ylabel('MPG')
plt.show()