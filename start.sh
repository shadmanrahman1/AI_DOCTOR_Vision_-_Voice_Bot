#!/bin/bash

# Install Python dependencies
pip install -r requirements-render.txt

# Start the Gradio app
python gradio_app_render.py
