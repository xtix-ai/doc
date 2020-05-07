.. _extra/refunds_list/begin:

===========================
Работа со списком возвратов
===========================


.. _extra/refunds_list/get:


Получаем список возвратов
=========================

**Запрос**

.. http:get:: /v2/resources/refund_requests

    :query created_at: Дата создания возврата, :ref:`isodatetime <extra/types/isodatetime>` промежуток через запятую
    :query finished_at: Дата завершения возврата, :ref:`isodatetime <extra/types/isodatetime>` промежуток через запятую
    :query events: Фильтр по списку мероприятий
    :query status: Фильтр по списку статусов возратов (new | in_progress | approved | rejected)
    :query page: Порядковый номер страницы результатов запроса (по умолчанию -- первая)
    :query page_size: Кол-во записей на страницу результатов запроса (минимум 1, максимум 200, по умолчанию 50)


**Пример запроса**

    .. sourcecode:: http

        GET /v2/resources/refund_requests?created_at=2018-01-01T00:00:00,2019-07-01T00:00:00&events=5b23b53b9c9b19000c6c4180 HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d


**Пример ответа**

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": [
                {
                    "created_at": "2018-07-24 13:26:00",
                    "culprit": "user",
                    "delta": "13500.00",
                    "event": "5b23b53b9c9b19000c6c4180",
                    "refund_nominal" "13500.00",
                    "finished_at": "2018-07-24 13:26:14",
                    "id": "5b5728e886e7040069eb7f86",
                    "order": "5b57281886e704000b424741",
                    "org": "5b0286ce517565000d9cb1ca",
                    "policy": "general",
                    "status": "approved",
                    "tickets": [
                        ...
                    ],
                    "vendor": "5b0286ce517565000d9cb1ca"
                },
                ...
            ],
            "pagination": {
                "page": 1,
                "page_size": 50,
                "total": 1
            },
            "refs": {
                "events": {
                    ...
                },
                "orders": {
                    ...
                },
                "partners": {
                    ...
                },
                "tickets": {
                    ...
                }
            }
        }
