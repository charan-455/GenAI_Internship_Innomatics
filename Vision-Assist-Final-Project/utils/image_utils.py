import streamlit as st
from PIL import Image
import requests
import os 
from pathlib import Path
from imageai.Detection import ObjectDetection

# convert the image to tensor
def get_image_data(image_path):
    
    image_data = Image.open(image_path)

    return image_data

# Download the uploaded or url image
def download_image(path=None,image=None):
    
    if path is not None and image is not None:
    
        extension = Path(path).suffix
        save_path = os.path.join("outputs",f"input{extension}")
        image.save(save_path)

        print("Image downloaded")

# Function to handle image upload
def upload_image():
    st.subheader("Upload an image 🖼️")
    uploaded_file = st.file_uploader(" ", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Loaded Image")
        st.session_state.image_data = image  # Store image in session state

        download_image(uploaded_file.name,image)

        return image
    
    return None

# Function to handle image from URL
def get_image_from_url():
    st.subheader("Enter the image URL 🔗")
    with st.form(key='image_form'):
        url = st.text_area(" ", placeholder="🔗 Paste the URL of the image here...")
        submit_button = st.form_submit_button("Submit")
    
    if submit_button and url:
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                
                try: 
                    image = Image.open(response.raw)

                    # Ensure image is in a consistent format (RGBA)
                    if image.mode == 'RGBA':
                        image = image.convert('RGB')

                    st.image(image, caption="Converted PNG Image")
                    st.session_state.image_data = image  # Store image in session state
                    
                    download_image(url,image)

                    return image
                
                except Exception as e:
                    st.error(f"Error processing image: {e}")

            else:
                st.error(f"Error loading image from URL (Status code: {response.status_code}).")
        except requests.exceptions.RequestException as e:
            st.error(f"Error loading image from URL: {e}")
    
    return None

# Main function to manage the image selection process
def get_image(image_source):
    image = None

    if image_source == f":red-background[Upload Image ⬆️]":
        image = upload_image()
    elif image_source == f":green-background[Open from URL 🔗]":
        image = get_image_from_url()

    if image is not None:
        return image, image_source
    return None, image_source  # Return None explicitly if no valid image is found

# Function that highlights the objects
def highlight_image(input_image_path = r"images\image3.jpg",
                    output_imag_path = r"outputs\output_image.jpg"):


    execution_path = os.getcwd()
    model_path = os.path.join(execution_path, r"models\yolov3.pt")  # Ensure you have the YOLO model file in your working directory
    input_image_fullpath = os.path.join(execution_path, input_image_path)  # Path to your input image
    output_image_fullpath = os.path.join(execution_path, output_imag_path )  # Path to save the output image

    # Initialize the object detection model
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(model_path)
    detector.loadModel()

    # Perform object detection
    detector.detectObjectsFromImage(input_image=input_image_fullpath, 
                                    output_image_path=output_image_fullpath,
                                    extract_detected_objects=False,
                                    display_percentage_probability=False)

    return output_image_fullpath