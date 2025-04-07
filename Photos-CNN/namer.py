import os

def rename_files_in_folder(folder_path, prefix, start_number):
    try:
        # Get a list of files in the folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        files.sort()  # Sort files to ensure consistent renaming order

        # Rename each file
        for index, file_name in enumerate(files):
            file_extension = os.path.splitext(file_name)[1]  # Get the file extension
            new_name = f"{prefix}_{start_number + index:03d}{file_extension}"  # Format new name
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {file_name} -> {new_name}")

        print("Renaming completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
folder_path = input("Enter the folder path: ")
prefix = input("Enter the prefix: ")
start_number = int(input("Enter the starting number: "))
rename_files_in_folder(folder_path, prefix, start_number)