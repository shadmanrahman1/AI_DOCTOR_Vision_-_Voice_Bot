from brain_of_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient_render import record_audio_and_transcribe
from voice_of_the_doctor_render import text_to_speech

import gradio as gr
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please
"""


def process_inputs(audio_filepath, image_filepath):
    try:
        if not audio_filepath:
            return "No audio recorded", "Please record your voice first", None

        speech_to_text_output = record_audio_and_transcribe(
            GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
            audio_file_path=audio_filepath,
            stt_model="whisper-large-v3-turbo",
        )

        if image_filepath:
            doctor_analysis = analyze_image_with_query(
                query=system_prompt + speech_to_text_output,
                encoded_image=encode_image(image_filepath),
                model="meta-llama/llama-4-scout-17b-16e-instruct",
            )
        else:
            doctor_analysis = (
                "No image provided for analysis. Based on your description: "
                + speech_to_text_output
            )

        voice_of_doctor = text_to_speech(text=doctor_analysis, output_file="Temp.mp3")
        return (
            speech_to_text_output,
            doctor_analysis,
            voice_of_doctor,
        )
    except Exception as e:
        error_msg = f"Error processing request: {str(e)}"
        return error_msg, error_msg, None


# Gradio interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(
            sources=["microphone"],
            type="filepath",
            label="🎤 Record Your Medical Concern",
        ),
        gr.Image(type="filepath", label="📷 Upload Medical Image (Optional)"),
    ],
    outputs=[
        gr.Textbox(
            label="🗣️ Speech to Text Output",
            placeholder="Your spoken input will appear here...",
        ),
        gr.Textbox(
            label="🏥 Doctor's Analysis",
            placeholder="AI medical analysis will appear here...",
        ),
        gr.Audio(label="🔊 Voice Response"),
    ],
    title="🏥 AI Doctor - Vision & Voice Bot",
    description="Upload an image and record your voice to get AI-powered medical insights. **For educational purposes only.**",
    theme=gr.themes.Soft(),
    css="""
    .gradio-container {
        max-width: 900px;
        margin: auto;
    }
    .title {
        text-align: center;
        color: #2c5aa0;
    }
    """,
)

if __name__ == "__main__":
    print("🏥 Starting AI Doctor - Vision & Voice Bot...")
    print("📝 This is for educational purposes only!")
    print("🌐 Open your browser and go to the URL shown below")

    # Get port from environment for Render deployment
    port = int(os.environ.get("PORT", 7860))

    iface.launch(
        server_name="0.0.0.0",  # Required for Render
        server_port=port,  # Use PORT environment variable
        debug=True,
        show_error=True,
    )
