import requests
import json
import threading

from kivy.clock import Clock


class Database:

    def __init__(self, key: str,
                 endpoint: str,
                 path="/"):
        self.apiKey = key
        self.endpoint = endpoint
        self.current_path = path

    def child(self, path: str):
        return Database(key=self.apiKey, endpoint=self.endpoint, path=self.current_path + f"/{path}")

    def _set(self, value):
        r = requests.put(self.endpoint + self.current_path + ".json", data=json.dumps(value),
                         params={'key': self.apiKey})

    def _get(self, dt):
        return requests.get(self.endpoint + self.current_path + ".json", params={'key': self.apiKey}).json()

    def get(self, parallel=False):
        if parallel:
            Clock.schedule_once(self._get)
        else:
            return requests.get(self.endpoint + self.current_path + ".json", params={'key': self.apiKey}).json()

    def set(self, value):
        t1 = threading.Thread(target=self._set, args=(value,))
        t1.start()

    def _delete(self):
        return requests.delete(self.endpoint + self.current_path + ".json",
                               params={'key': self.apiKey}).json()

    def delete(self):
        t1 = threading.Thread(target=self._delete)
        t1.start()