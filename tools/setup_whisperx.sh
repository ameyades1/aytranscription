#!/bin/bash -x

sudo apt update && sudo apt upgrade -y

# Core dependencies
sudo apt install -y ffmpeg git python3 python3-pip python3-venv build-essential

# Create isolated environment
python3 -m venv whisperx-env
source whisperx-env/bin/activate

# Upgrade pip tools
pip install --upgrade pip setuptools wheel

# Install PyTorch CPU version (important for WSL CPU usage)
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install WhisperX
pip install whisperx

