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

    .. http:post:: /v2/resources/orders

        :jsonparam event: Обязателен


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
                "event": objectid
                "number": int
                "org": objectid
                "origin": 'api' | 'salespoint' | 'widget' | 'control_panel'
                "promocodes": [
                    str
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
                        "venue": objectid
                        "age_rating": int
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
                            "percentage" | "fix": str
                        },
                        "id": objectid
                        "lifetime": {
                            "start": isodatetime
                            "finish": isodatetime
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
                },
                "venues": {
                    id: {
                        "address": str
                        "city": {
                            "_id": int,
                            "name": {
                                "default": str
                                "en": str
                                "ru": str
                            },
                            "timezone": str
                        },
                        "country": {
                            "_id": str
                            "name": {
                                "default": str
                                "en": str
                                "ru": str
                            }
                        },
                        "desc": str
                        "id": objectid
                        "name": str
                    }
                }
            }
        }


**Пример запроса**

    .. sourcecode:: http

        POST /v2/resources/orders HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "event": "5d31fbdd27649b0dff076117"
        }

**Пример ответа**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "created_at": "2019-07-25 14:41:11",
                "event": "5d31fbdd27649b0dff076117",
                "expired_after": "2019-07-25 14:56:11",
                "id": "5d39bf878cd381a4891e07b7",
                "number": 54877,
                "org": "5b04229196c055000d87c2b5",
                "origin": "api",
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
                        "5d31fbfa27649b0dff07611b": {
                            "discount": "0.00",
                            "id": "5d31fbfa27649b0dff07611b",
                            "nominal": "150.00",
                            "price": "150.00",
                            "promocode": null
                        },
                        "5d31fbfa8a75c12c9d64de13": {
                            "discount": "0.00",
                            "id": "5d31fbfa8a75c12c9d64de13",
                            "nominal": "1050.00",
                            "price": "1050.00",
                            "promocode": null
                        }
                    },
                    "viral_promocodes": []
                },
                "vendor": "5b02d6e9517565000d9cb1ce",
                "vendor_data": {}
            },
            "refs": {
                "events": {
                    "5d31fbdd27649b0dff076117": {
                        "id": "5d31fbdd27649b0dff076117",
                        "lifetime": {
                            "finish": "2019-08-28 21:50:00",
                            "start": "2019-08-15 21:20:00"
                        },
                        "org": "5b04229196c055000d87c2b5",
                        "status": "public",
                        "timezone": "Europe/Moscow",
                        "title": {
                            "desc": "1",
                            "text": "1234567890"
                        },
                        "age_rating": 16,
                        "venue": "552322649cb5384154e028b2"
                    }
                },
                "partners": {
                    "5b02d6e9517565000d9cb1ce": {
                        "id": "5b02d6e9517565000d9cb1ce",
                        "name": "Rasp new"
                    },
                    "5b04229196c055000d87c2b5": {
                        "id": "5b04229196c055000d87c2b5",
                        "name": "My best org"
                    }
                },
                "promocodes": {},
                "sets": {},
                "venues": {
                    "552322649cb5384154e028b2": {
                        "address": "ул. Родионова, 4",
                        "city": {
                            "_id": 520555,
                            "name": {
                                "default": "Nizhniy Novgorod",
                                "en": "Nizhny Novgorod",
                                "ru": "Нижний Новгород"
                            },
                            "timezone": "Europe/Moscow"
                        },
                        "country": {
                            "_id": "RU",
                            "name": {
                                "default": "Russia",
                                "en": "Russia",
                                "ru": "Россия"
                            }
                        },
                        "desc": "MILO Concert Hall - новая большая профессиональная площадка в Нижнем Новгороде",
                        "id": "552322649cb5384154e028b2",
                        "name": "MILO Concert Hall"
                    }
                }
            }
        }

.. note::

   ШК появляется только у заказа в статусе ``done``


.. seealso::

   :ref:`Заказ в статусе executed <extra/lifecycle/executed>`,
   :ref:`Жизненный цикл заказа <extra/lifecycle/begin>`



**Возможные ошибки при создании заказа**
    При ошибках возвращается список текстовых сообщений:

    .. sourcecode:: http

        HTTP/1.1 400
        Content-Type: application/json

        {
            "errors": [
                "Event <event_id> not found"
            ]
        }

