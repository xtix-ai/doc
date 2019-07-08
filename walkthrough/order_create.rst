.. _walkthrough/order_create/begin:

======================
Шаг 2: Создание заказа
======================

.. note::

   Примеры ответов и запросов в данном разделе упрощены.
   Тем не менее этого достаточно для интеграции.
   Детальная информация по каждому разделу присутствует в блоках *См. также*



.. _walkthrough/order_create/create:

Создание
========

**Запрос**

    .. http:post:: /v2/resources/orders/

        :query event: Обязателен


**Ответ**

.. _walkthrough/order_create/object:

Объект заказа

    .. sourcecode:: js

        {
            "data": {
                "id": objectid
                "status": 'executed' | 'in_progress' | 'done' | 'cancelled' | 'expired'
                "created_at": isodatetime
                "done_at": isodatetime
                "expired_after": isodatetime
                "custom_fields": {
                    "order": [...],
                    "tickets": [...]
                }
                "event": objectid
                "number": int
                "org": objectid
                "origin": 'api' | 'salespoint' | 'widget' | 'control_panel'
                "payments": [
                    {
                        "id": objectid
                        "type": '_testpay_core' | '_testpay_partner' | 'invoice' | 'platron' | 'cloudpayments' | 'payu' | 'stripe'
                        "status": 'executed' | 'in_progress' | 'done' | 'cancelled'
                        "amount": money
                    },
                ]
                "promocodes": [
                    {
                        "id": objectid
                    },
                ]
                "settings": {
                    "invitation": bool
                    "send_tickets": bool
                    "courier": bool
                    "customer": {
                        "name": str
                        "email": email
                        "phone": str
                        "lang": 'en' | 'ru'
                    }
                }
                "sessions": {
                    "ga": str
                    "utm": objectid
                    "roistat": str
                },
                "tickets": [
                    {
                        "id": objectid
                        "serial": str
                        "number": int
                        "seat": {
                            "row": str
                            "number": str
                            "sector": objectid
                        }
                        "status": str
                        "price": money
                        "nominal": money
                        "discount": money
                        "extra": money
                        "full": money
                    },
                ]
                "values": {
                    "discount": money
                    "extra": money
                    "full": money
                    "nominal": money
                    "price": money
                    "sets_values": {
                        id: {
                            "discount": money
                            "id": objectid
                            "nominal": money // price with discount
                            "price": money
                            "promocode": objectid | None
                        },
                        ...
                    }
                    "viral_promocodes": [...]
                },
                "vendor": objectid
                "vendor_data": {
                    "order_id": str
                    "raw": {
                        ...
                    }
                }
            },
            "refs": {
                "events": {
                    id: {
                        "id": objectid
                        "lifetime": {
                            "finish": isodatetime
                            "start": isodatetime
                        },
                        "org": objectid
                        "status": str
                        "timezone": str
                        "title": {
                            "desc": str
                            "text": str
                        }
                    }
                },
                "partners": {
                    id: {
                        "id": objectid
                        "name": str
                    }
                },
                "promocodes": {
                    id: {
                        "code": str
                        "discount": {
                            "percentage"
                        },
                        "id": objectid
                        "lifetime"
                        "sets": [...],
                        "tickets_count": {
                            ...
                        },
                        "viral": bool
                    },
                },
                "sets": {
                    id: {
                        "id": objectid
                        "name": str
                        "price": money
                        "with_seats": bool
                    },
                }
            }
        }


**Пример запроса**

    .. sourcecode:: http

        POST /v2/resources/orders HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "event": "5c87d5871a2778000c7e7771"
        }

**Пример ответа**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "created_at": "2019-07-02 13:54:15",
                "custom_fields": {
                    "order": [],
                    "tickets": []
                },
                "event": "5c87d5871a2778000c7e7771",
                "expired_after": "2019-07-02 14:09:15",
                "id": "5d1b62074ed1c53b328ad4f0",
                "number": 52906,
                "org": "5b04229196c055000d87c2b5",
                "origin": "api",
                "payments": [],
                "promocodes": [],
                "settings": {
                    "invitation": false,
                    "send_tickets": false,
                    "subscribe_agree": false
                },
                "status": "executed",
                "tickets": [],
                "values": {
                    "discount": "0.00",
                    "extra": "0.00",
                    "full": "0.00",
                    "nominal": "0.00",
                    "price": "0.00",
                    "sets_values": {
                        "5c87d59e1a2778000bd96e58": {
                            "discount": "0.00",
                            "id": "5c87d59e1a2778000bd96e58",
                            "nominal": "920.00",
                            "price": "920.00",
                            "promocode": null
                        },
                        "5ca715ab7cf2a70015eeabba": {
                            "discount": "0.00",
                            "id": "5ca715ab7cf2a70015eeabba",
                            "nominal": "0.00",
                            "price": "0.00",
                            "promocode": null
                        },
                        "5d073f870e9d2b63a2e558c3": {
                            "discount": "0.00",
                            "id": "5d073f870e9d2b63a2e558c3",
                            "nominal": "100.00",
                            "price": "100.00",
                            "promocode": null
                        },
                        "5d073f970e9d2b63a2e558c7": {
                            "discount": "0.00",
                            "id": "5d073f970e9d2b63a2e558c7",
                            "nominal": "110.00",
                            "price": "110.00",
                            "promocode": null
                        },
                        "5d073fc20e9d2b63a2e558cc": {
                            "discount": "0.00",
                            "id": "5d073fc20e9d2b63a2e558cc",
                            "nominal": "120.00",
                            "price": "120.00",
                            "promocode": null
                        },
                        "5d073fc20e9d2b63a2e558d0": {
                            "discount": "0.00",
                            "id": "5d073fc20e9d2b63a2e558d0",
                            "nominal": "130.00",
                            "price": "130.00",
                            "promocode": null
                        },
                        "5d073fc2a5f32c07a1b71b94": {
                            "discount": "0.00",
                            "id": "5d073fc2a5f32c07a1b71b94",
                            "nominal": "140.00",
                            "price": "140.00",
                            "promocode": null
                        }
                    },
                    "viral_promocodes": []
                },
                "vendor": "5b04229196c055000d87c2b5",
                "vendor_data": {}
            },
            "refs": {
                "events": {
                    "5c87d5871a2778000c7e7771": {
                        "id": "5c87d5871a2778000c7e7771",
                        "lifetime": {
                            "finish": "2019-12-27 14:00:00",
                            "start": "2019-12-27 13:00:00"
                        },
                        "org": "5b04229196c055000d87c2b5",
                        "status": "public",
                        "timezone": "Europe/Moscow",
                        "title": {
                            "desc": "ацуа",
                            "text": "АЛЬФА_БАНК"
                        }
                    }
                },
                "partners": {
                    "5b04229196c055000d87c2b5": {
                        "id": "5b04229196c055000d87c2b5",
                        "name": "\"Έλληνας διοργανωτής\""
                    }
                },
                "promocodes": {},
                "sets": {}
            }
        }


