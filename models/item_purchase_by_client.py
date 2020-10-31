from dataclasses import dataclass, field
from typing import List

from models.order_create import OrderResponse


@dataclass
class Item:
    item_id: str = None
    purchased: bool = None
    last_order_number: str = None
    last_purchase_date: str = field(default='date', compare=False)
    purchase_count: str = None

    @classmethod
    def from_order(cls, order: OrderResponse):
        return cls(item_id=str(order.order_id), purchased=True, last_order_number=order.order_number, purchase_count=)

@dataclass
class ItemPurchaseByClientRequest:
    client_id: str = None
    items: List[str] = field(default_factory=list)


@dataclass
class ItemPurchaseByClient:
    items: List[Item] = field(default_factory=list)
