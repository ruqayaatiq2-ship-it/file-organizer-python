import os
import shutil

source = "files"

images = "images"
documents = "documents"

os.makedirs(images, exist_ok=True)
os.makedirs(documents, exist_ok=True)

for file in os.listdir(source):

    if file.endswith(".jpg"):

        shutil.move(source + "/" + file, images + "/" + file)

    elif file.endswith(".txt"):

        shutil.move(source + "/" + file, documents + "/" + file)

print("Files Organized")
