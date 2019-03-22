class KandinskyFigureGenerator:

   kandinsky_colors = ['red','yellow', 'blue']

   def square (d,cx,cy,s,f):
        s = 0.7 * s
        d.rectangle(((cx-s/2, cy-s/2), (cx+s/2, cy+s/2)), fill=f)

   def circle (d,cx,cy,s,f):
        # correct the size to  the same area as an square
        s = 0.7 * s * 4 / math.pi 
        d.ellipse(((cx-s/2, cy-s/2), (cx+s/2, cy+s/2)), fill=f)

   def triangle (d,cx,cy,s,f):
        r = math.radians(30)
        # correct the size to  the same area as an square
        s = 0.7 * s * 3 * math.sqrt(3) / 4
        dx = s * math.cos (r) / 2
        dy = s * math.sin (r) / 2
        d.polygon([(cx,cy-s/2), (cx+dx, cy+dy), (cx-dx,cy+dy)], fill = f)

   kandinsky_shapes = [square, circle, triangle]


   def __init__(self, width=200, minobj = 4, maxobj = 4):
      self.width = width
      self.minobj = minobj
      self.maxobj = maxobj

   def checkShape(self, shape):
