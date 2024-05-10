import img2pdf
import os

def pngs_to_pdf(png_folder, output_pdf):
    png_files = sorted(os.listdir(png_folder))
    png_files = [os.path.join(png_folder, file) for file in png_files if file.endswith('.jpg')]
    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(png_files))

def back_swap(png_folder, output_folder):
    output_pdf = os.path.join(output_folder, 'output.pdf')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    pngs_to_pdf(png_folder, output_pdf)
