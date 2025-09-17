===============
Базовые понятия
===============

.. note:: Для интеграции вам необходимо пройти `регистрацию`_
    и `заключить`_ сделку с организатором мероприятия

.. _регистрацию: https://support.xtix.ai/%D0%B4%D0%BB%D1%8F-%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D0%B5%D0%B9/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F
.. _заключить: https://support.xtix.ai/%D0%B4%D0%BB%D1%8F-%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D0%B5%D0%B9/%D0%BA%D0%B0%D0%BA-%D0%B7%D0%B0%D0%BA%D0%BB%D1%8E%D1%87%D0%B0%D1%82%D1%8C-%D1%81%D0%B4%D0%B5%D0%BB%D0%BA%D0%B8-%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D0%B8%D1%8F-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%B1%D0%B8%D0%BB%D0%B5%D1%82%D0%BE%D0%B2



.. _walkthrough/basics/begin:

XTIX API построено с учетом `REST` с авторизацией по API ключу.
В теле запросов и ответов используется `JSON`.

Для демонстрации запросов к API используется утилита `HTTPie`_

.. _HTTPie: https://httpie.org/



.. _walkthrough/basics/prefixes:

Основные URL
=============

Все ссылки на запросы к API в данной документации обращаются к основному URL:

`https://hub.xtix.ai`

Для облегчения интеграции и отладки существует также стейдж сервер:

`https://hub.xtix.dev/`


.. _walkthrough/basics/authorization:

Авторизация
============

Для авторизации в заголовке :http:header:`Authorization` передаётся ключ с префиксом `key`.

Пример запроса:

    .. sourcecode:: http

        GET /v2/resources/orders HTTP/1.1
        Authorization: key 9bd8359943b545500278875r49c5b96d

Пример ответа:

    .. sourcecode:: js

        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "data": [
                ...
            ],
            "pagination": {
                ...
            },
            "refs": {
                ...
            }
        }

.. warning::
    Все запросы к API осуществляются только через `HTTPS`.
    Запросы через `HTTP` будут отклонены со статусом :http:statuscode:`301`.
