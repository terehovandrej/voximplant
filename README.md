# voximplant

По факту необходимо написать тесты на абстрактную функцию service/v1/item/purchase/by-client (v1/client/create и v1/order/create вспомогательные функции, которые могут потребоваться для реализации тестов).

Сделать на свое усмотрение базовую структуру проекта с тестами и выложиnm на любой публичный репозиторий. Тесты должны быть написаны на Python(3+) + pytest. 



service/v1/item/purchase/by-client

Функция возвращает, сколько раз клиент покупал/не покупал конкретные item_id(из запроса), номер последнего заказа и дату его создания.

Request:

{

  "client_id": "string",

  "item_ids": [

    "string"

  ]

}

Response:

{

  "items": [

    {

      "item_id": "string",

      "purchased": true/false,

      "last_order_number": "string",

      "last_purchase_date": "2020-01-16T13:33:00.000Z",

      "purchase_count": "string"

    }

  ]

}



service/v1/client/create

Функция создает клиента

Request:

{

  "name": "string",

  "surname": "string",

  "phone": "string"

}

Response:

{

  "client_id": int

}

service/v1/order/create

Функция создает заказ

Request:

{

  "client_id": int,

  "address": "string",

  "phone": "string",

  "items": [

    {

      "item_id": int,

      "price": float,

      "quantity": int,

    }

  ]

}

Response:

{

  "order_id": int,

  "order_number": "string"

}



