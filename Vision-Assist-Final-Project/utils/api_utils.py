#Importing python libraries
import google.generativeai as genai

# Importing custom functions

from utils.audio_utils import gen_voice
from utils.markdown_remover import remove_markdown
from utils.image_utils import get_image_data

# from task.get_prompts import modify_response

def get_key(path=None):
    if path is None:
        f = open(r"path\to\key")
        key = f.read()
    else:
        f = open(path)
        key = f.read()

    return key

def get_genai_response(imag_data=None,prompt=None,highlighted_image_path=None):

    key = get_key()
    genai.configure(api_key=key)

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")


    if highlighted_image_path is not None:

        highlighted_image_data = get_image_data(highlighted_image_path)
        response = model.generate_content([imag_data,highlighted_image_data,prompt])

    else:
        highlighted_image_data = None
        response = model.generate_content([imag_data,prompt])
    
    # response = model.generate_content(f"{modify_response} \n\n {response.text}")
    
    pure_text = remove_markdown(response.text)
        
    audio_path = gen_voice(pure_text)

    return {'response':response.text,'audio_path':audio_path,'highlighted_image_data':highlighted_image_data}





