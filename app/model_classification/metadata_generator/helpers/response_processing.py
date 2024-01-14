import json

# Convert blank string from llm response to JSON dict
async def response_to_json(response: str) -> dict:
    start_index = response.find('{')
    end_index = response.rfind('}')
    cleaned_string = response[start_index:end_index + 1]

    json_data = json.loads(cleaned_string)

    return json_data
