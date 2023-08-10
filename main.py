#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Folder containing your coloring book images
IMAGE_FOLDER = './imgs/'

# Output PDF file name
OUTPUT_PDF = 'coloring_book.pdf'

# Page dimensions for 8.5" x 11" (in points)
PAGE_WIDTH, PAGE_HEIGHT = letter

def convert_images_to_pdf(image_folder, output_pdf):
    # Get list of all image files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
    image_files.sort()  # Sort the files to maintain order

    # Create a new PDF
    c = canvas.Canvas(output_pdf, pagesize=letter)

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        img = Image.open(image_path)

        # Resize image to fit the page, maintaining aspect ratio
        img_width, img_height = img.size
        aspect_ratio = img_width / img_height
        new_width = PAGE_WIDTH
        new_height = int(new_width / aspect_ratio)

        if new_height > PAGE_HEIGHT:
            new_height = PAGE_HEIGHT
            new_width = int(new_height * aspect_ratio)

        x_offset = (PAGE_WIDTH - new_width) / 2
        y_offset = (PAGE_HEIGHT - new_height) / 2

        # Draw the image on the PDF
        c.drawInlineImage(image_path, x_offset, y_offset, width=new_width, height=new_height)
        c.showPage()  # Move to the next page

    c.save()

convert_images_to_pdf(IMAGE_FOLDER, OUTPUT_PDF)

