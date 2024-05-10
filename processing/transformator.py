from pdf2image import convert_from_path
from pathlib import Path
import os

def transform(path):
    target_folder = path + '/images'

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    p = Path(path)
    for pdf_file in p.rglob("*.pdf"):
        images = convert_from_path(pdf_file, 500)
        for i, image in enumerate(images):
            image.save(os.path.join(target_folder, f"{pdf_file.stem}_page{i}.jpg"), 'JPEG')

    return target_folder