.. _walkthrough/events/begin:

========================================
Шаг 1: Информация о мероприятии
========================================


.. _walkthrough/events/simple:

Получаем список мероприятий
===========================


Мероприятия можно получить запросом `/v1/services/simple/events`.
В поле `events` содержится список эвентов, по которым у вас заключена сделка с организатором.
Остальные поля представляют собой объекты с информацией о каждой сущности,
присутствующей на данной странице в любом из эвентов.

**Запрос**:

    .. sourcecode:: js

        GET /v1/services/simple/events


**Ответ**:

    - ``id`` **str**::ref:`objectid <extra/types/objectid>` - id мероприятия
    - ``created_at`` **str**::ref:`isodatetime <extra/types/isodatetime>` - дата создания
    - ``updated_at`` **str**::ref:`isodatetime <extra/types/isodatetime>`- дата последнего изменения
    - ``lifetime`` **str**:*VEVENT*  - :ref:`vevent <extra/types/vevent>`, время проведения мероприятия
    - ``status`` **str** - текущий статус мероприятия. `public` — публичное мероприятие, можно продавать билеты)

    - ``title`` **object**
    
       - ``text`` **str** - название мероприятия
       - ``desc`` **str** - описание мероприятия

    - ``media`` :ref:`media <extra/types/media>` логитипы в различных размерах:

       - ``cover_original`` **object**:*media*
       - ``cover`` **object**:*media*
       - ``cover_small`` **object**:*media*

    - ``org`` **object** информация об организаторе мероприятия

       - ``id`` **str**::ref:`objectid <extra/types/objectid>` - id организатора
       - ``name`` **str** - название организатора
       - ``desc`` **str** - краткое описание
       - ``media`` **object** - media логотипы
       - ``contact`` - контактная информация
         
    - ``venue`` место проведения
      
       - ``id`` **str**::ref:`objectid <extra/types/objectid>` - venue id
       - ``address`` **str** - адрес
       - ``country`` страна
       - ``city`` город
       - ``name`` **str** - название
       - ``desc`` **str** - краткое описание
       - ``point`` координата (`GeoJSON <http://geojson.org>`_'s point)

    - ``map`` схема зала

    - ``sets`` билетные категории

       - ``id`` **str**::ref:`objectid <extra/types/objectid>`
       - ``pos`` **int** - порядковый номер категории (для сортировки)
       - ``name`` **str** - название категории
       - ``amount`` **int** - общее количество билетов в сете
       - ``amount_vacant`` **int** - количество билетов, доступных для продажи
       - ``price_org`` **str**:*Money* - номинальная цена билета
       - ``price_extra`` **str**:*Money* - сервисный сбор
       - ``price`` **str**:*Money* - общая цена билета
       - ``with_seats`` **bool** - наличие посадочных мест в категории
       - ``seats`` **object** - row: numbers (**list**)
       - ``sector`` сектор

    - ``rules`` правила

       - ``id``
       - ``cal`` :ref:`vevent <extra/types/vevent>`, время действия правила
       - ``current`` **bool** - `true` если правило текущее
       - ``price_org`` **str**:*Money* - номинальная цена
       - ``price_extra`` - сервисный сбор
       - ``price`` **str**:*Money* - конечная цена


**Пример запроса**:

    .. sourcecode:: http

        GET /v1/services/simple/events HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d

**Пример ответа**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "age_rating": 21,
                "allow_other_ps": false,
                "created_at": "2019-03-01T14:58:47.791000+00:00",
                "deal": null,
                "id": "5c7948a71bf4e5000cf34ad3",
                "lifetime": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20190228T210000Z\r\nDTEND;VALUE=DATE-TIME:20190629T210000Z\r\nEND:VEVENT\r\n",
                "map": null,
                "media": {
                    "cover": {
                        "author": "5b04229196c055000d87c2b5",
                        "content_type": "image/jpeg",
                        "id": "5c7948aa1bf4e5000cf34ad7",
                        "length": 127017,
                        "md5hash": "265c3340dd7681609249d56c91741bb0",
                        "url": "https://ticketscloud.com/s3/media.ticketscloud/stage/image/2019-03/5c7948aa1bf4e5000cf34ad7.jpg"
                    },
                    "cover_original": {
                        "author": "5b04229196c055000d87c2b5",
                        "content_type": "image/jpeg",
                        "id": "5c7948aa1bf4e5000cf34ad8",
                        "length": 181962,
                        "md5hash": "e0a246d0c113972133a01b872030553d",
                        "url": "https://ticketscloud.com/s3/media.ticketscloud/stage/image/2019-03/5c7948aa1bf4e5000cf34ad8.jpg"
                    },
                    "cover_small": {
                        "author": "5b04229196c055000d87c2b5",
                        "content_type": "image/jpeg",
                        "id": "5c7948a91bf4e5000cf34ad6",
                        "length": 41396,
                        "md5hash": "89687f959541eec5deaa868cfa721f02",
                        "url": "https://ticketscloud.com/s3/media.ticketscloud/stage/image/2019-03/5c7948a91bf4e5000cf34ad6.jpg"
                    }
                },
                "org": {
                    "contact": {
                        "address": "Greek",
                        "email": "noreplay@ticketscloud.org",
                        "name": "",
                        "phones": [
                            "79666666666"
                        ],
                        "www": "www.google.gr"
                    },
                    "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                    "id": "5b04229196c055000d87c2b5",
                    "media": {
                        "logo": {
                            "author": "5b04229196c055000d87c2b5",
                            "content_type": "image/jpeg",
                            "id": "5b04229196c055000c6688c6",
                            "length": 15715,
                            "md5hash": "d71dfeeb9fae5391903c7f9e05431b9e",
                            "url": "https://ticketscloud.com/s3/media.ticketscloud/stage/image/2018-05/5b04229196c055000c6688c6.jpg"
                        },
                        "logo_original": {
                            "author": "5b04229196c055000d87c2b5",
                            "content_type": "image/jpeg",
                            "id": "5b04229196c055000d87c2b7",
                            "length": 10626,
                            "md5hash": "75dd76e10455d79f14591dc677d8e334",
                            "url": "https://ticketscloud.com/s3/media.ticketscloud/stage/image/2018-05/5b04229196c055000d87c2b7.jpg"
                        },
                        "logo_small": {
                            "author": "5b04229196c055000d87c2b5",
                            "content_type": "image/jpeg",
                            "id": "5b04229196c055000c6688c7",
                            "length": 23865,
                            "md5hash": "7aaf9478b8104da351586514097b09f9",
                            "url": "https://ticketscloud.com/s3/media.ticketscloud/stage/image/2018-05/5b04229196c055000c6688c7.jpg"
                        }
                    },
                    "name": "My best partner",
                    "tags": [
                        "Театры",
                        "Выставки",
                        "Здоровье",
                        "Балет"
                    ]
                },
                "partner": {
                    "contact": {
                        "address": "Greek",
                        "email": "noreplay@ticketscloud.org",
                        "name": "",
                        "phones": [
                            "79666666666"
                        ],
                        "www": "www.google.gr"
                    },
                    "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                    "id": "5b04229196c055000d87c2b5",
                    "media": {
                        "logo": {
                            "author": "5b04229196c055000d87c2b5",
                            "content_type": "image/jpeg",
                            "id": "5b04229196c055000c6688c6",
                            "length": 15715,
                            "md5hash": "d71dfeeb9fae5391903c7f9e05431b9e",
                            "url": "https://ticketscloud.com/s3/media.ticketscloud/stage/image/2018-05/5b04229196c055000c6688c6.jpg"
                        },
                        "logo_original": {
                            "author": "5b04229196c055000d87c2b5",
                            "content_type": "image/jpeg",
                            "id": "5b04229196c055000d87c2b7",
                            "length": 10626,
                            "md5hash": "75dd76e10455d79f14591dc677d8e334",
                            "url": "https://ticketscloud.com/s3/media.ticketscloud/stage/image/2018-05/5b04229196c055000d87c2b7.jpg"
                        },
                        "logo_small": {
                            "author": "5b04229196c055000d87c2b5",
                            "content_type": "image/jpeg",
                            "id": "5b04229196c055000c6688c7",
                            "length": 23865,
                            "md5hash": "7aaf9478b8104da351586514097b09f9",
                            "url": "https://ticketscloud.com/s3/media.ticketscloud/stage/image/2018-05/5b04229196c055000c6688c7.jpg"
                        }
                    },
                    "name": "My best partner",
                    "tags": [
                        "Театры",
                        "Выставки",
                        "Здоровье",
                        "Спорт",
                        "Балет"
                    ]
                },
                "sets": [],
                "status": "public",
                "tags": [
                    "Выставки"
                ],
                "ticket_template": {
                    "fan_cover_url": null,
                    "name": null,
                    "text_color": null
                },
                "tickets_amount": 0,
                "tickets_amount_vacant": 0,
                "title": {
                    "desc": "event desk",
                    "text": "PK--fenomen"
                },
                "updated_at": "2019-06-03T08:15:42.083000+00:00",
                "venue": {
                    "address": "Череповецкая, 3Б",
                    "city": {
                        "country": "RU",
                        "id": 524901,
                        "name": {
                            "af": "Moskou",
                            "ar": "موسكو",
                            "arc": "ܡܘܣܩܒܐ",
                            "ast": "Moscú",
                            "be": "Горад Масква",
                            "bg": "Москва",
                            "zh": "莫斯科"
                        },
                        "timezone": "Europe/Moscow"
                    },
                    "country": {
                        "id": "RU",
                        "name": {
                            "be": "Расійская Федэрацыя",
                            "default": "Russia",
                            "en": "Russia",
                            "fr": "Russie",
                            "ru": "Россия",
                            "zh": "俄罗斯"
                        }
                    },
                    "desc": null,
                    "id": "5863cea3515e3500184ca18b",
                    "name": "Череповецкая, 3Б",
                    "point": {
                        "coordinates": [
                            37.56571599999995,
                            55.899187
                        ],
                        "type": "Point"
                    }
                }
            },
        ]


