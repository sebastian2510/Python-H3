import requests
import json

# Convert the following code to classes
# {'items': [{'subjects': [], 'title': "", 'aliases': [], 'details': ""}]}

class FBIWantedItem:
    def __init__(self):
        self.subjects = []
        self.title = ""
        self.aliases = []
        self.details = ""

class FBIWantedList:
    def __init__(self):
        self.items = []

    def fetch(self):
        response = requests.get("https://api.fbi.gov/wanted/v1/list")
        if response.status_code == 200:
            data = json.loads(response.text)
            self.items = data['items']

    def get_items(self) -> FBIWantedItem:
        return FBIWantedItem(self.items)
    
print(FBIWantedList().fetch().get_items())

