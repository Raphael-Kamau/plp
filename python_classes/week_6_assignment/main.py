import requests
import os
import hashlib
from urllib.parse import urlparse

def get_filename_from_url(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    return filename if filename else "downloaded_image.jpg"

def is_duplicate(content, directory):
    """Check if image content already exists in the directory using hash comparison."""
    new_hash = hashlib.md5(content).hexdigest()
    for existing_file in os.listdir(directory):
        existing_path = os.path.join(directory, existing_file)
        if os.path.isfile(existing_path):
            with open(existing_path, 'rb') as f:
                existing_hash = hashlib.md5(f.read()).hexdigest()
                if new_hash == existing_hash:
                    return True
    return False

def fetch_image(url, directory="Fetched_Images"):
    try:
        # Validate URL scheme
        if not url.lower().startswith(("http://", "https://")):
            print(f"✗ Invalid URL scheme: {url}")
            return

        # Fetch with headers
        headers = {
            "User-Agent": "UbuntuImageFetcher/1.0",
            "Accept": "image/*"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Check content type
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped non-image content: {content_type}")
            return

        # Check for duplicates
        if is_duplicate(response.content, directory):
            print(f"⚠️ Duplicate image skipped: {url}")
            return

        # Save image
        filename = get_filename_from_url(url)
        filepath = os.path.join(directory, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ Error saving image from {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Create directory
    os.makedirs("Fetched_Images", exist_ok=True)

    # Get multiple URLs
    urls = input("Enter image URLs separated by commas:\n").split(',')

    for url in map(str.strip, urls):
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
