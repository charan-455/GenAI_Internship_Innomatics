from task.get_response import surround_assistance,navigation,real_time,text2speech
from task.get_prompts import object_detect_prompt,real_time_scene_prompt,text_speech_prompt,personalize_prompt
from utils.image_utils import highlight_image

import streamlit as st

def task_to_api(task,image_data):

    match task:
        case "real_time_scene":
            with st.spinner("Generating real time scene description...."):
                return real_time(imag_data=image_data,
                                 real_time_scene_prompt=real_time_scene_prompt)
            
        case "text_to_speech":
            with st.spinner("Generating speech ...."):
                return text2speech(imag_data=image_data,
                                   text_speech_prompt=text_speech_prompt)
            
        case "object_detection":
            with st.spinner("Identifying objects ...."):
                
                highlighted_image_path = highlight_image(r"outputs\input.jpg")
                
                return surround_assistance(imag_data=image_data,
                                           object_detect_prompt=object_detect_prompt,
                                           highlight_path=highlighted_image_path)
            
        case "personal_assistance":
            with st.spinner("Generating Assistance response ...."):
                return navigation(imag_data=image_data,
                                  personalize_prompt=personalize_prompt)
        case _:
            return {'response':"Invalid solution key"}