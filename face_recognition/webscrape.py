import os
import time
import random
from google_images_search import GoogleImagesSearch

# Google API Key & CX (Replace with your actual keys)
#If you want to use this code, you need to get your own API Key and CX from Google Custom Search API
API_KEY = "Input your API Key"
CX = "Input your CX"

gis = GoogleImagesSearch(API_KEY, CX)

# Read celebrity names from a text file
def load_celebrities(filename="celebrities.txt"):
    """Loads celebrity names from a text file, one per line."""
    if not os.path.exists(filename):
        print("❌ Error: celebrities.txt not found!")
        return []
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]  # Remove empty lines

celebrities = load_celebrities()


def download_images(celeb_name, num_images=1, output_folder="celebs"):
    """Downloads images of a single celebrity and names files after them."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        search_params = {
            'q': f"{celeb_name} face",
            'num': num_images,
            'fileType': 'jpg|png',
            'imgType': 'photo',
            'safe': 'off'
        }
        gis.search(search_params)

        for idx, image in enumerate(gis.results()):
            filename = f"{output_folder}/{celeb_name.replace(' ', '_')}.jpg"
            image.download(output_folder)  # Download image
            os.rename(f"{output_folder}/{image.path.split('/')[-1]}", filename)  # Rename file
            print(f"✅ Downloaded: {filename}")
    
    except Exception as e:
        print(f"⚠️ Error downloading {celeb_name}: {e}")

# Download images for all 500 celebrities
for i, celeb in enumerate(celebrities[:500]):
    print(f"[{i+1}/500] Downloading image for: {celeb}")
    download_images(celeb, num_images=1)
    
    time.sleep(random.uniform(2, 5))  # Delay to avoid hitting API limits

print("✅ Finished downloading 500 images!")
