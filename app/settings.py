"""
CONSTANTS
& CONFIG
"""

# OS CONFIG
CSV_FILE_PATH = "__temp__/data.csv"

DOWNLOAD_PATH = "__temp__/00_raw/"
METADATA_PATH = "__temp__/01_metadata/"
OUTPUT_PATH = "__temp__/02_processed/"

# VERTEX AI CONFIG
PROJECT_ID = '' # Enter your Vertex AI Project
LOCATION = '' # Enter your Vertex AI Project

DEFAULT_FUNCTION = """Given a Video Thumbnail and Video Title """
CUSTOM_FUNCTION = """Given a Video Thumbnail, Title and Voiceover Draft"""

SYSTEM_PROMPT = """, infer a 1 to 3 sentence, descriptive voiceover relevant to the video."""

# EDITOR CONFIG
VOLUME_MULTIPLIER = 1.8 # For Voiceover

FONT_PATH = "__temp__/monster.ttf"
FONT_SIZE = 400
FONT_POSITION = ('center', 0.25)

FONT_COLOR = '#04FF76'
FONT_ACCENT_COLOR = '#04FF76'
