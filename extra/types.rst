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

