# pip install numpy matplotlib pillow tensorflow streamlit

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import tensorflow as tf

from PIL import Image


def main():
    st.title("cifar10 web classifier")
    st.write("upload any image that you think fits")

    file = st.file_uploader("please upload an image", type=["jpg", "png"])
    if file:
        image = Image.open(file)
        st.image(image, use_column_width=True)

        resized_image = image.resize((32, 32))
        img_array = np.array(resized_image) / 255
        img_array = img_array.reshape((1, 32, 32, 3))

        model = tf.keras.models.load_model("cifer10_model.h5")

        prediction = model.predict(img_array)
        cifer10_classes = [
            "airplane",
            "automobile",
            "bird",
            "cat",
            "deer",
            "frog",
            "horse",
            "ship",
            "truck",
        ]

        fig, ax = plt.subplots()
        y_pos = np.arange(len(cifer10_classes))
        ax.barh(y_pos, prediction[0], align="center")
        ax.set_yticks(y_pos)
        ax.set_yticklabels(cifer10_classes)
        ax.invert_yaxis()
        ax.set_xlabel("probability")
        ax.set_title("cifar10 predictions")

        st.pyplot(fig)
    else:
        st.text("you have not uploaded an image yet.")

if __name__ == '__main__':
    main()
