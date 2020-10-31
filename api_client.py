import requests

from constants import BASE_URL


class APIClient:
    """
    Упрощенный клиент для работы с API
    Инициализируется базовым url на который пойдут запросы
    """

    def __init__(self):
        self.base_address = BASE_URL

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        print("POST request to {}".format(url))
        response = requests.post(url=url, params=params, data=data, headers=headers)
        return response.json()

    def get(self, path="/", params=None):
        url = self.base_address + path
        print("GET request to {}".format(url))
        response = requests.get(url=url, params=params)
        return response.json()
