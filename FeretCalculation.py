import cv2
import numpy as np
#from feret import feret_diameter
import feret
import tifffile as tif

# Load color image
image = cv2.imread("TEK.jpg")  # Replace with your image path

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold to binary
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours
#contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#if len(contours) == 0:
#    raise ValueError("No contours found!")

# Assuming only one object, use the largest contour
#main_contour = max(contours, key=cv2.contourArea)
cv2.imshow('debug',binary)
#image=cv2.imencode('binary.jpg',binary)
tif.imwrite("binary_image.tiff", binary)
image=tif.imread('binary_image.tiff') 

maxf, minf, minf90, maxf90 = feret.all(image)

print(maxf)
print(minf)

feret.plot(image)

# Convert contour to 2D numpy array of shape (N, 2)
#points = main_contour[:, 0, :]  # Extract (x, y) points

# Compute Feret diameters
#dmin, dmax = feret_diameter(points)

#print(f"Minimum Feret diameter: {dmin:.2f} pixels")
#print(f"Maximum Feret diameter: {dmax:.2f} pixels")
