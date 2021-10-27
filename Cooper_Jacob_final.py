# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:17:40 2021

@author: corre
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


indata = pd.read_excel("15.xlsx",
                   sheet_name = "Rebaixamento",
                   skiprows = 13, nrows = 10)

t = np.copy(indata.iloc[:,0]) # Tempo
s = np.copy(indata.iloc[:,3]) # Rebaixamento
Q = 400*24#np.nanmean(np.copy(indata.iloc[:,2])) #Vazão (ultima)
num_medições = len(s)


plt.scatter(t,s)
a, b = np.polyfit(np.log(t), s, 1)

print(a,b,Q)
plt.semilogx(t, a * np.log(t) + b, 'g--')

#r = 30
t0 = (np.exp(-b/a))/(24*60)
s1 =  a * np.log(1) + b
s2 =  a * np.log(10) + b
T = (2.3*Q)/(4*3.141592653589793*(s2-s1))
#S = (2.25*T*t0)/(r*r)
print(num_medições, 't0',t0,'s1', s1,'s2', s2,'T',T, 'Q', Q)
plt.xscale('log')

plt.show()