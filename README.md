# Convert PDF to MP3-File

# Check youre Python Version, has to be V3
python3 --version

# Import Modules for automation
python3 -m venv .venv

# Direct in the source for "activate" for installing pyttsx3
source .venv/bin/activate
python3 -m pip install pyttsx3

# Update Pyttsx3
pip install --upgrade pip

# Install the PDF-Modul
python3 -m pip install PyPDF2