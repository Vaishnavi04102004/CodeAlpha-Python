import os
import shutil

source = "source"
destination = "destination"

if not os.path.exists(destination):
    os.makedirs(destination)

extensions = (".jpg", ".jpeg", ".png")

moved = 0

for file in os.listdir(source):
    source_path = os.path.join(source, file)

    if os.path.isfile(source_path) and file.lower().endswith(extensions):
        destination_path = os.path.join(destination, file)

        if os.path.exists(destination_path):
            name, ext = os.path.splitext(file)
            count = 1

            while True:
                new_name = f"{name}_{count}{ext}"
                destination_path = os.path.join(destination, new_name)

                if not os.path.exists(destination_path):
                    break

                count += 1

        shutil.move(source_path, destination_path)
        print(f"Moved: {os.path.basename(destination_path)}")
        moved += 1

print(f"\nTotal Files Moved: {moved}")