.. seealso::

   :ref:`Заказ в статусе executed <extra/lifecycle/executed>`,
   :ref:`Жизненный цикл заказа <extra/lifecycle/begin>`



.. _walkthrough/order_create/tickets:

Резервирование билетов
======================

.. note::

   Все действия с заказом, кроме его создания, делаются по запросу :http:patch:`/v2/resources/orders/:id`.
   В один запрос одновременно может быть добавленно нескольно действий.
   Все запросы на изменение конкретного заказа, должны делаться синхронно.
   В случае получения запроса до конца обработки предыдущего,
   будет возвращена ошибка :http:statuscode:`409`.

   Это ограничение касается только работы с одним заказом,
   а работать одновременно с несколькими заказами можно.

За резервирование билетов отвечают три поля:

   - :ref:`tickets <walkthrough/order_create/ticket>`
   - :ref:`random <walkthrough/order_create/random>`
   - :ref:`all_or_nothing <walkthrough/order_create/all_or_nothing>`


.. _walkthrough/order_create/ticket:

Поле ``tickets``
----------------

В поле tickets передаются все `id` билетов, которые должны быть зарезервированы
текущим заказом. Если заказ изменяется (покупатель решил добавить ещё один билет),
то в обязательном порядке передаются все билеты,
которые должны быть в заказе (в т.ч. те, что уже зарезервированы).
Для удаления конкретного билета из заказа, нужно передать все билеты, кроме удаляемого.

.. warning:: 

   Нельзя использовать в одном запросе с :ref:`random <walkthrough/order_create/random>`.

**Запрос**

    .. http:patch:: /v2/resources/orders/:id

        :query tickets: список id билетов

**Пример запроса**

    .. sourcecode:: http

        PATCH /v2/resources/orders/5b0eab671b2042000ea83850 HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "tickets": [
                "5b0e8af09adc660001b0ab25",
                "5b0e8afa9adc660001b0ab6c"
            ]
        }


.. _walkthrough/order_create/random:

Поле ``random``
---------------

Поле random предназначено для резервирования случайных билетов из указанных категорий.
Оно нужно для того, чтобы добавлять в заказ билеты без мест.
Имеет вид объекта, где ключ является id категории, а значение — количество билетов.
Так же, как и в tickets, всегда нужно передавать желаемое состояние.
Т.е. если пользователь удалил один билет из категории,
то передать надо random со всеми категориями и количествами, только в одной из категорий будет на один билет меньше.
В ответе от сервера всегда будет список забронированных билетов в поле tickets.

.. warning::

   Нельзя использовать в одном запросе с :ref:`tickets <walkthrough/order_create/ticket>`.

**Запрос**

    .. http:patch:: /v2/resources/orders/:id

        :query random: массив: ключ -- id категории, значение -- кол-во мест

**Пример запроса**

    .. sourcecode:: http

        PATCH /v2/resources/orders/5d1b62074ed1c53b328ad4f0 HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "random": {
                "592841f8515e35002dead91e": 2
            }
        }


.. _walkthrough/order_create/all_or_nothing:

Поле ``all_or_nothing``
-----------------------

Если значение поля ``all_or_nothing`` равно ``true``, то резервируются либо все билеты, либо ни одного.

При изменении заказа с одновременным разрезервированием и резервированием билетов,
в случае неудачи с резервированием хотя бы одного билета, разрезервирования не происходит,
т.е. список зарезервированных билетов не изменяется.

Если значение не указано, или ``false``, то билеты,
которые не удалось забронировать пропускаются и
отсутствуют поле :ref:`tickets <walkthrough/order_create/ticket>` в ответе.

.. note::

   Можно использовать, как с ``tickets``, так и с ``random``