.. _walkthrough/events/tickets:

Получаем список билетов с местами по мероприятию
================================================


Получение списка билетов мероприятия для категорий с рассадкой.

**Зарпос**

    .. http:get:: /v1/resources/events/:id/tickets

       :query status: Фильтр-список по списку статусов (``vacant`` | ``reserved`` | ``sold`` | ``pending``). По умолчанию включены билеты во всех статусах, кроме ``pending``.
       :query sector: Фильтр-список по списку секторов


**Ответ**

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "id": objectid
                "number": int
                "reserved_till": isodatetime | null
                "seat": {
                    "number": int
                    "row": int
                    "sector": objectid
                },
                "serial": str
                "set": objectid
                "status": str
            },
            ...
        ]


**Пример запроса**:

    .. sourcecode:: http

        GET /v1/resources/events/5b0d157f445143000114e321/tickets?status=vacant&sector=55abfa669cb5382abebd9fad HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d


**Пример ответа:**

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "id": "5b0d157f445143000114e4ef",
                "number": 110581,
                "reserved_till": null,
                "seat": {
                    "number": 1,
                    "row": 1,
                    "sector": "55abfa669cb5382abebd9fad"
                },
                "serial": "OPT",
                "set": "5b0d1580445143000114e92d",
                "status": "vacant"
            },
            {
                "id": "5b0d157f445143000114e4f0",
                "number": 110582,
                "reserved_till": null,
                "seat": {
                    "number": 2,
                    "row": 1,
                    "sector": "55abfa669cb5382abebd9fad"
                },
                "serial": "OPT",
                "set": "5b0d1580445143000114e92d",
                "status": "vacant"
            },
        ]


