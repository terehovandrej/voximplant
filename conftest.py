import pytest
from dacite import from_dict
from faker import Faker
from api_client import VoximplantAPI
from models.client_create import ClientRequest, ClientResponse
from models.order_create import OrderRequest, OrderItem, OrderResponse


@pytest.fixture()
def client():
    faker = Faker()
    request = ClientRequest(name=faker.first_name(), surname=faker.last_name(), phone=faker.phone())
    client_res = VoximplantAPI().create_client(request=request)
    assert client_res, "Empty response"
    return from_dict(data_class=ClientResponse,
                     data=client_res)


@pytest.fixture()
def prepare_items(request):
    return [OrderItem.random_init() for _ in range(request.param)]


@pytest.fixture()
def single_order(client, prepare_items):
    request = OrderRequest(client_id=client['client_id'], address="test", phone="00000000", items=prepare_items)
    order_res = VoximplantAPI().create_order(request=request)
    assert order_res, "Empty response"
    return from_dict(data_class=OrderResponse,
                     data=order_res)


@pytest.fixture()
def double_order(client, prepare_items):
    request = OrderRequest(client_id=client['client_id'], address="test", phone="00000000", items=prepare_items)
    first_order_res = VoximplantAPI().create_order(request=request)
    second_order_res = VoximplantAPI().create_order(request=request)
    assert first_order_res, "Empty first_order response"
    assert second_order_res, "Empty second_order response"
    return from_dict(data_class=OrderResponse,
                     data=second_order_res)


@pytest.fixture()
def single_order_other_client(client, prepare_items):
    request = OrderRequest(client_id='12345', address="test", phone="00000000", items=prepare_items)
    order_res = VoximplantAPI().create_order(request=request)
    assert order_res, "Empty response"
    return from_dict(data_class=OrderResponse,
                     data=order_res)
