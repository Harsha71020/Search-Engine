import os

def read_files_from_folder(folder_path):
    files_content = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                files_content[filename] = f.read()
    return files_content