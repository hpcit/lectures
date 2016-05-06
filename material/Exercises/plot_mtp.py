#!/usr/bin/python 

import numpy as np
import matplotlib.pyplot as plt

mydtype=np.dtype([('Year','<f8'),('Jan', '<f8'), ('Feb', '<f8'), ('March', '<f8'), ('April', '<f8'), ('May', '<f8'), ('June', '<f8'), ('July', '<f8'), ('August', '<f8'), ('Sept', '<f8'), ('Oct', '<f8'), ('Nov', '<f8'), ('Dec', '<f8'),('Annual','<f8')])

data =  np.loadtxt('mtcimone.co2',skiprows=17,dtype=mydtype)


A = np.vstack([data['Year'], np.ones(data['Year'].size)])   # A.shape (19,2)
A = A.transpose()
result = np.linalg.lstsq(A,data['Annual'])  # A->x, data['Annual']->y
m,b = result[0]  # m,b coefficients of y = mx + b 

mp,bp = np.polyfit(data['Year'],data['Annual'],1) # alternative way to
                                                  # calculate m,b coefficients 

plt.plot(data['Year'],data['Annual'], 'o',
         data['Year'],m * data['Year'] + b,'b',
         data['Year'],mp * data['Year'] + bp,'g',) # test the fit 


plt.show()
