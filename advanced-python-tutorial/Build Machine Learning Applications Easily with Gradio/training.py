import tensorflow as tf
from keras import layers, models

(train_images, train_labels), (
    test_images,
    test_labels,
) = tf.keras.datasets.mnist.load_data()

train_images = train_images.reshape((60000, 28, 28, 1)).astype("float32") / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype("float32") / 255


train_labels = tf.keras.utils.to_categorical(train_labels)
test_labels = tf.keras.utils.to_categorical(test_labels)

models = models.Sequential()
models.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)))
models.add(layers.MaxPooling2D(2, 2))
models.add(layers.Conv2D(64, (3, 3), activation="relu"))
models.add(layers.MaxPooling2D(2, 2))
models.add(layers.Conv2D(64, (3, 3), activation="relu"))
models.add(layers.Flatten())
models.add(layers.Dense(64, activation="relu"))
models.add(layers.Dense(10, activation="softmax"))

models.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
models.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.1)

models.save("model.h5")
