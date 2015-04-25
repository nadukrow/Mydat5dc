# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 13:40:43 2015

@author: nadukrow
"""

#PART 1: read in the data, parse it, and store it in a list of lists called 'data'
#Hint: this is a tsv file, and csv.reader() needs to be told how to handle it

#The answer is  import csv #Imported the csv reading module
with open('airline_safety.csv', 'rU') as f: #Used this method to create a list of lists.
    data = [row for row in csv.reader(f)]
    
#PART 2: separate the header and data into two different lists
    
head = data[0] #Head becomes the first line of the data.
data = data[1:] #Data becomes the actual data after the first row which was the header information.

#PART 3: calculate the average price of an order
#Hint: examine the data to see if the 'quantity' column is relevant to this calculation
#Hint: work smarter, not harder! (this can be done in a few lines of code)

#To calculate the average price of an order we need to have the sum of all prices be the numerator and total number of orders be the denominator.
total_orders = 1864 #When looking at the data set you see that the last order of the list is 1864.
prices = [float(row[4][1:-1]) for row in data] #It keeps saying could not convert string to float?
sum(prices) / total_orders #The answer we get is $18.50. We get this by getting the sum of the prices and dividing that by the total number of orders. 

#PART 4: create a list (or set) of all unique sodas and soft drinks that they sell
#Note: just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'

sodas = [] #First create an empty list labeled sodas.
for row in data: #For each row in data...
    if 'Canned' in row[2]: #If the string Canned appears... 
        sodas.append(row[3][1:-1])      #Add those rows to the empty sodas list.
        
unique_sodas = set(sodas) #The set function allows us to only print the repeated items in the new sodas list.

#PART 5: calculate the average number of toppings per burrito
#Note: let's ignore the 'quantity' column to simplify this task
#Hint: think carefully about the easiest way to count the number of toppings
#Hint: 'hello there'.count('e')

#???

#PART 6: create a dictionary in which the keys represent chip orders and
  #the values represent the total number of orders
#Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
#Note: please take the 'quantity' column into account!
#Advanced: learn how to use 'defaultdict' to simplify your code

chips = {} #Create an empty dictionary for chips

# if chip order is not in dictionary, then add a new key/value pair
# if chip order is already in dictionary, then update the value for that key
for row in data:
    if 'Chips' in row[2]: #If the order for chips is in the dictionary than we add a new key/value
        if row[2] not in chips:
            chips[row[2]] = int(row[1])     # this is a new key, so create key/value pair
        else:             #If the chip order is already in the dictionary this will update the value for that key.
            chips[row[2]] += int(row[1])    # this is an existing key, so add to the value