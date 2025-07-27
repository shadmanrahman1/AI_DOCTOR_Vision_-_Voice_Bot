# 🏥 AI Doctor - Vision & Voice Bot

An intelligent medical assistant that combines voice input, image analysis, and AI-powered medical insights using Groq's LLaMA-4 Scout model.

## 🌟 Features

- **🎤 Voice Input**: Record patient complaints via microphone
- **📷 Image Analysis**: Upload and analyze medical images
- **🧠 AI Diagnosis**: Get medical insights using advanced LLaMA-4 Scout model
- **🔊 Voice Output**: Text-to-speech responses for accessibility
- **🌐 Web Interface**: Easy-to-use Gradio-based UI

##  Prerequisites

- Python 3.8+
- Groq API Key
- Microphone access for voice input
- Internet connection for AI model access

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-doctor-bot.git
   cd ai-doctor-bot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file and add your Groq API key
   echo "GROQ_API_KEY=your_groq_api_key_here" > .env
   ```

## 🎯 Usage

1. **Start the application**
   ```bash
   python gradio_app.py
   ```

2. **Open your browser**
   - Navigate to `http://127.0.0.1:7860`

3. **Use the AI Doctor**
   - Click the microphone to record your medical concern
   - Upload an image (optional) for visual analysis
   - Click Submit to get AI medical insights
   - Listen to the audio response

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### Models Used

- **Speech-to-Text**: `whisper-large-v3-turbo`
- **Vision & Language**: `meta-llama/llama-4-scout-17b-16e-instruct`
- **Text-to-Speech**: Google Text-to-Speech (gTTS)

## 📁 Project Structure

```
ai-doctor-bot/
├── 📄 README.md              # Project documentation
├── 📄 requirements.txt       # Python dependencies
├── 📄 .env.example          # Environment variables template
├── 📄 .gitignore            # Git ignore rules
├── 📄 gradio_app.py         # Main application interface
├── 📄 brain_of_doctor.py    # AI analysis core
├── 📄 voice_of_the_patient.py # Speech-to-text functionality
├── 📄 voice_of_the_doctor.py  # Text-to-speech functionality
└── 📁 assets/              # Sample images and media
```

## ⚠️ Disclaimer

**This AI Doctor Bot is for educational and demonstration purposes only. It is NOT a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified healthcare providers with any questions regarding medical conditions.**

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Made with ❤️ for healthcare innovation**
