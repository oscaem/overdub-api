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
PROJECT_ID = 'project-shorts-411002'
LOCATION = 'us-central1'

DEFAULT_FUNCTION = """Given a TikTok video Thumbnail and video title """
CUSTOM_FUNCTION = """Given a TikTok video Thumbnail, title and Voiceover Draft"""

SYSTEM_PROMPT = """, infer a 1 to 3 sentence voiceover relevant to the video. 
Optimal is engaging vocabulary like 'Look at what these sweet X are doing!'.
It should have a clear hook that pulls the viewer in, raises curiosity and makes them watch the video.
Also infer a very short tile, video description and 3 tags. 
Return dub, title, description and tags in JSON format. 
Provide only the JSON starting / ending with {} and nothing else."""

# EDITOR CONFIG
VOLUME_MULTIPLIER = 1.8

FONT_PATH = "__temp__/monster.ttf"
FONT_SIZE = 400
FONT_POSITION = ('center', 0.25)

FONT_COLOR = '#04FF76'
FONT_ACCENT_COLOR = '#04FF76'