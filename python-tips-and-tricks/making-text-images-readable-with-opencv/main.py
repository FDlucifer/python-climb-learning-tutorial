import cv2 as cv

img = cv.imread('bookpage.jpg')
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

_, result = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
adaptive = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 21, 4)

cv.imshow('Image', img)
cv.imshow('Result', result)
cv.imshow('adaptive result', adaptive)

cv.waitKey(0)
cv.destroyAllWindows()