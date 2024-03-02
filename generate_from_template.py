import csv

CSV_FILE = 'data/names.csv'
TEMPLATE_FILE = './assets/template.svg'
OUTPUT_DIR = 'outputs/'

with open(CSV_FILE, 'r', encoding='utf-8') as names:
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as template:
        reader = csv.reader(names)
        template_text = template.read()

        for row in reader:
            first_name, last_name, position = row
            first_name = first_name.title()
            last_name = last_name.title()
            position = position.upper()

            modified_template_text = template_text.replace("First Name", first_name)
            modified_template_text = modified_template_text.replace("Last Name", last_name)
            modified_template_text = modified_template_text.replace("Position", position)
            modified_template_file = OUTPUT_DIR + f"{first_name}_{last_name}.svg"

            with open(modified_template_file, 'w', encoding='utf-8') as output_file:
                output_file.write(modified_template_text)
