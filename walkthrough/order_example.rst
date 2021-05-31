.. _walkthrough/order_example/begin:

========================
Пример проведения заказа
========================

.. note::

    С нуля создадим и проведем смешанный заказ: один билет с рассадкой, другой -- без.
    Будет два примера, отличающихся порядком добавления этих билетов.


0. :ref:`Получаем <walkthrough/events/simple>` информацию о событиях
====================================================================

На этом этапе выбираем мероприятие, на которое будем проводить заказ

    .. sourcecode:: http

        GET /v1/services/simple/events HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json


    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "age_rating": 12,
                "allow_other_ps": false,
                "created_at": "2019-09-05T16:15:18.618000+00:00",
                "deal": null,
                "id": "5d7134962110d30a34e95b96",
                "lifetime": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20200612T150000Z\r\nDTEND;VALUE=DATE-TIME:20200612T180000Z\r\nEND:VEVENT\r\n",
                "map": {
                    "desc": "",
                    "id": "5a8dd58d6e55b2064c67c141",
                    "name": "Cхема 21.02",
                    "sectors": [
                        {
                            "desc": "",
                            "id": "5a8dd58e6e55b2064c67c142",
                            "name": "A0"
                        },
                        {
                            "desc": "",
                            "id": "5a8dd58e6e55b2064c67c15c",
                            "name": "Танцевальный партер"
                        },
                        ...
                    ],
                    "svg": {
                        "map": {
                            "author": null,
                            "content_type": "image/svg+xml",
                            "id": "5a8dd5976e55b2064c67c192",
                            "length": null,
                            "md5hash": "d4a00e67a129fb2782e518fdc084bdab",
                            "url": "https://ticketscloud.com/s3/media.ticketscloud/production/map/2018-02/5a8dd58d6e55b2064c67c141-5a8dd58d6e55b2064c67c140-Megasport.svg"
                        },
                        ...
                    }
                },
                "media": {},
                "org": {
                    ...
                },
                "partner": {
                    ...
                },
                "sets": [
                    {
                        "amount": 250,
                        "amount_vacant": 248,
                        "desc": "",
                        "id": "5d7135112110d30a34e97e2d",
                        "name": "Фан зона",
                        "pos": 0,
                        "price": "5600.00",
                        "price_extra": "0.00",
                        "price_org": "5600.00",
                        "rules": [
                            {
                                "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20190903T210000Z\r\nDTEND;VALUE=DATE-TIME:20200612T180000Z\r\nEND:VEVENT\r\n",
                                "current": true,
                                "id": "5d7135112110d30a34e97e2c",
                                "price": "5600.00",
                                "price_extra": "0.00",
                                "price_org": "5600.00"
                            }
                        ],
                        "seats": null,
                        "sector": "5a8dd58e6e55b2064c67c15d",
                        "with_seats": false
                    },
                    {
                        "amount": 310,
                        "amount_vacant": 162,
                        "desc": "",
                        "id": "5d71353b2110d30a34e97e31",
                        "name": "A2",
                        "pos": 0,
                        "price": "990.00",
                        "price_extra": "0.00",
                        "price_org": "990.00",
                        "rules": [
                            {
                                "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20190903T210000Z\r\nDTEND;VALUE=DATE-TIME:20200612T180000Z\r\nEND:VEVENT\r\n",
                                "current": true,
                                "id": "5d71353b2110d30a34e97e30",
                                "price": "990.00",
                                "price_extra": "0.00",
                                "price_org": "990.00"
                            }
                        ],
                        "seats": {
                            "1": [
                                [
                                    1,
                                    8
                                ],
                                [
                                    13,
                                    23
                                ]
                            ],
                            ...
                        },
                        "sector": "5a8dd58e6e55b2064c67c144",
                        "with_seats": true
                    },
                    ...
                ],
                "status": "public",
                "tags": [
                    "Бизнес"
                ],
                "ticket_template": {
                    "fan_cover_url": null,
                    "name": null,
                    "text_color": null
                },
                "tickets_amount": 6747,
                "tickets_amount_vacant": 6541,
                "title": {
                    "desc": "ref",
                    "text": "Slipknot"
                },
                "updated_at": "2019-09-18T10:13:21.827000+00:00",
                "venue": {
                    "address": "Ходынский б-р, 3",
                    "city": {
                        "country": "RU",
                        "id": 524901,
                        "name": {
                            "af": "Moskou",
                            ...
                        },
                        "timezone": "Europe/Moscow"
                    },
                    "country": {
                        "id": "RU",
                        "name": {
                            "be": "Расійская Федэрацыя",
                            "default": "Russia",
                            "en": "Russia",
                            ...
                        }
                    },
                    "desc": "",
                    "id": "58595d0f515e3500141a0c50",
                    "name": "Дворец Спорта \"Мегаспорт\"",
                    "point": {
                        "coordinates": [
                            37.539649000000054,
                            55.786475
                        ],
                        "type": "Point"
                    }
                }
            },
            ...
        ]


