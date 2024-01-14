from .helpers import load_webp_from_url, response_to_json, save_metadata_to_json
from settings import PROJECT_ID, LOCATION, DEFAULT_FUNCTION, CUSTOM_FUNCTION, SYSTEM_PROMPT

import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part, Image


class Metadata:
    """
        Represents model_classification.metadata_generator for a video.

        Parameters:
        - dub (str): The dub information for the video.
        - title (str): The title of the video.
        - description (str): The description of the video.
        - credit (str): The credit information for the video.
        - tags (list[str]): List of tags associated with the video.
        """

    def __init__(self, id: str, dub: str, title: str, description: str, credit: str, tags: list[str]):
        self.id = id
        self.dub = dub
        self.title = title
        self.description = description
        self.credit = credit
        self.tags = tags


async def create_metadata(video_id: str, raw_title: str, raw_thumbnail_path: str,
                          raw_draft: str = None) -> Metadata | None:
    """
    Creates model_classification.metadata_generator for a raw video data.

    Parameters:
    - raw_video (RawVideo): An instance of the RawVideo class representing the raw video data.
    - draft: optional str parameter to nudge voiceover

    Returns:
    - Metadata | None: An instance of the Metadata class if successful, otherwise None.
    """
    try:
        # Configure GCP Vertex AI
        vertexai.init(project=PROJECT_ID, location=LOCATION)
        multi_modal = GenerativeModel("gemini-pro-vision")

        # Fetch thumbnail
        thumbnail_image = await load_webp_from_url(raw_thumbnail_path)

        # Construct prompt
        if not raw_draft:
            prompt = DEFAULT_FUNCTION + SYSTEM_PROMPT + "Title: " + thumbnail_image
        else:
            prompt = CUSTOM_FUNCTION + SYSTEM_PROMPT + " Title: " + raw_title + "Draft: " + raw_draft

        print("[LLM] Retrieving model_classification.metadata_generator with prompt: " + prompt)
        # Generate content using GCP Vertex AI Generative Model
        response = multi_modal.generate_content(
            [
                prompt,
                Part.from_image(thumbnail_image),
            ],
        )

        # Process the response into JSON format
        processed_response = await response_to_json(response.text)

        metadata = Metadata(id=video_id, dub=processed_response["dub"], title=processed_response["title"],
                            description=processed_response["description"], credit='NA', tags=processed_response["tags"])

        # Print model_classification.metadata_generator information (for demonstration purposes)
        print("[Metadata] Generated. Saving to disk..")

        await save_metadata_to_json(metadata.id, metadata.dub, metadata.title, metadata.description, metadata.credit,
                                    metadata.tags)

        return metadata


    except Exception as e:
        # Handle exceptions and print an error message
        print(f"Error creating model_classification.metadata_generator: {e}")
        return None
