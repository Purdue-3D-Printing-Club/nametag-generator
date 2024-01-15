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
        dwg.add(dwg.text(first_name, insert=(60, 40)))

        # Add the last name
        dwg.add(dwg.text(last_name, insert=(60, 70)))

        logo = svgwrite.Drawing(size=(100, 100), profile='full')

        # Define the path data
        # Using a random svg from the organizerv2 figma in place of the logo for now
        path_data = "M17.2262 0H32.8065V9.27385H37C37.5523 9.27385 38 9.72157 38 10.2739V17.5477C38 18.0999 37.5523 18.5477 37 18.5477H33.5834L28.4432 27.8215H21.5897L16.4495 18.5477H13.0328C12.4805 18.5477 12.0328 18.0999 12.0328 17.5477V10.2739C12.0328 9.72157 12.4805 9.27385 13.0328 9.27385H17.2262V0ZM2 35.5C2 34.1193 3.11929 33 4.5 33H20C20 31.3431 21.3431 30 23 30H26C27.6569 30 29 31.3431 29 33V35C29 36.6569 27.6569 38 26 38H25.5H23H4.5C3.11929 38 2 36.8807 2 35.5Z"

        # Create the path element
        logo.add(dwg.path(d=path_data, fill="black"))

        # Add the logo to the existing SVG file
        dwg.add(logo)

        # Save the modified SVG file
        dwg.save()
