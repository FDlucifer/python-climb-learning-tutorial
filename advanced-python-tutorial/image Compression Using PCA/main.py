# pip install sklearn scikit-learn matplotlibb opencv-python numpy

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

img = cv2.cvtColor(cv2.imread("image1.jpg"), cv2.COLOR_BGR2RGB)
img.shape

plt.imshow(img)

r,g,b = cv2.split(img)
r,g,b = r/255, g/255, b/255

plt.imshow(r)
plt.imshow(g)
plt.imshow(b)

pca_components = 50

pca_r = PCA(n_components=pca_components)
reduced_r = pca_r.fit_transform(r)

pca_g = PCA(n_components=pca_components)
reduced_g = pca_g.fit_transform(g)

pca_b = PCA(n_components=pca_components)
reduced_b = pca_b.fit_transform(b)

combined = np.array([reduced_r, reduced_g, reduced_b])

