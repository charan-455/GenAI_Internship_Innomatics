base_prompt = '''
                I face challenges in perceiving and engaging with my environment due to a visual impairment.
                I find it difficult to comprehend my surroundings, read visual materials, 
                and carry out tasks that necessitate sight. I would appreciate your assistance.
            '''

format_prompt = '''
                I would like the response to be straightforward, easy to understand, and comprehensive, 
                with all essential information categorized under headings and subheadings.

                Please refrain from reiterating the task or prompt itself.
            '''

personalize_prompt = f''' 
                
                {base_prompt}
               
                Tailored Assistance for Daily Activities

                Kindly provide step-by-step instructions based on the uploaded image, 
                including:

                1. Identifying objects  
                2. Analyzing labels or text  
                3. Providing context-specific information  
                4. Spotting items within the image  
                5. Assisting with navigation or movement

                {format_prompt} '''

object_detect_prompt = f''' 
            
                {base_prompt}

                Please evaluate this image to assist with safety and navigation.

                Offer a thorough analysis of the following:

                1. Identify possible obstacles or risks in the image  
                2. Provide advice on safe movement  
                3. Calculate distances and spatial connections between objects  
                4. Issue necessary safety alerts  
                5. Suggest strategies for safely navigating the area

                Structure the information into clear sections and utilize bullet points if necessary.

                {format_prompt} '''

real_time_scene_prompt = f''' 
                
                {base_prompt}
                
                Comprehending the Scene in Real-Time

                Please describe:

                1. The overall environment, mood, and weather conditions  
                2. Main objects and their placements  
                3. Individuals present and their activities  
                4. The scene's color palette and lighting  
                5. Any notable or important features

                Present the information in simple, easy-to-read sections.
                
                {format_prompt} '''

text_speech_prompt = f''' 
                
                {base_prompt}

                Transforming Text from Images into Speech

                Utilize OCR technology to extract text from the uploaded image and 
                convert it into spoken words for easier access to the content.

                Please ensure the following:

                1. Fix any visible OCR mistakes  
                2. Structure the text into well-defined sections  
                3. Emphasize key information  
                4. Provide necessary background information  
                5. Arrange numbers, dates, and essential details in a logical order  

                Present the text in a clear, well-structured manner.
                
                {format_prompt} '''

modify_response = '''
                Kindly modify the response in accordance with the provided instructions.
                '''