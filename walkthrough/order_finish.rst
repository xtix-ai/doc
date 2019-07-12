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

    .. http:post:: /v2/resources/orders/

        :query status: Обязателен (``done`` | ``cancelled``)

**Ответ**

    :ref:`Объект заказа <walkthrough/order_create/object>`


**Пример запроса**

    .. sourcecode:: http

        PATCH /v2/resources/orders/5b0eab671b2042000ea83850 HTTP/1.1
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
                "code": "ztzoih9o",
                "created_at": "2018-05-30 13:47:19",
                "custom_fields": {
                    "order": [],
                    "tickets": []
                },
                "done_at": "2019-07-02 15:33:18",
                "event": "5b0e8adc04bcc7000b2a279e",
                "expired_after": "2018-05-30 13:57:19",
                "id": "5b0eab671b2042000ea83850",
                "number": 72,
                "org": "5b0286ce517565000d9cb1ca",
                "origin": "api",
                "payments": [],
                "promocodes": [
                    "5b0eab2d1b2042000db2438f"
                ],
                "sessions": {
                    "utm": "5b0eab5d1b2042000db24390"
                },
                "settings": {
                    "invitation": false,
                    "send_tickets": true
                },
                "status": "done",
                "tickets": [
                    {
                        "barcode": null,
                        "discount": "4500.00",
                        "extra": "0.00",
                        "full": "0.00",
                        "id": "5b0e8afa9adc660001b0ab6c",
                        "nominal": "0.00",
                        "number": 110042,
                        "price": "4500.00",
                        "serial": "HTY",
                        "set": "5b0e8afa04bcc7000b2a6ec1",
                        "status": "reserved"
                    }
                ],
                "values": {
                    "discount": "4500.00",
                    "extra": "0.00",
                    "full": "0.00",
                    "nominal": "0.00",
                    "price": "4500.00",
                    "sets_values": {
                        "5b0e8af004bcc7000b2a6ebd": {
                            "discount": "5000.00",
                            "id": "5b0e8af004bcc7000b2a6ebd",
                            "nominal": "0.00",
                            "price": "5000.00",
                            "promocode": "5b0eab2d1b2042000db2438f"
                        },
                        "5b0e8af404bcc7000c7458b7": {
                            "discount": "1000.00",
                            "id": "5b0e8af404bcc7000c7458b7",
                            "nominal": "0.00",
                            "price": "1000.00",
                            "promocode": "5b0eab2d1b2042000db2438f"
                        },
                        "5b0e8afa04bcc7000b2a6ec1": {
                            "discount": "4500.00",
                            "id": "5b0e8afa04bcc7000b2a6ec1",
                            "nominal": "0.00",
                            "price": "4500.00",
                            "promocode": "5b0eab2d1b2042000db2438f"
                        },
                        "5b0e8b0304bcc7000b2a6ec5": {
                            "discount": "3300.00",
                            "id": "5b0e8b0304bcc7000b2a6ec5",
                            "nominal": "0.00",
                            "price": "3300.00",
                            "promocode": "5b0eab2d1b2042000db2438f"
                        },
                        "5b0e8b1604bcc7000b2a6ec9": {
                            "discount": "4000.00",
                            "id": "5b0e8b1604bcc7000b2a6ec9",
                            "nominal": "0.00",
                            "price": "4000.00",
                            "promocode": "5b0eab2d1b2042000db2438f"
                        }
                    },
                    "viral_promocodes": []
                },
                "vendor": "5b0286ce517565000d9cb1ca",
                "vendor_data": {}
            },
            "refs": {
                "events": {
                    "5b0e8adc04bcc7000b2a279e": {
                        "id": "5b0e8adc04bcc7000b2a279e",
                        "lifetime": {
                            "finish": "2019-03-29 15:00:00",
                            "start": "2019-03-22 11:00:00"
                        },
                        "org": "5b0286ce517565000d9cb1ca",
                        "status": "finished",
                        "timezone": "Europe/Moscow",
                        "title": {
                            "desc": "Тест-111122",
                            "text": "Для статистики-11122"
                        }
                    }
                },
                "partners": {
                    "5b0286ce517565000d9cb1ca": {
                        "id": "5b0286ce517565000d9cb1ca",
                        "name": "New organiser"
                    }
                },
                "promocodes": {
                    "5b0eab2d1b2042000db2438f": {
                        "code": "100",
                        "discount": {
                            "percentage": "100%"
                        },
                        "id": "5b0eab2d1b2042000db2438f",
                        "lifetime": null,
                        "sets": [],
                        "tickets_count": {},
                        "viral": false
                    }
                },
                "sets": {
                    "5b0e8afa04bcc7000b2a6ec1": {
                        "id": "5b0e8afa04bcc7000b2a6ec1",
                        "name": "Фан-зона левая сторона",
                        "price": null,
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
