import csv


async def parse_csv(csv_file_path: str) -> list | None:
    try:
        parsed_data = []

        with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Get URL and optional draft from CSV
                url = row['url']
                draft = row.get('draft', None)

                parsed_data.append({'url': url, 'draft': draft})

        return parsed_data


    except Exception as e:
        print(f"Error parsing csv: {e}")
        return None
