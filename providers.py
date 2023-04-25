import requests
import json

class IMDbProvider:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://imdb-api.com/en/API/"

    def get_movie_metadata(self, imdb_id):
        url = self.base_url + f"Title/{self.api_key}/{imdb_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            return None

    def get_tv_show_metadata(self, imdb_id):
        url = self.base_url + f"Serie/{self.api_key}/{imdb_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            return None


class TheTVDBProvider:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.thetvdb.com/"
        self.token = self.get_token()

    def get_token(self):
        headers = {'Content-Type': 'application/json'}
        data = {'apikey': self.api_key}
        response = requests.post(self.base_url + "login", headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return json.loads(response.content)["token"]
        else:
            return None

    def get_tv_show_metadata(self, tvdb_id):
        headers = {'Authorization': f"Bearer {self.token}"}
        url = self.base_url + f"series/{tvdb_id}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return json.loads(response.content)["data"]
        else:
            return None
