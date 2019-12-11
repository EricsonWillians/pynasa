import requests
import shutil
import json
import os
import errno
from PIL import Image


class MarsRover:

    MARS_PHOTOS_URL = "https://api.nasa.gov/mars-photos/api/v1/rovers"
    ROVER_LIST = [
        "Curiousity",
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
                 rover=MarsRover.ROVER_LIST[0], 
                 sol=1, camera=[MarsRover.CAMERA_LIST[0]], api_key="DEMO_KEY"):
        self.rover = rover
        self.sol = sol,
        self.camera = camera
        self.api_key = api_key

    

if __name__ == "__main__":
    pass
