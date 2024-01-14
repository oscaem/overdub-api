from .helpers import convert_bytes_to_flac

from google.cloud import speech

# exported function
def generate_timestamps_for_audio(audio: bytes) -> list | None:
    try:
        word_timings = []

        response = speech_to_text(audio)

        for result in response.results:
            word_timings = create_word_timings(result)
            print(f"[Timestamps] Analyzed word timings: {word_timings}")

        return word_timings

    except Exception as e:
        print(f"[Classification -> Timestamp Generation] Error creating timestamps: {e}")
        return None


def speech_to_text(audio: bytes) -> speech.RecognizeResponse:
    client = speech.SpeechClient()

    # Convert audio data
    bytes = convert_bytes_to_flac(audio)

    # Configure Engine
    config = speech.RecognitionConfig(
        language_code="en",
        enable_automatic_punctuation=True,
        enable_word_time_offsets=True,
    )


    audio = speech.RecognitionAudio(
        content=bytes,
    )

    # Synchronous speech recognition request
    response = client.recognize(config=config, audio=audio)

    return response


def create_word_timings(result: speech.SpeechRecognitionResult):
    word_timings = []
    best_alternative = result.alternatives[0]

    for word in best_alternative.words:
        start_s = word.start_time.total_seconds()
        end_s = word.end_time.total_seconds()

        word_timings.append({
            "startTime": start_s,
            "endTime": end_s,
            "word": word.word,
            "isKeyword": False,
        })

    return word_timings