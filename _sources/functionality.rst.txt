=============
Functionality
=============


Slack
=====

At regular intervals the bot will notify the `#09_impactspheres`__
channel of guide statuses.

__ https://agilityscales.slack.com/messages/G7B5DUUC8

You can also use the :code:`/guides` `Slash Command`__.

__ https://get.slack.help/hc/en-us/articles/201259356-Slash-commands


Slash commands
--------------

On Slack, users can use the `/guides` `Slash command`__
to monitor our Impact Spheres work status
without leaving Slack.

__ https://api.slack.com/slash-commands


.. code:: robotframework

  *** Test cases ***
  Using the guides command
    Slack can request guide reports

  These are valid Slack commands
    [Template]  Valid command
    guides  ${EMPTY}
    guides  queues
    guides  review
    guides  daily
    guides  an unknown text command is still valid

  These are invalid Slack commands  [Template]  Invalid command
    guide   ${EMPTY}
    guidez  queues  


Google Docs
===========

Install the Add-On from `the Google Chrome webstore`__.

__ https://chrome.google.com/webstore/detail/mind-settlers/dcaffcejnkpkgiggodipjbcgdiioemnp

.. code:: robotframework

  *** Test cases ***
  Search for guides
    the addon can search guides
    search returns empty collection if there are no searchresults



About this document
===================

This document is an executable specification.
To execute the test case in this document, run::

    make test-webapp

The following Robotframework settings are used:

.. code:: robotframework

    *** Settings ***
    Library          OperatingSystem
    Library          ./lib/WebappLibrary.py

