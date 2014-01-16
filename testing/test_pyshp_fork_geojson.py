### FOR THIS SCRIPT TO WORK YOU NEED THE ORIGINAL CODE \
### SAVED AS shapefile.py AND THE FORKED VERSION AS shapefile_mod.py

# demonstrates the new geojson importing feature
print "initializing pyshp test comparison"
#basics
import sys, os, time, itertools
#for shapefile loading
import shapefile, shapefile_mod
#for shape manipulation
import shapely.ops as shapelyops
#for shape conversion
from shapely.geometry import shape as geojsontoshapely
from shapely.geometry import mapping as shapelytogeojson

# tester input
testshapepath = r"D:\My Files\GIS Data\General\Global Subadmins\gadm2.shp"
testhowmanyshapes = 50
testnumpy = False
testresults_savepath = r"C:\Users\BigKimo\Desktop\pyshp_geoj_union_test.shp"

# send shapefile to shapely to be unioned, and import results back into pyshp for saving
print "TEST 1: send shapefile to shapely to be unioned, and import results back into pyshp for saving"
print "loading file"
shapereader = shapefile_mod.Reader(testshapepath)
print "collecting geometries"
allshapes = []
for shape in itertools.islice(shapereader.iterShapes(numpyspeed=testnumpy),testhowmanyshapes):
    # send to shapely
    shape = geojsontoshapely(shape.__geo_interface__)
    allshapes.append(shape)
print "running union on shapes"
testresults = shapelyops.cascaded_union(allshapes)
print "converting result to geojson"
testresults_geoj = shapelytogeojson(testresults)
print "writing and saving result"
shapewriter = shapefile_mod.Writer()
shapewriter.field("field1")
shapewriter.write_geoj(testresults_geoj)
shapewriter.record(["record1"])
shapewriter.save(testresults_savepath)
print "shapefile successfully sent to shapely, unioned, received back, and saved"

# convert to geojson and then back to pyshp again, showing that before and after are the same
print "\nTEST 2: converting shapefile to geojson and then back to pyshp again (without changing it)"
print "(before and after should be the same)"
time.sleep(3)
print "loading file"
shapereader = shapefile_mod.Reader(testshapepath)
t = time.clock()
for shape in itertools.islice(shapereader.iterShapes(numpyspeed=testnumpy),testhowmanyshapes):
    print "----------"
    print "ORIG"
    print "coords",str(shape.points)[:100]
    print "type",shape.shapeType
    print "parts",shape.parts
    print "GEOJ"
    geoj = shape.__geo_interface__
    print "coords",str(geoj["coordinates"])[:100]
    print "type",geoj["type"]
    print "BACKTOORIG"
    converted = shapefile_mod.geojson_to_pyshp(geoj)
    print "coords",str(converted.points)[:100]
    print "type",converted.shapeType
    print "parts",converted.parts

print time.clock()-t, " seconds"
print "test of geojson capabilites finished"