+------------------------------------------------------+--------------------------------------------------------+
| Сообщение                                            | Причина                                                |
+======================================================+========================================================+
| Event <event_id> not found                           | не найдено мероприятие для заказа                      |
+------------------------------------------------------+--------------------------------------------------------+
| Deal not found                                       | не найдена сделка                                      |
+------------------------------------------------------+--------------------------------------------------------+
| Promokey needed                                      | промоключ должен быть                                  |
+------------------------------------------------------+--------------------------------------------------------+
| Promokey not founded                                 | промоключ не найден                                    |
+------------------------------------------------------+--------------------------------------------------------+
| Promokey expired                                     | промоключ истек                                        |
+------------------------------------------------------+--------------------------------------------------------+
| Promokey fully reserved                              | промоключ полностью зарезервирован                     |
+------------------------------------------------------+--------------------------------------------------------+
| Promokey already reserved                            | промоключ уже зарезервирован                           |
+------------------------------------------------------+--------------------------------------------------------+
| Only one of tickets or random can be set             | только один: tickets или random может быть установлено |
+------------------------------------------------------+--------------------------------------------------------+
| 'tickets' or 'random' must be                        | обязан быть: tickets или random                        |
+------------------------------------------------------+--------------------------------------------------------+
| Cant use promocode when event have promotion         | нельзя использовать промокод, пока                     |
|                                                      | на мероприятии действует промоакция                    |
+------------------------------------------------------+--------------------------------------------------------+
| expired_after is not changable                       | время жизни не может быть изменено                     |
+------------------------------------------------------+--------------------------------------------------------+
| max expired_after is {dt}                            | время жизни истекло <dt :%Y-%m-%d %H:%M:%S>            |
+------------------------------------------------------+--------------------------------------------------------+
| Promokey needed to add these tickets                 | необходим промоключ, чтобы добавить эти билеты         |
+------------------------------------------------------+--------------------------------------------------------+
| ticket (id = {}) does not belong to current event    | билет не относится к текущему мероприятию              |
+------------------------------------------------------+--------------------------------------------------------+
| value should be formatted 'YYYY-MM-DD'               | для дополнительного поля "Дата",                       |
|                                                      | значение имеет неверный формат                         |
+------------------------------------------------------+--------------------------------------------------------+
| value should be True or False                        | для дополнительного поля "Галочка",                    |
|                                                      | значение должно быть булевым                           |
+------------------------------------------------------+--------------------------------------------------------+
| value is not a list                                  | для дополнительного поля "Выбор нескольких вариантов", |
|                                                      | значение должно быть списком                           |
+------------------------------------------------------+--------------------------------------------------------+
| list length is less than <len>                       | для дополнительного поля "Выбор нескольких вариантов", |
|                                                      | значение должно быть длиннее чем <len>                 |
+------------------------------------------------------+--------------------------------------------------------+
| list length is greater than <len>                    | для дополнительного поля "Выбор нескольких вариантов", |
|                                                      | значение должно быть короче чем <len>                  |
+------------------------------------------------------+--------------------------------------------------------+
| value is less than <value>                           | для дополнительного поля "Выбор одного варианта",      |
|                                                      | значение должно быть больше чем <value>                |
+------------------------------------------------------+--------------------------------------------------------+
| value is greater than <value>                        | для дополнительного поля "Выбор одного варианта",      |
|                                                      | значение должно быть меньше чем <value>                |
+------------------------------------------------------+--------------------------------------------------------+
| value should be less than <value>                    | для дополнительного поля "Выбор одного варианта",      |
|                                                      | значение должно быть меньше либо равно <value>         |
+------------------------------------------------------+--------------------------------------------------------+
| value should be greater than <value>                 | для дополнительного поля "Выбор одного варианта",      |
|                                                      | значение должно быть больше либо равно <value>         |
+------------------------------------------------------+--------------------------------------------------------+
| value is not a string                                | для дополнительного поля "Текст/Длинный текст",        |
|                                                      | значение должно быть представлено строкой              |
+------------------------------------------------------+--------------------------------------------------------+
| blank value is not allowed                           | для дополнительного поля "Текст/Длинный текст",        |
|                                                      | значение не должно быть пустым                         |
+------------------------------------------------------+--------------------------------------------------------+
| String is shorter than <len> characters              | для дополнительного поля "Текст/Длинный текст",        |
|                                                      | значение должно быть длиннее <len> символов            |
+------------------------------------------------------+--------------------------------------------------------+
| String is longer than <len> characters               | для дополнительного поля "Текст/Длинный текст",        |
|                                                      | значение должно быть короче <len> символов             |
+------------------------------------------------------+--------------------------------------------------------+
| does not match pattern <pattern>                     | для дополнительного поля "Текст/Длинный текст",        |
|                                                      | значение должно соответствовать формату <pattern>      |
+------------------------------------------------------+--------------------------------------------------------+

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

        :jsonparam tickets: список id билетов

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

        :jsonparam random: массив: ключ -- id категории, значение -- кол-во мест

