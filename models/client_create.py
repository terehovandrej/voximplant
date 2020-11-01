from dataclasses import dataclass


@dataclass
class ClientRequest:
    name: str = None
    surname: str = None
    phone: str = None


@dataclass()
class ClientResponse:
    client_id: int = None
