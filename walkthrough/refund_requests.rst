.. _walkthrough/refund_requests/begin:

=====================
Шаг 4: Возврат заказа
=====================


.. _walkthrough/refund_requests/create:

Создание возврата
=================

**Запрос**

    .. http:post:: /v2/resources/refund_requests/

       :jsonparam order: Id заказа
       :jsonparam culprit: Виновник возврата (``user`` | ``org``)
       :jsonparam tickets: Список id билетов для возврата
       :jsonparam requested_at: Дата и время заявки на возврат. Необязательный параметр.


**Ответ**

.. _walkthrough/refund_requests/object:

Объект возврата

    .. sourcecode:: js

       {
           "data": {
               "id": objectid,
               "status": "new" | "in_progress" | "approved" | "rejected",
               "culprit": "user" | "org",
               "created_at": ISODatetime,
               "finished_at": ISODatetime,
               "requested_at": ISODatetime,
               "refund_nominal": money // сумма возврата
               "delta": money // Устарело. Необходимо использовать `refund_nominal`,
               "event": objectid,
               "org": objectid,
               "order": objectid,
               "policy": "general" | "law_ru_193",  // политика возврата.
                                                    // general - стандартные условия.
                                                    // law_ru_193 - применяются условия по ФЗ-193
               "tickets": Array[objectid],
               "vendor": objectid
            }
       }


**Пример запроса**

   .. sourcecode:: http

      POST /v2/resources/refund_requests HTTP/1.1
      Authorization: key 9bd8359943b545500278875r49c5b88d
      Content-Type: application/json

      {
        "culprit": "user",
        "order": "5def7c43e3ed5ae2a8d6908b",
        "requested_at": "2019-12-15T13:01:02",
        "tickets": [
            "5dd5469b05fe4df8940eb613"
        ]
    }



**Пример ответа**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "created_at": "2019-12-18 12:46:28",
                "culprit": "user",
                "customer_money": "1000.00",
                "delta": "1000.00",
                "event": "5dd5468f05fe4df8940eb602",
                "id": "5dfa1fa437077b6b6ed0f6b3",
                "order": "5def7c43e3ed5ae2a8d6908b",
                "org": "5b2d06ac5c3eb3000c475e36",
                "policy": "law_ru_193",
                "refund_nominal": "1000.00",
                "requested_at": "2019-12-15 13:01:02",
                "status": "new",
                "tickets": [
                    "5dd5469b05fe4df8940eb613"
                ],
                "vendor": "5b2d06ac5c3eb3000c475e36"
            },
            "refs": {
                "events": {
                    "5dd5468f05fe4df8940eb602": {
                        "age_rating": 0,
                        "id": "5dd5468f05fe4df8940eb602",
                        "lifetime": {
                            "finish": "2020-01-01 20:00:00",
                            "start": "2020-01-01 17:00:00"
                        },
                        "org": "5b2d06ac5c3eb3000c475e36",
                        "status": "public",
                        "timezone": "Europe/Moscow",
                        "title": {
                            "desc": "Metal music for all",
                            "text": "MetalGrid"
                        },
                        "venue": "583d9307515e350019da3ef6"
                    }
                },
                "orders": {
                    "5def7c43e3ed5ae2a8d6908b": {
                        "code": "k0xvxvel",
                        "created_at": "2019-12-10 11:06:43",
                        "custom_fields": {
                            "order": [],
                            "tickets": []
                        },
                        "done_at": "2019-12-10 11:11:54",
                        "event": "5dd5468f05fe4df8940eb602",
                        "expired_after": "2019-12-10 11:21:43",
                        "id": "5def7c43e3ed5ae2a8d6908b",
                        "number": 121,
                        "org": "5b2d06ac5c3eb3000c475e36",
                        "origin": "api",
                        "payments": [],
                        "promocodes": [],
                        "settings": {
                            "invitation": false,
                            "send_tickets": false,
                            "subscribe_agree": false
                        },
                        "status": "done",
                        "tickets": [
                            {
                                "barcode": "61534165115017991",
                                "discount": "0.00",
                                "extra": "0.00",
                                "full": "1000.00",
                                "id": "5dd5469b05fe4df8940eb613",
                                "nominal": "1000.00",
                                "number": 324762,
                                "price": "1000.00",
                                "serial": "APP",
                                "set": "5dd5469b05fe4df8940eb606",
                                "status": "reserved"
                            }
                        ],
                        "values": {
                            "discount": "0.00",
                            "extra": "0.00",
                            "full": "1000.00",
                            "nominal": "1000.00",
                            "price": "1000.00",
                            "sets_values": {
                                "5dd5469b05fe4df8940eb606": {
                                    "discount": "0.00",
                                    "id": "5dd5469b05fe4df8940eb606",
                                    "nominal": "1000.00",
                                    "price": "1000.00",
                                    "promocode": null
                                }
                            },
                            "viral_promocodes": []
                        },
                        "vendor": "5b2d06ac5c3eb3000c475e36",
                        "vendor_data": {}
                    }
                },
                "partners": {
                    "5b2d06ac5c3eb3000c475e36": {
                        "id": "5b2d06ac5c3eb3000c475e36",
                        "name": "Funky Box"
                    }
                },
                "tickets": {
                    "5dd5469b05fe4df8940eb613": {
                        "discount": "0.00",
                        "extra": "0.00",
                        "full": "1000.00",
                        "id": "5dd5469b05fe4df8940eb613",
                        "nominal": "1000.00",
                        "number": 324762,
                        "price": "1000.00",
                        "serial": "APP",
                        "set": "5dd5469b05fe4df8940eb606",
                        "status": "reserved"
                    }
                }
            }
        }



.. _walkthrough/refund_requests/approve:

Подтверждение и отмена возврата
===============================

**Запрос**

    .. http:patch:: /v2/resources/refund_requests/:refund_id

       :jsonparam status: ``approved`` | ``rejected``

**Ответ**

    :ref:`Объект возврата <walkthrough/refund_requests/object>`


**Пример запроса**

   .. sourcecode:: http

      PATCH /v2/resources/refund_requests/5dfa1fa437077b6b6ed0f6b3 HTTP/1.1
      Authorization: key 9bd8359943b545500278875r49c5b88d
      Content-Type: application/json

      {
          "status": "approved"
      }
