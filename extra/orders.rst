.. _extra/orders/begin:

==================
Действия с заказом
==================

.. note::

   Все действия с заказом, кроме его создания, делаются по запросу :http:patch:`/v2/resources/orders/:id`.
   В один запрос одновременно может быть добавленно нескольно действий.
   Все запросы на изменение конкретного заказа, должны делаться синхронно.
   В случае получения запроса до конца обработки предыдущего,
   будет возвращена ошибка :http:statuscode:`409`.

   Это ограничение касается только работы с одним заказом,
   а работать одновременно с несколькими заказами можно.

   В ответ на все PATCH запросы приходит обновленный :ref:`объект заказа <walkthrough/order_create/object>`


.. _extra/orders/customer:

Добавить информацию о покупателе
================================

**Запрос**

    .. http:post:: /v2/resources/orders/:id

        :query settings:

            - **name** (str)
            - **email** (str)
            - **phone** (str)
            - **lang** (en|ru)


**Ответ**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

    :ref:`Объект заказа <walkthrough/order_create/object>`


**Пример запроса**

    .. sourcecode:: http

        PATCH /v2/resources/orders/5bacf64ea0eb2f000c45160a HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "settings": {
                "customer": {
                    "email": "hello@world.ru",
                    "lang": "ru",
                    "name": "Ivan Ivanov",
                    "phone": "+79991234576"
                }
            }
        }


**Пример ответа**

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "created_at": "2018-09-27 15:25:02",
                "event": "5b23b53b9c9b19000c6c4180",
                "expired_after": "2018-11-16 00:00:00",
                "id": "5bacf64ea0eb2f000c45160a",
                "number": 41564,
                "org": "5b0286ce517565000d9cb1ca",
                "origin": "api",
                "promocodes": [],
                "settings": {
                    "customer": {
                        "email": "hello@world.ru",
                        "lang": "ru",
                        "name": "Ivan Ivanov",
                        "phone": "+79991234576"
                    },
                    "invitation": false,
                    "send_tickets": true
                },
                "status": "executed",
                "tickets": [
                    ...
                ],
                "values": {
                    ...
                },
                "vendor": "5b0286ce517565000d9cb1ca",
                "vendor_data": {}
            },
            "refs": {
                ...
            }
        }


.. _extra/orders/vendor_data:

Добавить произвольную информацию в :ref:`объект заказа <walkthrough/order_create/object>`
==========================================================================================

**Запрос**

    .. http:post:: /v2/resources/orders/:id

        :query vendor_data:

            - **order_id**  (str) (Необязательно) Номер заказа в системе распространителя. Максимальная длина 64 символа
            - **raw** (object) Объект с произвольными полями.

.. warning::

   | Максимальное кол-во ключей в поле ``raw`` - 20
   | Максимальная длина ключа - 40 символов
   | Все значения - String с максимальной длиной 128 символов.

**Ответ**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

    :ref:`Объект заказа <walkthrough/order_create/object>`

**Пример запроса**

    .. sourcecode:: http

        PATCH /v2/resources/orders/5bacf64ea0eb2f000c45160a HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "vendor_data": {
                "order_id": "5bacf64ea0eb2f000c45160a",
                "raw": {
                    "enable_call_to_customer": true,
                    "call_counter": 3
                }
            }
        }

**Пример ответа**

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "created_at": "2018-09-27 15:25:02",
                "event": "5b23b53b9c9b19000c6c4180",
                "expired_after": "2018-11-16 00:00:00",
                "id": "5bacf64ea0eb2f000c45160a",
                "number": 41564,
                "org": "5b0286ce517565000d9cb1ca",
                "origin": "api",
                "promocodes": [],
                "settings": {
                    ...
                },
                "status": "executed",
                "tickets": [
                    ...
                ],
                "values": {
                    ...
                },
                "vendor": "5b0286ce517565000d9cb1ca",
                "vendor_data": {
                    "order_id": "5bacf64ea0eb2f000c45160a",
                    "raw": {
                        "enable_call_to_customer": true,
                        "call_counter": 3
                    }
                }
            },
            "refs": {
                ...
            }
        }


.. _extra/orders/send_tickets:

Отправка билетов покупателю на email
====================================

При значении ``true`` билеты отправляет платформа ticketscloud на ``email``,
указанный в поле :ref:`customer <extra/orders/customer>`.
По умолчанию ``false``, в этом случаи билеты должны отправить вы сами.

**Запрос**

    .. http:post:: /v2/resources/orders/:id

        :query settings:

            - **send_tickets** (bool)

**Ответ**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

    :ref:`Объект заказа <walkthrough/order_create/object>`

**Пример запроса**

    .. sourcecode:: http

        PATCH /v2/resources/orders/5bacf64ea0eb2f000c45160a HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "settings": {
                "send_tickets": true
            }
        }

