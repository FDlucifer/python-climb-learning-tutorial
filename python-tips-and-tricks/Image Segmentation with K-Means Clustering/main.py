# pip install scikit-learn matplotlib opencv-python

import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

image = mpl.image.imread("test.png")
plt.imshow(image)
plt.show()
print(image.shape)

X = image.reshape(-1, 3)
kmeans = KMeans(n_clusters=5, n_init=10)
kmeans.fit(X)
segmented_img = kmeans.cluster_centers_[kmeans.labels_]
segmented_img = segmented_img.reshape(image.shape)
plt.imshow(segmented_img / 255)
plt.show()

import cv2

cv2.imwrite("test1.png", cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
cv2.imwrite("test2.png", cv2.cvtColor(segmented_img.astype("uint8"), cv2.COLOR_BGR2RGB))
