## Overdub API

#### Introduction

Welcome to **Overdub API**. This API serves as an automated tool to create narrated, subtitled videos from raw content with minimal guidance needed. It's a streamlined process to convert any raw video into accessible, and social-media-ready content.
Getting Started

#### Prerequisites

To use this software, you will need:
- Python 3.6 or higher
- A [ElevenLabs API](https://elevenlabs.io/docs/introduction) key
- A Google Cloud account with gcloud installed on your local machine. You can follow this [guide to setup gcloud](https://cloud.google.com/sdk/docs/install).
#### Cloning the Repository


```git clone https://github.com/your-username/Overdub-API.git``` `<br>`
```cd Overdub-API```
#### Setting Up the Virtual Environment

It's best practice to create a virtual environment to manage dependencies for the project:

``python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate``
#### Install Requirements

Install the required packages for the project using the provided requirements.txt file:

`pip install -r requirements.txt`
#### Setup Environment Variables

Rename the .env.example file to .env and add your ElevenLabs API key to it.

`ELEVENLABS_API_KEY='your-api-key'`
#### Google Cloud Configuration

Ensure you've installed gcloud and then set up gcloud for your local environment. Please refer to the Google Cloud documentation provided above to authenticate and set up your local environment.
Configure your Google Cloud project to match the settings in the `settings.py` file.
#### Configure settings.py

Adjust the `settings.py` file to match your requirements. The file includes parameters for video processing, API keys, and other configurations.
### How it Works

#### Content Processing

The software processes each video file listed in the input CSV. By default, this file should be located in the `__temp__/ directory`. The CSV should contain video URLs or file paths, with an optional content direction field to describe what is happening in the video, which can improve the results.
#### Metadata Generation

The API uses Google's Vertex AI to generate metadata. It classifies content through image data extracted from the video, complemented with the optional content direction field if provided.
#### Overdubbing and Subtitles

Once metadata is obtained, ElevenLabs' capabilities are used to overdub the video with natural-sounding speech. Subsequent steps involve generating dub timestamps for the overdub and creating dynamic subtitles that fit the requirements for various social media platforms, all of which are configurable within the `settings.py` file.
#### Output

Processed videos are outputted to the `__temp__/02_processed` directory. Any generated metadata will be stored in `__temp__/01_metadata`.
### Usage

To start processing your content, place your CSV file in the `__temp__/ directory` or specfiy a location in `settings.py` and run the main script:

`python main.py`
Make sure your environment variables and Google Cloud settings are correctly configured before running the script.
#### Contributing

Currently this project is self-mainted. If you are interested in contributing, please open a pull request. Thank you.
#### License

This project is released under the [MIT License](https://opensource.org/license/mit/).
#### Disclaimer

By using this API, you agree to the terms and conditions of both ElevenLabs and Google Cloud services.
We strive to make automated video processing as seamless as possible. With this tool, we simplify the path from raw content to engaging digital media. Should you encounter any issues or have suggestions, please open up an issue in the repository.
Happy processing!
