from transformator import transform
from make_predict import final
from back_transformator import back_swap
import shutil
import os

path_to_pdfs = 'Doc_detect/predicts'
target = transform(path_to_pdfs)

path_to_converted = final(target)

output_folder = 'Doc_detect/predicts/output'
back_swap(path_to_converted, output_folder)

shutil.rmtree(target)
shutil.rmtree(path_to_converted)
