.. _walkthrough/refund_requests/begin:

=====================
Шаг 4: Возврат заказа
=====================


.. _walkthrough/refund_requests/create:

Создание возврата
=================

**Запрос**

    .. http:post:: /v2/resources/refund_requests/

       :query order: Id заказа
       :query culprit: Виновник возврата (``user``|``org``)
       :query tickets: Список id билетов для возврата


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
               "delta": money // сумма возврата,
               "event": objectid,
               "org": objectid,
               "order": objectid,
               "tickets": Array[objectid],
               "vendor": objectid
            }
       }


**Пример запроса**

   .. sourcecode:: http

      POST /v2/resources/refund_requests HTTP/1.1
      Authorization: key 9bd8359943b545500278875r49c5b96d
      Content-Type: application/json
      
      {
          "order": "5bfd0f7533836a000da16b41",
          "culprit": "user",
          "tickets": [
              "5bfd0f7533836a000da16b41",
          ]
      }


**Пример ответа**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "created_at": "2019-07-05 09:54:46",
                "culprit": "user",
                "delta": "0.00",
                "event": "5d1f1d568edbb6017b2d8d35",
                "id": "5d1f1e668edbb6017b2d8db4",
                "order": "5bfd0f7533836a000da16b41",
                "org": "5b04229196c055000d87c2b5",
                "status": "new",
                "tickets": [
                    "5bfd0f7533836a000da16b41",
                ],
                "vendor": "5b04229196c055000d87c2b5"
            },
            "refs": {
                "events": {
                    "5d1f1d568edbb6017b2d8d35": {
                        "id": "5d1f1d568edbb6017b2d8d35",
                        "lifetime": {
                            "finish": "2019-07-12 16:00:00",
                            "start": "2019-07-12 12:00:00"
                        },
                        "org": "5b04229196c055000d87c2b5",
                        "status": "public",
                        "timezone": "Europe/Moscow",
                        "title": {
                            "desc": "sdfgsdfg",
                            "text": "dfgdsfg"
                        }
                    }
                },
                "orders": {
                    "5bfd0f7533836a000da16b41": {
                        "code": "rbbcmabl",
                        "created_at": "2019-07-05 09:50:36",
                        "done_at": "2019-07-05 09:50:36",
                        "event": "5d1f1d568edbb6017b2d8d35",
                        "expired_after": "2019-07-05 10:05:36",
                        "id": "5d1f1d6c8edbb6017b2d8dad",
                        "number": 37,
                        "org": "5b04229196c055000d87c2b5",
                        "origin": "control_panel",
                        "payments": [],
                        "settings": {
                            "customer": {
                                "email": "duxamax@gmail.com",
                                "lang": "ru"
                            },
                            "invitation": true,
                            "send_tickets": true,
                            "subscribe_agree": false
                        },
                        "status": "done",
                        "tickets": [],
                        "values": {
                            "discount": "0.00",
                            "extra": "0.00",
                            "full": "0.00",
                            "nominal": "0.00",
                            "price": "0.00",
                            "sets_values": {
                                "5d1f1d5e8edbb6017b2d8d39": {
                                    "discount": "0.00",
                                    "id": "5d1f1d5e8edbb6017b2d8d39",
                                    "nominal": "123.00",
                                    "price": "123.00",
                                    "promocode": null
                                }
                            },
                        },
                        "vendor": "5b04229196c055000d87c2b5",
                        "vendor_data": {}
                    }
                },
                "partners": {
                    "5b04229196c055000d87c2b5": {
                        "id": "5b04229196c055000d87c2b5",
                        "name": "Test Organizer"
                    }
                },
                "tickets": {
                    "5bfd0f7533836a000da16b41": {
                        "discount": "123.00",
                        "extra": "0.00",
                        "full": "0.00",
                        "id": "5d1f1d5e8edbb6017b2d8d3e",
                        "nominal": "0.00",
                        "number": 183393,
                        "price": "123.00",
                        "serial": "ABK",
                        "set": "5d1f1d5e8edbb6017b2d8d39",
                        "status": "refunded"
                    }
                }
            }
        }


.. _walkthrough/refund_requests/approve:

Подтверждение и отмена возврата
===============================

**Запрос**

    .. http:patch:: /v2/resources/refund_requests/:refund_id

       :query status: "approved" | "rejected**

**Ответ**

    :ref:`Объект возврата <walkthrough/refund_requests/object>`


**Пример запроса**

   .. sourcecode:: http

      PATCH /v2/resources/refund_requests/5d1f1e668edbb6017b2d8db4 HTTP/1.1
      Authorization: key 9bd8359943b545500278875r49c5b96d
      Content-Type: application/json
      
      {
          "status": "approved"
      }

