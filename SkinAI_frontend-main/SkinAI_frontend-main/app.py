import streamlit as st
import requests
from PIL import Image
import io
import numpy as np

import re

classes = [
        'Acne and Rosacea Photos',
        'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions',
        'Atopic Dermatitis Photos',
        'Bullous Disease Photos',
        'Cellulitis Impetigo and other Bacterial Infections',
        'Eczema Photos',
        'Exanthems and Drug Eruptions',
        'Hair Loss Photos Alopecia and other Hair Diseases',
        'Herpes HPV and other STDs Photos',
        'Light Diseases and Disorders of Pigmentation',
        'Lupus and other Connective Tissue diseases',
        'Melanoma Skin Cancer Nevi and Moles',
        'Nail Fungus and other Nail Disease',
        'Poison Ivy Photos and other Contact Dermatitis',
        'Psoriasis pictures Lichen Planus and related diseases',
        'Scabies Lyme Disease and other Infestations and Bites',
        'Seborrheic Keratoses and other Benign Tumors',
        'Systemic Disease',
        'Tinea Ringworm Candidiasis and other Fungal Infections',
        'Urticaria Hives',
        'Vascular Tumors',
        'Vasculitis Photos',
        'Warts Molluscum and other Viral Infections'
    ]
    

def get_prediction(image):
    # Define the API endpoint URL
    url = "https://skin-ai-3ly6to7w7a-ew.a.run.app/SkinAI"

    # Prepare the image data
    img_bytes = image
    files = {"img": img_bytes}

    # Send a POST request to the API
    response = requests.post(url, files=files)

    # print(response)
    # print(response.text)


    # # Get the predicted class from the response
    # predicted_class = response.json()["class"]


    return response.text

descriptions_dict ={
        'Acne and Rosacea Photos':' Inflammatory skin conditions that cause pimples, redness, and swelling',
        'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions':'Pre-cancerous and cancerous growths on the skin',
        'Atopic Dermatitis Photos':' A chronic inflammatory skin condition that causes itchy, red, and scaly patches',
        'Bullous Disease Photos':' A group of conditions that cause blisters on the skin or mucous membranes',
        'Cellulitis Impetigo and other Bacterial Infections':' Infections of the skin caused by bacteria',
        'Eczema Photos':'A chronic inflammatory skin condition that causes itchy, red, and scaly patches',
        'Exanthems and Drug Eruptions':'Skin rashes caused by medication, viral infections, or other factors',
        'Hair Loss Photos Alopecia and other Hair Diseases':' Conditions that cause hair loss or hair damage',
        'Herpes HPV and other STDs Photos':'Sexually transmitted infections that can cause skin lesions, blisters, or warts',
        'Light Diseases and Disorders of Pigmentation':'Skin conditions that affect pigmentation, including vitiligo and melasma',
        'Lupus and other Connective Tissue diseases':'Autoimmune disorders that can affect the skin, joints, and other organs',
        'Melanoma Skin Cancer Nevi and Moles':'Cancerous and non-cancerous growths on the skin',
        'Nail Fungus and other Nail Disease':' Infections and other conditions that affect the nails',
        'Poison Ivy Photos and other Contact Dermatitis':'Skin rashes caused by contact with irritants or allergens',
        'Psoriasis pictures Lichen Planus and related diseases':'Chronic inflammatory skin conditions that cause scaly patches or bumps',
        'Scabies Lyme Disease and other Infestations and Bites':'Skin infestations or infections caused by insects or other parasites',
        'Seborrheic Keratoses and other Benign Tumors':'Non-cancerous growths on the skin',
        'Systemic Disease':'Medical conditions that affect multiple organs, including the skin',
        'Tinea Ringworm Candidiasis and other Fungal Infections':'Infections of the skin caused by fungi',
        'Urticaria Hives':'A skin condition that causes itchy, raised welts on the skin',
        'Vascular Tumors':'Benign or cancerous growths that arise from blood vessels or lymphatic vessels',
        'Vasculitis Photos':' Inflammatory conditions that cause damage to blood vessels, leading to skin changes or other symptoms',
        'Warts Molluscum and other Viral Infections':'Skin growths caused by viral infections'
}


# Set up the Streamlit app
st.set_page_config(page_title="Skin Disease Predictor", page_icon=":microscope:", layout="wide")

# Set the background color and font
#st.markdown("""<style>body{background-color: #F5F5F5; font-family: sans-serif;}</style>""", unsafe_allow_html=True)

st.title("Skin Disease Predictor")
st.write("Upload an image of a skin lesion and we'll predict the type of skin disease it might be.")

# Define the app title and header
# st.title("Skin Disease Classification")
# st.header("Upload an image to classify the skin disease")

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Check if an image has been uploaded
if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(io.BytesIO(uploaded_file.read()))
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Get the predicted class
    predicted_class = get_prediction(uploaded_file.getvalue())
    # Remove the word Photos from prediction string
    # predicted_class = re.sub(r'Photos','',predicted_class)
    # Display the predicted class
    st.write("Prediction: ", classes[int(predicted_class)])
    st.write(descriptions_dict[ classes[int(predicted_class)]])
    
