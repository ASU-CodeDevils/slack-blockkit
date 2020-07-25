Module Documentation
====================

Modules in this project are based on the `Slack Block kit`_ . Pretty much all classes
(save the utility modules) have a one-to-one relationship with components of the block
kit.

All documentation is replicated from `Slack's block kit home page`_. Please visit
their documentation for all the most recent updates for all versions following this
documentation release. 

.. note::

   ``btype`` is synonymous with Slack's ``type``. Since ``type`` is a reserved keyword
   in Python, ``btype`` is used in its place in all block component modules. Once the
   block is rendered, this is replaced with the correct ``type`` component in the
   rendered dict.

.. toctree::
   :maxdepth: 2
   :caption: Modules:

   block
   block_element
   composition_object
   layout_block
   view_payload
   utils/index

.. _`Slack Block kit`: https://api.slack.com/block-kit
.. _`Slack's block kit home page`: https://api.slack.com/block-kit
