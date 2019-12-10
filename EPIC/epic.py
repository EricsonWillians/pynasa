import requests
import shutil
import json
import os
import errno
from PIL import Image  

class Epic:

    EPIC_URL = "https://epic.gsfc.nasa.gov/api/natural"
    EPIC_ARCHIVE_ROOT = "https://epic.gsfc.nasa.gov/archive/natural"
    EPIC_FILE_TYPE = "jpg"

    def __init__(self):
        self.json_data = self.fetch_data()

    def fetch_data(self):
        response = requests.get(self.EPIC_URL)
        json_data = json.loads(response.text)
        return json_data

    def get_dates_by_id(self):
        dates = {}
        for data in self.json_data:
            date = data["date"].split(' ')[0]
            _id = data["image"]
            dates[_id] = date
        return dates

    def get_links(self):
        links = []
        for item in self.get_dates_by_id().items():
            _id = item[0]
            date = item[1].replace('-', '/')
            link = f"{self.EPIC_ARCHIVE_ROOT}/{date}/{self.EPIC_FILE_TYPE}/{_id}.{self.EPIC_FILE_TYPE}"
            links.append(link)
        return links

    def save_links(self):
        count = 0
        file_dir = os.path.dirname(os.path.realpath(__file__))
        for link in self.get_links():
            filename = f"{file_dir}/out/epic_{count}"
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            response = requests.get(link, stream=True)
            with open(filename, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            count += 1

    def printData(self):
        print(json.dumps(self.fetch_data(), indent=4, sort_keys=True))

if __name__ == "__main__":
    epic = Epic()
    epic.save_links()