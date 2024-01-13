import csv
import svgwrite

# Path to the CSV file
csv_file = 'data/names.csv'

# Path to the output directory for SVG files
output_dir = 'outputs/'

# Read the CSV file
with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in reader:
        first_name, last_name = row

        # Create a new SVG file
        svg_file = output_dir + f'{first_name}_{last_name}.svg'
        dwg = svgwrite.Drawing(svg_file, profile='tiny')

        # Add your SVG content here
        # For example, you can add text elements for the first and last name
        dwg.add(dwg.text(first_name, insert=(10, 20)))
        dwg.add(dwg.text(last_name, insert=(10, 40)))

        # Save the SVG file
        dwg.save()
