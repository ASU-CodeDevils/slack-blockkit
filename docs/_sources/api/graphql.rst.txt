.. GraphQL API documentation

GraphQL
=======

.. image:: data:image/png;base64,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
    :target: https://graphql.org/
    :alt: GraphQL

Overview
--------

`GraphQL`_ is a query language for APIs and aims to replace traditional RESTful APIs
with more flexiblility. It allows for dynamic requests that match the end user's needs
while providing standardized documentation all from a single endpoint.

Current Version
^^^^^^^^^^^^^^^

This is the first version of the CodeDevils GraphQL API. Unlike RESTful APIs, GraphQL
is serviced from a single endpoint (``/api/graphql``) and does not explicitly state
versions.

Schema
^^^^^^

All API access is over HTTPS, and accessed from `https://codedevils.org/api/graphql/`. As per
GraphQL standard, all data is sent and received as JSON.

All timestamps are returned in the format ``YYYY-MM-DDThh:mm:ss.nnnnnn+00:00``. All timestamps are in
UTC.

.. warning::

    The ``api/graphql/`` endpoint must end in a slash (``/``). Failing to do so will result in
    a ``500`` level status code.

.. _Authentication Overview:

Authentication
--------------

Authentication is done through ``Token`` authentication. To obtain a token, contact `our webmasters`_.
Provide the token in the header with each API request:

.. code::

    Authorization: Token XXXXXXXXX

Failed Authentication
^^^^^^^^^^^^^^^^^^^^^

Permission Denied
*****************

You will get a permission denied error message if you fail to pass a token:

.. code::

    {
        "errors": [
            "permission denied"
        ]
    }

Make sure your authorization is the header format specified in :ref:`Authentication Overview`.

Invalid token
*************

You will get an invalid token error message if the token you pass is invalid:

.. code::

    {
        "errors": [
            "Invalid token."
        ]
    }

To confirm your token, send your username to `our webmasters`_ and they will confirm
your token.

Usage
-----

Documentation
^^^^^^^^^^^^^

The most recent documentation can be found through our `GraphiQL`_ page. Here you can check
out query and mutation documentation, as well as run live tests and one-off queries.

Relay
^^^^^

The CodeDevils GraphQL uses the Relay server standard to handle pagination. Not all nodes
require the pagination as it only becomes effective with larger datasets (i.e. users), but
is used regardless to keep things standardized.

You can learn more about Relays with this `GraphQL relay tutorial`_. Think of relays as
linked lists. Relays are enabled for all ``NodeConnection`` classes. Take for example
the ``CustomUrlNodeConnection``:

.. code::

    links(before: String
          after: String
          first: Int
          last: Int
          name: String
          name_Icontains: String
          name_Istartswith: String
          slug: String
    ): CustomUrlNodeConnection

The ``before: String``, ``after: String``, ``first: Int``, and ``last: Int`` are filters
that can be used to navigate the nodes:

* ``before: String`` - Filter all objects before a given ID.
* ``after: String`` - Filter all objects after a given ID.
* ``first: Int`` - Get the first # number of results.
* ``last: Int`` - Get the last # number of results.

A ``CustomUrlNodeConnection`` has 2 components:

* ``pageInfo: PageInfo!`` - Pagination data for this connection.
* ``edges: [CustomUrlNodeEdge]!`` - Contains the nodes in this connection. This is the actual data.

The ``pageInfo`` class contains navigation to navigate between ``edges``:

.. code::

    domains {
        pageInfo {
            hasNextPage
            hasPreviousPage
            startCursor
            lastCursor
        }
    }

This helps with traversing the edges:

* ``hasNextPage: Boolean!`` - When paginating forwards, are there more items?
* ``hasPreviousPage: Boolean!`` - When paginating backwards, are there more items?
* ``startCursor: String`` - When paginating backwards, the cursor to continue.
* ``endCursor: String`` - When paginating forwards, the cursor to continue.

The edges themselves are where the nodes (or the data) are:

.. code::

    domains {
        edges {
            cursor
            node {
                id
                name
                url
                slug
            }
        }
    }

The ``cursor`` is the base-64 ID of the object and is used to navigate through the edges. The previous 
``before``, ``after``, ``startCursor``, and ``endCursor`` are references to these cursor objects. Use
them to navigate the edges. Say for example we want to grab all the links over multiple pages. The first
request should look something like:

.. code::

    {
        links(first: 2) {
            pageInfo {
                hasNextPage
            }
            edges {
                cursor
                node {
                    name
                    slug
                    url
                }
            }
        }
    }

The result comes out to:

.. code:: json

    {
        "data": {
            "links": {
                "pageInfo": {
                    "hasNextPage": true
                },
                "edges": [
                    {
                        "cursor": "YXJyYXljb25uZW0aW9uOjA=",
                        "node": {
                            "name": "Documentation",
                            "slug": "documentation",
                            "url": "https://asu-codedevils.github.io/codedevils_org/"
                        }
                    },
                    {
                        "cursor": "YXJyYXljb25uZW0aW9uOjE=",
                        "node": {
                            "name": "GitHub",
                            "slug": "github",
                            "url": "https://github.com/ASU-CodeDevils/"
                        }
                    }
                ]
            }
        }
    }

Then subsequent requests should take the last cursor (this case is ``"YXJyYXljb25uZW0aW9uOjE="``) and
make it the ``after`` parameter in ``links`` until ``hasNextPage`` is equal to ``false``:

.. code::

    {
        links(first: 2, after: "YXJyYXljb25uZW0aW9uOjE=") {
            pageInfo {
                hasNextPage
            }
            edges {
                cursor
                node {
                    name
                    slug
                    url
                }
            }
        }
    }

Continue this until ``hasNextPage`` is ``false``. This is a basic query. For more information, check
out this `GraphQL relay tutorial`_.

Development
-----------

There are many resources when working with GraphQL. Some of our preferred methods:

* `GraphiQL`_ - The CodeDevils documentation and GraphQL UI.
* `GraphQL Playground`_ - An intuitive GraphQL UI that allows enhanced features on top of `GraphiQL`_.
* `Postman`_ - For those already familiar with Postman, it offers the same Postman architecture with GraphQL-specific body styling.


.. _`GraphQL`: https://graphql.org/
.. _`GraphiQL`: https://codedevils.org/api/graphql/
.. _`GraphQL Playground`: https://github.com/prisma-labs/graphql-playground
.. _`GraphQL relay tutorial`: https://docs.graphene-python.org/projects/django/en/latest/tutorial-relay/
.. _`Postman`: https://www.postman.com/
.. _`our webmasters`: mailto:webmaster@codedevils.org?subject=Obtain%20Access%20Token