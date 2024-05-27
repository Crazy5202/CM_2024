from .transformator import transform
from .make_predict import final
from .back_transformator import back_swap
import shutil

def process(path):
    target = transform(path)

    path_to_converted, count = final(target, path)

    back_swap(path_to_converted, path)

    shutil.rmtree(target)
    shutil.rmtree(path_to_converted)
    return count

if __name__ == '__main__':
    path = input()
    result = process(path)