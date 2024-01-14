from settings import VOLUME_MULTIPLIER
import tempfile
import os

from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip, CompositeVideoClip


async def attach_dub_to_video(video_path: str, audio: bytes, subtitles: list, output_path: str, output_filename: str) -> str | None:
    """
    Combine raw video file with dub audio
    """
    try:
        # Load video clip
        video_clip = VideoFileClip(video_path)

        # Create a temporary audio file
        with tempfile.NamedTemporaryFile(delete=False) as temp_audio_file:
            temp_audio_file.write(audio)
        temp_audio_file_path = temp_audio_file.name

        try:
            # Convert raw audio bytes to AudioFileClip
            dub_audio_clip = AudioFileClip(temp_audio_file_path)

            # Increase audio clip volume, ignore warning
            dub_audio_clip = dub_audio_clip.volumex(VOLUME_MULTIPLIER)

            # Attach dub audio at the beginning of the video
            video_clip = video_clip.set_audio(CompositeAudioClip([dub_audio_clip, video_clip.audio]))

            # Attach subtitles
            video_clip = CompositeVideoClip([video_clip] + subtitles)

            # Define output file path
            output_file_path = os.path.join(output_path, output_filename)

            # Save the updated video file
            video_clip.write_videofile(output_file_path, codec="libx264", audio_codec="aac",
                                       temp_audiofile="temp_audio.mp4",
                                       remove_temp=True,
                                       threads=6
                                       )

            return output_file_path

        finally:
            # Close the video clip explicitly
            video_clip.close()

            # Close and remove the temporary audio file
            temp_audio_file.close()
            os.remove(temp_audio_file_path)

    except Exception as e:
        print("Error merging video and audio data: " + str(e))
        return None
