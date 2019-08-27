.. _extra/orders_list/begin:

=========================
Работа со списком заказов
=========================


.. _extra/orders_list/get:

Получение списка заказов
==========================

.. _extra/orders_list/get_params:

**Запрос**

.. http:get:: /v2/resources/orders

    :query created_at: Дата создания заказа в формате ISO от и до, через запятую
    :query status: Список статусов заказа
    :query events: Список мероприятий
    :query only_with_customer: ``bool``; Если ``true`` -- Показываем заказы, только если есть кастомер
    :query page: Порядковый номер страницы результатов запроса
    :query page_size: Кол-во записей на страницу результатов запроса


**Ответ**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

    Список :ref:`объектов заказа <walkthrough/order_create/object>`


**Пример запроса**

    .. sourcecode:: http

        GET /v2/resources/orders?status=done,cancelled&created_at=2000-07-28T13:00:00,2020-07-28T13:00:00 HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d


**Пример ответа**

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": [
                {
                    "code": "97elgi8j",
                    "created_at": "2019-07-25 14:56:16",
                    "done_at": "2019-07-25 14:57:47",
                    "event": "5d31fbdd27649b0dff076117",
                    "expired_after": "2019-07-25 15:11:16",
                    "id": "5d39c3108cd381a4891e07e0",
                    "number": 54881,
                    "org": "5b04229196c055000d87c2b5",
                    "origin": "api",
                    "promocodes": [],
                    "settings": {
                        "invitation": false,
                        "send_tickets": false,
                        "subscribe_agree": false
                    },
                    "status": "done",
                    "tickets": [
                        {
                            "barcode": "17174251182011730",
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
                ...
            ],
            "pagination": {
                "page": 1,
                "page_size": 50,
                "total": 1
            },
            "refs": {
                "events": {
                    "5c13b5b1867efb000be1ebd7": {
                        "id": "5c13b5b1867efb000be1ebd7",
                        "lifetime": {
                            "finish": "2019-08-31 16:00:00",
                            "start": "2019-08-31 15:00:00"
                        },
                        "org": "5ba10ea90c43fc000b0fc786",
                        "status": "public",
                        "timezone": "Europe/Moscow",
                        "title": {
                            "desc": "ауц",
                            "text": "KoЯn"
                        }
                    },
                    ...
                },
                "partners": {
                    "5b02d6e9517565000d9cb1ce": {
                        "id": "5b02d6e9517565000d9cb1ce",
                        "name": "Rasp new"
                    },
                    "5b04229196c055000d87c2b5": {
                        "id": "5b04229196c055000d87c2b5",
                        "name": "My best org"
                    },
                    "5ba10ea90c43fc000b0fc786": {
                        "id": "5ba10ea90c43fc000b0fc786",
                        "name": "Тест VK Pay"
                    },
                    "5bb333389049ea000d2ba9c7": {
                        "id": "5bb333389049ea000d2ba9c7",
                        "name": "Newbie"
                    }
                },
            }
        }


.. _extra/orders_list/send_to_email:

Отправка списка заказов на почту
=====================================


**Описание параметров:**

**Запрос**

.. http:get:: /v2/resources/orders/export

    :query created_at: Дата создания заказа в формате ISO от и до, через запятую
    :query status: Список статусов заказа
    :query events: Список мероприятий
    :query only_with_customer: ``bool``; Если ``true`` -- Показываем заказы, только если есть кастомер
    :query email: Обязательно


**Ответ**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Length: 0
        Content-Type: text/html; charset=UTF-8

**Пример запроса**

    .. sourcecode:: http

        POST /v2/resources/orders/export HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "created_at": "2000-07-28T13:00:00,2020-07-28T13:00:00",
            "email": "hello@world.hello",
            "status": [
                "done",
                "cancelled"
            ]
        }
