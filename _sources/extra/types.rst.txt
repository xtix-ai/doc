.. _extra/types/begin:

======================
Повторяющиеся сущности
======================


.. _extra/types/vevent:

VEVENT
======

Поле типа vevent, это строка в формате ``VEVENT`` из :rfc:`2445`.
В настоящий момент поддерживается только два значения: ``DTSTART`` и ``DTEND``. Значения указываются только в `UTC <https://goo.gl/QGpQCU>`_

Пример::

    BEGIN:VEVENT\r\n
    DTSTART;VALUE=DATE-TIME:20160124T160000Z\r\n
    DTEND;VALUE=DATE-TIME:20160124T173000Z\r\n
    END:VEVENT\r\n


.. _extra/types/media:

Media
=====

Различные медиа-данные имеют общий формат.

    :id:
    :author: id создателя
    :content_type: тип файла (например, "image/jpeg")
    :length: размер в байтах
    :md5hash: хеш md5 от содержимого
    :url: полный урл до файла

.. _extra/types/objectid:

ObjectId
========

Уникальный идентификатор в рамках сущности -- строка из 24 символов ([[a-zA-Z0-9])

.. _extra/types/isodatetime:

ISODatetime
===========

Строка, содержащая дату-время в формате ISO8601_

.. _ISO8601: https://www.cl.cam.ac.uk/~mgk25/iso-time.html
