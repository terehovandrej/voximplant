from dataclasses import dataclass, field
from typing import List


@dataclass
class OrderItem:
    item_id: str = "1"
    price: int = 100
    quantity: int = 1


@dataclass
class OrderRequest:
    client_id: str = None
    address: str = None
    phone: str = None
    items: List[OrderItem] = field(default_factory=list)


@dataclass()
class OrderResponse:
    order_id: int = None
    order_number: str = None
