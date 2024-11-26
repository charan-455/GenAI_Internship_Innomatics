from utils.api_utils import get_genai_response

def text2speech(imag_data=None,text_speech_prompt=None):

    return get_genai_response(imag_data,text_speech_prompt)

def navigation(imag_data=None,personalize_prompt=None):

    return get_genai_response(imag_data,personalize_prompt)

def real_time(imag_data,real_time_scene_prompt):

    return get_genai_response(imag_data,real_time_scene_prompt)

def surround_assistance(imag_data=None,object_detect_prompt=None,highlight_path=None):

    return get_genai_response(imag_data,object_detect_prompt,highlight_path)
