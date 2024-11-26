import pyttsx3    

def gen_voice(prompt = "Hello, this is a test for sync synthesis function"):

    try:
        # Initialize TTS engine

        audio_path = r"outputs\temp.wav"
        engine = pyttsx3.init()
        
        # Speak the text
        engine.save_to_file(prompt,audio_path)
        engine.runAndWait()
        
        engine.stop()  # Stop the engine after use

        return audio_path
        
    except Exception as e:
        raise RuntimeError(f"Failed to convert text to speech. Error: {e}")


if __name__ == "__main__":
    gen_voice()