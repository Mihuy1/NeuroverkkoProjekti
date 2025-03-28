from PIL import Image
import os

TARGET_SIZE = (180, 180)
BASE_DIR = './Photos-CNN/Photos'
folders = ['Train', 'Test', 'Validation']

def resize_images_in_folder(folder_path):
    for category in os.listdir(folder_path):
        category_path = os.path.join(folder_path, category)

        if not os.path.isdir(category_path):
            continue

        for filename in os.listdir(category_path):
            file_path = os.path.join(category_path, filename)

            try:
                with Image.open(file_path) as img:
                    img = img.resize(TARGET_SIZE)
                    img.save(file_path)
                    print(f"Scaled: {file_path}")
            except Exception as e:
                print(f"Error {file_path}: {e}")


if __name__ == "__main__":
    for folder in folders:
        folder_path = os.path.join(BASE_DIR, folder)
        resize_images_in_folder(folder_path)
