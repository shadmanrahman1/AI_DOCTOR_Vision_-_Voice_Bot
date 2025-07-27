# step 1 : setup text to speech - TTS - model for transcription(gtts & ElevenLabs)
import os
from gtts import gTTS


def text_to_speech_old(text, output_file):
    language = "en"

    audio_obj = gTTS(text=text, lang=language, slow=False)
    audio_obj.save(output_file)


# input_text = "Hello, this is AI voice texting. This is a test of the text to speech functionality."
# text_to_speech_old(input_text, "gtts_auto_output.mp3")

# step 2 : use model for text output to voice

import subprocess
import platform


def text_to_speech(text, output_file):
    language = "en"

    audio_obj = gTTS(text=text, lang=language, slow=False)
    audio_obj.save(output_file)
    os_name = platform.system()
    try:
        if os_name == "Windows":
            subprocess.call(["start", output_file], shell=True)
        elif os_name == "Darwin":
            subprocess.call(["afplay", output_file])
        else:
            subprocess.call(["xdg-open", output_file])
    except Exception as e:
        print(f"Error occurred while playing audio: {e}")


# text_to_speech(input_text, "gtts_output.mp3")
