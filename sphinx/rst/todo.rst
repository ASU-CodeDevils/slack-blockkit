To Do
=====

Just some recommendations to make this whole thing better!

.. todo::

    Implement remaining interactive components in `Slack's Block Kit`_.

    There are still some interactive components that are a bit more complex than the standard
    ones provided here.

.. todo::

    Use ``__setattr__`` instead of ``__init__`` for type validation.

    Type validation is done during ``__init__``, and therefore will only validate attributes once
    the object is created. Changing it to ``__setattr__`` will validate types on every update to
    the object. 

.. todo::

    Finish implementing more concrete type validation.

    Type validation is inconsistent. Right now there is validation in a couple different places,
    but it's not complete and won't make creating more block types any easier. Finish that to make
    attribute validation easier.

.. todo::

    Implement more utils for faster block generation.

    Current block utilities are shaky at best. Create more and make all of them more consistent.

.. todo::

    More documentation!

    More documentation on how everything works wouldn't hurt!

.. _`Slack's Block Kit`: https://api.slack.com/block-kit
