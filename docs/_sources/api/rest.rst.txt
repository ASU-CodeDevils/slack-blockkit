.. REST API documentation

REST API
========

Overview
--------

You can use CodeDevils REST API to obtain and utilize the data needed to integrate seamlessly
with CodeDevils.

.. note::

    It is recommended you use the :doc:`GraphQL API <graphql>` as it providers greater flexibility
    and lower latency. This API is maintained for existing technologies that only support
    RESTful APIs.

Current Version
^^^^^^^^^^^^^^^

This is the first version of the CodeDevils REST API, and therefore is not explicitly labeled
in the URL.

Schema
^^^^^^

All API access is over HTTPS, and accessed from `https://codedevils.org/api/`. All data is sent
and received as JSON. Blank fields are marked as ``null`` instead of being ommitted.

All timestamps are returned in the format ``YYYY-MM-DDThh:mm:ss.nnnnnnZ``. All timestamps are in
UTC.

.. warning::

    All ``POST``, ``PUT``, and ``PATCH`` requests need to end with a slash. Failing to do so will result
    in a ``500`` level status code.

Authentication
--------------

Authentication is done through ``Token`` authentication. To obtain a token, contact `our webmasters`_.
Provide the token in the header with each API request:

.. _`our webmasters`: mailto:webmaster@codedevils.org?subject=Obtain%20Access%20Token

.. code::

    Authorization: Token XXXXXXXXX

An example request:

.. code:: bash

    curl --location --request GET 'https://codedevils.org/api/test' \
        --header 'Authorization: Token XXXXXXXXX'

Obtain a Token
^^^^^^^^^^^^^^

Tokens can be obtained with a ``POST`` request to the ``api/auth-token`` endpoint with your
username and password provided by a Webmaster.

.. code:: bash

    curl --location --request POST 'https://codedevils.org/api/auth-token/' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "username": "<your username>",
            "password": "<your password>"
        }'

Failed Authentication
^^^^^^^^^^^^^^^^^^^^^

Authentication credentials were not provided
********************************************

If no token is provided, a ``401`` status code will be returned with the body:

.. code:: json

    {
        "detail": "Authentication credentials were not provided."
    }

Invalid token
*************

If the API key is invalid, a ``401`` status code will be returned with the body:

.. code:: json

    {
        "detail": "Invalid token."
    }

Usage
-----

Documentation
^^^^^^^^^^^^^

Use our `Swagger Documentation`_ to see a full list of available APIs.

Pagination
^^^^^^^^^^

List views (views named ending in ``_list`` on the `Swagger Documentation`_ page come with offset
pagination. Pagination by default includes 100 records per call and links to the next set of
corresponding records (stored in ``next``) and previous set (stored in ``previous``):

.. code-block:: json
   :emphasize-lines: 3,4

    {
        "count": 200,
        "next": "https://codedevils.org/api/links/?offset=2",
        "previous": null,
        "results": [
            
        ]
    }

You can specify the number of results by passing a ``limit`` parameter:

.. code::

    https://codedevils.org/api/links/?limit=10

This will decrease pagination to 10 records per call (or whatever number you specify).

.. _`Swagger Documentation`: https://codedevils.org/api/docs/