1. :ref:`Получаем <walkthrough/events/tickets>` информацию о билетах
====================================================================

Взяв id события из п.0, получаем его места (можно использовать :ref:`фильтры <walkthrough/events/tickets>`)

    .. sourcecode:: http

        GET /v1/resources/events/5d7134962110d30a34e95b96/tickets HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json


    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "id": "5d7134962110d30a34e95e06",
                "number": 136094,
                "reserved_till": null,
                "seat": {
                    "number": 9,
                    "row": 17,
                    "sector": "5a8dd58e6e55b2064c67c144"
                },
                "serial": "EOY",
                "set": "5d71353b2110d30a34e97e31",
                "status": "reserved"
            },
            {
                "id": "5d7134962110d30a34e95dfb",
                "number": 136083,
                "reserved_till": null,
                "seat": {
                    "number": 9,
                    "row": 16,
                    "sector": "5a8dd58e6e55b2064c67c144"
                },
                "serial": "EOY",
                "set": "5d71353b2110d30a34e97e31",
                "status": "sold"
            },
            {
                "id": "5d7134962110d30a34e95cfe",
                "number": 135830,
                "reserved_till": null,
                "seat": {
                    "number": 14,
                    "row": 2,
                    "sector": "5a8dd58e6e55b2064c67c144"
                },
                "serial": "EOY",
                "set": "5d71353b2110d30a34e97e31",
                "status": "vacant"
            },
            ...
        ]


2a. Создаем заказ (добавляем билет :ref:`без места <walkthrough/order_create/random>`)
======================================================================================

Берем id добавляемого сета из п.0

    .. sourcecode:: http

        POST /v2/resources/orders HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "event": "5d7134962110d30a34e95b96",
            "random": {
                "5d7135112110d30a34e97e2d": 1
            }
        }


    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "created_at": "2019-09-25 16:14:01",
                "event": "5d7134962110d30a34e95b96",
                "expired_after": "2019-09-25 16:29:01",
                "id": "5d8b924971a0bf323bd6a6ed",
                "number": 59743,
                "org": "5ba10ea90c43fc000b0fc786",
                "origin": "api",
                "status": "executed",
                "tickets": [
                    {
                        "barcode": null,
                        "discount": "0.00",
                        "extra": "560.00",
                        "full": "6160.00",
                        "id": "5d7135113f18da51a186ad16",
                        "nominal": "5600.00",
                        "number": 168475,
                        "price": "5600.00",
                        "serial": "PYX",
                        "set": "5d7135112110d30a34e97e2d",
                        "status": "reserved"
                    }
                ],
                "values": {
                    "discount": "0.00",
                    "extra": "560.00",
                    "full": "6160.00",
                    "nominal": "5600.00",
                    "price": "5600.00",
                    "sets_values": {
                        "5d713505255895db3c30b0c5": {
                            "discount": "0.00",
                            "id": "5d713505255895db3c30b0c5",
                            "nominal": "6666.00",
                            "price": "6666.00",
                            "promocode": null
                        },
                        ...
                    },
                    "viral_promocodes": []
                },
                "vendor": "5ba10ea90c43fc000b0fc786",
            },
            "refs": {
                "events": {
                    "5d7134962110d30a34e95b96": {
                        "id": "5d7134962110d30a34e95b96",
                        "lifetime": {
                            "finish": "2020-06-12 18:00:00",
                            "start": "2020-06-12 15:00:00"
                        },
                        "org": "5ba10ea90c43fc000b0fc786",
                        "status": "public",
                        "timezone": "Europe/Moscow",
                        "title": {
                            "desc": "ref",
                            "text": "Slipknot"
                        }
                    }
                },
                "partners": {
                    "5ba10ea90c43fc000b0fc786": {
                        "id": "5ba10ea90c43fc000b0fc786",
                        "name": "Тест VK Pay"
                    }
                },
                "promocodes": {},
                "sets": {
                    "5d7135112110d30a34e97e2d": {
                        "id": "5d7135112110d30a34e97e2d",
                        "name": "Фан зона",
                        "price": "5600.00",
                        "with_seats": false
                    }
                }
            }
        }


