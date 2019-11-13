import math

import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageColor


class kandinskyShape:
  def __init__(self):
          self.shape = "circle"
          self.color = "red"
          self.x     = 0.5
          self.y     = 0.5
          self.size  = 0.5
  
  def __str__(self):  
      return self.color + " " +  self.shape + " (" + \
             str(self.size) + "," + str(self.x) + "," + str(self.y) + ")"

class SimpleUniverse:
   kandinsky_colors = ['red','yellow', 'blue']
   kandinsky_shapes = ['square', 'circle', 'triangle']

class ExtendedUniverse:
   # still have to add drawing functions below 
   kandinsky_colors = ['red', 'yellow', 'blue', "green", "orange"]
   kandinsky_shapes = ['square', 'circle', 'triangle', "star"]


def square (d,cx,cy,s,f):
        s = 0.6 * s
        d.rectangle(((cx-s/2, cy-s/2), (cx+s/2, cy+s/2)), fill=f)

def circle (d,cx,cy,s,f):
        # correct the size to  the same area as an square
        s =  0.6 * math.sqrt (4 * s * s / math.pi)
        d.ellipse(((cx-s/2, cy-s/2), (cx+s/2, cy+s/2)), fill=f)

def triangle (d,cx,cy,s,f):
        r = math.radians(30)
        # correct the size to  the same area as an square
        s =  0.6 * math.sqrt (4 * s * s / math.sqrt(3))
        s =  math.sqrt(3) * s / 3
        dx = s * math.cos (r) 
        dy = s * math.sin (r) 
        d.polygon([(cx,cy-s), (cx+dx, cy+dy), (cx-dx,cy+dy)], fill = f)


def kandinskyFigureAsImagePIL (shapes, width=600, subsampling = 4):

  image = Image.new("RGBA", (subsampling*width,subsampling*width), (150,150,150,255))
  d = ImageDraw.Draw(image)
  w = subsampling * width

  for s in shapes:
      globals()[s.shape]( d, w*s.x, w*s.y, w*s.size, s.color)
  if subsampling>1:
    image.thumbnail( (width,width), Image.ANTIALIAS)

  return image


def kandinskyFigureAsImage (shapes, width=600, subsampling = 4):

  w = subsampling * width
  img = np.zeros((w, w, 3), np.uint8)
  img[:, :] = [150, 150, 150]

  for s in shapes:
      # not sure if this is the right color for openCV
      rgbcolorvalue = ImageColor.getrgb (s.color)

      if s.shape == "circle":
          size  =  0.5 * 0.6 * math.sqrt (4 * w*s.size * w*s.size / math.pi)
          cx = round(w*s.x)
          cy = round(w*s.y)
          cv2.circle (img,(cx, cy), round(size), rgbcolorvalue, -1)

      if s.shape == "triangle":
          r = math.radians(30)
          size  = 0.5 * math.sqrt(3) * w*s.size / 3
          dx = size * math.cos (r) 
          dy = size * math.sin (r) 
          p1 = (round(w*s.x), round(w*s.y-size))
          p2 = (round(w*s.x+dx), round(w*s.y+dy))
          p3 = (round(w*s.x-dx), round(w*s.y+dy))
          points = np.array([p1, p2, p3])
          cv2.fillConvexPoly (img, points, rgbcolorvalue, 1)

      if s.shape == "square":
          size  =  0.5 * 0.6  * w*s.size 
          xs = round(w*s.x - size)
          ys = round(w*s.y - size)
          xe = round(w*s.x + size)
          ye = round(w*s.y + size)
          cv2.rectangle (img,(xs, ys), (xe,ye), rgbcolorvalue, -1)

  img_resampled= cv2.resize(img, (width, width), interpolation=cv2.INTER_AREA)        
  image = Image.fromarray(img_resampled)
  
  return image

def overlaps (shapes, width=1024):

  image = Image.new("L", (width,width), 0)
  sumarray = np.array(image)
  d = ImageDraw.Draw(image)
  w = width

  for s in shapes:
    image      = Image.new("L", (width,width), 0)
    d = ImageDraw.Draw(image)
    globals()[s.shape]( d, w*s.x, w*s.y, w*s.size, 10)
    sumarray = sumarray + np.array(image)

  sumimage = Image.fromarray (sumarray)
  return sumimage.getextrema ()[1] > 10
