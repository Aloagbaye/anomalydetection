# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 04:33:04 2017

@author: Aloagbaye
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as mt
import scipy.stats as sp

def prob(x,miu,sigma,store_prob):
     pbt = [0]*len(x[0,:]);
     for j in range(len(x[0,:])):
        if sigma[j]==0:
           pbt[j]=[1]*len(x[:,0]);
        else:
           pbt[j] = sp.norm.pdf(x[:,j],miu[j],mt.sqrt(sigma[j]));
     pbt=np.array(pbt)
     print(pbt)
     for j in range(len(x[:,0])): 
        store_prob[j]=np.prod(pbt[:,j]);

#cols= ['Read1', 'Write1', 'Read2', 'Write2', 'Read3', 'Write3', 'Read4', 'Write4']
df = pd.read_csv('anomali.csv')
x= df.drop(0)
#x=x.drop(1)
x=x.as_matrix()
x=np.array(x).astype(np.float)
i=0;
b=len(x[:,0])
c=len(x[0,:])
store_means=[0]*b;
store_vars=[0]*b; 
store_prob=[0]*b;    
store_means[0]=np.mean(x[0,:c]);
store_vars[0]=x[0,:c].var();           
for j in range(len(x[0,:])):
    store_means[j]=np.mean(x[0:,j])
    store_vars[j]=x[0:,j].var()
 
prob(x,store_means,store_vars,store_prob)
outliers=np.asarray(np.where(np.array(store_prob) <= 0.00248))
plt.figure() 
plt.plot(store_prob,"-bo", markevery=outliers[0])
#plt.plot(outliers,'bo') 
plt.show()
print(outliers)

#                a= a*((1/(mt.sqrt(2*mt.pi*sigma[i])))*mt.pow(mt.e, -(mt.pow(x[i,j]-miu[i], 2)/(2*sigma[i]))));
