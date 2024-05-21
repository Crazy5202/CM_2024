from .initialize_model import model
import os

def final(dir_path, predict_path):
    # predict_path = 'Doc_detect/predicts/' #папка, куда нужно положить размеченные фотки
    # Создаем папку для сохранения результатов, если она не существует
    predict_dir = os.path.join(predict_path, 'predict6') #внутри папки создаёт папки для модели номер 6
    os.makedirs(predict_dir, exist_ok=True)

    # Собираем пути к файлам изображений
    img_files = [os.path.join(dir_path, filename) for filename in os.listdir(dir_path) if
                 (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'))]

    # Запускаем модель на каждом изображении и сохраняем результаты
    for img_file in img_files:

        results = model.predict(img_file, conf=0.19, iou=0.3, verbose=False)
        # Путь для сохранения результатов
        save_path = os.path.join(predict_dir, os.path.basename(img_file))

        # Cохраняем изображение
        for result in results:
            result.save(save_path)

    return predict_dir