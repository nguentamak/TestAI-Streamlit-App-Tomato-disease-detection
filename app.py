import streamlit as st
import cv2
import numpy as np

st.title("Détection des maladies de la tomate 🍅")

# Activer/Désactiver la caméra
if "camera_active" not in st.session_state:
    st.session_state.camera_active = False

def toggle_camera():
    st.session_state.camera_active = not st.session_state.camera_active

st.button("📷 Activer/Désactiver la caméra", on_click=toggle_camera)

# Capture vidéo avec OpenCV
if st.session_state.camera_active:
    cap = cv2.VideoCapture(0)  # 0 pour la webcam

    if not cap.isOpened():
        st.error("Impossible d'ouvrir la caméra")
    else:
        stframe = st.empty()  # Espace pour afficher la vidéo

        while st.session_state.camera_active:
            ret, frame = cap.read()
            if not ret:
                st.error("Erreur de capture vidéo")
                break

            # Convertir en RGB pour Streamlit
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            stframe.image(frame, channels="RGB")

        cap.release()
