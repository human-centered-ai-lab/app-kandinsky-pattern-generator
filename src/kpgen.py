import os

from PIL import Image
from kp import KandinskyUniverse, RandomKandinskyFigure, SimpleObjectAndShape, ShapeOnShapes, KandinskyCaptions

u  = KandinskyUniverse.SimpleUniverse()
cg = KandinskyCaptions.CaptionGenerator (u)


def generateImagesAndCaptions (basedir, kfgen, n=50):
    os.makedirs(basedir, exist_ok=True)
    for (i, kf) in enumerate(kfgen.true_kf (n)):
        image = KandinskyUniverse.kandinskyFigureAsImage (kf)
        image.save (basedir + "/%06d" % i + ".png")
        print ("========================")
        print (cg.colorShapesSize (kf))
        print (cg.numbers (kf))
        print (cg.pairs (kf))
    
def generateClasses (basedir, kfgen, n=50,  contrafactuals = False):
    os.makedirs(basedir + "/true", exist_ok=True)
    os.makedirs(basedir + "/false", exist_ok=True)
    for (i, kf) in enumerate(kfgen.true_kf (n)):
        image = KandinskyUniverse.kandinskyFigureAsImage (kf)
        image.save (basedir + "/true/%06d" % i + ".png")
    for (i, kf) in  enumerate(kfgen.false_kf (n)):
        image = KandinskyUniverse.kandinskyFigureAsImage (kf)
        image.save (basedir + "/false/%06d" % i + ".png")
    if (contrafactuals):
        os.makedirs(basedir + "/contrafactuals", exist_ok=True)
        for (i, kf) in enumerate(kfgen.almost_true_kf (n)):
            image = KandinskyUniverse.kandinskyFigureAsImage (kf)
            image.save (basedir + "/contrafactuals/%06d" % i + ".png")

if (__name__ == '__main__'):

    print('Welcome to the Kandinsky Figure Generator') 

    randomkf =  RandomKandinskyFigure.Random (u,4,4)
    generateImagesAndCaptions ("../test/randomkf", randomkf, 50)

    redobjects = SimpleObjectAndShape.ContainsRedObjects(u,4,4)
    generateClasses ("../test/onered", redobjects, 50)

    triangleobjects = SimpleObjectAndShape.ContainsTriangles(u,4,4)
    generateClasses ("../test/onetriangle", triangleobjects, 50)

    shapeOnshapeObjects = ShapeOnShapes.ShapeOnShape (u, 20, 40)
    generateClasses ("../test/shapeonshapes", shapeOnshapeObjects, 50, contrafactuals = True)
