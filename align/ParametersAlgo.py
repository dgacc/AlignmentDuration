'''
Created on May 28, 2015

@author: joro
'''
import logging
from docutils.nodes import math
from numpy.ma.core import  floor

######### PARAMS:
class ParametersAlgo(object):
    
    FOR_JINGJU = 0
    FOR_MAKAM = 0
    
    GLOBAL_WAIT_PROB = 0.8
    
    THRESHOLD_PEAKS = -70

    DEVIATION_IN_SEC = 0.1

    # unit: num frames
    NUMFRAMESPERSECOND = 100
    # same as WINDOWSIZE in wavconfig singing. unit:  seconds. TOOD: read from there automatically
    WINDOW_SIZE = 0.025
    
    # in frames
    
    ONLY_MIDDLE_STATE = 1
    
    WITH_SHORT_PAUSES = 1
    
    # padded a short pause state at beginning and end of sequence
    WITH_PADDED_SILENCE = 1
    
    # no feature vectors at all. all observ, probs. set to 1
    WITH_ORACLE_PHONEMES = -1
    WITH_ORACLE_PHONEMES = 0

    PATH_TO_HCOPY= '/usr/local/bin/HCopy'
    # ANDRES. On kora.s.upf.edu
    # PATH_TO_HCOPY= '/srv/htkBuilt/bin/HCopy'      
    
    POLYPHONIC = 0
    
    WITH_ORACLE_ONSETS = 1
    ### no onsets at all. 
    WITH_ORACLE_ONSETS = -1
    
    # Sigma of onset smoothing function g: normal distribution
    ONSET_SIGMA = 0.075
    ONSET_SIGMA_IN_FRAMES = int(floor(ONSET_SIGMA * NUMFRAMESPERSECOND))
    if ONSET_SIGMA_IN_FRAMES % 2 == 0:
        ONSET_SIGMA_IN_FRAMES += 1
    
#     ONSET_TOLERANCE_WINDOW = 0.02 # seconds. to work implement decoding with one onset only
    ONSET_TOLERANCE_WINDOW = 0 # seconds

    # in _ContinousHMM.b_map cut probabilities
    CUTOFF_BIN_OBS_PROBS = 30
    
    # for jingju
    CONSONANT_DURATION_IN_SEC = 0.3
    # for makam
#     CONSONANT_DURATION_IN_SEC = 0.1 
    
    CONSONANT_DURATION = NUMFRAMESPERSECOND * CONSONANT_DURATION_IN_SEC;
    
    CONSONANT_DURATION_DEVIATION = 0.7
    
    #####
    LOGGING_LEVEL = logging.DEBUG
    VISUALIZE = 0
