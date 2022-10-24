#useful librairies
import streamlit as st
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras_preprocessing.image import load_img, img_to_array
import numpy as np

st.markdown("<h1 style='text-align: center; color: black;'>👩‍⚕️ Pneumonia Detection using Chest X-Ray 👨‍⚕️</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: grey;'>Data Camp Project - Master 1</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    model = load_model('model/model_test.h5')
    #test image Normal
    #img = load_img('C:\\Users\\annej\\Documents\\S7\\Data camp\\chest_xray\\chest_xray\\val\\NORMAL\\NORMAL2-IM-1427-0001.jpeg',target_size=(224,224))
    #test image Pneumonia
    img = load_img('C:\\Users\\annej\\Documents\\S7\\Data camp\\chest_xray\\chest_xray\\val\\PNEUMONIA\\person1946_bacteria_4874.jpeg',target_size=(224,224))
    but = st.button('Click here to see the chest X-ray ! 🔍')
    if but:
        st.image(img)
    else:
        st.write('Let us see the result...')

    image_loaded = img_to_array(img)
    image_loaded = np.expand_dims(image_loaded, axis=0)
    img_data = preprocess_input(image_loaded)
    test = model.predict(img_data)
    but2 = st.button('Click here to see the result...✅')
    if but2:
        st.image(img)
        result=int(test[0][0])
        if result == 0:
            st.subheader("Result is Pneumonia")
        else:
            st.subheader("Result is Normal")
            st.balloons()

with col3:
    st.write(' ')

st.markdown("<h2 style='text-align: center; color: black;'>The Doctors Team 👩‍⚕️👨‍⚕️</h2>", unsafe_allow_html=True)
col4, col5, col6 = st.columns(3)
with col4:
    anneju = 'AnneJu.jpg'
    st.image(anneju)
    st.write('Anne-Julie HOTTIN')
with col5:
    arthur = 'Arthur.jpg'
    st.image(arthur)
    st.write('Arthur GODINHO')
with col6:
    faty = 'Faty.png'
    st.image(faty)
    st.write('Fatima-Zahra IBRAHIMI')


"""
model=load_model('model/model_test.h5')
img = st.file_uploader(label="Choose a file",type=['png','jpg','jpeg'])
st.image(img)
x=img_to_array(img)
x=np.expand_dims(x, axis=0)
img_data=preprocess_input(x)
classes=model.predict(img_data)
result=int(classes[0][0])
if result==0:
    st.write("Result is Pneumonia")
else:
    st.write("Result is Normal")
"""

st.markdown("<h2 style='text-align: center; color: grey;'>© Fatima-Zahra IBRAHIMI / Arthur GODINHO / Anne-Julie HOTTIN</h2>", unsafe_allow_html=True)
