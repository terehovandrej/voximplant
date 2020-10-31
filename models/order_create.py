from dataclasses import dataclass, field
from typing import List


@dataclass
class Item:
    item_id: str = 1
    price: int = 200
    quantity: int = 1


@dataclass
class OrderRequest:
    client_id: str = None
    address: str = None
    phone: str = None
    items: List[Item] = field(default_factory=list)


@dataclass()
class OrderResponse:
    order_id: int = None
    order_number: str = None
