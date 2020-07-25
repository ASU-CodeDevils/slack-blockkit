.. Instructions on how to update language settings and translations.

Languages
=========

CodeDevils is a world-wide organization, so we offer translations of the
website where ever possible to make communication easier.

Supported Languages
-------------------

* Arabic (`ar`)
* English - US (`en-us`) *default*
* French (`fr`)
* Hindi (`hi`)
* Spanish (`es`)

Translating the Project
-----------------------

Languages are defined as locales in the project 
`base settings module <https://github.com/ASU-CodeDevils/codedevils_org/blob/master/config/settings/base.py>`.
The default is set to `en-us`:

.. code:: python

    LANGUAGE_CODE = env("DJANGO_LANGUAGE_CODE", default="en-us")

You can change it by setting the `DJANGO_LANGUAGE_CODE` in your environment file. Languages
available are located just below that in `LANGUAGES`:

.. code:: python

    LANGUAGES = [
        ("es", _("Spanish")),
        ("en-us", _("English")),
        ("fr", _("French")),
        ("ar", _("Arabic")),
        ("nl", _("Dutch")),
        ("hi", _("Hindi"))
    ]

Locale translations
-------------------

Property Object (PO) hold translations for each of the languages.

::

    locale
    ├── ar
    │   └── LC_MESSAGES
    │       ├── django.mo
    │       └── django.po
    ├── es
    ├── fr      
    ├── hi
    ├── nl
    └── README.rst

Update Translations
^^^^^^^^^^^^^^^^^^^

Each update to one of the templates requires you to update the corresponding translation.
You can do so locally by visiting the `rosetta/` endpoint. Here will give you the original
string with a text field to add the translation:

.. image:: https://codedevils.org/static/img/rosetta.png
    :alt: Rosetta

Once you've completed all translations, you can compile them by running:

.. code:: bash

    ./manage.py compilemessages

Or for a specific language:

.. code:: bash

    ./manage.py compilemessages -l ar

You will need to perform this same compilation on the server once you update the project.

Start a New Language
^^^^^^^^^^^^^^^^^^^^

To create a new language locale, simply use the `makemessages` command and specify the
language code (for this example, we'll make the German [de] language):

.. code:: bash

    ./manage.py makemessages -l de

You will see a new folder appear in the `locale/` directory with the language. Update the
`config.settings.base` settings module with the new language:

.. code:: python

    LANGUAGES = [
        ("es", _("Spanish")),
        ("en-us", _("English")),
        ("fr", _("French")),
        ("ar", _("Arabic")),
        ("nl", _("Dutch")),
        ("hi", _("Hindi")),
        ("de", _("German")      # new language
    ]

Once you have translated everything and completed the PO file, you can compile the language
for use:

.. code:: bash

    ./manage.py compilemessages -l de