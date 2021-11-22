import os

for file_type in ["positivas"]:
    for img in os.listdir(file_type):
        os.rename(file_type + "/" + img, file_type + "/" + img.replace(" ", "_teste"))

for file_type in ["negativas"]:
    for img in os.listdir(file_type):
        os.rename(file_type + "/" + img, file_type + "/" + img.replace(" ", "_teste"))
