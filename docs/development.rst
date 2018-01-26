.. _development:

===========
Development
===========

This repository contains our Python Scripts.
This document will help you to get started if you want to contribute to those. 

We also have a Google Docs Add-On that is maintained outside this repository.
It is available in the Impact Spheres guides folder.
Impact Spheres contributors can access `the script here`__

__ https://docs.google.com/document/d/1ISqiBCOewgPYycaId4vUCFuARObpr5eg9XNWb0_oCVQ/edit

Prerequisites
=============

The Scripts target Python 3.
Developed on OSX, Python version 3.6.

Virtualenv
----------

It is recommended that you develop in `a virtual environment`__. 

__ http://docs.python-guide.org/en/latest/dev/virtualenvs/#lower-level-virtualenv

I set up mine like this (assuming virtualenv 1.7+)::

    cd [impact-spheres-drive-monitor]
    virtualenv -p /usr/local/bin/python3 venv
    source venv/bin/activate

Bootstrap your environment
--------------------------

After setting up your environment, from a terminal, run::

    make bootstrap

This should install all dependencies. At this stage:

.. code:: robotframework

    *** Test Cases ***    
    The development environment is bootstrapped 
        File should exist    requirements.txt
        All dependencies should be installed

We have got some work left to do,
but now you can already verify whether your environment 
is properly setup for development::

    make check-environment

When running this the first time, you will see many failing tests.
In the remainder of this document 
we'll setup your environment so that you can hack away.

Don't worry, it shouldn't take long.


Run tests
=========

You should be able to run the tests now. Try::

    make test

This runs the unit tests in the `tests` directory.


Access Google Drive
===================

The directory `google` contains scripts 
for inspecting our content on Google Drive.

To use these scripts you'll need a Google account.
To access drive files, you need a Google API key. 
You can configure access using the `Google API management console`_.

To access the private drive files in our `Impact Spheres directory`_, 
an authorized human being has to give consent.
This consent can be given `using OAuth2`__. 

__ https://developers.google.com/drive/v3/web/quickstart/python

.. warning ::

    Giving consent gives the script access to ALL your data on Google Drive,
    From the moment you give consent, the script can impersonate you
    as long as the client ID is active.
    Consider using a dedicated Google account instead of your personal account.

.. warning ::

    Do NOT share your OAuth client secret.

API keys as well as client IDs can be managed in your personal
`Google API management console`_.

If you have setup your API key and client id, 
then save your client id and secret as 
`drive_client_secret.json` in the root folder.

To setup your Google credentials, run::

    make auth-google

This will open a browser to login to a Google account 
and to give consent to access data. 

Add your Google API key to your environment variables.
Add your client id and secret to your environment as well.

.. note::

   I strongly recommend using a tool like `direnv`_ 
   to manage your environment variables.


At this stage:

.. code:: robotframework

    *** Test Cases ***
    Google client id and secret should be saved on disk
        File should exist   drive_client_secret.json

    Google environment variables should be set
        Environment Variable Should Be Set    GOOGLE_API_KEY
        Environment Variable Should Be Set    GOOGLE_CREDENTIALS

    The scripts can access Impact Spheres data on Google Drive
        Can access review folder


Access Slack
============

The directory `slack` contains scripts 
for interaction wit Slack.

Slack uses OAuth2 as well. 
The `Slack sign-in process`_ is documented well and worth a quick read.

Slack integration is provided by the `Impact Spheres App`_ 
on `Agilityscales.slack.com`__ .

__ https://agilityscales.slack.com/

The client ID, client secret and verification token are managed on the 
`Impact Spheres App management page`_.
Marijn_, Jurgen_ and Thomas_ have management access to this app.
You might want ask one of them to add you as a collaborator.

Now set the client ID and secret in your environment variables,
as well as the `SLACK_BOT_SCOPE` environment variable:

.. code:: robotframework

    *** Test Cases ***
    The environment is ready for authenticating with Slack
        Environment Variable Should Be Set    SLACK_CLIENT_ID
        Environment Variable Should Be Set    SLACK_CLIENT_SECRET
        Environment Variable Should Be Set    SLACK_BOT_SCOPE
        Should be equal   %{SLACK_BOT_SCOPE}  chat:write:bot

You can authorize your script for local development::

    make auth-slack

Open a browser at http://localhost:5000/begin_auth.
Follow the link to start an oauth flow.
A token will be created on your behalf.
Store this token in your environment variables.
At this stage: 


.. code:: robotframework

    *** Test Cases ***
    The scripts can post to Slack on your behalf
        Environment Variable Should Be Set    SLACK_BOT_TOKEN
        Send Marijn a direct message


Access Contentful
=================

The directory `content` contains scripts 
for accessing content on the Mind Settlers Contentful database.

Guides are stored in a Contentful document store.
It has an API that uses OAuth2 for authentication.
This application was created by follwing the section 
"Creating an OAuth 2.0 application" in `Contentful docs on authentication`_.

Client id and secret are managed from Marijn's Contentful account.

.. code:: robotframework

    *** Test Cases ***
    The environment is ready for authenticating with Contentful:
        Environment Variable Should Be Set    CONTENTFUL_CLIENT_ID
        Environment Variable Should Be Set    CONTENTFUL_CLIENT_SECRET

You can authorize your script for local development::

    make auth-contentful

Open a browser at http://localhost:5000/begin_auth.
Follow the link to start an oauth flow.
A token will be created on your behalf.
Store this token in your environment variables.


.. code:: robotframework

    *** Test Cases ***
    The scripts can query contentful on your behalf  
        Environment Variable Should Be Set    CONTENTFUL_TOKEN
        Search for guides                     big wall


Run the webapp locally
======================

In debug mode::

    make server

In heroku local mode::

    make heroku-local


The app is available at http://localhost:5000.


About this guide
================

This document is an executable specification.
To execute the test case in this document, run::

    make check-environment

The following Robotframework settings are used:

.. code:: robotframework

    *** Settings ***
    Library          OperatingSystem
    Library          ./lib/DevLibrary.py
    Library          ./lib/GoogleLibrary.py
    Library          ./lib/SlackLibrary.py
    Library          ./lib/ContentfulLibrary.py


.. References

.. _Impact Spheres directory: https://drive.google.com/drive/u/0/folders/0B9xuqHFCF4WMMUN5bENtaFEtSmM
.. _Drive Python API quickstart: https://developers.google.com/drive/v3/web/quickstart/python
.. _Python Drive API: https://developers.google.com/resources/api-libraries/documentation/drive/v3/python/latest/
.. _Google API management console: https://console.developers.google.com/apis/credentials?project=ageless-aquifer-176113
.. _Slack Python API: http://slackapi.github.io/python-slackclient/basic_usage.html#sending-a-message
.. _Slack sign-in process: https://api.slack.com/docs/sign-in-with-slack
.. _Impact Spheres App: https://agilityscales.slack.com/apps/A7RHUFQ90-impact-spheres-app
.. _Impact Spheres App management page: https://api.slack.com/apps/A7RHUFQ90
.. _Marijn on Slack: https://agilityscales.slack.com/messages/C3N27KRT9/team/U5S1Q0YQ5/
.. _Slash Commands: https://api.slack.com/slash-commands
.. _Contentful docs on authentication: https://www.contentful.com/developers/docs/references/authentication/
.. _direnv: https://direnv.net/
.. _Marijn: https://agilityscales.slack.com/team/U5S1Q0YQ5
.. _Jurgen: https://agilityscales.slack.com/team/U3MDKTU84
.. _Thomas: https://agilityscales.slack.com/team/U46M319FF
