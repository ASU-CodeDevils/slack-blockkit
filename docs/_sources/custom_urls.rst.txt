.. custom url template tags and management

Custom URLs
===========

The CodeDevils Network (CDN) is vast and includes tons of different websites
managing everything from team collaboration to software development. Custom
URLs are a means to keep track of all these URLs and utilize them on the
website.

Defining Custom URLs
--------------------

Navigate to the `admin console`_. Here you will be able to add custom urls.
You will have the following options:

* ``name`` - A familiar name for the link.
* ``url`` - The link
* ``slug`` - The identifying slug used for creating shortcuts, updating links, and obtaining them in the API.
* ``notify_in`` - The number of hours, days, or months until an officer is notified that this link needs to be updated. The default is 12.
* ``notify_interval`` - The notification interval in hours, days, or months. This will be coupled with the ``notify_in`` to send a notification to officers to update. The default is MONTHS.
* ``acknowledge`` - Whether or not this link has been acknowledged since the last notification.
* ``last_updated`` - The date this link was last updated.

Notifications
^^^^^^^^^^^^^

Notifications are defined by ``notify_in notify_interval``. For example, if ``notify_in`` is 12 and ``notify_interval``
is MONTHS, then the next notification is in 12 months.

Shortcuts
^^^^^^^^^

Custom shortcuts are automatically generated when a ``CustomUrl`` is created. Simply visit:

``https://codedevils.org/<slug>/``

Where the ``slug`` is the slug of the ``CustomUrl``.

.. _admin console: https://www.codedevils.org/en-us/admin/cd_url/customurl/