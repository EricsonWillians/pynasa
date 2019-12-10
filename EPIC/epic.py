import requests
import json

class Epic:

    EPIC_URL = "https://epic.gsfc.nasa.gov/api/natural"
    EPIC_ARCHIVE_ROOT = "https://epic.gsfc.nasa.gov/archive/natural"
    EPIC_FILE_TYPE = "png"

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

    def printData(self):
        print(json.dumps(self.fetch_data(), indent=4, sort_keys=True))

if __name__ == "__main__":
    epic = Epic()
    print(epic.get_links())