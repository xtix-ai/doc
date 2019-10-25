.. _extra/promocodes/begin:

==========
Проимокоды
==========



.. _extra/promocodes/check:

Проверка промокода
==================



**Запрос**

    .. http:post:: /v2/services/promocodes/check

            - **event** (str)
            - **code** (str)


**Ответ**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "discount": {
                    "percentage": str
                    "fix": str
                },
                "lifetime": {
                    "finish": iso8601
                    "start": iso8601
                },
                "sets": [oid, ... ],
                "tickets_count": {
                    "min": int
                    "max": int
                }
            },
            "refs": {
                "sets": {
                    oid: {
                        "id": oid
                        "name": str
                        "price": str
                    }
                    ...
                }
            }
        }


**Пример запроса**

    .. sourcecode:: http

        POST /v2/services/promocodes/check HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "code": "fix100",
            "event": "5db2d8504d9134a8c7ec2cf5"
        }


**Пример ответа**

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json


        {
            "data": {
                "discount": {
                    "fix": "100.00"
                },
                "sets": [],
                "tickets_count": {}
            },
            "refs": {
                "sets": {}
            }
        }


**Пример запроса**

    .. sourcecode:: http

        POST /v2/services/promocodes/check HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "code": "all",
            "event": "5d765a4a221988d7da985875"
        }



**Пример ответа**

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "discount": {
                    "percentage": "25%"
                },
                "lifetime": {
                    "finish": "2019-11-30 20:59:00",
                    "start": "2019-10-30 21:00:00"
                },
                "sets": [
                    "5d765a59221988d7da985879"
                ],
                "tickets_count": {
                    "min": 2
                }
            },
            "refs": {
                "sets": {
                    "5d765a59221988d7da985879": {
                        "id": "5d765a59221988d7da985879",
                        "name": "Билетище",
                        "price": "1099.00"
                    }
                }
            }
        }
