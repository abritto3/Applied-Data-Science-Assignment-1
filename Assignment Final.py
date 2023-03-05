# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 23:25:12 2023

@author: HP
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Line Plot showing growth in GDP

gdp_growth = pd.read_excel(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\GDP growth.xlsx")
gdp_growth_year = np.array(gdp_growth["Year"])

Brazil = np.array(gdp_growth["Brazil"])
China = np.array(gdp_growth["China"])
Ghana = np.array(gdp_growth["Ghana"])
Germany = np.array(gdp_growth["Germany"])
India = np.array(gdp_growth["India"])
Japan = np.array(gdp_growth["Japan"])
Netherlands = np.array(gdp_growth["Netherlands"])
Switzerland = np.array(gdp_growth["Switzerland"])


plt.figure()
plt.plot(gdp_growth_year,Brazil,label = 'Brazil',marker = ".")
plt.plot(gdp_growth_year,China,label = 'China',marker = ".")
plt.plot(gdp_growth_year,Ghana,label = 'Ghana',marker = ".")
plt.plot(gdp_growth_year,Germany,label = 'Germany',marker = ".")
plt.plot(gdp_growth_year,India,label = 'India',marker = ".")
plt.plot(gdp_growth_year,Japan,label = 'Japan',marker = ".")
#plt.plot(gdp_growth_year,Netherlands,label = 'Netherlands',marker = ".")
#plt.plot(gdp_growth_year,Switzerland,label = 'Switzerland',marker = ".")
plt.xlabel("Year")
plt.ylabel("GDP Growth %")
plt.xlim(2007, 2016)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1), borderaxespad=0)
plt.title("GDP Growth rate %")
plt.show()

#Bar Plot comparing male vs female uunemployment rate

male_unemployment = pd.read_excel(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Unemployment figures Male.xlsx")
female_unemployment = pd.read_excel(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Unemployment figures Female.xlsx")
year = np.array(male_unemployment['Year'])

plt.figure()

plt.subplot(2, 2, 1)
plt.bar(year, male_unemployment['Brazil'], color = "cyan",label = "Male")
plt.bar(year, female_unemployment['Brazil'],bottom = male_unemployment['Brazil'], color = "pink", label = "Female") 
plt.xlim(2007, 2016)
plt.title("Brazil")
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

plt.legend(loc='lower left', bbox_to_anchor=(1.1,1.1), borderaxespad=0)
plt.tight_layout()
plt.show()

#Scatter Plot showing average growth in GDP


plt.figure()
plt.scatter("Brazil",np.average(Brazil),s=np.average(Brazil)*50,label = 'Brazil')
plt.scatter("China",np.average(China),s=np.average(China)*50,label = 'China')
plt.scatter("Ghana",np.average(Ghana),s=np.average(Ghana)*50,label = 'Ghana')
plt.scatter("Germany",np.average(Germany),s=np.average(Germany)*50,label = 'Germany')
plt.scatter("India",np.average(India),s=np.average(India)*50,label = 'India')
plt.scatter("Japan",np.average(Japan),s=np.average(Japan)*50,label = 'Japan')
#plt.scatter("Netherlands",np.average(Netherlands),s=np.average(Netherlands)*50,label = 'Netherlands')
#plt.scatter("Switzerland",np.average(Switzerland),s=np.average(Switzerland)*50,label = 'Switzerland')
plt.xlabel("Countries")
plt.ylabel("Average GDP Growth %")
lgnd = plt.legend(loc='upper right', bbox_to_anchor=(1.25,1), borderaxespad=0,labelspacing = 1.2)
for handle in lgnd.legendHandles:
    handle.set_sizes([150.0])
plt.title("Average GDP Growth through 2007 - 2016")
plt.show()

#Pie Chart comparing combined Male and Fermale Unemployment between the years 2010 and 2014

plt.figure()

plt.subplot(1, 2, 1)
plt.pie(male_unemployment.iloc[3,1:] + female_unemployment.iloc[3,1:])
plt.title("2010")

plt.subplot(1, 2, 2 )
plt.pie(male_unemployment.iloc[8,1:] + female_unemployment.iloc[8,1:])
plt.title("2014")

plt.tight_layout()
plt.suptitle('                     Total unemployment figures in 2010 vs 2014')
plt.legend(labels = male_unemployment.iloc[:,1:],bbox_to_anchor=(1.5,0.95))
plt.show() 
