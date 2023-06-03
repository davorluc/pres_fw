import shutil
import os

md_source_path = "../../slides.md"
img_source_path = "../../img"
md_destination_path = "slides.md"
img_destination_path = "./img"

def copy_md():
    shutil.copyfile(md_source_path, md_destination_path)
    print("slides.md file copied successfully.")

def copy_img():
    if not os.path.exists(img_destination_path):
        os.makedirs(img_destination_path)

    img_extenstions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".ico"]

    for filename in os.listdir(img_source_path):
        source_file = os.path.join(img_source_path, filename)

        if os.path.isfile(source_file) and any(filename.lower().endswith(ext) for ext in img_extenstions):
            destination_file = os.path.join(img_destination_path, filename)

            shutil.copy2(source_file, destination_file)
            print(f"Copied {filename} to {img_destination_path}")


copy_md()
copy_img()
