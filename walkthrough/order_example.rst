.. _walkthrough/order_example/begin:

========================
Пример проведения заказа
========================

.. note::

   Пример будет смешанного заказа из двух билетов: один билет с рассадкой, другой -- без


Создаем заказ
=============

    .. sourcecode:: http

        POST /v2/resources/orders HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "event": "5d7134962110d30a34e95b96"
        }


    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "created_at": "2019-09-23 15:43:16",
                "event": "5d7134962110d30a34e95b96",
                "expired_after": "2019-09-23 15:58:16",
                "id": "5d88e814982d975add9dfc05",
                "number": 59471,
                "org": "5ba10ea90c43fc000b0fc786",
                "origin": "api",
                "status": "executed",
                "tickets": [],
                "values": {
                    "discount": "0.00",
                    "extra": "0.00",
                    "full": "0.00",
                    "nominal": "0.00",
                    "price": "0.00",
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
                "sets": {}
            }
        }


Заполняем заказ
===============

    .. sourcecode:: http

        PATCH /v2/resources/orders/5d88e814982d975add9dfc05 HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d
        Content-Type: application/json

        {
            "random": {
                "5d713505255895db3c30b0c5": 1,
                "5d80caa838d7c9920bec1b47": 1
            }
        }


    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": {
                "created_at": "2019-09-23 15:43:16",
                "event": "5d7134962110d30a34e95b96",
                "expired_after": "2019-09-23 15:58:16",
                "id": "5d88e814982d975add9dfc05",
                "number": 59471,
                "org": "5ba10ea90c43fc000b0fc786",
                "origin": "api",
                "status": "executed",
                "tickets": [
                    {
                        "barcode": null,
                        "discount": "0.00",
                        "extra": "666.60",
                        "full": "7332.60",
                        "id": "5d71350576a6bda00a86ad2f",
                        "nominal": "6666.00",
                        "number": 137456,
                        "price": "6666.00",
                        "serial": "PTY",
                        "set": "5d713505255895db3c30b0c5",
                        "status": "reserved"
                    },
                    {
                        "barcode": null,
                        "discount": "0.00",
                        "extra": "0.00",
                        "full": "0.00",
                        "id": "5d7134962110d30a34e95b97",
                        "nominal": "0.00",
                        "number": 135471,
                        "price": "0.00",
                        "seat": {
                            "number": "3",
                            "row": "10",
                            "sector": "5a8dd58e6e55b2064c67c142"
                        },
                        "serial": "EOY",
                        "set": "5d80caa838d7c9920bec1b47",
                        "status": "reserved"
                    }
                ],
                "values": {
                    "discount": "0.00",
                    "extra": "666.60",
                    "full": "7332.60",
                    "nominal": "6666.00",
                    "price": "6666.00",
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
                "sets": {
                    "5d713505255895db3c30b0c5": {
                        "id": "5d713505255895db3c30b0c5",
                        "name": "Танцевальный партер",
                        "price": "6666.00",
                        "with_seats": false
                    },
                    "5d80caa838d7c9920bec1b47": {
                        "id": "5d80caa838d7c9920bec1b47",
                        "name": "A0",
                        "price": "0.00",
                        "with_seats": true
                    }
                }
            }
        }


Завершаем заказ
===============

    .. sourcecode:: http

        PATCH /v2/resources/orders/5d88e814982d975add9dfc05 HTTP/1.1
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
                "code": "n8b974vz",
                "created_at": "2019-09-23 15:43:16",
                "done_at": "2019-09-23 15:48:35",
                "event": "5d7134962110d30a34e95b96",
                "expired_after": "2019-09-23 15:58:16",
                "id": "5d88e814982d975add9dfc05",
                "number": 59471,
                "org": "5ba10ea90c43fc000b0fc786",
                "origin": "api",
                "status": "done",
                "tickets": [
                    {
                        "barcode": "71834260666980937",
                        "discount": "0.00",
                        "extra": "666.60",
                        "full": "7332.60",
                        "id": "5d71350576a6bda00a86ad2f",
                        "nominal": "6666.00",
                        "number": 137456,
                        "price": "6666.00",
                        "serial": "PTY",
                        "set": "5d713505255895db3c30b0c5",
                        "status": "reserved"
                    },
                    {
                        "barcode": "24213355289384412",
                        "discount": "0.00",
                        "extra": "0.00",
                        "full": "0.00",
                        "id": "5d7134962110d30a34e95b97",
                        "nominal": "0.00",
                        "number": 135471,
                        "price": "0.00",
                        "seat": {
                            "number": "3",
                            "row": "10",
                            "sector": "5a8dd58e6e55b2064c67c142"
                        },
                        "serial": "EOY",
                        "set": "5d80caa838d7c9920bec1b47",
                        "status": "reserved"
                    }
                ],
                "values": {
                    "discount": "0.00",
                    "extra": "666.60",
                    "full": "7332.60",
                    "nominal": "6666.00",
                    "price": "6666.00",
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
                "sets": {
                    "5d713505255895db3c30b0c5": {
                        "id": "5d713505255895db3c30b0c5",
                        "name": "Танцевальный партер",
                        "price": "6666.00",
                        "with_seats": false
                    },
                    "5d80caa838d7c9920bec1b47": {
                        "id": "5d80caa838d7c9920bec1b47",
                        "name": "A0",
                        "price": "0.00",
                        "with_seats": true
                    }
                }
            }
        }
