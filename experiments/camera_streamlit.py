# Webcam with streamlit

from PIL import Image
import streamlit as st

# Zeigt eine Kamerakomponente an, die es dem Benutzer ermöglicht, ein Bild aufzunehmen
with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

# Überprüft, ob ein Bild aufgenommen wurde, bevor fortgefahren wird
if camera_image is not None:
    # Erstellt eine PIL-Image-Instanz aus dem aufgenommenen Bild
    img = Image.open(camera_image)

    # Konvertiert das Bild in Graustufen
    gray_img = img.convert("L")

    # Zeigt das Graustufenbild in der Streamlit-App an
    st.image(gray_img)

# ____________________________
# Upload field for pdf´s

with st.expander("Upload files"):
    upload_image = st.file_uploader("Upload Image")

if upload_image is not None:
    upload = Image.open(upload_image)
    gray_upload = upload.convert("L")
    st.image(gray_upload)