.. Defines how domains and emails are blacklisted

Emails
======

Overview
--------

Emails and domains are blacklisted to filter the people that contact us,
and are made available publicly through our :doc:`api/index`.

Blacklisting
------------

Blaclisted Emails
^^^^^^^^^^^^^^^^^

Blacklisted emails are defined within the ``BlacklistEmail`` model and can be turned
on and off with the ``BlacklistEmail.is_blocked`` attribute.

Blacklisted Domains
^^^^^^^^^^^^^^^^^^^

Domains can also be blacklisted within the ``BlacklistDomain`` model and can be turned
on and off with the ``BlacklistEmail.is_blocked`` attribute. Emails ending in this domain
will be blocked. Note that in order to escape blocking domains matching non-spam emails,
the entire domain must be matched. For example, in order to block ``@xgoogle.com``, the
domain should be ``xgoogle.com`` so that ``google.com`` is not blocked.

Contact Us
^^^^^^^^^^

The `Contact Us`_ page on the CodeDevils website filters emails using this mechanism.
Blacklisted domains and emails will be blocked from sending emails using this form.
