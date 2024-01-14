Generate Overdubbed and Subtitled Shorts from Video URL

- Extensible for business as:

1. Create automated shorts from tiktok or reels (grayzone)
2. Automatically overdub your videos
3. Automatically overdub and subtitle your videos

suggested refacored module structure

__temp__ (temporary media files)
  00_raw
  01_metadata
  02_processed
file_processing
  file_processing.csv_parser
  video_importer
model_classification
  metadata_generator
    __main.py__
    helpers/
  model_classification.overdub_generator
  model_classification.timestamp_generator
video_editing
  subtitle_generator
  video_processor
main.py
models.py
settings.py

  

