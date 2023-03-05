# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 23:25:12 2023

@author: Akhil Jose Britto
"""
#Importing the modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Defining the Line Plot showing growth % in GDP
def line_plot():
    plt.figure()
    #Plotting a line plot with the year in x-axis and each corresponding country in the y-axis
    plt.plot(gdp_growth_year,Brazil,label = 'Brazil',marker = ".")
    plt.plot(gdp_growth_year,China,label = 'China',marker = ".")
    plt.plot(gdp_growth_year,Ghana,label = 'Ghana',marker = ".")
    plt.plot(gdp_growth_year,Germany,label = 'Germany',marker = ".")
    plt.plot(gdp_growth_year,India,label = 'India',marker = ".")
    plt.plot(gdp_growth_year,Japan,label = 'Japan',marker = ".")
    #Label both axis
    plt.xlabel("Year")
    plt.ylabel("GDP Growth %")
    #Removing the white spaces at the start and end of the x-axis plot
    plt.xlim(2007, 2016)
    #Show the legend outside the plot so as to not interfere within the plot
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1), borderaxespad=0)
    #Set the plot title
    plt.title("GDP Growth rate %")
    plt.show()


#Defining the Bar Plot comparing male vs female unemployment rate
def bar_plot():
    plt.figure()
    #Form 4 Subplots of shape 2x2
    plt.subplot(2, 2, 1)
    #Plot a bar plot with Year on the x-axis and the rate of unemployment in y-axis
    plt.bar(year, male_unemployment['Brazil'], color = "cyan",label = "Male")
    #Stack the bar plot representing the female rate on top of the male rate
    plt.bar(year, female_unemployment['Brazil'],bottom = male_unemployment['Brazil'], color = "pink", label = "Female") 
    #Remove the white spaces at the ends of the x-axis
    plt.xlim(2007, 2016)
    #Set the plot title
    plt.title("Brazil")
    #Set the axis labels
    plt.xlabel("Year")
    plt.ylabel("Unemployment Rate")

    plt.subplot(2, 2, 2)
    plt.bar(year, male_unemployment['China'], color = "cyan",label = "Male")
    plt.bar(year, female_unemployment['China'],bottom = male_unemployment['China'], color = "pink", label = "Female")
    plt.xlim(2007, 2016)
    plt.title("China")
    plt.xlabel("Year")
    plt.ylabel("Unemployment Rate")

    plt.subplot(2, 2, 3) 
    plt.bar(year, male_unemployment['India'], color = "cyan",label = "Male")
    plt.bar(year, female_unemployment['India'],bottom = male_unemployment['India'], color = "pink", label = "Female") 
    plt.xlim(2007, 2016)
    plt.title("India")
    plt.xlabel("Year")
    plt.ylabel("Unemployment Rate")

    plt.subplot(2, 2, 4)
    plt.bar(year, male_unemployment['Japan'], color = "cyan",label = "Male")
    plt.bar(year, female_unemployment['Japan'],bottom = male_unemployment['Japan'], color = "pink", label = "Female") 
    plt.xlim(2007, 2016)
    plt.title("Japan")
    plt.xlabel("Year")
    plt.ylabel("Unemployment Rate")
    #Plot the legend just outside the graph
    plt.legend(loc='lower left', bbox_to_anchor=(1.1,1.1), borderaxespad=0)
    #Set the layout as tight so that the plot labels do not overlap with each other
    plt.tight_layout()
    plt.show()

#Defining the Scatter Plot showing average growth in GDP over the period in the line plot
def scatter_plot():
    plt.figure()
    #Scatter plot points with the Country name on the x-axis and the average value right above it on the y-axis
    plt.scatter("Brazil",np.average(Brazil),s=np.average(Brazil)*50,label = 'Brazil')
    #Use np.average() to calculate the average value of each country from the previous data set
    plt.scatter("China",np.average(China),s=np.average(China)*50,label = 'China')
    #Set s as the average value * 50 to represent the plot point thickness respective to it's value
    plt.scatter("Ghana",np.average(Ghana),s=np.average(Ghana)*50,label = 'Ghana')
    plt.scatter("Germany",np.average(Germany),s=np.average(Germany)*50,label = 'Germany')
    plt.scatter("India",np.average(India),s=np.average(India)*50,label = 'India')
    plt.scatter("Japan",np.average(Japan),s=np.average(Japan)*50,label = 'Japan')
    #Set the axis labels
    plt.xlabel("Countries")
    plt.ylabel("Average GDP Growth %")
    #Define the legend outside the grapth so it doesn't overlap with the plot points
    lgnd = plt.legend(loc='upper right', bbox_to_anchor=(1.25,1), borderaxespad=0,labelspacing = 1.2)
    #Set the marker size of elements in the legend to a common font  
    for handle in lgnd.legendHandles:
        handle.set_sizes([150.0])
    #Set the graph title
    plt.title("Average GDP Growth through 2007 - 2016")
    plt.show()

#Defining the Pie Chart comparing combined Male and Fermale Unemployment between the years 2010 and 2014
def pie_chart():
    plt.figure()
    #Create 2 sub plot pie charts of shape 1x2
    plt.subplot(1, 2, 1)
    #Plot the chart with the sum of both male and female rates from the year 2010
    plt.pie(male_unemployment.iloc[3,1:] + female_unemployment.iloc[3,1:])
    #Set the subplot title as the year
    plt.title("2010")

    plt.subplot(1, 2, 2 )
    #Plot the chart with the sum of both male and female rates from the year 2014
    plt.pie(male_unemployment.iloc[8,1:] + female_unemployment.iloc[8,1:])
    plt.title("2014")
    #Set the format as tight layout so the plot is arranged without overlapping other values
    plt.tight_layout()
    #Set the Main title for both subplotss
    plt.suptitle('                     Total unemployment figures in 2010 vs 2014')
    #Set the location for legend so there's no overlapping with the plot values
    plt.legend(labels = male_unemployment.iloc[:,1:],bbox_to_anchor=(1.5,0.95))
    plt.show()

#Main program

#Line and Scatter Plot data
gdp_growth = pd.read_excel(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\GDP growth.xlsx")
#Extracting the data from the GDP Growth % excel sheet into a pandas data frame
gdp_growth_year = np.array(gdp_growth["Year"])
#Taking the Year column from the data frame into a numpy array

Brazil = np.array(gdp_growth["Brazil"])
#Extracting each country column values from the data frame into a numpy array
China = np.array(gdp_growth["China"])
Ghana = np.array(gdp_growth["Ghana"])
Germany = np.array(gdp_growth["Germany"])
India = np.array(gdp_growth["India"])
Japan = np.array(gdp_growth["Japan"])

#Bar plot and Pie chart data
male_unemployment = pd.read_excel(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Unemployment figures Male.xlsx")
female_unemployment = pd.read_excel(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Unemployment figures Female.xlsx")
#Extracting the excel sheet values into Pandas DataFrame
year = np.array(male_unemployment['Year'])
#Taking the year column from the data frame which is common to both Male and Female Graphs 

#Excecute the graphs    
line_plot()
bar_plot()
scatter_plot()
pie_chart()
