import math

import inflect
import numpy as np
from PIL import Image, ImageDraw

inflectEng = inflect.engine()

class CaptionGenerator:

    def __init__(self, universe):
        self.u = universe
      
    def colorShapesSize (self, kf, prefix = ''):
        descrition = prefix
        multipleshape = False
        addsizeattribute = False

        mins = 999999999999
        maxs = 0
        for s in kf:
            if s.size < mins: mins = s.size
            if s.size > maxs: maxs = s.size    
        d = maxs - mins
        if d > 0.2:
            addsizeattribute = True
            smallsizecheck = mins + d/3
            bigsizecheck = maxs - d/3

        for s in kf:
            if multipleshape: descrition = descrition + " and " + prefix 
            if addsizeattribute:    
                sizestring = ''
                if s.size < smallsizecheck: sizestring = 'small'
                if s.size > bigsizecheck:   sizestring = 'big'
                if len (sizestring) > 0:  descrition = descrition + sizestring +  " "
            descrition = descrition  +  s.color +  " " +  s.shape
            multipleshape = True 
        
        return descrition
  
  
    def numbers (self, kf):  
        descrition =  self.colorShapesSize (kf, 'one ')
        ns = {}
        nc = {}
        for s in self.u.kandinsky_shapes: ns[s] = 0
        for s in self.u.kandinsky_colors: nc[s] = 0
        for s in kf:
            ns[s.shape] += 1
            nc[s.color] += 1
        maxcolor = ''
        maxshape = ''
        maxnumcolor = 0
        maxnumshap  = 0
        for c in self.u.kandinsky_colors: 
            if nc[c] > maxnumcolor:
                maxnumcolor = nc[c]
                maxcolor = c
        for s in self.u.kandinsky_shapes: 
            if ns[s] > maxnumshap:
                maxnumshap = ns[s]
                maxshape = s

        if maxnumcolor > 1 or maxnumshap > 1:
            if maxnumcolor >= maxnumshap:
                descrition =  inflectEng.number_to_words(maxnumcolor) + " " + maxcolor + " shapes"
            else:  
                descrition = inflectEng.number_to_words(maxnumcolor) + " " + maxshape + "s"
            if (maxnumcolor == maxnumshap):
                descrition = inflectEng.number_to_words(maxnumcolor) + " " + maxcolor + " " + maxshape + "s"
            
        return descrition  
    

    def pairs (self, kf):  
        # thats not perfect, it e.g. does not describe two pairs, or a pair, if some other shape has 3 objects
        descrition =  ""
        ns = {}
        for s in self.u.kandinsky_shapes: 
            ns[s] = 0
        for s in kf:
            ns[s.shape] += 1
        maxshape = ''
        maxnumshap  = 0
        for s in self.u.kandinsky_shapes: 
            if ns[s] > maxnumshap:
                maxnumshap = ns[s]
                maxshape = s
        if maxnumshap ==  2:
            descrition = "a pair of "+ maxshape + "s"    
        return descrition
