import streamlit as st
import cv2
import numpy as np

# Fonction pour capturer la vidéo en continu
def video_stream():
    cap = cv2.VideoCapture(0)  # 0 pour la webcam par défaut
    frame_window = st.image([])  # Widget pour afficher la vidéo

    stop_button = st.button("❌ Arrêter la caméra", key="stop_camera")  # Clé unique pour éviter l'erreur

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error("Erreur lors de la capture vidéo.")
            break
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir BGR → RGB
        frame_window.image(frame, channels="RGB")

        # Vérifier si l'utilisateur a cliqué sur le bouton pour arrêter
        if stop_button:
            break

    cap.release()
    cv2.destroyAllWindows()

# Interface Streamlit
st.title("📷 Flux Vidéo en Temps Réel avec OpenCV")
st.write("Cliquez sur le bouton ci-dessous pour démarrer le flux vidéo.")

if st.button("▶️ Démarrer la caméra", key="start_camera"):
    video_stream()
