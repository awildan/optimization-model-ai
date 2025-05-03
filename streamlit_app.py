import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

# Load model
model = tf.keras.models.load_model("car_bike_model_best.h5")

# Judul app
st.title("Klasifikasi Gambar: Mobil vs Motor")

# Upload gambar
uploaded_file = st.file_uploader("Upload gambar", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # image = Image.open(uploaded_file).resize((64, 64))
    image = Image.open(uploaded_file).convert("RGB").resize((64, 64))
    st.image(image, caption="Gambar yang diupload", use_container_width=True)

    img_array = np.expand_dims(np.array(image) / 255.0, axis=0)

    prediction = model.predict(img_array)
    st.markdown(prediction)
    label = "Mobil 🚗" if prediction[0][0] > 0.5 else "Motor 🏍️"
    confidence = (1 - prediction[0][0]) if prediction[0][0] < 0.5 else prediction[0][0]

    st.markdown(f"### Prediksi: **{label}** ({confidence*100:.2f}%)")
