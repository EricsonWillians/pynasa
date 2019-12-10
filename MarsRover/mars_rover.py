import requests
import shutil
import json
import os
import errno
from PIL import Image

class MarsRover:

    MARS_PHOTOS_URL = "https://api.nasa.gov/mars-photos/api/v1/rovers"

    def __init__(self, rover="curiosity", camera="fhaz"):
        self.rover = rover
        self.camera = camera

if __name__ == "__main__":
    pass