.. _extra/partgner_legal/begin:

========================================
Получение юр. информации об организаторе
========================================


**Запрос**:

    .. http:get:: /v1/resources/partners/:id

        :query fields-schema: отображаемые поля = ``legal{type,bank,detail,who}``


**Ответ**:

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "legal": {
                "bank": {
                    "bik": str
                    "ks": str
                    "name": str
                    "rs": str
                },
                "detail": {
                    "address": str
                    "inn": str
                    "kpp": str
                    "name": str
                    "nds": bool
                    "ogrn": str
                    "taxes": str
                    "type": str
                },
                "type": str
                "who": {
                    "name": str
                    "position": str
                    "reason": str
                }
            }
        }


**Пример запроса**:

    .. sourcecode:: http

        GET /v1/resources/partners/5b0286ce517565000d9cb1ca?fields-schema=legal%7Btype,bank,detail,who%7D HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d


**Пример ответа**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "legal": {
                "bank": {
                    "bik": "354612399",
                    "ks": "98078976342444421357",
                    "name": "ООО \"Сибирский банка Развития\"",
                    "rs": "98702345234586791211"
                },
                "detail": {
                    "address": "г. Москва, Графский переулок, дом 140, строение 52, 8 этаж",
                    "inn": "2345835521",
                    "kpp": "245329523",
                    "name": "ОАО \"Первая Развлекательная компания\"",
                    "nds": false,
                    "ogrn": "3452349462112",
                    "taxes": "usn",
                    "type": "ru/ltd"
                },
                "type": "ru/ltd",
                "who": {
                    "name": "Петров Василий Семенович",
                    "position": "Бухгалтер",
                    "reason": "на основании доверенности №235422345 от 01.04.2016"
                }
            }
        }