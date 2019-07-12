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
                "custom_fields": {
                    ...
                },
                "event": "5b23b53b9c9b19000c6c4180",
                "expired_after": "2018-11-16 00:00:00",
                "id": "5bacf64ea0eb2f000c45160a",
                "number": 41564,
                "org": "5b0286ce517565000d9cb1ca",
                "origin": "api",
                "payments": [],
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
                "custom_fields": {
                    "order": [],
                    "tickets": []
                },
                "event": "5b23b53b9c9b19000c6c4180",
                "expired_after": "2018-11-16 00:00:00",
                "id": "5bacf64ea0eb2f000c45160a",
                "number": 41564,
                "org": "5b0286ce517565000d9cb1ca",
                "origin": "api",
                "payments": [],
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
                "custom_fields": {
                    "order": [],
                    "tickets": []
                },
                "event": "5b23b53b9c9b19000c6c4180",
                "expired_after": "2018-11-16 00:00:00",
                "id": "5bacf64ea0eb2f000c45160a",
                "number": 41564,
                "org": "5b0286ce517565000d9cb1ca",
                "origin": "api",
                "payments": [],
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

    .. http:post:: /v2/resources/orders/:id

        :query promocodes: (list of string)

**Ответ**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

    :ref:`Объект заказа <walkthrough/order_create/object>`

.. warning::

    Успешность применения промокода не влияет на код ответа, и его оценить
    можно по тому, что значение поля ``promocodes`` изменилось

**Пример запроса**

    .. sourcecode:: http

        PATCH /v2/resources/orders/5bacf64ea0eb2f000c45160a HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "promocodes": [
                "TOP50"
            ]
        }

**Пример ответа**

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "created_at": "2018-09-27 15:25:02",
                "custom_fields": {
                    "order": [],
                    "tickets": []
                },
                "event": "5b23b53b9c9b19000c6c4180",
                "expired_after": "2018-11-16 00:00:00",
                "id": "5bacf64ea0eb2f000c45160a",
                "number": 41564,
                "org": "5b0286ce517565000d9cb1ca",
                "origin": "api",
                "payments": [],
                "promocodes": ["TOP50"],
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
                    ...
                }
            },
            "refs": {
                ...
            }
        }
