# -*- coding: utf-8 -*-
"""
@author: nadukrow
"""

'''
Part 1
Load the data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt) 
into a DataFrame.  Try looking at the "head" of the file in the command line
to see how the file is delimited and how to load it.
Note:  You do not need to turn in any command line code you may use.
'''

import pandas as pd #Import the pandas module and use it as pd.
auto = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt', sep='|')
#The method above is to read it from an internet source. Another method below is to read it when you download the file.
auto = pd.read_table('auto_mpg.txt', sep='|')

'''
Part 2
Get familiar with the data.  Answer the following questions:
- What is the shape of the data?  How many rows and columns are there?
- What variables are available?
- What are the ranges for the values in each numeric column?
- What is the average value for each column?  Does that differ significantly
  from the median?
'''

auto.shape # This tells how many rows and columns. There are 392 rows and 9 columns

auto.columns # This lists the column names/variables in the data.

#To find the range you need the max - min for all the columns. 
auto.min(numeric_only=True) # This will print the minimums for the variables.
auto.max(numeric_only=True) # This will print the maximums for the variables.
auto.max(numeric_only=True) - auto.min(numeric_only=True) # Pirint this will give you the range.

auto.median() #Mean for all variables.
auto.mean() #Median for all variables.
auto.mean() - auto.median() #The mean is greater than the median in most cases between variables.
#In some variables such as mpg or acceleration the mean isn't that much greater.

'''
Part 3
Use the data to answer the following questions:
- Which 5 cars get the best gas mileage?  
- Which 5 cars with more than 4 cylinders get the best gas mileage?
- Which 5 cars get the worst gas mileage?  
- Which 5 cars with 4 or fewer cylinders get the worst gas mileage?
'''

auto.sort_index(by='mpg', ascending=False)[0:5][['car_name','mpg']] # Five cars that get the best gas mileage

auto[auto.cylinders > 4].sort_index(by='mpg', ascending=False)[0:5][['car_name','mpg']] # Five cars with more than 4 cylinders that get the best gas mileage

auto.sort_index(by='mpg')[0:5][['car_name','mpg']] # Five cars that get worst gas mileage

auto[auto.cylinders > 4].sort_index(by='mpg')[0:5][['car_name','mpg']] #Five cars with 4 or fewer cylinders that get the worst gas mileage

'''
Part 4
Use groupby and aggregations to explore the relationships 
between mpg and the other variables.  Which variables seem to have the greatest
effect on mpg?
Some examples of things you might want to look at are:
- What is the mean mpg for cars for each number of cylindres (i.e. 3 cylinders,
  4 cylinders, 5 cylinders, etc)?
- Did mpg rise or fall over the years contained in this dataset?
- What is the mpg for the group of lighter cars vs the group of heaver cars?
Note: Be creative in the ways in which you divide up the data.  You are trying
to create segments of the data using logical filters and comparing the mpg
for each segment of the data.
'''

auto.groupby(by='cylinders').mpg.mean() # This is the mean grouped by each number of cylinders.

auto.groupby(by='model_year').mpg.mean() # Miles per gallon actually rose ovder the years.

auto[auto.weight <= auto.weight.median()].mpg.mean() # Prints the average of the lighter cars in the dataset. The lighter being any car under the median.
auto[auto.weight > auto.weight.median()].mpg.mean() # Prints the average of the heavier cars in the dataset. The heavier being any car over the median.
# The lighter cars get better miles per gallon than the heavier cars in the dataset.