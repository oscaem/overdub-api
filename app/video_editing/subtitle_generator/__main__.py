from moviepy.editor import TextClip
import cv2

from settings import FONT_PATH, FONT_SIZE, FONT_POSITION, FONT_COLOR, FONT_ACCENT_COLOR

# Constants
MARGIN_PERCENT = 0.025  # 5% margin
SHRINK_DURATION = 0.1  # The duration of the shrink effect
CROSSFADE_DURATION = 0.06
VERTICAL_POSITION_PERCENT = 0.70  # 30% from the bottom


ORIGINAL_FONT_SIZE = FONT_SIZE  # The original font size used for designing your subtitles
ORIGINAL_STROKE_WIDTH = 24


# Helper functions
def get_video_dimensions(path: str):
    cap = cv2.VideoCapture(path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()
    return width, height


def calculate_fontsize_for_width(text, font_path, color, width, initial_fontsize):
    margin = width * 2 * MARGIN_PERCENT
    target_width = width - margin
    min_fontsize, max_fontsize = 1, initial_fontsize
    best_fit_fontsize = initial_fontsize

    while min_fontsize <= max_fontsize:
        fontsize = (max_fontsize + min_fontsize) // 2
        text_clip = TextClip(text, fontsize=fontsize, font=font_path, color=color, stroke_color='black', stroke_width=18)
        text_width = text_clip.size[0]
        text_clip.close()  # Release resources as soon as possible.

        if text_width <= target_width:
            best_fit_fontsize = fontsize  # Best fit so far
            min_fontsize = fontsize + 1  # Try finding a larger font size
        else:
            max_fontsize = fontsize - 1  # Text is too wide, try smaller font sizes

    scale_factor = best_fit_fontsize / ORIGINAL_FONT_SIZE
    scaled_stroke_width = max(1, int(ORIGINAL_STROKE_WIDTH * scale_factor))


    return best_fit_fontsize, scaled_stroke_width


def create_shrinking_text_clip(text, start_time, duration, width, height):
    adjusted_fontsize, adjusted_stroke_width = calculate_fontsize_for_width(
        text, FONT_PATH, FONT_COLOR, width, FONT_SIZE
    )

    text_clip = TextClip(
        text,
        fontsize=adjusted_fontsize,
        font=FONT_PATH, color=FONT_COLOR,
        stroke_color='black',
        stroke_width=adjusted_stroke_width # set this to int value for fixed value
    ).set_duration(duration)

    def resize_func(t):
        return 0.9 if t >= SHRINK_DURATION else 1 - (t / SHRINK_DURATION) * (1 - 0.9)

    def position_func(t):
        current_width = text_clip.w * resize_func(t)
        x = (width - current_width) / 2
        y = height * VERTICAL_POSITION_PERCENT - text_clip.h / 2
        return x, y

    print("[Subtitles] generating subtitles..")
    text_clip = text_clip.set_position(position_func).resize(resize_func).set_start(start_time)
    return text_clip.crossfadein(CROSSFADE_DURATION)


# Main exported function
def generate_subtitles_from_timestamps(timestamps: list, video_path: str) -> list | None:
    try:
        print("[Subtitles] getting video dimensions..")
        width, height = get_video_dimensions(video_path)
        print("[Subtitles] calculating subtitle data..")
        clips = [
            create_shrinking_text_clip(
                stamp['word'],
                stamp['startTime'],
                stamp['endTime'] - stamp['startTime'],
                width,
                height
            )
            for stamp in timestamps
        ]
        print("[Subtitles] Generated dynamic subtitles.")
        return clips
    except Exception as e:
        print(f"[Subtitle Generator] Error: {e}")
        return None