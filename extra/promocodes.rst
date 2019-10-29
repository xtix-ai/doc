.. _extra/promocodes/begin:

==========
Промокоды
==========


.. _extra/promocodes/check:

Проверка промокода
==================

Существует возможность проверить актуальность промокода для мероприятия.
Вслучае если промокод невозможно применить возвращается ответ BadRequest
c кодом ответа 400. В остальных случаях возвращаются параметры промкоода
и ограничения на его использование.


**Запрос**

    .. http:post:: /v2/services/promocodes/check

            - **event** (str)
            - **code** (str)


**Ответ**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "discount": {           // Размер скидки промокода, в процентах
                                        // или фиксированной величины. Одновременно
                                        // может быть только один из параметров.
                    "percentage": str   // или фиксированной величины. Одновременно
                    "fix": str          // может быть только один из параметров.
                },
                "lifetime": {           // Ограничение по времени действия промокода.
                                        // Необязательное поле.
                    "finish": iso8601
                    "start": iso8601
                },
                "sets": [oid, ... ],    // Ограничение по категориям билетов на которые
                                        // действует скидка. Пустой массив означает
                                        // отсутствие ограничений.

                "tickets_count": {      // Ограничение по количеству билетов в заказе,
                                        // на которое дейтвует скидка.
                    "min": int          // min - минимальное количество билетов в заказе,
                                        // после которого начинает начисляться скидка.
                                        // Необязательное поле.
                    "max": int          // max - максимальное количество билетов в заказе,
                                        // после которого скидка больше не начисляется.
                                        // Необязательное поле.
                }
            },
            "refs": {
                "sets": {
                    oid: {
                        "id": oid      // id категории
                        "name": str    // название категории
                        "price": str   // цена категории (оригинальная, без скидки)
                    }
                    ...
                }
            }
        }


Примеры
-------


**Запрос**

    .. sourcecode:: http

        POST /v2/services/promocodes/check HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "code": "fix100",
            "event": "5db2d8504d9134a8c7ec2cf5"
        }


**Ответ**

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json


        {
            "data": {
                "discount": {
                    "fix": "100.00"
                },
                "sets": [],
                "tickets_count": {}
            },
            "refs": {
                "sets": {}
            }
        }


**Запрос**

    .. sourcecode:: http

        POST /v2/services/promocodes/check HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "code": "all",
            "event": "5d765a4a221988d7da985875"
        }



**Ответ**

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "discount": {
                    "percentage": "25%"
                },
                "lifetime": {
                    "finish": "2019-11-30 20:59:00",
                    "start": "2019-10-30 21:00:00"
                },
                "sets": [
                    "5d765a59221988d7da985879"
                ],
                "tickets_count": {
                    "min": 2
                }
            },
            "refs": {
                "sets": {
                    "5d765a59221988d7da985879": {
                        "id": "5d765a59221988d7da985879",
                        "name": "Билетище",
                        "price": "1099.00"
                    }
                }
            }
        }


**Запрос**

    .. sourcecode:: http

        POST /v2/services/promocodes/check HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "code": "not_exists",
            "event": "5d765a4a221988d7da985875"
        }



**Ответ**

    .. sourcecode:: js

        HTTP/1.1 400 Bad Request
        Content-Type: application/json

        {
            "error": "HTTPBadRequest",
            "reason": "Promocode not found"
        }
