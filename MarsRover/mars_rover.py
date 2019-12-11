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
        self.sol = str(sol),
        self.camera = camera.lower()
        self.api_key = api_key
        self.json_data = self.fetch_data()

    def fetch_data(self):
        url = f"{self.MARS_PHOTOS_URL}/{self.rover}/photos?sol={self.sol}&camera={self.camera}&api_key={self.api_key}"
        response = requests.get(url)
        json_data = json.loads(response.text)
        return json_data

    def print_data(self):
        print(json.dumps(self.fetch_data(), indent=4, sort_keys=True))

if __name__ == "__main__":
    mars_rover = MarsRover()
    mars_rover.print_data()
