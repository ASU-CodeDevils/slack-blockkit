block_element
=============

Block elements can be used inside of ``section``, ``context``, and ``actions`` layout blocks.
Inputs can only be used inside of input blocks.

This overview of `app surfaces that support Block Kit`_ shows you where add blocks.

Finally, our `handling user interactivity guide`_ will help you prepare your app to allow for the
use of the interactive components listed below.

You can see the `full Slack documentation`_ on block elements to see examples and the most up-to-date styling information.

.. _`full Slack documentation`: https://api.slack.com/reference/block-kit/block-elements

.. _`app surfaces that support Block Kit`: https://api.slack.com/messaging/composing/layouts
.. _`handling user interactivity guide`: https://api.slack.com/interactivity/handling

BlockElement
------------

.. autoclass:: slack_blockkit.block_element.BlockElement
    :members:

ButtonElement
-------------

.. autoclass:: slack_blockkit.block_element.ButtonElement
    :members:

PrimaryButtonElement
--------------------

.. autoclass:: slack_blockkit.block_element.PrimaryButtonElement
    :members:

DangerButtonElement
-------------------

.. autoclass:: slack_blockkit.block_element.DangerButtonElement
    :members:

DefaultButtonElement
--------------------

.. autoclass:: slack_blockkit.block_element.DefaultButtonElement
    :members:

DatepickerElement
-----------------

.. autoclass:: slack_blockkit.block_element.DatepickerElement
    :members:

ImageElement
------------

.. autoclass:: slack_blockkit.block_element.ImageElement
    :members:

OverflowElement
---------------

.. autoclass:: slack_blockkit.block_element.OverflowElement
    :members:

PlainTextInputElement
---------------------

.. autoclass:: slack_blockkit.block_element.PlainTextInputElement
    :members:

RadioButtonGroupElement
-----------------------

.. autoclass:: slack_blockkit.block_element.RadioButtonGroupElement
    :members:
