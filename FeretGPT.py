import cv2
import numpy as np
import feret
import tifffile as tif

# Load image
image = cv2.imread("TOP.jpg")

# Convert to HSV to detect red
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Red has two hue ranges (0–10 and 160–180)
lower_red1 = np.array([0, 70, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 70, 50])
upper_red2 = np.array([180, 255, 255])

# Create masks for red
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)

# Close the dashed gaps using dilation followed by closing
kernel = np.ones((15, 15), np.uint8)
closed = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)
filled = cv2.dilate(closed, kernel, iterations=2)

# Fill the contour (largest connected component)
contours, _ = cv2.findContours(filled, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
mask_filled = np.zeros_like(filled)
cv2.drawContours(mask_filled, contours, -1, color=255, thickness=cv2.FILLED)

# Save the binary mask as a TIFF
tif.imwrite("binary_image.tiff", mask_filled)

# Read and analyze
image = tif.imread("binary_image.tiff")
maxf, minf, minf90, maxf90 = feret.all(image)
print("Max Feret:", maxf)
print("Min Feret:", minf)

feret.plot(image)

