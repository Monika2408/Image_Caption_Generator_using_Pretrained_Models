import os
import pickle
import streamlit as st
from module import main

# Define a function to validate the uploaded file
def validate_file(file):
    if file is None:
        st.warning("Please upload an image.")
        return False
    elif not file.type.startswith("image"):
        st.warning("Please upload an image file.")
        return False
    else:
        return True

# Create a Streamlit file uploader widget
file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# If a file has been uploaded, validate it and pass the file name to the main function


    
if validate_file(file):
    file_name = file.name
    image = file.read()
    captions = main(file_name)  # Assign output of main function to variable
    st.image(image, use_column_width=True)
    for caption in captions:
        st.write(caption)
    
    

