import argparse
from PIL import Image

def display_image_metadata(image_path):
    img = Image.open(image_path)
    meta = img.info
    for key, value in meta.items():
        print(f"{key}: {value}")
    
    return img

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display image metadata.")
    parser.add_argument("image_path", type=str, help="Path to the image file.")
    args = parser.parse_args()
    
    display_image_metadata(args.image_path)