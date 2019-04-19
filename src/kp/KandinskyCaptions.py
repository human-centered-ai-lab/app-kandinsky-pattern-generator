import math
from collections import defaultdict

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
  

    def _getMaxShapesAndColorsPatterns (self, kf):
        result = []
        ncs = defaultdict(dict)
        nc = defaultdict(dict)
     
        for s in self.u.kandinsky_shapes: 
            for c in self.u.kandinsky_colors: 
                ncs[s][c] = 0      
        for c in self.u.kandinsky_colors: 
                nc[c] = 0      
        for s in kf: 
            ncs[s.shape][s.color] = ncs[s.shape][s.color] + 1
            nc[s.color] = nc[s.color] + 1      
     
        maxcolor = ''
        maxshape = ''
        maxn = 0
        for s in kf:
            if ncs[s.shape][s.color] > maxn:
                maxn = ncs[s.shape][s.color] 
                maxcolor = s.color
                maxshape = s.shape

        maxo = 0
        for s in kf:
            if nc[s.color] > maxo:
                maxo = nc[s.color] 
                maxcoloro = s.color

        # color is stringer than object pairs
        colordominance = False
        if maxo > maxn:
            maxn = maxo
            maxcolor = maxcoloro
            colordominance = True

        if maxn > 0:
            kfnew = []
            if colordominance:
                maxshape = 'object'
                for s in kf:
                    if s.color != maxcolor:  kfnew.append (s)
            else:  
                for s in kf:  
                    if s.shape !=  maxshape or s.color != maxcolor:  kfnew.append (s)

            r_rest = []     
            if len(kfnew) > 0:
                r_rest = self._getMaxShapesAndColorsPatterns (kfnew)

            descrition = inflectEng.number_to_words(maxn) + " " + maxcolor + " " + maxshape 
            if maxn > 1:
                descrition = descrition + "s"
            result = [{'n': maxn, 'd': descrition }] + r_rest
        return result        

    def numbers (self, kf):  
        descrition = ''
        unsortedDesc = self._getMaxShapesAndColorsPatterns (kf)
        if len(unsortedDesc) > 0:
            sortesDesc   = sorted(unsortedDesc, reverse=True, key=lambda k: k['n']) 
            multiple = False
            descrition = []

            for d in sortesDesc:
                if multiple: 
                    descrition = descrition + " and " + d['d']  
                else:
                    descrition = d['d']  
                    multiple = True 

        return descrition  

    def simpleNumbers (self, kf):  
        return str(len (kf)) + ", " + inflectEng.number_to_words(len (kf))      
