import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace="D:/Watershed/"

inRaster="D:/Watershed/tamtr14_1m"

arcpy.CheckOutExtension("Spatial")

outCon=Con(IsNull(inRaster), FocalStatistics (inRaster, NbrRectangle (5,5, "CELL"), "MEAN"), inRaster)

outCon.save("D:/Watershed/outCon")