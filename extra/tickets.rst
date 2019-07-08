.. _extra/tickets/begin:

=============================
Список билетов по мероприятию
=============================


Все билеты с местами по мероприятию
-----------------------------------

**Запрос**

    .. http:get:: /v1/resources/events/:id/tickets

        :query status: Фильтр-список по статусам (``vacant``, ``reserved``, ``sold``, ``pending``)
        :query sector: Фильтр-список по секторам


**Ответ**

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "id": objectid
                "number": int
                "reserved_till": isodatetime | null
                "seat": {
                    "number": int
                    "row": int
                    "sector": objectid
                },
                "serial": str
                "set": objectid
                "status": str
            },
            ...
        ]


**Пример запроса**

    .. sourcecode:: http

        GET /v1/resources/events/5b0d157d445143000114d0a3/tickets?status=vacant,done&sector=55abfa669cb5382abebd9fad HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d


**Пример ответа**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "id": "5b0d157d445143000114d271",
                "number": 110461,
                "reserved_till": null,
                "seat": {
                    "number": 1,
                    "row": 1,
                    "sector": "55abfa669cb5382abebd9fad"
                },
                "serial": "BET",
                "set": "5b0d157d445143000114d6af",
                "status": "vacant"
            },
            {
                "id": "5b0d157d445143000114d272",
                "number": 110462,
                "reserved_till": null,
                "seat": {
                    "number": 2,
                    "row": 1,
                    "sector": "55abfa669cb5382abebd9fad"
                },
                "serial": "BET",
                "set": "5b0d157d445143000114d6af",
                "status": "vacant"
            },
        ]
