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
        first_name = first_name.title()
        last_name = last_name.title()

        # Create a new SVG file
        svg_file = output_dir + f'{first_name}_{last_name}.svg'
        dwg = svgwrite.Drawing(svg_file, profile='full')

        # Add a box with rounded corners
        BOX_WIDTH = 200
        BOX_HEIGHT = 80
        BOX_RADIUS = 10
        dwg.add(dwg.rect(insert=(10, 10), size=(BOX_WIDTH, BOX_HEIGHT), rx=BOX_RADIUS, ry=BOX_RADIUS, fill='none', stroke='black'))

        # Add the first name
        dwg.add(dwg.text(first_name, insert=(20, 40)))

        # Add the last name
        dwg.add(dwg.text(last_name, insert=(20, 70)))

        # Save the SVG file
        dwg.save()
