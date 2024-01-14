from .helpers import synthesize_audio_elevenlabs

from settings import OUTPUT_PATH
from video_editing import attach_dub_to_video

async def overdub(dub_text: str) -> bytes | None:
    try:
        """
        Create overdub for raw video file
        """
        audio = await synthesize_audio_elevenlabs(dub_text)

        return audio

    except Exception as e:
        print("Error overdubbing video: " + str(e))
        return None
