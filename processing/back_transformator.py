import img2pdf
import os

def pngs_to_pdf(png_folder, output_pdf):
    png_files = [os.path.join(png_folder, file) for file in sorted(os.listdir(png_folder)) if file.endswith('.jpg')]

    if not png_files:
        raise ValueError("No .jpg files found in the specified folder")

    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(png_files))

def back_swap(png_folder, output_folder):
    output_pdf = os.path.join(output_folder, 'output.pdf')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pngs_to_pdf(png_folder, output_pdf)
