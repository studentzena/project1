# Apply Filters to Your Favourite Picture

In this activity, you will apply filters to your favourite pictures.

Follow the given steps to complete this activity:

1. Apply filters

- Convert the color image to grayscale image.

  `grayscaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)`

2. Convert image to Sketch Image

- Invert the grayscale image.

  `invertedImg = 255 - grayscaleImage`

- Apply Gaussian blur.

  `blurredImg = cv2.GaussianBlur(invertedImg, (21, 21), 0)`

- Blend the grayscale image and the blurred image using the color dodge blend mode.

  `sketchImg = cv2.divide(grayscaleImage, 255 - blurredImg, scale=256)`

- Save the sketch image to disk.

  `outputPath = 'converted/sketch.png'`
  `cv2.imwrite(outputPath, sketchImg)`

- Display the converted image.

  `cv2.imshow('Sketch Image', sketchImg)`

- Save and run the code to check the output.
