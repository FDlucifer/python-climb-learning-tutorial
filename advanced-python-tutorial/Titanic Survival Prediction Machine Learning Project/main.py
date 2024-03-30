# pip install numpy pandas matplotlib scikit-learn seaborn

from cv2 import split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic_data = pd.read_csv('data/train.csv')

# print(titanic_data.describe())
import seaborn as sns

sns.heatmap(titanic_data.corr(), cmap="YlGnBu")
plt.show()