**Пример запроса**

    .. sourcecode:: http

        PATCH /v2/resources/orders HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "random": {
                "5d31fbfa27649b0dff07611b": 1
            }
        }

**Пример ответа**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "created_at": "2019-07-25 14:41:11",
                "event": "5d31fbdd27649b0dff076117",
                "expired_after": "2019-07-25 14:56:11",
                "id": "5d39bf878cd381a4891e07b7",
                "number": 54877,
                "org": "5b04229196c055000d87c2b5",
                "origin": "api",
                "settings": {
                    "invitation": false,
                    "send_tickets": false,
                    "subscribe_agree": false
                },
                "status": "executed",
                "tickets": [
                    {
                        "barcode": null,
                        "discount": "0.00",
                        "extra": "6.00",
                        "full": "156.00",
                        "id": "5d31fbfb306fdcc187b91179",
                        "nominal": "150.00",
                        "number": 157495,
                        "price": "150.00",
                        "serial": "OOX",
                        "set": "5d31fbfa27649b0dff07611b",
                        "status": "reserved"
                    }
                ],
                "values": {
                    "discount": "0.00",
                    "extra": "6.00",
                    "full": "156.00",
                    "nominal": "150.00",
                    "price": "150.00",
                    "sets_values": {
                        "5d31fbfa27649b0dff07611b": {
                            "discount": "0.00",
                            "id": "5d31fbfa27649b0dff07611b",
                            "nominal": "150.00",
                            "price": "150.00",
                            "promocode": null
                        },
                        "5d31fbfa8a75c12c9d64de13": {
                            "discount": "0.00",
                            "id": "5d31fbfa8a75c12c9d64de13",
                            "nominal": "1050.00",
                            "price": "1050.00",
                            "promocode": null
                        }
                    },
                    "viral_promocodes": []
                },
                "vendor": "5b02d6e9517565000d9cb1ce",
                "vendor_data": {}
            },
            "refs": {
                "events": {
                    "5d31fbdd27649b0dff076117": {
                        "id": "5d31fbdd27649b0dff076117",
                        "lifetime": {
                            "finish": "2019-08-28 21:50:00",
                            "start": "2019-08-15 21:20:00"
                        },
                        "org": "5b04229196c055000d87c2b5",
                        "status": "public",
                        "timezone": "Europe/Moscow",
                        "title": {
                            "desc": "1",
                            "text": "1234567890"
                        }
                    }
                },
                "partners": {
                    "5b02d6e9517565000d9cb1ce": {
                        "id": "5b02d6e9517565000d9cb1ce",
                        "name": "Rasp new"
                    },
                    "5b04229196c055000d87c2b5": {
                        "id": "5b04229196c055000d87c2b5",
                        "name": "My best org"
                    }
                },
                "sets": {
                    "5d31fbfa27649b0dff07611b": {
                        "id": "5d31fbfa27649b0dff07611b",
                        "name": "обычные",
                        "price": "150.00",
                        "with_seats": false
                    }
                }
            }
        }

.. note::

   Хотя ``tickets`` и ``random`` нельзя использовать в одном запросе, передать все билеты можно.
   
   Алгоритм такой:
   
   - Запрос с ``random``.

   - Получить из ответа id билетов в поле ``tickets``.

   - Расширить список полученных id новым билетом.

   - Отправить запрос с полем ``tickets``, заполненным списком id билетов.

   - Проверить в ответе, что всё забронировалось корректно.


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
