import pytest
from api_client import VoximplantAPI
from models.item_purchase_by_client import ItemPurchaseByClientRequest, ItemPurchaseByClient, Item


@pytest.mark.parametrize('items_req', [2], indirect=True)
def test_item_purchase_by_client_item_req(client, items_req, single_order, items_resp):
    api = VoximplantAPI()
    request = ItemPurchaseByClientRequest(client_id=client['client_id'], items=items_req)
    items_fact = api.item_purchase_by_client(request=request)
    assert items_fact == items_resp
