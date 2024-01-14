from PIL import Image as PILImage
from io import BytesIO
import requests

from vertexai.preview.generative_models import Image


# Generate Vertex AI compatible Image Instance from webp URL
async def load_webp_from_url(url: str) -> Image | None:
    try:
        response = requests.get(url)
        response.raise_for_status()
        webp_bytes = response.content

        image_bytes = convert_webp_to_jpeg_bytes(webp_bytes)

        image = Image.from_bytes(image_bytes)
        return image

    except requests.exceptions.RequestException as e:
        print(f"Error loading image from URL: {e}")
        return None


# Convert webp byte data to jpeg byte data
def convert_webp_to_jpeg_bytes(webp_bytes: bytes) -> bytes | None:
    try:
        webp_image = PILImage.open(BytesIO(webp_bytes))

        converted_bytes_io = BytesIO()
        webp_image.save(converted_bytes_io, format="jpeg")
        converted_bytes = converted_bytes_io.getvalue()

        return converted_bytes

    except Exception as e:
        print(f"Error converting webp to jpeg: {e}")
        return None
