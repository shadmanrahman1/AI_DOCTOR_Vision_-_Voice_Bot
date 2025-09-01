# 🚀 Render Deployment Guide for AI Doctor Bot

## Problem Fixed
The original deployment failed because **PyAudio requires system-level audio libraries** that aren't available in cloud environments like Render. This has been resolved by creating deployment-specific files that remove the PyAudio dependency.

## 📁 Files Created for Deployment

### Core Deployment Files
- `requirements-render.txt` - Dependencies without PyAudio
- `gradio_app_render.py` - Modified app for cloud deployment
- `voice_of_the_patient_render.py` - Audio processing without PyAudio
- `voice_of_the_doctor_render.py` - Text-to-speech for cloud
- `start.sh` - Startup script for Render
- `runtime.txt` - Python version specification

## 🔧 Step-by-Step Deployment Instructions

### 1. Push to GitHub
```bash
git add .
git commit -m "Add Render deployment configuration"
git push origin main
```

### 2. Set up Render Service
1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Use these settings:

**Basic Settings:**
- **Name**: `ai-doctor-bot` (or your preferred name)
- **Environment**: `Python 3`
- **Region**: Choose closest to your users
- **Branch**: `main`

**Build & Deploy Settings:**
- **Build Command**: `chmod +x start.sh && ./start.sh`
- **Start Command**: `python gradio_app_render.py`
- **Python Version**: `3.11.0` (specified in runtime.txt)

### 3. Environment Variables
In Render dashboard, add these environment variables:

**Required:**
- `GROQ_API_KEY` = `your_groq_api_key_here`
- `PORT` = `10000` (Render automatically sets this)

**Optional:**
- `ENVIRONMENT` = `production`

### 4. Deploy
- Click **"Create Web Service"**
- Render will automatically deploy your app
- Wait for deployment to complete (usually 2-5 minutes)

## 🌐 Access Your App
After deployment, you'll get a URL like:
```
https://your-app-name.onrender.com
```

## 🎯 Key Changes Made

### 1. Removed PyAudio Dependency
- **Before**: Used PyAudio for microphone recording
- **After**: Uses Gradio's built-in audio recording component

### 2. Modified Audio Processing
- **Before**: `speech_recognition` with PyAudio backend
- **After**: Direct file processing with Groq API

### 3. Cloud-Optimized Configuration
- **Server binding**: `0.0.0.0` (required for Render)
- **Port handling**: Uses `PORT` environment variable
- **Error handling**: Enhanced for cloud deployment

## 🔍 Troubleshooting

### Common Issues:

1. **Build Fails with Audio Dependencies**
   - Solution: Use `requirements-render.txt` instead of `requirements.txt`

2. **App Not Accessible**
   - Check if `server_name="0.0.0.0"` is set in `gradio_app_render.py`
   - Verify `PORT` environment variable is set

3. **Groq API Errors**
   - Verify `GROQ_API_KEY` is correctly set in Render environment variables
   - Check API key has sufficient credits

4. **Audio Upload Issues**
   - Ensure browser has microphone permissions
   - Try uploading an audio file instead of recording

## 🏥 Features Still Available
✅ Voice recording via browser microphone  
✅ Audio file upload  
✅ Image analysis with medical insights  
✅ Text-to-speech responses  
✅ Groq AI integration  
✅ Educational medical analysis  

## 🔒 Security Notes
- Never commit your `.env` file with real API keys
- Use Render's environment variables for sensitive data
- The app includes disclaimers for educational use only

## 📱 Usage Instructions for Users
1. Visit your deployed URL
2. Click the microphone icon to record voice
3. Upload a medical image (optional)
4. Get AI-powered medical insights
5. Listen to the voice response

## 💡 Next Steps
- Consider adding rate limiting for production use
- Add user authentication if needed
- Monitor usage and costs on Groq dashboard
- Set up custom domain if desired

---
**Note**: This deployment removes PyAudio dependency completely, making it fully compatible with cloud platforms like Render, Heroku, and similar services.
