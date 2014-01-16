### FOR THIS SCRIPT TO WORK YOU NEED THE ORIGINAL CODE \
### SAVED AS shapefile.py AND THE FORKED VERSION AS shapefile_mod.py

# compares shape reading speed of original vs modded shapefile module
print "initializing pyshp speed test comparison"
import sys, os, time
import shapefile, shapefile_mod

# tester input
testshapepath = r"D:\My Files\GIS Data\General\Global Subadmins\gadm2.shp"
testnumpy = True

# run test comparisons
print "testing speed of the modified version"
if testnumpy:
    print "(the new numpy feature is enabled for faster shapereading)"
t = time.clock()
shapereader = shapefile_mod.Reader(testshapepath)
for eachshape in shapereader.iterShapes(numpyspeed=testnumpy):
    pass
print time.clock()-t, " seconds"

print "testing speed of the original version"
t = time.clock()
shapereader = shapefile.Reader(testshapepath)
for eachshape in shapereader.iterShapes():
    pass
print time.clock()-t, " seconds"

print "test comparison finished"
