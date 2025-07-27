#!/usr/bin/env python3
"""
Setup script for AI Doctor Bot
Run this script to check and install dependencies
"""

import subprocess
import sys
import os


def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    print(f"✅ Python {sys.version} detected")


def install_requirements():
    """Install required packages"""
    try:
        print("📦 Installing requirements...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
        )
        print("✅ Requirements installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        sys.exit(1)


def check_env_file():
    """Check if .env file exists"""
    if not os.path.exists(".env"):
        print("⚠️  .env file not found")
        print("📝 Please create a .env file based on .env.example")
        print("🔑 Add your Groq API key to the .env file")
        return False
    print("✅ .env file found")
    return True


def main():
    """Main setup function"""
    print("🏥 AI Doctor Bot Setup")
    print("=" * 30)

    check_python_version()
    install_requirements()
    env_exists = check_env_file()

    print("\n🎉 Setup completed!")
    if env_exists:
        print("🚀 You can now run: python gradio_app.py")
    else:
        print("📝 Don't forget to set up your .env file first!")


if __name__ == "__main__":
    main()
