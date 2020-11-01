from dataclasses import asdict
import requests
from dacite import from_dict
from constants import BASE_URL
from models.client_create import ClientRequest, ClientResponse
from models.item_purchase_by_client import ItemPurchaseByClientRequest, ItemPurchaseByClient
from models.order_create import OrderRequest, OrderResponse


class APIClient:

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


class VoximplantAPI(APIClient):

    def create_order(self, request: OrderRequest) -> OrderResponse:
        return from_dict(data_class=OrderResponse,
                         data=self.post(path='/service/v1/order/create', data=asdict(request)))

    def create_client(self, request: ClientRequest) -> ClientResponse:
        return from_dict(data_class=ClientResponse,
                         data=self.post(path='/service/v1/client/create', data=asdict(request)))

    def item_purchase_by_client(self, request: ItemPurchaseByClientRequest) -> ItemPurchaseByClient:
        return from_dict(data_class=ItemPurchaseByClient,
                         data=self.post(path='/service/v1/item/purchase/by-client', data=asdict(request)))
