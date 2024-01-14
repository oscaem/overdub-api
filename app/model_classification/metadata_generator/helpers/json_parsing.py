from settings import METADATA_PATH
from pathlib import Path
import json


async def save_metadata_to_json(video_id: str, text: str, title: str, description: str, credit: str, tags: list, output_location: str = METADATA_PATH):
    output_path = Path(output_location)

    json_data = {
        "text": text,
        "title": title,
        "description": description,
        "credit": credit,
        "tags": tags,
    }

    file_name = f"{video_id}_metadata.json"
    file_path = output_path / file_name

    with open(file_path, "w") as file:
        json.dump(json_data, file, indent=2)

    print(f"[Metadata] saved to: {file_path}")
