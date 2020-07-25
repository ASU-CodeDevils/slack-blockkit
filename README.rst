Slack Blockkit Builder
======================

.. image:: https://travis-ci.com/ASU-CodeDevils/slack-blockkit.svg?branch=master
    :target: https://travis-ci.com/ASU-CodeDevils/slack-blockkit
    :alt: Build
.. image:: https://codecov.io/gh/ASU-CodeDevils/slack-blockkit/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ASU-CodeDevils/slack-blockkit
    :alt: Codecov
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
    :alt: Black code style
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT
    :alt: License
.. image:: https://img.shields.io/badge/chat-slack-pink.svg
    :target: https://codedevils.slack.com/archives/GPNBSDM27
    :alt: Slack

Slack Blockkit Builder is a simple utility for developing code blocks for `Slack's Block Kit`_. It provides
Pythonic-style blocks to allow for dynamic generation of block kits where copy-and-paste just won't do it.

Visit the `documentation`_ for more examples and method/class docs.

Installation
------------

Installation is as easy as:

.. code:: bash

    pip install slack_blockkit

It is currently tested on Python3+, but can be used for Python 2.7.

Usage
-----

Categories
**********

`Slack's Block Kit`_ comes with 4 different block categories:

1. `Block elements`_ - The standard element of a block.
2. `Composition objects`_ - Composition objects can be used inside of block elements and certain message payload fields. They are simply common JSON object patterns that you'll encounter frequently when building blocks or composing messages.
3. `Interactive components`_ - Interactive components are a subset of Block Kit elements that add interactivity to various app surfaces.
4. `View payloads`_ - Views are app-customized visual areas within modals and Home tabs.

.. warning::

    Some interactive components are not implemented in version 0.0.4

Example Usage
*************

You can access the different components by importing them from their respective package. For example, `Block elements`_
can be accessed by importing ``from slack_blockkit.block_element import ...``. A common block element is the ``TextObject``:

.. code-block:: python

    from slack_blockkit.block_element import TextObject

    text_object = TextObject(btype="mrkdwn", text="This is a text block")

Blocks are inserted into a list as dicts. Each component comes with a `render()` method which will return a ``dict``:

.. code-block:: python

    text_object.render()  # {"type": "mrkdwn", "text": "This is a text block"}

.. note::

    **btype** in synonymous with Slack's **type**. **type** is reserved in Python.

Message Blocks
**************

Message payloads to Slack take a ``list`` of dictionaries. The ``slack_blockkit.utils`` module has a ``get_blocks``
method that takes Block objects and returns the formatted list:

.. code-block:: python

    from slack_blockkit.utils import get_blocks
    from slack_blockkit.text_object import TextObject
    from slack_blockkit.layout_block import DividerBlock, ImageBlock

    blocks = get_blocks(
        TextObject(btype="mrkdwn", text="Welcome to CodeDevils!"),
        DividerBlock(),
        ImageBlock(image_url="https://codedevils.org/static/img/logo", alt_text="Logo")
    )

Which makes ``blocks``:

.. code-block:: python

    {
        "type": "mrkdwn",
        "text": "Welcome to CodeDevils!"
    },
    {
        "type": "divider"
    },
    {
        "type": "image",
        "image_url": "https://codedevils.org/static/img/logo",
        "alt_text": "Logo"
    }

Online Message Blocks
*********************

Alternatively you can use the ``test_blocks_online`` if you want to test your blocks before
publishing them. The utility takes the blocks you input as arguments and creates a link that
takes you to `Slack's block kit builder`_. An example is:

.. code-block:: python

    from slack_blockkit.layout_block import SectionBlock
    from slack_blockkit.composition_object import PlainTextObject
    from slack_blockkit.utils import test_blocks_online

    section1 = SectionBlock(text=PlainTextObject(text="Section 1"))
    section2 = SectionBlock(text=PlainTextObject(text="Section 2"))
    test_blocks_online(section1, section2)

This will print out to the console:

.. code-block:: bash

    Copy and paste the following url into your browser:

        https://app.slack.com/block-kit-builder/#{"blocks": [{"block_id": "96dc84a2-d517-4a75-ab83-193770df62cc", "text": {"text": "Section 1", "emoji": false, "type": "plain_text"}, "type": "section"}, {"block_id": "182c3fc6-3d7b-464e-8fb9-0fb832e8cd02", "text": {"text": "Section 2", "emoji": false, "type": "plain_text"}, "type": "section"}]}

Copy and pasting this into your browser will open up `Slack's block kit builder`_ with the blocks
you created. 

Utils
*****

Common composite blocks are implemented for you in ``slack_blockkit.utils`` and include:

* ``get_task_block`` - Returns a task block, which is comprised of a paragraph of text followed by an information link at the bottom.
* ``get_text_block_with_image`` - Returns a text block with an image to the right of it.
* ``get_text_block_with_accessory`` - Returns a text block with an accessory.
* ``get_information_block`` - Returns an information block, which is a section with an info icon followed by linked text.
* ``get_checkmark`` - *Not* a block, but rather an emoji string for a checkmark. Pass ``True`` for a checked mark and ``False`` for unchecked.

.. _`documentation`: https://asu-codedevils.github.io/slack-blockkit/
.. _`Block elements`: https://api.slack.com/reference/block-kit/block-elements
.. _`Interactive components`: https://api.slack.com/reference/block-kit/interactive-components
.. _`Composition objects`: https://api.slack.com/reference/block-kit/composition-objects
.. _`View payloads`: https://api.slack.com/reference/block-kit/views
.. _`Slack's Block Kit`: https://api.slack.com/block-kit
.. _`Slack's block kit builder`: https://app.slack.com/block-kit-builder/
