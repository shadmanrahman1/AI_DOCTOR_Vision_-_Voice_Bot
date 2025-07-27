# step 1 : audio recorder (ffmeg & portaudiio)
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def record_audio_simple(file_path, timeout=20, phrase_time_limit=None):
    """
    Simplified audio recording function to record audio from the microphone and save it as MP3 file.

    Args:
        file_path (_type_): Path to save the recorded audio file.
        timeout (int, optional): Maximum time to wait for the user to speak.
        phrase_time_limit (_type_, optional): Maximum time for the phrase to be recorded.
    """

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking...")

            # Record audio from the microphone
            audio_data = recognizer.listen(
                source, timeout=timeout, phrase_time_limit=phrase_time_limit
            )
            logging.info("Recording complete.")

            # Convert audio to MP3 format
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3")

            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred while recording audio: {e}")
        raise


audio_file_path = "voice_of_the_patient.mp3"
# Record audio and save it to the specified file path
# record_audio_simple(file_path=audio_file_path)  # Commented out to prevent auto-recording

# step 2 : setup speech to text - STT - model for transcription
GROQQ_API_KEY = os.getenv("GROQ_API_KEY")

stt_model = "whisper-large-v3-turbo"


def record_audio_and_transcribe(stt_model, audio_file_path, GROQ_API_KEY):
    """
    Transcribe an existing audio file using the specified STT model.

    Args:
        stt_model (str): The STT model to use for transcription.
        audio_file_path (str): Path to the audio file to transcribe.
        GROQ_API_KEY (str): API key for Groq.

    Returns:
        str: Transcription of the audio file.
    """

    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY environment variable is not set.")

    client = Groq(api_key=GROQ_API_KEY)

    with open(audio_file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=stt_model,
            file=audio_file,
            language="en",
            response_format="text",
        )

    return transcription
