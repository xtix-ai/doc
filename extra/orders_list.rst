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

        GET /v2/resources/orders?status=done,cancelled&created_at=2000-07-28T13,2020-07-28T13 HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d


**Пример ответа**

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": [
                {
                    "created_at": "2019-06-27 10:50:13",
                    "custom_fields": {
                        ...
                    },
                    "event": "5cbd881dc406a70015d695f8",
                    "id": "5d149f651e53c7ce65454ab1",
                    "number": 52646,
                    "org": "5b0286ce517565000d9cb1ca",
                    "origin": "api",
                    "payments": [],
                    "promocodes": [],
                    "settings": {
                        ...
                    },
                    "status": "cancelled",
                    "tickets": [],
                    "values": {
                        "discount": "0.00",
                        "extra": "0.00",
                        "full": "0.00",
                        "nominal": "0.00",
                        "price": "0.00",
                        "sets_values": {
                            ...
                        },
                        "viral_promocodes": []
                    },
                    "vendor": "5b0286ce517565000d9cb1ca",
                    "vendor_data": {}
                },
            ]
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
