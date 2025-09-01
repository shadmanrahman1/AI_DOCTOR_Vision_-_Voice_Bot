# step 1 : audio recorder (for Render deployment - no PyAudio dependency)
import logging
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
    Simplified audio recording function - DISABLED for cloud deployment.
    This function is not used in Gradio deployment as audio is uploaded directly.
    """
    raise NotImplementedError(
        "Audio recording from microphone is not supported in cloud deployment. Use Gradio's audio upload instead."
    )


# step 2 : setup speech to text - STT - model for transcription
GROQQ_API_KEY = os.getenv("GROQ_API_KEY")

stt_model = "whisper-large-v3-turbo"


def record_audio_and_transcribe(stt_model, audio_file_path, GROQ_API_KEY):
    """
    Transcribe an existing audio file using the specified STT model.
    This works with uploaded audio files in Gradio.

    Args:
        stt_model (str): The STT model to use for transcription.
        audio_file_path (str): Path to the audio file to transcribe.
        GROQ_API_KEY (str): API key for Groq.

    Returns:
        str: Transcription of the audio file.
    """

    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY environment variable is not set.")

    if not os.path.exists(audio_file_path):
        raise FileNotFoundError(f"Audio file not found: {audio_file_path}")

    client = Groq(api_key=GROQ_API_KEY)

    try:
        with open(audio_file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model=stt_model,
                file=audio_file,
                language="en",
                response_format="text",
            )
        return transcription
    except Exception as e:
        logging.error(f"Error during transcription: {e}")
        raise