.. _walkthrough/events/widget:

..
    Получаем информацию для отображения виджета Мероприятия
    =======================================================


    Информацию для отображения виджета можно получить запросом :http:post:`/v1/services/widget`
    с параметрами `event` или `meta_event` в случае метаэвента.

    Пример запроса:

        .. sourcecode:: http

           http POST .../v1/services/widget Authorization:'key aa44673d78574172ad9a957ff25b27e6' event=5b34f8745c60ee000c67f409


    Описание полей ответа:

        - ``vendor`` **str**::ref:`objectid <extra/types/objectid>` - id распространителя
        - ``org`` **str**::ref:`objectid <extra/types/objectid>` - id организатора
        - ``meta_event`` **str**::ref:`objectid <extra/types/objectid>` | **null** - cсылка на метаэвент
        - ``event`` **object** объект эвента :ref:`объект эвента <walkthrough/events/simple>`
        - ``settings`` **object** объект с настройками эвента
        - ``sets`` **object** объект с категориями билетов где ключ - id категории, значение объект категории:

            - ``id`` **str**::ref:`objectid <extra/types/objectid>` - id категории
            - ``name`` **str**
            - ``desc`` **str**
            - ``pos``
            - ``sector`` **str**::ref:`objectid <extra/types/objectid>` - id сектора
            - ``amount`` **int** - кол-во билетов
            - ``amount_vacant`` **int** - кол-во билетов в статусе ``vacant``
            - ``with_seats`` **bool** - Категория с рассадкой/без
            - ``prices`` **array** - Список правил динамического ценообразования

        - ``tickets`` **object** - Объект с билетами где ключ - id сектора,
            значение - объект с ключами -- рядами значениями билетами:

            - ``id`` **str**::ref:`objectid <extra/types/objectid>` - id билета
            - ``set`` **str**::ref:`objectid <extra/types/objectid>` - id категории
            - ``status`` **str**::ref:`objectid <extra/types/objectid>` - Статус билета
            - ``reserved_till``

        - ``venue`` **object** - Объект с информацией о месте проведения мероприятия:

            - ``id`` **str**::ref:`objectid <extra/types/objectid>` - id площадки
            - ``name`` **str**
            - ``desc`` **str**
            - ``address`` **str**
            - ``point`` **object**
            - ``country`` **object**
            - ``city`` **object**

        - ``map`` **object**
        - ``partners`` **object**
        - ``payment_settings`` **object**
        - ``tz`` **str** таймзона
        - ``ga_id`` **str** Google Analytics id
        - ``ym_id`` **str** Yandex Metrics id
        - ``vk_pixel`` **str** VK pixel id
        - ``fb_pixel`` **str** Facebook Pixel id
        - ``has_promocodes`` **bool**
        - ``kryptonite_send`` **bool**
        - ``lang_switcher`` **bool**
        - ``viral_promocodes_enabled`` **bool**


    Пример ответа:

    .. sourcecode:: http

       {
            "vendor": "5b0286ce517565000d9cb1ca",
            "org": "5b0286ce517565000d9cb1ca",
            "meta_event": null,
            "event": {
                "id": "5b34f8745c60ee000c67f409",
                "title": {
                    "text": "FACE \u0432 \u041c\u043e\u0441\u043a\u0432\u0435",
                    "desc": "\u041d\u043e\u0432\u044b\u0439 \u0442\u0443\u0440 FACE\n\n\u0412\u043e\u0437\u0440\u0430\u0441\u0442\u043d\u043e\u0435 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435: 16+"
                },
                "age_rating": 16,
                "media": {},
                "org": "5b0286ce517565000d9cb1ca",
                "lifetime": {
                    "start": "2018-11-30T17:00:00+00:00",
                    "finish": "2018-11-30T19:00:00+00:00"
                },
                "widget_ext": null,
                "tickets_limit": null,
                "category": "592841f8515e35002dead938",
                "tags": [
                    "592841f8515e35002dead94a",
                    "592841f8515e35002dead93b"
                ]
            },
            "settings": {
                "translator": false,
                "show_cover": false,
                "show_description": false,
                "white_label": false,
                "price_change": false,
                "tickets_left": 10,
                "sets_to_show": 3,
                "support_phone": null,
                "support_email": null,
                "css_link": null,
                "contract_link": null,
                "redirect_link": null
            },
            "sets": {
                "5b34f8765c60ee000c67f553": {
                    "id": "5b34f8765c60ee000c67f553",
                    "name": "\u0422\u0430\u043d\u0446\u0435\u0432\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0442\u0435\u0440",
                    "desc": "\u0411\u0438\u043b\u0435\u0442 \u0440\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u043d \u043d\u0430 \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0435 \u0437\u043e\u043d\u044b \u0442\u0430\u043d\u0446\u043f\u043e\u043b\u0430 \u0432 \u043e\u0434\u043d\u043e\u043c \u043b\u0438\u0446\u0435.\n\u0412\u043e\u0437\u0440\u0430\u0441\u0442\u043d\u043e\u0435 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435: 16+",
                    "pos": 0,
                    "sector": "5b2930886e55b206059b760b",
                    "amount": 26,
                    "amount_vacant": 23,
                    "with_seats": false,
                    "prices": [
                        {
                            "start": "2018-06-18 21:00:00",
                            "finish": "2018-11-30 19:00:00",
                            "nominal": "800.00",
                            "extra": "0.00",
                            "full": "800.00"
                        }
                    ]
                },
                "tickets": {
                    "5b2930886e55b206059b760f": {
                        "21": {
                            "168": {
                                "id": "5b34f8745c60ee000c67f529",
                                "set": "5b34f8775c60ee000c67f557",
                                "status": "sold",
                                "reserved_till": null
                            },
                            "166": {
                                "id": "5b34f8745c60ee000c67f527",
                                "set": "5b34f8775c60ee000c67f557",
                                "status": "vacant",
                                "reserved_till": null
                            },
                        },
                        "22": {
                            "175": {
                                "id": "5b34f8745c60ee000c67f530",
                                "set": "5b34f8775c60ee000c67f557",
                                "status": "sold",
                                "reserved_till": null
                            },
                            "173": {
                                "id": "5b34f8745c60ee000c67f52e",
                                "set": "5b34f8775c60ee000c67f557",
                                "status": "vacant",
                                "reserved_till": null
                            },
                        }
                    }
                },
                "venue": {
                    "id": "5ad9abd9d35286001a4f8991",
                    "name": "Cition Hall",
                    "desc": "",
                    "address": "\u0428\u043c\u0438\u0442\u043e\u0432\u0441\u043a\u0438\u0439 \u043f\u0440\u043e\u0435\u0437\u0434, 32\u0410 \u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 1",
                    "point": {
                        "type": "Point",
                        "coordinates": [
                            37.53011900000001,
                            55.75682
                        ]
                    },
                    "country": {
                        "iso": "RU",
                        "iso3": "RUS",
                        "name": {
                            "en": "Russia",
                            "ru": "\u0420\u043e\u0441\u0441\u0438\u044f"
                        }
                    },
                    "city": {
                        "name": {
                            "en": "Moscow",
                            "ru": "\u041c\u043e\u0441\u043a\u0432\u0430"
                        }
                    }
                },
                "map": {
                    "id": "5b2930886e55b206059b760a",
                    "name": "\u0421\u0445\u0435\u043c\u0430 \u0441 \u0440\u0430\u0441\u0441\u0430\u0434\u043a\u043e\u0439 \u043f\u043e \u043c\u0435\u0441\u0442\u0430\u043c",
                    "desc": "",
                    "sectors": [
                        {
                            "id": "5b2930886e55b206059b760b",
                            "name": "\u0422\u0430\u043d\u0446\u0435\u0432\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u0430\u0440\u0442\u0435\u0440",
                            "desc": "",
                            "with_seats": false,
                            "seats": null,
                            "type": "chairs"
                        },
                        {
                            "id": "5b2930886e55b206059b760c",
                            "name": "VIP LEFT",
                            "desc": "",
                            "with_seats": true,
                            "seats": {
                                "1": [
                                    [
                                        1,
                                        8
                                    ]
                                ],
                                "2": [
                                    [
                                        9,
                                        16
                                    ]
                                ],
                                "3": [
                                    [
                                        17,
                                        24
                                    ]
                                ],
                                "4": [
                                    [
                                        25,
                                        32
                                    ]
                                ]
                            },
                            "type": "chairs"
                        },
                        {
                            "id": "5b2930886e55b206059b760d",
                            "name": "VIP RIGHT",
                            "desc": "",
                            "with_seats": true,
                            "seats": {
                                "1": [
                                    [
                                        1,
                                        8
                                    ]
                                ],
                                "2": [
                                    [
                                        9,
                                        16
                                    ]
                                ],
                                "3": [
                                    [
                                        17,
                                        24
                                    ]
                                ],
                                "4": [
                                    [
                                        25,
                                        32
                                    ]
                                ]
                            },
                            "type": "chairs"
                        },
                        {
                            "id": "5b2930886e55b206059b760e",
                            "name": "SUPER VIP",
                            "desc": "",
                            "with_seats": true,
                            "seats": {
                                "1": [
                                    [
                                        1,
                                        8
                                    ]
                                ],
                                "2": [
                                    [
                                        9,
                                        16
                                    ]
                                ],
                                "3": [
                                    [
                                        17,
                                        24
                                    ]
                                ],
                                "4": [
                                    [
                                        25,
                                        32
                                    ]
                                ],
                                "5": [
                                    [
                                        33,
                                        40
                                    ]
                                ],
                                "6": [
                                    [
                                        41,
                                        48
                                    ]
                                ],
                                "7": [
                                    [
                                        49,
                                        56
                                    ]
                                ]
                            },
                            "type": "chairs"
                        },
                        {
                            "id": "5b2930886e55b206059b760f",
                            "name": "VIP CENTER",
                            "desc": "",
                            "with_seats": true,
                            "seats": {
                                "1": [
                                    [
                                        1,
                                        8
                                    ]
                                ],
                                "2": [
                                    [
                                        9,
                                        16
                                    ]
                                ],
                                "3": [
                                    [
                                        17,
                                        24
                                    ]
                                ],
                                "4": [
                                    [
                                        25,
                                        32
                                    ]
                                ],
                                "5": [
                                    [
                                        33,
                                        40
                                    ]
                                ],
                                "6": [
                                    [
                                        41,
                                        48
                                    ]
                                ],
                                "7": [
                                    [
                                        49,
                                        56
                                    ]
                                ],
                                "8": [
                                    [
                                        57,
                                        64
                                    ]
                                ],
                                "9": [
                                    [
                                        65,
                                        72
                                    ]
                                ],
                                "10": [
                                    [
                                        73,
                                        80
                                    ]
                                ],
                                "11": [
                                    [
                                        81,
                                        88
                                    ]
                                ],
                                "12": [
                                    [
                                        89,
                                        96
                                    ]
                                ],
                                "13": [
                                    [
                                        97,
                                        104
                                    ]
                                ],
                                "14": [
                                    [
                                        105,
                                        112
                                    ]
                                ],
                                "15": [
                                    [
                                        113,
                                        120
                                    ]
                                ],
                            },
                            "type": "chairs"
                        }
                    ],
                    "svg": {
                        "source": "https://ticketscloud.org/s3/media.ticketscloud/production/map/2018-06/5b2930886e55b206059b7609.svg",
                        "map_main_svg": "https://ticketscloud.org/s3/media.ticketscloud/production/map/2018-06/5b2930886e55b206059b760a-5b2930886e55b206059b7609-main.svg",
                        "map_main_svgz": "https://ticketscloud.org/s3/media.ticketscloud/production/map/2018-06/5b2930886e55b206059b760a-5b2930886e55b206059b7609-main.svgz",
                        "map": "https://ticketscloud.org/s3/media.ticketscloud/production/map/2018-06/5b2930886e55b206059b760a-5b2930886e55b206059b7609-main.svg",
                        "mapz": "https://ticketscloud.org/s3/media.ticketscloud/production/map/2018-06/5b2930886e55b206059b760a-5b2930886e55b206059b7609-main.svgz"
                    }
                },
                "partners": {
                    "5b0286ce517565000d9cb1ca": {
                        "id": "5b0286ce517565000d9cb1ca",
                        "role": "org",
                        "name": "New organiser",
                        "desc": "Test",
                        "media": {},
                        "currency": "RUB",
                        "legal": {
                            "name": "\u041e\u0410\u041e \"\u041f\u0435\u0440\u0432\u0430\u044f \u0420\u0430\u0437\u0432\u043b\u0435\u043a\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044f\"",
                            "address": "\u0433. \u041c\u043e\u0441\u043a\u0432\u0430, \u0413\u0440\u0430\u0444\u0441\u043a\u0438\u0439 \u043f\u0435\u0440\u0435\u0443\u043b\u043e\u043a, \u0434\u043e\u043c 14, \u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 2, 4 \u044d\u0442\u0430\u0436",
                            "inn": "2345423521",
                            "ogrn": "3452340982112",
                            "ogrnip": null,
                            "type": "ru/ltd"
                        }
                    }
                },
                "payment_settings": {
                    "invoice": {
                        "type": "invoice",
                        "core": true,
                        "testing": false
                    },
                    "cloudpayments": {
                        "type": "cloudpayments",
                        "core": true,
                        "testing": true,
                        "merchant": "pk_aab8ffc2acac0d2bb3400671c832f",
                        "applepay_id": null
                    }
                },
                "tz": "Europe/Moscow",
                "ga_id": null,
                "ym_id": null,
                "fb_pixel": null,
                "vk_pixel": null,
                "has_promocodes": true,
                "kryptonite_send": false,
                "lang_switcher": true,
                "viral_promocodes_enabled": true
            }
