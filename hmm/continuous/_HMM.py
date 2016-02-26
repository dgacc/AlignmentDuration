'''
Created on Feb 24, 2016

@author: joro
'''
from hmm.continuous._ContinuousHMM import _ContinuousHMM
import numpy
import sys
from numpy.core.numeric import Infinity
from django.contrib.gis.shortcuts import numpy


class _HMM(_ContinuousHMM):
    '''
    classical Viterbi
    '''
    
    def __init__(self,statesNetwork, numMixtures, numDimensions, transMatrix):
    
#     def __init__(self,n,m,d=1,A=None,means=None,covars=None,w=None,pi=None,min_std=0.01,init_type='uniform',precision=numpy.double, verbose=False):
            '''
            See _ContinuousHMM constructor for more information
            '''
            means, covars, weights, pi = self._constructHMMNetworkParameters(statesNetwork, numMixtures, numDimensions)
             
            n = len(statesNetwork)
            min_std=0.01
            init_type='uniform'
            precision=numpy.double
            verbose = False 
            _ContinuousHMM.__init__(self, n, numMixtures, numDimensions, transMatrix, means, covars, weights, pi, min_std,init_type,precision,verbose) #@UndefinedVariable
    
            self.statesNetwork = statesNetwork
            

      
    def _constructHMMNetworkParameters(self,  statesSequence, numMixtures, numDimensions):
        '''
        tranform other htkModel params to  format of gyuz's hmm class
        '''
        
       
        numStates = len(statesSequence)
        means = numpy.empty((numStates, numMixtures, numDimensions))
        
        # init covars
        covars = [[ numpy.matrix(numpy.eye(numDimensions,numDimensions)) for j in xrange(numMixtures)] for i in xrange(numStates)]
        
        weights = numpy.ones((numStates,numMixtures),dtype=numpy.double)
        
        # start probs :
        pi = numpy.zeros((numStates), dtype=numpy.double)
        
        # avoid log(0) 
        pi.fill(sys.float_info.min)
#          allow to start only at first state
        pi[0] = 1

#         pi[0] = 0.33
#         pi[1] = 0.33
#         pi[2] = 0.33
        
        # equal prob. for states to start
#         pi = numpy.ones( (numStates)) *(1.0/numStates)
        
    
         
        if statesSequence==None:
            sys.exit('no state sequence')
               
        for i in range(len(statesSequence) ):
            state  = statesSequence[i] 
            
            for (numMixture, weight, mixture) in state.mixtures:
                
                weights[i,numMixture-1] = weight
                
                means[i,numMixture-1,:] = mixture.mean.vector
                
                variance_ = mixture.var.vector
                for k in  range(len( variance_) ):
                    covars[i][numMixture-1][k,k] = variance_[k]
        return means, covars, weights, pi    
        
        
        
    def initDecodingParameters(self, observations):
        '''
        helper method to init all params
        '''
        lenObservations = len(observations)
        
        self._mapB(observations)
#         self._mapB_OLD(observations)
        
        self.phi = numpy.empty((lenObservations,self.n),dtype=self.precision)
        self.phi.fill(-Infinity)
    
       
        # backpointer: form which prev. state
        self.psi = numpy.empty((lenObservations, self.n), dtype=self.precision)
        self.psi.fill(-1)
        
        for x in xrange(self.n):
            currLogPi = numpy.log(self.pi[x])
            self.phi[0][x] = currLogPi + self.B_map[x][0]
            self.psi[0][x] = 0
    
    def viterbi_fast(self, observations):
        
        for t in xrange(1,len(observations)):
            self.logger.debug("at time {} out of {}".format(t, len(observations)))
            for j in xrange(self.n):
#                 for i in xrange(self.n):
#                     if (delta[t][j] < delta[t-1][i]*self.A[i][j]):
#                         delta[t][j] = delta[t-1][i]*self.A[i][j]
                        
                        
                        sliceA = self.A[:,j] 
#                         print "shape A:" + str(self.A.shape)
#                         print "shape phi:" + str(self.phi.shape)
                        AandPhi = numpy.add(self.phi[t-1,:], sliceA)
                        
                        self.phi[t][j] = numpy.max(AandPhi)
                        self.phi[t][j] =+ self.B_map[j][t]

                        self.psi[t][j] = numpy.argmax(AandPhi)
                    
        return self.psi
        