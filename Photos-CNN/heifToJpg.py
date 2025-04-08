import os
import subprocess

def heic_to_jpg(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")

            try:
                result = subprocess.run(
                    ["heif-convert", input_path, output_path],
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                print(f"Converted: {filename} -> {os.path.basename(output_path)}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to convert {filename}:\n{e.stderr.decode('utf-8')}")
            except Exception as e:
                print(f"An unexpected error occurred with {filename}: {e}")

if __name__ == "__main__":
    input_folder = "../NeuroverkkoProjekti/Photos-CNN/PhotosCutlery/Validation/Spoon"
    output_folder = "../NeuroverkkoProjekti/Photos-CNN/PhotosCutlery/Validation/Spoon"
    heic_to_jpg(input_folder, output_folder)