3a. Заполняем заказ (добавляем билет :ref:`с местом <walkthrough/order_create/ticket>`)
=======================================================================================

Берем id добавляемого места из п.1, но при этом еще добавляем id билета, полученного в ответе из п.2a

    .. sourcecode:: http

        PATCH /v2/resources/orders/5d8b924971a0bf323bd6a6ed HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "tickets": [
                "5d7135113f18da51a186ad16",
                "5d7134962110d30a34e95cfe"
            ]
        }


    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "created_at": "2019-09-25 16:14:01",
                "event": "5d7134962110d30a34e95b96",
                "expired_after": "2019-09-25 16:29:01",
                "id": "5d8b924971a0bf323bd6a6ed",
                "number": 59743,
                "org": "5ba10ea90c43fc000b0fc786",
                "origin": "api",
                "status": "executed",
                "tickets": [
                    {
                        "barcode": null,
                        "discount": "0.00",
                        "extra": "560.00",
                        "full": "6160.00",
                        "id": "5d7135113f18da51a186ad16",
                        "nominal": "5600.00",
                        "number": 168475,
                        "price": "5600.00",
                        "serial": "PYX",
                        "set": "5d7135112110d30a34e97e2d",
                        "status": "reserved"
                    },
                    {
                        "barcode": null,
                        "discount": "0.00",
                        "extra": "99.00",
                        "full": "1089.00",
                        "id": "5d7134962110d30a34e95cfe",
                        "nominal": "990.00",
                        "number": 135830,
                        "price": "990.00",
                        "seat": {
                            "number": "14",
                            "row": "2",
                            "sector": "5a8dd58e6e55b2064c67c144"
                        },
                        "serial": "EOY",
                        "set": "5d71353b2110d30a34e97e31",
                        "status": "reserved"
                    }
                ],
                "values": {
                    "discount": "0.00",
                    "extra": "659.00",
                    "full": "7249.00",
                    "nominal": "6590.00",
                    "price": "6590.00",
                    "sets_values": {
                        "5d713505255895db3c30b0c5": {
                            "discount": "0.00",
                            "id": "5d713505255895db3c30b0c5",
                            "nominal": "6666.00",
                            "price": "6666.00",
                            "promocode": null
                        },
                        ...
                    },
                    "viral_promocodes": []
                },
                "vendor": "5ba10ea90c43fc000b0fc786",
            },
            "refs": {
                "events": {
                    "5d7134962110d30a34e95b96": {
                        "id": "5d7134962110d30a34e95b96",
                        "lifetime": {
                            "finish": "2020-06-12 18:00:00",
                            "start": "2020-06-12 15:00:00"
                        },
                        "org": "5ba10ea90c43fc000b0fc786",
                        "status": "public",
                        "timezone": "Europe/Moscow",
                        "title": {
                            "desc": "ref",
                            "text": "Slipknot"
                        }
                    }
                },
                "partners": {
                    "5ba10ea90c43fc000b0fc786": {
                        "id": "5ba10ea90c43fc000b0fc786",
                        "name": "Тест VK Pay"
                    }
                },
                "promocodes": {},
                "sets": {
                    "5d7135112110d30a34e97e2d": {
                        "id": "5d7135112110d30a34e97e2d",
                        "name": "Фан зона",
                        "price": "5600.00",
                        "with_seats": false
                    },
                    "5d71353b2110d30a34e97e31": {
                        "id": "5d71353b2110d30a34e97e31",
                        "name": "A2",
                        "price": "990.00",
                        "with_seats": true
                    }
                }
            }
        }


2b. Создаем заказ (добавляем билет :ref:`с местом <walkthrough/order_create/ticket>`)
=====================================================================================

