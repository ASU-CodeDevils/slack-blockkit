layout_block
============

Blocks are a series of components that can be combined to create visually rich and compellingly interactive messages.

Read our guide to `building block layouts`_ to learn where and how to use each of these components. You can include 
up to 50 blocks in each message, and 100 blocks in modals or home tabs.

You can see the `full Slack documentation`_ on layout blocks to see examples and the most up-to-date styling information.

.. note::

    A ``block_id`` can be specified for all layout block objects. If one is not specified, a randomly-generated UUID (v4)
    will be assigned. UUID v1 poses security risks as it exposes the MAC address of the server. For more about the
    differences in the 2 versions, read `this blog`_.

.. _`building block layouts`: https://api.slack.com/block-kit/building
.. _`full Slack documentation`: https://api.slack.com/reference/block-kit/blocks
.. _`this blog`: https://www.sohamkamani.com/blog/2016/10/05/uuid1-vs-uuid4/

LayoutBlock
-----------

.. autoclass:: slack_blockkit.layout_block.LayoutBlock
    :members:

ActionsBlock
------------

.. autoclass:: slack_blockkit.layout_block.ActionsBlock
    :members:

ContextBlock
------------

.. autoclass:: slack_blockkit.layout_block.ContextBlock
    :members:

DividerBlock
------------

.. autoclass:: slack_blockkit.layout_block.DividerBlock
    :members:

FileBlock
---------

.. autoclass:: slack_blockkit.layout_block.FileBlock
    :members:

ImageBlock
----------

.. autoclass:: slack_blockkit.layout_block.ImageBlock
    :members:

InputBlock
----------

.. autoclass:: slack_blockkit.layout_block.InputBlock
    :members:

SectionBlock
------------

.. autoclass:: slack_blockkit.layout_block.SectionBlock
    :members:

