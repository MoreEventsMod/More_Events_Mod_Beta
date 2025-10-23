import os
from PIL import Image

# Make sure you have installed pillow with DDS support:
# pip install pillow pillow-dds

def crop_dds(file_path):
    with Image.open(file_path) as img:
        if img.size != (98, 98):
            print(f"Skipping {file_path}: not 98x98, found {img.size}")
            return
        
        # Top-right 78x78 → starts at (20, 0)
        left = 98 - 78  # 20
        top = 0
        right = 98
        bottom = 78

        cropped = img.crop((left, top, right, bottom))
        cropped.save(file_path)  # overwrite original

def main():
    for filename in os.listdir("."):
        if filename.lower().endswith(".dds"):
            crop_dds(filename)
            print(f"Cropped: {filename}")

if __name__ == "__main__":
    main()
