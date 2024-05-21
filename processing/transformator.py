from pdf2image import convert_from_path
from pathlib import Path
import os
from PIL import Image

Image.MAX_IMAGE_PIXELS = 200000000


def transform(path):
    target_folder = os.path.join(path, 'images')

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    pdf_folder = Path(path)
    for pdf_file in pdf_folder.rglob("*.pdf"):
        pdf_file_path = str(pdf_file)
        images = convert_from_path(pdf_file_path, 500)
        for i, image in enumerate(images):
            image_path = os.path.join(
                target_folder, f"{pdf_file.stem}_page{i}.jpg")
            image.save(image_path, 'JPEG')
            del image

    return target_folder
