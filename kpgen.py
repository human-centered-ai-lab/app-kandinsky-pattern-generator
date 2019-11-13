import os

from PIL import Image
from kp import KandinskyUniverse, RandomKandinskyFigure, SimpleObjectAndShape, ShapeOnShapes, NumbersKandinskyFigure,  KandinskyCaptions
import cv2

u  = KandinskyUniverse.SimpleUniverse()
cg = KandinskyCaptions.CaptionGenerator (u)


def generateImagesAndCaptions(basedir, kfgen, n=50, width=200):

    os.makedirs(basedir, exist_ok=True)
    capt_color_shape_size_file = open(basedir + "/color_shape_size.cap", "w")
    capt_numbers  = open(basedir + "/numbers.cap", "w")
    for (i, kf) in enumerate(kfgen.true_kf (n)):
        image = KandinskyUniverse.kandinskyFigureAsImage (kf, width)
        image.save (basedir + "/%06d" % i + ".png")       
        capt_color_shape_size_file.write(str(i) + '\t' +  cg.colorShapesSize (kf, 'one ')+'\n' )
        capt_numbers.write( str(i) + '\t' +  cg.numbers (kf)+  '\n' )
    capt_color_shape_size_file.close()
    capt_numbers.close()

def generateSimpleNumbersCaptions (basedir, kfgen, n=50, width=200):
    os.makedirs(basedir, exist_ok=True)
    capt_numbers_file = open(basedir + "/numbers.cap", "w")
    for (i, kf) in enumerate(kfgen.true_kf (n)):
        image = KandinskyUniverse.kandinskyFigureAsImage (kf, width)
        image.save (basedir + "/%06d" % i + ".png")       
        # imagePIL = KandinskyUniverse.kandinskyFigureAsImagePIL (kf, width)
        # image.save (basedir + "/%06d" % i + "_PIL.png")       
        capt_numbers_file.write(str(i) + '\t' +  cg.simpleNumbers (kf)+'\n' )
    capt_numbers_file.close()
    
def generateClasses (basedir, kfgen, n=50,  width=200, counterfactual = False):
    os.makedirs(basedir + "/true", exist_ok=True)
    os.makedirs(basedir + "/false", exist_ok=True)
    for (i, kf) in enumerate(kfgen.true_kf (n)):
        image = KandinskyUniverse.kandinskyFigureAsImage (kf, width)
        image.save (basedir + "/true/%06d" % i + ".png")  

    for (i, kf) in  enumerate(kfgen.false_kf (n)):
        image = KandinskyUniverse.kandinskyFigureAsImage (kf, width)
        image.save (basedir + "/false/%06d" % i + ".png")
    if (counterfactual):
        os.makedirs(basedir + "/counterfactual", exist_ok=True)
        for (i, kf) in enumerate(kfgen.almost_true_kf (n)):
            image = KandinskyUniverse.kandinskyFigureAsImage (kf, width)
            image.save (basedir + "/counterfactual/%06d" % i + ".png")



if (__name__ == '__main__'):

    print('Welcome to the Kandinsky Figure Generator') 

    # fixednumberskf = NumbersKandinskyFigure.FixedNumber (u,5,5)
    # generateClasses ("../test/number_5", fixednumberskf, 10, counterfactual = True, width=600)

    # fixednumberskf = NumbersKandinskyFigure.FixedNumber (u,3,3)
    # generateClasses ("../test/number_3", fixednumberskf, 10, counterfactual = True, width=600)

    # randomkf =  RandomKandinskyFigure.Random (u,1,10)
    # generateSimpleNumbersCaptions ("../test/randomnumbers", randomkf, 10, width=600)

    # redobjects = SimpleObjectAndShape.ContainsRedObjects(u,4,4)
    # generateClasses ("../test/onered", redobjects, 50, width=600,)

    # triangleobjects = SimpleObjectAndShape.ContainsTriangles(u,4,4)
    # generateClasses ("../test/onetriangle", triangleobjects, 50, width=600,)

    # shapeOnshapeObjects = ShapeOnShapes.ShapeOnShape (u, 20, 40)
    # generateClasses ("../test/shapeonshapes", shapeOnshapeObjects, n=1000, width=600, counterfactual = True)

    twoPairsOnlyOneWithSameColor = SimpleObjectAndShape.twoPairsOnlyOneWithSameColor (u, 4, 4)
    generateClasses ("../test/twopairs", twoPairsOnlyOneWithSameColor, n=1000, width=600, counterfactual = False)
