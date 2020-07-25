composition_object
==================

Composition objects can be used inside of block elements and certain message payload fields. 
They are simply common JSON object patterns that you'll encounter frequently when building blocks
or composing messages.

The guide to Block Kit in app surfaces shows you where you can use blocks.

You can see the `full Slack documentation`_ on composition objects to see examples and the most up-to-date styling information.

.. _`full Slack documentation`: https://api.slack.com/reference/block-kit/composition-objects

TextObject
----------

.. autoclass:: slack_blockkit.composition_object.TextObject
    :members:

PlainTextObject
---------------

.. autoclass:: slack_blockkit.composition_object.PlainTextObject
    :members:

MarkdownTextObject
------------------

.. autoclass:: slack_blockkit.composition_object.MarkdownTextObject
    :members:

ConfirmObject
-------------

.. autoclass:: slack_blockkit.composition_object.ConfirmObject
    :members:

OptionObject
------------

.. autoclass:: slack_blockkit.composition_object.OptionObject
    :members:

OptionGroupObject
-----------------

.. autoclass:: slack_blockkit.composition_object.OptionGroupObject
    :members:
