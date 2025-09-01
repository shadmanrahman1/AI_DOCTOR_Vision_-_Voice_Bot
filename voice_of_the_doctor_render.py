# step 1 : setup text to speech - TTS - model for transcription (Render deployment)
from gtts import gTTS


def text_to_speech_old(text, output_file):
    language = "en"

    audio_obj = gTTS(text=text, lang=language, slow=False)
    audio_obj.save(output_file)


# step 2 : use model for text output to voice (cloud deployment version)
def text_to_speech(text, output_file):
    """
    Generate speech from text and save to file.
    Returns the output file path for Gradio audio component.
    """
    language = "en"

    try:
        audio_obj = gTTS(text=text, lang=language, slow=False)
        audio_obj.save(output_file)

        # Return the file path for Gradio to play
        return output_file

    except Exception as e:
        print(f"Error occurred while generating audio: {e}")
        return None
