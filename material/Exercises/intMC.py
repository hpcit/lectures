#!/usr/bin/python

import numpy as np
from random import random
import time

##### input section  ########

n = 1000000   # number of random points 

a = 0.0
b = 1.0

def func(x):
  return 1+2*x

##### input section  ########


# loop version
integral = 0.0
t1 = time.clock()
for i in xrange(n):
  x = (b-a)*random()+a
  integral += func(x) * (b-a)/n
t2 = time.clock()
print 'integral %s calculated in %s sec' % (integral,t2-t1) 


# NumPy version
integral = 0.0
t1 = time.clock()
x = np.random.uniform(a,b,n)
integral = (func(x)*(b-a)/n).sum() 
t2 = time.clock()
print 'integral %s calculated in %s sec' % (integral,t2-t1) 
