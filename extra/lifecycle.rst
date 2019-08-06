.. _extra/lifecycle/begin:

=====================
Жизненный цикл заказа
=====================

.. _extra/lifecycle/diagram_simple:

Список состояний (статусов) заказа без платежей
==================================================

.. _extra/lifecycle/executed:

executed
--------

Заказ всегда создаётся в статусе executed.
Через 10 минут, заказ в этом состоянии переходит в :ref:`expired <extra/lifecycle/expired>`

С заказом в состоянии executed возможны следующие :ref:`действия <extra/orders/begin>`:

    - :ref:`забронировать билеты <walkthrough/order_create/tickets>`
    - :ref:`добавить информацию о покупателе <extra/orders/customer>`
    - :ref:`изменить параметр send_tickets <extra/orders/send_tickets>`
    - :ref:`добавить произвольные поля в заказ <extra/orders/vendor_data>`
    - :ref:`отменить <walkthrough/order_finish/status>`
    - :ref:`перевести в статус done <extra/lifecycle/done>`


.. _extra/lifecycle/done:

done
----

Заказ в этом статусе уже оплачен.


.. _extra/lifecycle/cancelled:

cancelled
---------

Заказ отменён.


.. _extra/lifecycle/expired:

expired
-------

Заказ просрочен, забронированные билеты снова вернулись в продажу.
