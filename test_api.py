from dataclasses import asdict

from models.item_purchase_by_client import ItemPurchaseByClientRequest


# client['client_id']
# def test_item_purchase_by_client(api_client, client, single_order):
def test_item_purchase_by_client(api_client):
    request = ItemPurchaseByClientRequest(client_id="12", items=['1'])
    res = api_client.post(
        path="service/v1/item/purchase/by-client",
        data=asdict(request))
    expected_items = {"items": [{"item_id": "1", "purchased": True, "last_order_number": single_order["order_number"],
                                 "last_purchase_date": "2020-01-16T13:33:00.000Z", "purchase_count": "string"}]}
