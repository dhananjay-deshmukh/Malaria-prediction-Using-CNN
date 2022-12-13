# from win32com.client import Dispatch
from keras.models import load_model
import cv2
import os
from PIL import Image, ImageEnhance
import numpy as np
import streamlit as st
import warnings
warnings.filterwarnings('ignore')
import tensorflow




model = tensorflow.keras.models.load_model("malaria_prediction.h5")


def preprocessing(img):
    try:
        img = img.astype('uint8')
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # img = cv2.equalizeHist(img)
        img = img/255
        return img
    except Exception as e:
        img = img.astype('uint8')
        # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # img = cv2.equalizeHist(img)
        img = img/255
        return img


def main():
    st.title("malaria Prediction using CNN")
    st.set_option('deprecation.showfileUploaderEncoding', False)
    nav = st.sidebar.radio("Navigation", ["Home"])



    if nav == "Home":
        st.subheader("Kindly upload file below")
        img_file = st.file_uploader("Upload File", type=['png', 'jpg', 'jpeg'])
        if img_file is not None:
            up_img = Image.open(img_file)
            st.image(up_img)
        if st.button("Predict Now"):
            try:
                img = np.asarray(up_img)
                img = cv2.resize(img, (130,130))
                img = preprocessing(img)
                img = img.reshape(1, 130, 130, 3)
                prediction = model.predict(img)
                if prediction > 0.5:
                    st.write("The cell is not infected!")
                else:
                    st.write("The cell has been parasitized!")
                # classIndex = model.predict_classes(img)
                # st.write(classIndex)
                # st.write(prediction)
               
               
            except Exception as e:
                st.error("Connection Error")

   


if __name__ == '__main__':
    main()