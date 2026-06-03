import os
import shutil

folder = "."  # Current folder

for file in os.listdir(folder):
    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):

        if file.endswith((".jpg", ".png", ".jpeg")):
            destination = os.path.join(folder, "Images")

        elif file.endswith((".pdf", ".txt", ".docx")):
            destination = os.path.join(folder, "Documents")

        else:
            destination = os.path.join(folder, "Others")

        os.makedirs(destination, exist_ok=True)
        shutil.move(file_path, os.path.join(destination, file))

print("Files organized successfully!")