import pytest
from api_client import VoximplantAPI
from models.item_purchase_by_client import ItemPurchaseByClientRequest, Item


class TestItemPurchaseByClient:
    # Предусловие: У тестового клиента создан 1 заказ, с 1, 2мя айтемами
    # Ожидаемый результат: сервис вернет 2 айтема из предусловия
    @pytest.mark.parametrize('prepare_items', [1, 2], indirect=True)
    def test_item_purchase_by_client_single_order(self, client, prepare_items, single_order):
        expected_items = [
            Item.from_order(item=order_item, order=single_order) for order_item in prepare_items]
        request = ItemPurchaseByClientRequest(client_id=client['client_id'], items=prepare_items)
        items_fact = VoximplantAPI().item_purchase_by_client(request=request)
        assert items_fact == expected_items

    # У тестового клиента создано 2 заказ, с 1-2мя айтемами
    # Ожидаемый результат: сервис вернет 2 айтема из предусловия, с количеством айтемов * 2,
    # номер и дата послднего заказа равны 2ому заказу из предусловия
    @pytest.mark.parametrize('prepare_items', [1, 2], indirect=True)
    def test_item_purchase_by_client_double_order(self, client, prepare_items, double_order):
        expected_items = [
            Item.from_double_order(item=order_item, order=double_order) for order_item in prepare_items]
        request = ItemPurchaseByClientRequest(client_id=client['client_id'], items=prepare_items)
        items_fact = VoximplantAPI().item_purchase_by_client(request=request)
        assert items_fact == expected_items

    # Не у тестируемого клиента создан заказ с 1-2мя айтемами
    # Ожидаемый результат: сервис не вернет айтемы из предусловия, так как они созданы у другого клиента,
    @pytest.mark.parametrize('prepare_items', [1, 2], indirect=True)
    def test_item_purchase_by_client_double_order(self, client, prepare_items, single_order_other_client):
        expected_items = []
        request = ItemPurchaseByClientRequest(client_id=client['client_id'], items=prepare_items)
        items_fact = VoximplantAPI().item_purchase_by_client(request=request)
        assert items_fact == expected_items
