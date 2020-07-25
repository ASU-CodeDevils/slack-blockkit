.. Installation file for downloading the project

Installation
============

This installation details how to download and run the website locally. These
instructions work for both Debian Stretch and Mac. Note that the CodeDevils
website is installed on a Debian Stretch OS, so it is the preferred OS>

Dependencies
^^^^^^^^^^^^
* Python 3.7
* Django 3.0
* MySQL
* Redis (optional when installed locally)
* Celery (optional when installed locally)

Instructions
^^^^^^^^^^^^

Clone from GitHub
-----------------

Clone the repository from GitHub.

.. code:: bash

   git clone https://github.com/ASU-CodeDevils/codedevils_org.git
   cd codedevils_org
   git checkout dev     # all branches need to be created from the dev branch

Install Dependencies
--------------------

First create the virtual environment. For this example, the virtual environment
will be created in the root directory of the project.

.. code:: bash

    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip

You should source the virtual environment each time before running the project.

.. note::

    Best practice is to install Django globally rather than through the virtual
    environment. Due to the server configuration, this project installs Django in
    the virtual environment.

Install the dependencies to the virtual environment:

.. code:: bash

    pip install -r requirements/local.txt

Configure the Database
----------------------

.. note::

    These instructions do not detail how to install MySQL, but the requirements for
    configuring your MySQL server for the website. See instructions on how to `install on Debian Stretch`_
    or `install on Mac`_.

.. _`install on Debian Stretch`: https://tecadmin.net/install-mysql-server-on-debian9-stretch/
.. _`install on Mac`: https://dev.mysql.com/doc/mysql-osx-excerpt/5.7/en/osx-installation-pkg.html

In MySQL create a database called `cdwebtest` and a user on that database named `test`. You
can do so using the command-line, but it may be easier if you use the MySQL workbench. In this
example, log in using the command-line:

.. code:: bash

    mysql -u root -p

Then run the following to configure the database:

.. code-block::

    CREATE DATABASE cdwebtest;
    GRANT ALL PRIVILEGES ON cdwebtest.* TO 'test'@'localhost' IDENTIFIED BY 'test';
    \q

Configure the Environment Variables
-----------------------------------

Within the root directory of the project of the project create a `.env` file and begin
editing with your favorite editor:

.. code:: bash

    touch .env

Inside the .env file put the following configuration:

.. code:: ini

    DATABASE_URL=mysql://test:test@127.0.0.1/cdwebtest
    CELERY_BROKER_URL=
    EMAIL_HOST_PASSWORD=None
    DJANGO_LANGUAGE_CODE=en-us
    DJANGO_ADMIN_URL=admin/

.. note::

    Emails sent in the local environment will show over the command line instead of sending an
    actual email.

Finish configuration
--------------------

To complete the configuration, run the following `django-admin` commands:

.. code:: bash

    ./manage.py migrate             # for creating the database tables
    ./manage.py compilemessages     # for compiling translations

VS Code configuration
^^^^^^^^^^^^^^^^^^^^^

A good VSCode integration for this project is:

`settings.json`

.. code:: json

    {
        "python.linting.pylintEnabled": true,
        "python.pythonPath": "${workspaceFolder}/ven/bin/python",
        "files.associations": {
            "**/*.html": "html",
            "**/templates/**/*.html": "django-html",
            "**/templates/*.html": "django-html",
            "**/templates/**/*": "django-txt",
            "**/requirements{/**,*}.{txt,in}": "pip-requirements"
        }
    }

`launch.json`

.. code:: json

    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Django",
                "type": "python",
                "request": "launch",
                "program": "${workspaceFolder}/manage.py",
                "args": [
                    "runserver",
                    "--noreload"
                ],
                "django": true
            },
            {
                "type": "firefox",
                "request": "launch",
                "reAttach": true,
                "name": "Launch localhost",
                "url": "http://localhost:8000",
                "webRoot": "${workspaceFolder}/public/"
            }
        ]
    }
