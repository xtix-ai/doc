===============
Базовые понятия
===============

.. note:: Для интеграции вам необходимо пройти `регистрацию`_ 
    и `заключить`_ сделку с организатором мероприятия

.. _регистрацию: http://support.ticketscloud.org/%D0%B4%D0%BB%D1%8F-%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D0%B5%D0%B9/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F
.. _заключить: http://support.ticketscloud.org/%D0%B4%D0%BB%D1%8F-%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D0%B5%D0%B9/%D0%BA%D0%B0%D0%BA-%D0%B7%D0%B0%D0%BA%D0%BB%D1%8E%D1%87%D0%B0%D1%82%D1%8C-%D1%81%D0%B4%D0%B5%D0%BB%D0%BA%D0%B8-%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D0%B8%D1%8F-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%B1%D0%B8%D0%BB%D0%B5%D1%82%D0%BE%D0%B2



.. _walkthrough/basics/begin:

Ticketscloud API построено с учетом :term:`REST`. 
С авторизацией через :term:`HTTP Basic Auth`.
В теле запросов и ответов используется :term:`JSON`. 
Для демонстрации запросов к API используется утилита `HTTPie`_

.. _HTTPie: https://httpie.org/



.. _walkthrough/basics/prefixes:

Основные URL
=============

Все ссылки на запросы к API в данной документации оюращаются к основному URL:
`https://ticketscloud.com`

Для облегчения интеграции и отладки существует также стейдж сервер:
`https://stage.freetc.net`


.. _walkthrough/basics/authorization:

Авторизация
============

Для авторизации по ключу, значение заголовка 
:http:header:`Authorization` имеет префикс `key`

Пример запроса:

    .. sourcecode:: http

       http GET https://ticketscloud.com/v2/resources/orders?number=52899 Authorization:'key 9bd8359943b545500278875r49c5b96d'

.. warning::
    Все запросы к API осуществляются только через :term:`HTTPS`.
    Запросы через :term:`HTTP` будут отклонены со статусом :http:statuscode:`301`.

