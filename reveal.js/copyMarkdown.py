import shutil

# Specify the source and destination paths
source_path = "../../slides.md"
destination_path = "slides.md"

# Copy the file
shutil.copyfile(source_path, destination_path)

print("slides.md file copied successfully.")

