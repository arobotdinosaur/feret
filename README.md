FeretGPT is the script that works with dashed images, just change the image path as needed. It unfortunately adds a fair bit of inaccuracy as part of the filling-in process. FeretCalc should work for non-dashed lines with much higer accuracy.

Simple script to give you the maximum and minimum possible feret distances for an object. Most of the complexity just comes from the fact that it fills in dashed lines in 
source images, otherwise it is pretty much just using the wonderful feret library as-is.