Берем id добавляемого места из п.1

    .. sourcecode:: http

        POST /v2/resources/orders/5d8b924971a0bf323bd6a6ed HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "tickets": [
                "5d7134962110d30a34e95cfe"
            ]
        }


    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "created_at": "2019-09-25 16:14:01",
                "event": "5d7134962110d30a34e95b96",
                "expired_after": "2019-09-25 16:29:01",
                "id": "5d8b924971a0bf323bd6a6ed",
                "number": 59743,
                "org": "5ba10ea90c43fc000b0fc786",
                "origin": "api",
                "status": "executed",
                "tickets": [
                    {
                        "barcode": null,
                        "discount": "0.00",
                        "extra": "99.00",
                        "full": "1089.00",
                        "id": "5d7134962110d30a34e95cfe",
                        "nominal": "990.00",
                        "number": 135830,
                        "price": "990.00",
                        "seat": {
                            "number": "14",
                            "row": "2",
                            "sector": "5a8dd58e6e55b2064c67c144"
                        },
                        "serial": "EOY",
                        "set": "5d71353b2110d30a34e97e31",
                        "status": "reserved"
                    }
                ],
                "values": {
                    "discount": "0.00",
                    "extra": "659.00",
                    "full": "7249.00",
                    "nominal": "6590.00",
                    "price": "6590.00",
                    "sets_values": {
                        "5d713505255895db3c30b0c5": {
                            "discount": "0.00",
                            "id": "5d713505255895db3c30b0c5",
                            "nominal": "6666.00",
                            "price": "6666.00",
                            "promocode": null
                        },
                        ...
                    },
                    "viral_promocodes": []
                },
                "vendor": "5ba10ea90c43fc000b0fc786",
            },
            "refs": {
                "events": {
                    "5d7134962110d30a34e95b96": {
                        "id": "5d7134962110d30a34e95b96",
                        "lifetime": {
                            "finish": "2020-06-12 18:00:00",
                            "start": "2020-06-12 15:00:00"
                        },
                        "org": "5ba10ea90c43fc000b0fc786",
                        "status": "public",
                        "timezone": "Europe/Moscow",
                        "title": {
                            "desc": "ref",
                            "text": "Slipknot"
                        }
                    }
                },
                "partners": {
                    "5ba10ea90c43fc000b0fc786": {
                        "id": "5ba10ea90c43fc000b0fc786",
                        "name": "Тест VK Pay"
                    }
                },
                "promocodes": {},
                "sets": {
                    "5d71353b2110d30a34e97e31": {
                        "id": "5d71353b2110d30a34e97e31",
                        "name": "A2",
                        "price": "990.00",
                        "with_seats": true
                    }
                }
            }
        }


3b. Заполняем заказ (добавляем билет :ref:`без места <walkthrough/order_create/random>`)
========================================================================================

Берем id добавляемого сета из п.2b (или из п.0), но при этом еще дописываем id сета от добавленного билета из п.2

    .. sourcecode:: http

        POST /v2/resources/orders HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "random": {
                "5d71353b2110d30a34e97e31": 1,
                "5d7135112110d30a34e97e2d": 1
            }
        }


