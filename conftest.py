import pytest
from dacite import from_dict
from faker import Faker

from api_client import VoximplantAPI
from models.client_create import ClientRequest, ClientResponse
from models.item_purchase_by_client import Item
from models.order_create import OrderRequest, OrderItem, OrderResponse


@pytest.fixture()
def client():
    faker = Faker()
    api = VoximplantAPI()
    request = ClientRequest(name=faker.first_name(), surname=faker.last_name(), phone=faker.phone())
    client_res = api.create_client(request=request)
    assert client_res, "Empty response"
    return from_dict(data_class=ClientResponse,
                     data=client_res)


@pytest.fixture()
def prepare_items(request):
    return [OrderItem() for _ in range(request.param)]


@pytest.fixture()
def items_resp(single_order, prepare_items):
    return [Item(item_id=order_item['item_id'], purchased=True, last_order_number=single_order['order_number'],
                 last_purchase_date=None,
                 purchase_count=1) for order_item in prepare_items]


@pytest.fixture()
def single_order(client, prepare_items):
    api = VoximplantAPI()
    request = OrderRequest(client_id=client['client_id'], address="тестовый", phone="00000000", items=prepare_items)
    order_res = api.create_order(request=request)
    assert order_res, "Empty response"
    return from_dict(data_class=OrderResponse,
                     data=order_res)
