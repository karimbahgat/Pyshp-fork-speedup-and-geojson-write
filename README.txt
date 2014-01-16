Temporary fork of J. Lawhead's original Pyshp shapefile read/write module (http://code.google.com/p/pyshp/). The hope is to eventually roll these changes into the original pyshp library repository. 

Use this modified/forked version by downloading the "shapefile.py" file and placing it in your "PythonXX/Lib/site-packages" folder. Rename it to something different if you don't want to overwrite the original "shapefile.py" file. 

Main changes are: 

1) General speedup for reading shapefile geometries (x1.5 faster).

2) Potentially drastic reading speedup if user has Numpy (x5.5 faster). Simply set the new "numpyspeed" option to True when using the "iterShapes" or "shape" methods of the Reader class.

3) Write shapes based on geojson input which makes it possible to RECEIVE shapes/results from modules like Shapely (previously it was only possible to SEND shapes to other modules). Simply use the new writer.write_geoj(geojdict) method. 

4) Added an iterShapeRecords method to iterate through both shapes and records at the same time (similar to a request and suggestion by another user, see issue 58 under the "Issues" tab of the original code website).

For more thorough details on the changes made in this fork see the "listof_fork_changes.txt" file.