4. :ref:`Завершаем <walkthrough/order_finish/begin>` заказ
==========================================================

    .. sourcecode:: http

        PATCH /v2/resources/orders/5d8b924971a0bf323bd6a6ed HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "status": "done"
        }


    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "code": "lw4bbl0o",
                "created_at": "2019-09-25 16:14:01",
                "done_at": "2019-09-25 16:20:40",
                "event": "5d7134962110d30a34e95b96",
                "expired_after": "2019-09-25 16:29:01",
                "id": "5d8b924971a0bf323bd6a6ed",
                "number": 59743,
                "org": "5ba10ea90c43fc000b0fc786",
                "origin": "api",
                "status": "done",
                "tickets": [
                    {
                        "barcode": "67454655075047921",
                        "discount": "0.00",
                        "extra": "560.00",
                        "full": "6160.00",
                        "id": "5d7135113f18da51a186ad16",
                        "nominal": "5600.00",
                        "number": 168475,
                        "price": "5600.00",
                        "serial": "PYX",
                        "set": "5d7135112110d30a34e97e2d",
                        "status": "reserved"
                    },
                    {
                        "barcode": "35348364979141729",
                        "discount": "0.00",
                        "extra": "99.00",
                        "full": "1089.00",
                        "id": "5d7134962110d30a34e95cfe",
                        "nominal": "990.00",
                        "number": 135830,
                        "price": "990.00",
                        "seat": {
                            "number": "14",
                            "row": "2",
                            "sector": "5a8dd58e6e55b2064c67c144"
                        },
                        "serial": "EOY",
                        "set": "5d71353b2110d30a34e97e31",
                        "status": "reserved"
                    }
                ],
                "values": {
                    "discount": "0.00",
                    "extra": "659.00",
                    "full": "7249.00",
                    "nominal": "6590.00",
                    "price": "6590.00",
                    "sets_values": {
                        "5d713505255895db3c30b0c5": {
                            "discount": "0.00",
                            "id": "5d713505255895db3c30b0c5",
                            "nominal": "6666.00",
                            "price": "6666.00",
                            "promocode": null
                        },
                        ...
                    },
                    "viral_promocodes": []
                },
                "vendor": "5ba10ea90c43fc000b0fc786",
            },
            "refs": {
                "events": {
                    "5d7134962110d30a34e95b96": {
                        "id": "5d7134962110d30a34e95b96",
                        "lifetime": {
                            "finish": "2020-06-12 18:00:00",
                            "start": "2020-06-12 15:00:00"
                        },
                        "org": "5ba10ea90c43fc000b0fc786",
                        "status": "public",
                        "timezone": "Europe/Moscow",
                        "title": {
                            "desc": "ref",
                            "text": "Slipknot"
                        }
                    }
                },
                "partners": {
                    "5ba10ea90c43fc000b0fc786": {
                        "id": "5ba10ea90c43fc000b0fc786",
                        "name": "Тест VK Pay"
                    }
                },
                "promocodes": {},
                "sets": {
                    "5d7135112110d30a34e97e2d": {
                        "id": "5d7135112110d30a34e97e2d",
                        "name": "Фан зона",
                        "price": "5600.00",
                        "with_seats": false
                    },
                    "5d71353b2110d30a34e97e31": {
                        "id": "5d71353b2110d30a34e97e31",
                        "name": "A2",
                        "price": "990.00",
                        "with_seats": true
                    }
                }
            }
        }


**Возможные ошибки при работе с заказом**
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
| Not allow to update order in status <status>         | нельзя менять заказ в статусе: <status>                |
+------------------------------------------------------+--------------------------------------------------------+
| Allow update the only status to cancelled            | разрешено только отменить заказ                        |
+------------------------------------------------------+--------------------------------------------------------+
| expired_after is not changable                       | время жизни не может быть изменено                     |
+------------------------------------------------------+--------------------------------------------------------+
| max expired_after is {dt}                            | время жизни истекло <dt :%Y-%m-%d %H:%M:%S>            |
+------------------------------------------------------+--------------------------------------------------------+
| only org can send invitations                        | только организатор может отправлять приглашения        |
+------------------------------------------------------+--------------------------------------------------------+
| invitation can send from control panel or            | приглашения можно отправить только из ЛК или из кассы  |
| salespoint only                                      |                                                        |
+------------------------------------------------------+--------------------------------------------------------+
| Courier must set only with salespoint                | запрос должен быть только из кассы                     |
+------------------------------------------------------+--------------------------------------------------------+
| Kryptonite integrations is disabled                  | интеграция с криптонитом выключена                     |
+------------------------------------------------------+--------------------------------------------------------+
| Cant set smart_tickets to false while kriptonite     | нельзя выключить "криптобилеты" пока выбрана интеграция|
| integration option is only smart_tickets             | "только криптобилеты"                                  |
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
| Not enough money, сontact to TicketsCloud manager    | недостаточно денег, свяжитесь с менеджером TicketsCloud|
+------------------------------------------------------+--------------------------------------------------------+
| there is no tickets in order                         | в заказе нет ни одного билета                          |
+------------------------------------------------------+--------------------------------------------------------+
| Incorrect status <status> for this operation         | нельзя выполнить перевод заказа в статус: <status>     |
+------------------------------------------------------+--------------------------------------------------------+
| Order <order_id> is not cancellable                  | заказ с id: <order_id> не может быть отменен           |
+------------------------------------------------------+--------------------------------------------------------+
