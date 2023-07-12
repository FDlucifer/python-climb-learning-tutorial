# pip install numpy matplotlib pillow tensorflow streamlit

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

from PIL import Image

import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.utils import to_categorical

(X_train, Y_train), (X_val, Y_val) = cifar10.load_data()
X_train = X_train / 255
X_val = X_val / 255

X_train = to_categorical(Y_train, 10)
Y_val = to_categorical(Y_val, 10)

model = Sequential(
    [
        Flatten(input_shape=(32, 32, 3)),
        Dense(1000, activation="relu"),
        Dense(10, activation="softmax"),
    ]
)

model.compile(loss="categorical_crossentropy", optimizer="adam", metric=["accuracy"])
model.fit(X_train, Y_train, batch_size=64, epoch=10, validation_data=(X_val, Y_val))
model.save("cifar10_model.h5")
