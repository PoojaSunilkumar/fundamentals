# -*- coding: utf-8 -*-
"""
Created on Wed May  3 19:03:44 2023

@author: BINEESHA BABY
"""

#import modules
import numpy as np
import matplotlib.pyplot as plt

#read data from file
data= np.genfromtxt('data9_1568485286.csv', delimiter=' ')
print (data)

#derive the distribution of values by binning them into 20 bins
#ohist contains numbers of entries in each bin, oedge contains bin boundaries
ohist, oedge = np.histogram(data, bins=20)

# calculate bin centre locations and bin widths
xdst=0.5*(oedge[1:]+oedge[:-1])
wdst=oedge[1:]-oedge[:-1]

# normalise the distribution
#ydist is a discrete PDF
ydst = ohist/np.sum(ohist)

#cumulative distribution
cdst=np.cumsum(ydst)

plt.figure(0)

# Plot the PDF
plt.bar(xdst, ydst, width=0.9*wdst)

plt.xlabel('Weight(Kg)', fontsize=15)
plt.ylabel('Probability', fontsize=15)
plt.title('Distribution of weight of Newborns', fontsize=15)

#Mean value
xmean=np.sum(xdst*ydst)
#and plot it
plt.plot([xmean,xmean],[0.0,max(ydst)], c='red')
text = ''' Mean Weight (W~): {} Kg'''.format(np.round(xmean, 2))
plt.text(x=xmean, y=max(ydst), s=text, fontsize=10, c='red')

# Calculate X such that 0.10 of newborns are born with a weight<X value
indx = np.argmin(np.abs(cdst-0.10))
xhigh=oedge[indx]
plt.bar(xdst[0:indx], ydst[0:indx], width=0.9*wdst[0:indx], color='green', label='10% of newborns from the \n distribution are born with a \n weight below: 2.69(X value)')
plt.bar(xdst[indx:], ydst[indx:], width=0.9*wdst[indx:], color='blue', label='Weight distribution')
plt.plot([xhigh,xhigh],[0.0,0.1], c='blue')
text ='''X Value: {}'''.format(np.round(xhigh, 2))
plt.text(x=2.0,y=0.1,s=text, fontsize=10, c='blue')

#add legend
plt.legend(loc='center left' ,fontsize='8',bbox_to_anchor=(0.0,0.88))