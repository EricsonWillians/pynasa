import requests
import shutil
import json
import os
import errno
from PIL import Image


class MarsRover:

    MARS_PHOTOS_URL = "https://api.nasa.gov/mars-photos/api/v1/rovers"
    ROVER_LIST = [
        "Curiosity",
        "Opportunity",
        "Spirit"
    ]
    CAMERA_LIST = [
        "FHAZ",
        "RHAZ",
        "MAST",
        "CHEMCAM",
        "MAHLI",
        "MARDI",
        "NAVCAM",
        "PANCAM",
        "MINITES"
    ]

    def __init__(self,
                 rover=ROVER_LIST[0], 
                 sol=1, camera=CAMERA_LIST[0], api_key="DEMO_KEY"):
        self.rover = rover.lower()
        self.sol = sol
        self.camera = camera.lower()
        self.api_key = api_key
        self.json_data = self.fetch_data()

    def fetch_data(self):
        url = f"{self.MARS_PHOTOS_URL}/{self.rover}/photos?sol={self.sol}&page=1&camera={self.camera}&api_key={self.api_key}"
        print(f"URL: {url}")
        response = requests.get(url)
        json_data = json.loads(response.text)
        return json_data

    def get_links(self):
        photos = []
        try:
            for photo in self.json_data["photos"]:
                photos.append(photo["img_src"])
        except Exception:
            print("ERROR: It wasn't possible to download the photos.")
            print("The response was: ")
            self.print_data()
            quit()
        return photos

    def save_links(self):
        file_dir = os.path.dirname(os.path.realpath(__file__))
        for link in self.get_links():
            filename = f"{file_dir}/out/{self.rover.upper()}_{link.split('/')[-1]}"
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise
            response = requests.get(link, stream=True)
            with open(filename, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

    def print_data(self):
        print(json.dumps(self.fetch_data(), indent=4, sort_keys=True))

if __name__ == "__main__":
    mars_rover = MarsRover()
    mars_rover.save_links()
