from .transformator import transform
from .make_predict import final
from .back_transformator import back_swap
import shutil

def process(path) -> bool:
    target = transform(path)

    path_to_converted, razm = final(target, path)

    back_swap(path_to_converted, path)

    shutil.rmtree(target)
    shutil.rmtree(path_to_converted)
    return razm

if __name__ == '__main__':
    path = input()
    result = process(path)