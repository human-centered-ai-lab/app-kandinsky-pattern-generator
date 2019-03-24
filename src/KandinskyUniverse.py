import PIL

class SimpleUniverse:

   kandinsky_colors = ['red','yellow', 'blue']
   kandinsky_shapes = ['square', 'circle', 'triangle']

class ExtendedUniverse:

   kandinsky_colors = ['red','yellow', 'blue', "green", "orange"]
   kandinsky_shapes = ['square', 'circle', 'triangle', "star"]


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


def kandinskyFigure (shapes, width=200, subsampling = 2):
  image = Image.new("RGBA", (subsampling*width,subsampling*width), (220,220,220,255))
  d = ImageDraw.Draw(image)
  for s in shapes:
      locals()[s['shape']]( d, width*s['cx'], width*s['cy'], width*s['size'], s['color'] )
  if subsampling>1:
    image.thumbnail( (width,width), Image.ANTIALIAS)
  return image

def overlaps (shapes, width=1024):
  image = Image.new("L", (,WIDTH), 0)
  sumarray = np.array(image)
  d = ImageDraw.Draw(image)
  
  for s in shapes:
    image      = Image.new("L", (width,width), 0)
    d = ImageDraw.Draw(image)
    locals()[s['shape'] ( d, s['cx'], s['cy'], s['size'], 10 )
    sumarray = sumarray + np.array(image)

  sumimage = Image.fromarray (sumarray)
  return sumimage.getextrema ()[1] > 10
