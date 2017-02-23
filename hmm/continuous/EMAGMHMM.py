'''
Created on Nov 14, 2012

@author: GuyZ
'''

import numpy

from DurationGMHMM import DurationGMHMM
from hmmDuration.weights.EWMA import EWMA


class EMAGMHMM(DurationGMHMM,EWMA):
    '''
    An Exponentially Weighted Moving Averages Gaussian Mixtures HMM - 
    This is a representation of a continuous HMM, containing a mixture of gaussians in 
    each hidden state, and includes an internal weighing function that gives more
    significance to newer observations.
    
    It should be noted that an open issue is that log likelihood fails to increase
    in each iteration using such weighted observations, although the equations
    appear to be sound. Nevertheless, this is the first open source implementation
    of such HMMs.
    
    For more information, refer to DurationGMHMM.
    '''

    def __init__(self,n,m,d=1,A=None,means=None,covars=None,w=None,pi=None,min_std=0.01,init_type='uniform',precision=numpy.double,verbose=False):
        print "Warning: weighted EMs may not converge to local optima, since the log-likelihood function may decrease."
        print
        
        DurationGMHMM.__init__(self,n,m,d,A,means,covars,w,pi,min_std,init_type,precision,verbose) #@UndefinedVariable
        EWMA.__init__(self)
        