**Пример ответа**

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "created_at": "2018-09-27 15:25:02",
                "event": "5b23b53b9c9b19000c6c4180",
                "expired_after": "2018-11-16 00:00:00",
                "id": "5bacf64ea0eb2f000c45160a",
                "number": 41564,
                "org": "5b0286ce517565000d9cb1ca",
                "origin": "api",
                "promocodes": [],
                "settings": {
                    "send_tickets": true,
                    ...
                },
                "status": "executed",
                "tickets": [
                    ...
                ],
                "values": {
                    ...
                },
                "vendor": "5b0286ce517565000d9cb1ca",
                "vendor_data": {
                    ...
                }
            },
            "refs": {
                ...
            }
        }


.. _extra/orders/promocodes:

Добавить промокоды к заказу
===========================

Регистр применяемых к заказу промокодов не важен

**Запрос**

    .. http:patch:: /v2/resources/orders/:id

        :query promocodes: (list of string)

**Ответ**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

    :ref:`Объект заказа <walkthrough/order_create/object>`

**Пример запроса**

    .. sourcecode:: http

        PATCH /v2/resources/orders/5bacf64ea0eb2f000c45160a HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "promocodes": [
                "PROMO100"
            ]
        }

**Пример ответа**

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "created_at": "2018-09-27 15:25:02",
                "event": "5b23b53b9c9b19000c6c4180",
                "expired_after": "2018-11-16 00:00:00",
                "id": "5bacf64ea0eb2f000c45160a",
                "number": 41564,
                "org": "5b0286ce517565000d9cb1ca",
                "origin": "api",
                "promocodes": [
                    "5d664d392a4191909a568b40"
                ],
                "status": "executed",
                "tickets": [
                    {
                        "barcode": null,
                        "discount": "100.00",
                        "extra": "46.12",
                        "full": "946.12",
                        "id": "5d664830b8a2cb5ce0576457",
                        "nominal": "900.00",
                        "number": 142278,
                        "price": "1000.00",
                        "serial": "BKC",
                        "set": "5d6648306b23e8a5f90ef047",
                        "status": "reserved"
                    }
                ],
                "values": {
                    "discount": "100.00",
                    "extra": "46.12",
                    "full": "946.12",
                    "nominal": "900.00",
                    "price": "1000.00",
                    "sets_values": {
                        "5d6648306b23e8a5f90ef047": {
                            "discount": "100.00",
                            "id": "5d6648306b23e8a5f90ef047",
                            "nominal": "900.00",
                            "price": "1000.00",
                            "promocode": "5d664d392a4191909a568b40"
                        },
                        "5d664830e4c685ae48bd2d3d": {
                            "discount": "100.00",
                            "id": "5d664830e4c685ae48bd2d3d",
                            "nominal": "400.00",
                            "price": "500.00",
                            "promocode": "5d664d392a4191909a568b40"
                        }
                    },
                    "viral_promocodes": []
                },
                "vendor": "5b0286ce517565000d9cb1ca",
                "vendor_data": {
                    ...
                }
            },
            "refs": {
                "promocodes": {
                    "5d664d392a4191909a568b40": {
                        "code": "promo100",
                        "discount": {
                            "fix": "100.00"
                        },
                        "id": "5d664d392a4191909a568b40",
                        "viral": false
                    }
                },
                "sets": {
                    "5d6648306b23e8a5f90ef047": {
                        "id": "5d6648306b23e8a5f90ef047",
                        "name": "Партер",
                        "price": "1000.00",
                        "with_seats": false
                    }
                },
                ...
            }
        }

Промокод может быть как на конкретную сумму, так и на процент:

    .. sourcecode:: js

        {
            ...
            "promocodes": {
                "5d66b9f9a80b147cadf87583": {
                    "id": "5d66b9f9a80b147cadf87583",
                    "code": "promo5%",
                    "discount": {
                        "percentage": "5%"
                    },
                    "viral": false
                }
            }
        }

Ошибки при работе с промокодами
-------------------------------

+------------------------------+------------------------------------------------------------------+
|          code                |                            msg                                   |
+==============================+==================================================================+
|  promocode_not_found         | Promocode not found                                              |
+------------------------------+------------------------------------------------------------------+
|  promocode_already_used      | Promocode already used                                           |
+------------------------------+------------------------------------------------------------------+
|  promocode_limit_min_tickets | Need more tickets in order for promocode activation /            |
|                              | Mimimum count of tickets in order for promocode activation is {} |
+------------------------------+------------------------------------------------------------------+
|  promocode_apply_info        | Cant apply promocode by some reason                              |
+------------------------------+------------------------------------------------------------------+

.. warning::

    Успешность применения промокода не влияет на код ответа

**Пример ошибки**

    .. sourcecode:: js

        {
            "data": {
                ...
            },
            "refs": {
                ...
            },
            "errors": [
                {
                    "code": "promocode_not_found",
                    "msg": "Promocode not found"
                }
            ],
        }
