from dataclasses import asdict
from dacite import from_dict

from models.item_purchase_by_client import ItemPurchaseByClientRequest, ItemPurchaseByClient, Item


def test_item_purchase_by_client(api_client, client, single_order):
    expected_items = [
        Item(item_id=single_order['item_id'], purchased=True, last_order_number=single_order['order_number'],
             last_purchase_date="date",
             purchase_count=single_order['quantity'])]
    request = ItemPurchaseByClientRequest(client_id=client['client_id'], items=single_order['order_id'])
    res = api_client.post(
        path="service/v1/item/purchase/by-client",
        data=asdict(request))
    fact_items = from_dict(data_class=ItemPurchaseByClient, data=res)
    assert expected_items == fact_items
