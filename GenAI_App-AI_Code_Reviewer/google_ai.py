import google.generativeai as genai

# Configure the API key
f = open("api_key.txt")
key = f.read()

genai.configure(api_key=key)

def review_code(code,code_language):
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    prompt = f""" I want check the given code is  {code} of {code_language} language  or not 
                If not please reply user the code provided and and selected programing language does not match polite manner
                If both matches check for typos, syntax,logical errors and suggest fixes also:\n """
    
    response = model.generate_content(prompt)
    
    return response.text
