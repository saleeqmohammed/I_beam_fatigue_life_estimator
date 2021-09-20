#!/usr/bin/env python
#author : Mohammed saleeq k
from numpy import fabs as fabs
import numpy as np

# uc_mult (float): partial-load scaling [opt, default=0.5]
def rainflow(array_ext,
               uc_mult=0.5):
   
    
    tot_num = array_ext.size                # total size of input array
    array_out = np.zeros((3, tot_num-1))    # initialize output array
    
    pr = 0                                  # index of input array
    po = 0                                  # index of output array
    j = -1                                  # index of temporary array "a"
    a  = np.empty(array_ext.shape)          # temporary array for algorithm
    
    # loop through each turning point stored in input array
    for i in range(tot_num):
        
        j += 1                  # increment "a" counter
        a[j] = array_ext[pr]    # put turning point into temporary array
        pr += 1                 # increment input array pointer
        
        while ((j >= 2) & (fabs( a[j-1] - a[j-2] ) <= \
                fabs( a[j] - a[j-1]) ) ):
            lrange = fabs( a[j-1] - a[j-2] )
              
            # partial range
            if j == 2:
                mean      = ( a[0] + a[1] ) / 2.
                
                a[0]=a[1]
                a[1]=a[2]
                j=1
                if (lrange > 0):
                    array_out[0,po] = lrange
                    array_out[1,po] = mean 
                    array_out[2,po] = uc_mult
                    po += 1
                
            # full range
            else:
                mean      = ( a[j-1] + a[j-2] ) / 2.
                a[j-2]=a[j]
                j=j-2
                if (lrange > 0):
                    array_out[0,po] = lrange
                    array_out[1,po] = mean
                    array_out[2,po] = 1.00
                    po += 1
                    
    # partial range
    for i in range(j):
        lrange    = fabs( a[i] - a[i+1] )
        mean      = ( a[i] + a[i+1] ) / 2.
        if (lrange > 0):
            array_out[0,po] = lrange
            array_out[1,po] = mean
            array_out[2,po] = uc_mult
            po += 1  
            
    # get rid of unused entries
    array_out = array_out[:,:po]

    return array_out
    
#output_format
#[Range,Mean,Count]