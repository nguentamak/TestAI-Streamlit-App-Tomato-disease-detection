import streamlit as st
from PIL import Image

st.title("📷 Capture d'image avec la caméra")

# Widget de capture d'image
image_file = st.camera_input("Prenez une photo")

if image_file:
    # Convertir l'image en format PIL
    image = Image.open(image_file)

    # Afficher l'image capturée
    st.image(image, caption="Image capturée", use_column_width=True)
