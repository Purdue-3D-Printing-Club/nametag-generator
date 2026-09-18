import csv
import os
import re

CSV_FILE = 'data/names.csv'
TEMPLATE_FILE = './assets/template.svg'
OUTPUT_DIR = 'outputs/'

# Change this number to control the Position font size in every generated SVG.
POSITION_FONT_SIZE = 18  # pixels


with open(CSV_FILE, 'r', encoding='utf-8') as names:
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as template:
        reader = csv.reader(names)
        template_text = template.read()

        os.makedirs(OUTPUT_DIR, exist_ok=True)

        for row in reader:
            first_name, last_name, position = row

            first_name = first_name.title()
            last_name = last_name.title()
            position = position.upper()

            # Change only the font size of the SVG element tagged
            # id="position-text".
            position_font_pattern = (
                r'(id="position-text"[\s\S]*?'
                r'style="[^"]*?font-size:)([^;"]+)'
            )

            modified_template_text, replacements = re.subn(
                position_font_pattern,
                lambda match: (
                    match.group(1)
                    + f'{POSITION_FONT_SIZE}px'
                ),
                template_text,
                count=1,
            )

            if replacements != 1:
                raise ValueError(
                    'Could not find the Position font-size in template.svg. '
                    'Make sure the Position text element has id="position-text".'
                )

            modified_template_text = modified_template_text.replace(
                "First Name", first_name
            )
            modified_template_text = modified_template_text.replace(
                "Last Name", last_name
            )
            modified_template_text = modified_template_text.replace(
                "Position", position
            )

            modified_template_file = os.path.join(
                OUTPUT_DIR,
                f"{first_name}_{last_name}.svg"
            )

            with open(
                modified_template_file,
                'w',
                encoding='utf-8'
            ) as output_file:
                output_file.write(modified_template_text)
