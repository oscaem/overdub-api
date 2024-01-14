from pydub import AudioSegment
import io

def convert_bytes_to_flac(audio: bytes) -> bytes:
    audio_segment = AudioSegment.from_file(io.BytesIO(audio))

    flac_bytes = audio_segment.export(format="flac").read()

    return flac_bytes