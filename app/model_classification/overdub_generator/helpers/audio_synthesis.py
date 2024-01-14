from elevenlabs import generate, set_api_key
from dotenv import load_dotenv
import os

load_dotenv()
set_api_key(os.getenv("ELEVEN_API_KEY"))


async def synthesize_audio_elevenlabs(dub: str) -> bytes | None:
    try:
        """
        Synthesize dub with Elevenlabs
        """
        audio = generate(
            text=dub,
            voice="Grace",
            model="eleven_multilingual_v2",
        )

        print("[Synthesized dub] " + dub)
        return audio

    except Exception as e:
        print("Error synthesizing audio: " + str(e))
        return None
