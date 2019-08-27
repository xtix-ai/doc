.. _walkthrough/order_finish/begin:

==========================
Шаг 3: Завершение заказа
==========================

.. note::

   На данном шаге рассматривается завершение заказа без работы
   с платежными системами.


.. _walkthrough/order_finish/status:

Смена статуса заказа
====================

**Запрос**

    .. http:patch:: /v2/resources/orders

        :jsonparam status: Обязателен (``done`` | ``cancelled``)

**Ответ**

    :ref:`Объект заказа <walkthrough/order_create/object>`


**Пример запроса**

    .. sourcecode:: http

        PATCH /v2/resources/orders/5d39c3108cd381a4891e07e0 HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "status": "done"
        }

**Пример ответа**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "code": "97elgi8j",
                "created_at": "2019-07-25 14:56:16",
                "done_at": "2019-07-25 14:57:47",
                "event": "5d31fbdd27649b0dff076117",
                "expired_after": "2019-07-25 15:11:16",
                "id": "5d39c3108cd381a4891e07e0",
                "number": 54881,
                "org": "5b04229196c055000d87c2b5",
                "origin": "api",
                "promocodes": [
                    "5b0eab2d1b2042000db2438f"
                ],
                "settings": {
                    "invitation": false,
                    "send_tickets": false,
                    "subscribe_agree": false
                },
                "status": "done",
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
                            "promocode": "5b0eab2d1b2042000db2438f"
                        },
                        "5d31fbfa8a75c12c9d64de13": {
                            "discount": "0.00",
                            "id": "5d31fbfa8a75c12c9d64de13",
                            "nominal": "1050.00",
                            "price": "1050.00",
                            "promocode": "5b0eab2d1b2042000db2438f"
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
                "promocodes": {
                    "5b0eab2d1b2042000db2438f": {
                        "code": "100",
                        "discount": {
                            "percentage": "0%"
                        },
                        "id": "5b0eab2d1b2042000db2438f",
                        "lifetime": null,
                        "viral": false
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


.. seealso::

   :ref:`Жизненный цикл заказа <extra/lifecycle/begin>`

.. warning::

   Заказ в статусе ``done`` больше нельзя изменять.
   Любые ``PATCH`` запросы на данный заказ будут отклонены со статусом
   :http:statuscode:`400`.

Поздравляем! Вы провели свой первый заказ через API!
