import streamlit as st 
from utils.definitions import *
from PIL import Image
import os
import glob

def clear_files(path):
    if os.path.exists(path):
        files = glob.glob(f"{path}\*")
        for f in files:
            os.remove(f)
            print(f"{f} deleted")
    else:
        os.makedirs(path,exist_ok=True)

def static_display():

    st.markdown(style,unsafe_allow_html=True)

    # Title
    st.title(title)

    st.subheader(sub_head)
    # Model Description
    st.markdown(f"<div class='description'> {model_description} </div>", unsafe_allow_html=True)


    st.sidebar.image(r"background_image.webp",width=400)

    # Solutions
    st.sidebar.subheader("**Solutions Provided** 💡")

    for key,emoji,color in zip(solutions.keys(),emojis,colors):
        st.sidebar.markdown(f"✅ :{color}[{solutions[key]} {emoji}]")

    image_source = None
    # Choose image source
    image_source = st.radio("Select Image Source:",(f":red-background[Upload Image ⬆️]",f":green-background[Open from URL 🔗]"),index=None)

    return image_source

def menu_display():
    st.subheader("Select a Solution")

    # Dropdown menu to select one solution 
    selected_option = st.selectbox(" ",  
                                   index = None,
                                   options = solutions.keys(),
                                   placeholder = "Choose a solution")
    
    if selected_option is not None:
        # Extract the selected key from the selected option string
        selected_key = [key for key, value in solutions.items() if key == selected_option][0]

        return selected_key

    return None  # Return None if no option is selected

def post_display(result):

    audio_path = result.get('audio_path',None)
    highlighted = result.get('highlighted_image_data',None)

    if highlighted is not None:

        st.image(highlighted, caption="Loaded Image")
        st.session_state.image_data = highlighted

    if audio_path is not None:

        audio_file = open(audio_path, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/wav')
        st.session_state.audio_data = audio_bytes

    st.write(result['response'])
