from .helpers import attach_dub_to_video


class ProcessedVideoData:
    def __init__(self, id: str, path: str, credits: str, title: str, description: str):
        self.id = id
        self.path = path
        self.credits = credits
        self.title = title
        self.description = description


async def process_video_file(video_id: str, video_title: str, video_description: str, raw_video_path: str, dub_audio: bytes,
                             subtitles: list, output_path: str) -> ProcessedVideoData | None:

    try:
        new_video_path = await attach_dub_to_video(raw_video_path, dub_audio, subtitles, output_path, video_id + ".mp4")

        processed_video_data = ProcessedVideoData(
            id=video_id,
            path=new_video_path,
            credits="NA",
            title=video_title,
            description=video_description,
        )

        return processed_video_data

    except Exception as e:
        print(f"[Video Editing -> Video Processor] Error processing video data: {e}")
        return None
