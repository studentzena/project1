import cv2

inputPath = 'static/dog.jpg'

originalImage = cv2.imread(inputPath)

# ------------Convert image to Grayscale --------------
grayscaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)


outputPath = 'converted/grayScale.png'
cv2.imwrite(outputPath, grayscaleImage)

cv2.imshow('Grayscale Image', grayscaleImage)
cv2.waitKey(0)


print('Converted Grayscale image saved to disk : ' + outputPath)
 # ----------------- Convert image to Sketch Image ---------------

# Invert the grayscale image

invertimg = 255-grayscaleImage

# Apply Gaussian blur
blur = cv2.GaussianBlur(invertimg, (21, 21), 0)

# Blend the grayscale image and the blurred image using the color dodge blend mode
sketchimg = cv2.divide(grayscaleImage, 255-blur, scale=256)


# Save the sketch image to disk

outputPath = 'converted/sketch.png'

# Display the converted image
cv2.imwrite(outputPath, sketchimg)
cv2.waitKey(0)

# Display a message indicating that the image has been saved
cv2.imshow('sketch', sketchimg)
cv2.waitKey(0)
print('Converted sketchimg and saved to disk'+ outputPath)
