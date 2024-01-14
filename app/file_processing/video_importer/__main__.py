from settings import DOWNLOAD_PATH
import json

from yt_dlp import YoutubeDL


# Class to store the raw video data
class RawVideoData:
    def __init__(self, id, uploader, title, description, thumbnail):
        self.id = id
        self.uploader = uploader
        self.title = title
        self.description = description
        self.thumbnail = thumbnail
        self.path = f"{DOWNLOAD_PATH}{self.id}.mp4"


# Load a TikTok video using the yt_dlp library
async def load_tiktok_video(url: str):
    # Get video ID directly from URL
    video_id = url.split("/video/")[1].split("?")[0]
    # Arguments for YoutubeDL class, default naming pattern to video ID
    ydl_options = {'paths': {'home': DOWNLOAD_PATH}, 'outtmpl': f'{video_id}.%(ext)s'}
    with YoutubeDL(ydl_options) as ydl:
        try:
            # Fetch classification.metadata and video file
            info = ydl.extract_info(url, download=True)

            # Dump video classification.metadata in json format
            json_info = json.dumps(ydl.sanitize_info(info))
            data = json.loads(json_info)

            # Instantiate RawVideo class with classification.metadata
            raw_video = RawVideoData(data["id"], data["uploader"], data["title"], data["description"],
                                     data["thumbnail"])

            print(
                "[Fetched video data] " + "id: " + raw_video.id + ", title: " + raw_video.title + ", path: " + raw_video.path + ", thumbnail: " + raw_video.thumbnail)

            return raw_video

        except Exception as e:
            print("Error loading video data: " + str(e))
            return None
