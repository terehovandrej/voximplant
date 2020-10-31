from dataclasses import asdict
import pytest
from dacite import from_dict
from faker import Faker

from api_client import APIClient
from models.client_create import ClientRequest
from models.order_create import OrderRequest, Item, OrderResponse


@pytest.fixture(scope="session")
def api_client():
    return APIClient()


@pytest.fixture()
def client(api_client):
    faker = Faker()
    request = ClientRequest(name=faker.first_name(), surname="Клиент", phone="89651237160")
    res = api_client.post(
        path="/service/v1/client/create",
        data=asdict(request))
    assert res, "Empty response"
    return res


@pytest.fixture()
def single_order(api_client, client):
    faker = Faker()
    request = OrderRequest(client_id=client['client_id'], address="тестовый", phone=faker.phone(), items=[Item()])
    res = api_client.post(
        path="/service/v1/order/create",
        data=asdict(request))
    order = from_dict(data_class=OrderResponse, data=res)
    assert order, "Empty response"
    return order


@pytest.fixture()
def single_order_double_item(api_client, client):
    item_1 = Item(item_id="2", price=100, quantity=1)
    item_2 = Item(item_id="3", price=300, quantity=2)
    request = OrderRequest(client_id=client['client_id'], address="тестовый", phone="89651237160", items=[item_1, item_2])
    res = api_client.post(
        path="/service/v1/order/create",
        data=asdict(request))
    assert res, "Empty response"
    return res
