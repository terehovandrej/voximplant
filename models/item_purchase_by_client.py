from dataclasses import dataclass, field
from typing import List
from models.order_create import OrderResponse, OrderItem
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%Y/%m/%d %H:%M:%S")


@dataclass
class Item:
    item_id: str = None
    purchased: bool = True
    last_order_number: str = None
    last_purchase_date: str = None
    purchase_count: str = None

    @classmethod
    def from_order(cls, item: OrderItem, order: OrderResponse):
        return cls(item_id=item.item_id, last_order_number=order.order_number, last_purchase_date=dt_string,
                   purchase_count=str(item.quantity))

    @classmethod
    def from_double_order(cls, item: OrderItem, order: OrderResponse):
        item = cls.from_order(item=item, order=order)
        item.purchase_count = str(2 * int(item.purchase_count))
        return item


@dataclass
class ItemPurchaseByClientRequest:
    client_id: str = None
    items: List[str] = field(default_factory=list)


@dataclass
class ItemPurchaseByClient:
    items: List[Item] = field(default_factory=list)
