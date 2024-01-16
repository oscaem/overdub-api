from file_processing import parse_csv, load_tiktok_video
from model_classification import create_metadata, overdub, generate_timestamps_for_audio
from video_editing import process_video_file, generate_subtitles_from_timestamps
from settings import CSV_FILE_PATH, OUTPUT_PATH

import subprocess
import asyncio


async def main():
    try:
        # --- Main Application Logic

        # 0. Parse csv video data with url, draft (optional)
        parsed_data = await parse_csv(CSV_FILE_PATH)

        if parsed_data:
            for entry in parsed_data:
                url = entry['url']
                draft = entry['draft']

                print("Draft: " + draft)

                # 1. Load the video
                raw_video = await load_tiktok_video(url)

                # 2. Create Metadata
                metadata = await create_metadata(
                    video_id=raw_video.id,
                    raw_title=raw_video.title,
                    raw_thumbnail_path=raw_video.thumbnail,
                    raw_draft=draft
                )

                # 3. Create Overdub
                overdub_audio = await overdub(metadata.dub)

                # 4. Create Timestamps
                timestamps = generate_timestamps_for_audio(overdub_audio)

                # 5. Generate Subtitles
                subtitle_text = generate_subtitles_from_timestamps(timestamps, raw_video.path)

                # 6. Process Video
                processed_video_data = await process_video_file(
                    video_id=raw_video.id,
                    video_title=metadata.title,
                    video_description=metadata.description,
                    raw_video_path=raw_video.path,
                    dub_audio=overdub_audio,
                    subtitles=subtitle_text,
                    output_path=OUTPUT_PATH
                )

                print(processed_video_data)

    except Exception as e:
        print(e)
    else:
        print('Done!')
        # Open the output path in Finder
        subprocess.call(["open", "-R", OUTPUT_PATH])


# Run the main function
if __name__ == '__main__':
    asyncio.run(main())
