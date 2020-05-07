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
Ограничить выдачу можно указанием параметров `page` и `page_size`: например, `page=2&page_size=3` вернёт мероприятия с 4-го по 6-е включительно.
Если указать `page_size` без `page`, вернётся первая страница.

**Запрос**:

    .. sourcecode:: js

        GET /v1/services/simple/events


**Ответ**:

    - ``id`` **str**::ref:`objectid <extra/types/objectid>` - id мероприятия
    - ``created_at`` **str**::ref:`isodatetime <extra/types/isodatetime>` - дата создания
    - ``updated_at`` **str**::ref:`isodatetime <extra/types/isodatetime>` - дата последнего изменения
    - ``lifetime`` **str**:*VEVENT*  - :ref:`vevent <extra/types/vevent>`, время проведения мероприятия (для отображения покупателям необходима поправка на часовой пояс места проведения)
    - ``status`` **str** - текущий статус мероприятия. `public` — публичное мероприятие, можно продавать билеты)
    - ``age_rating`` **int** - возрастное ограничение

    - ``deal`` **object** информация о сделке

       - ``org`` **str** - доля организатора
       - ``agent`` **str** - доля агента
       - ``extra`` **str** - сервисный сбор распространителя
       - ``media`` **list of string** - список ссылкок на медиа

    - ``partner`` **object** информация о партнере

       - ``id`` **str**::ref:`objectid <extra/types/objectid>` - id партнера
       - ``desc`` **str** - описание партнера
       - ``media`` **object** - медиа партнера
       - ``name`` **str** - имя партнера
       - ``tags`` **list of string** - теги категорий партнера
       - ``contact`` **object** - контактная информация
          - ``address`` **str** - адрес партнера
          - ``email`` **str** - электронная почта партнера
          - ``name`` **str** - имя контакта партнера
          - ``phones`` **str** - телефон партнера
          - ``www`` **str** - сайт партнера

    - ``tags`` **list of string** - теги
    - ``tickets_amount`` **int** - общее количество билетов
    - ``tickets_amount_vacant`` **int** - количество доступных для продажи билетов

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

    - ``legal_detail``: **object** юридическая информация

        - ``name`` **str** - название юр.лица
        - ``inn`` **str** - ИНН
        - ``ogrn`` **str** - ОГРН (опционален)
        - ``ogrnip`` **str** - ОГРНИП (опционален)
        - ``address`` **str** - юридический адрес

    - ``venue`` место проведения
      
       - ``id`` **str**::ref:`objectid <extra/types/objectid>`
       - ``address`` **str** - адрес
       - ``country`` страна
          - ``id`` **str** - буквенное короткое латинское название
          - ``name`` - ассоциативный массив названий на разных языках
       - ``city`` город
          - ``id`` **int**
          - ``country`` **str** - id страны
          - ``name`` - ассоциативный массив названий на разных языках
          - ``timezone`` **str** - временная зона
       - ``name`` **str** - название
       - ``desc`` **str** - краткое описание
       - ``point`` координата (`GeoJSON <http://geojson.org>`_'s point)
          - ``coordinates`` **list** список двух вещественных координат
          - ``type`` **str** - тип

    - ``map`` схема зала

    - ``sets`` билетные категории

       - ``id`` **str**::ref:`objectid <extra/types/objectid>`
       - ``pos`` **int** - порядковый номер категории (для сортировки)
       - ``name`` **str** - название категории
       - ``desc`` **str** - описание категории
       - ``amount`` **int** - общее количество билетов в сете
       - ``amount_vacant`` **int** - количество билетов, доступных для продажи
       - ``price_org`` **str**:*Money* - номинальная цена билета
       - ``price_extra`` **str**:*Money* - сервисный сбор
       - ``price`` **str**:*Money* - общая цена билета
       - ``with_seats`` **bool** - наличие посадочных мест в категории
       - ``seats`` **object** - row: numbers (**list**)
       - ``sector`` сектор

       - ``rules`` список правил
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

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        [
            {
                "age_rating": 21,
                "allow_other_ps": false,
                "created_at": "2019-07-19T17:20:29.717000+00:00",
                "deal": {
                    "agent": "5%",
                    "extra": "4%",
                    "media": [],
                    "org": "95%"
                },
                "id": "5d31fbdd27649b0dff076117",
                "lifetime": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20190815T212000Z\r\nDTEND;VALUE=DATE-TIME:20190828T215000Z\r\nEND:VEVENT\r\n",
                "map": null,
                "media": {},
                "org": {
                    "contact": {
                        "address": "Greek",
                        "email": "mail_org@ticketscloud.org",
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
                    "name": "My best org",
                    "tags": [
                        "Театры",
                        "Выставки",
                        "Здоровье",
                        "Детям",
                        "Вечеринки",
                        "Музеи",
                        "Экскурсии",
                        "Бизнес",
                        "Спорт",
                        "Балет"
                    ]
                },
                "partner": {
                    "contact": {
                        "address": "г. Москва, Графский переулок, дом 14, строение 2, 4 этаж",
                        "email": "mail_partner@ticketscloud.org",
                        "name": null,
                        "phones": [
                            "+79123456789"
                        ],
                        "www": "funkyfunky.ru"
                    },
                    "desc": null,
                    "id": "5b02d6e9517565000d9cb1ce",
                    "media": {},
                    "name": "Rasp new",
                    "tags": []
                },
                "sets": [
                    {
                        "amount": 50,
                        "amount_vacant": 50,
                        "desc": "",
                        "id": "5d31fbfa27649b0dff07611b",
                        "name": "обычные",
                        "pos": 0,
                        "price": "104.00",
                        "price_extra": "4.00",
                        "price_org": "100.00",
                        "rules": [
                            {
                                "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20190722T210000Z\r\nDTEND;VALUE=DATE-TIME:20190828T215000Z\r\nEND:VEVENT\r\n",
                                "current": false,
                                "id": "5d31fc1a306fdcc187b911b4",
                                "price": "156.00",
                                "price_extra": "6.00",
                                "price_org": "150.00"
                            },
                            {
                                "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20190717T210000Z\r\nDTEND;VALUE=DATE-TIME:20190722T205900Z\r\nEND:VEVENT\r\n",
                                "current": true,
                                "id": "5d31fc1a306fdcc187b911b5",
                                "price": "104.00",
                                "price_extra": "4.00",
                                "price_org": "100.00"
                            }
                        ],
                        "seats": null,
                        "sector": null,
                        "with_seats": false
                    },
                    {
                        "amount": 10,
                        "amount_vacant": 10,
                        "desc": "",
                        "id": "5d31fbfa8a75c12c9d64de13",
                        "name": "VIP",
                        "pos": 0,
                        "price": "1092.00",
                        "price_extra": "42.00",
                        "price_org": "1050.00",
                        "rules": [
                            {
                                "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20190717T210000Z\r\nDTEND;VALUE=DATE-TIME:20190726T205900Z\r\nEND:VEVENT\r\n",
                                "current": true,
                                "id": "5d31fc26306fdcc187b911b8",
                                "price": "1092.00",
                                "price_extra": "42.00",
                                "price_org": "1050.00"
                            },
                            {
                                "cal": "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE-TIME:20190726T210000Z\r\nDTEND;VALUE=DATE-TIME:20190828T215000Z\r\nEND:VEVENT\r\n",
                                "current": false,
                                "id": "5d31fc26306fdcc187b911b9",
                                "price": "1560.00",
                                "price_extra": "60.00",
                                "price_org": "1500.00"
                            }
                        ],
                        "seats": null,
                        "sector": null,
                        "with_seats": false
                    }
                ],
                "status": "public",
                "tags": [
                    "Балет"
                ],
                "ticket_template": {
                    "fan_cover_url": null,
                    "name": null,
                    "text_color": null
                },
                "tickets_amount": 60,
                "tickets_amount_vacant": 60,
                "title": {
                    "desc": "1",
                    "text": "1234567890"
                },
                "updated_at": "2019-07-19T17:21:42.409000+00:00",
                "venue": {
                    "address": "ул. Воздвиженка, д.1",
                    "city": {
                        "country": "RU",
                        "id": 524901,
                        "name": {
                            "af": "Moskou",
                            "als": "Moskau",
                            "am": "ሞስኮ",
                            "an": "Moscú",
                            "yi": "מאָסקװע",
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
                    "desc": "",
                    "id": "5540add49cb5385eeef17b4d",
                    "name": "Государственный Кремлевский Дворец",
                    "point": {
                        "coordinates": [
                            37.615342140197754,
                            55.75146296066621
                        ],
                        "type": "Point"
                    }
                }
            },
            ...
        ]


.. _walkthrough/events/tickets:

Получаем список билетов с местами по мероприятию
================================================


Получение списка билетов мероприятия для категорий с рассадкой.

**Запрос**

    .. http:get:: /v1/resources/events/:id/tickets

       :query status: Фильтр-список по списку статусов (``vacant`` | ``reserved`` | ``sold`` | ``pending``). По умолчанию включены билеты во всех статусах, кроме ``pending``.
       :query sector: Фильтр-список по списку секторов

       Постраничной выдачи для этого запроса не предусмотрено.


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
