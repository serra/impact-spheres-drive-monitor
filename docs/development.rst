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

The Scritps target Python 3.
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

From a terminal, run::

    make bootstrap

This should install all dependencies. At this stage

.. code:: robotframework

    *** Test Cases ***    
    All dependencies should be installed
        File should exist    requirements.txt

Run tests
=========

You should be able to run the tests now. Try::

    make boot



Drive Monitor
=============



Slack integration
=================






About this guide
================

You might not have noticed it, but this document is an executable specification.

.. code:: robotframework

    *** Settings ***
    Library          OperatingSystem


To do
=====



Heroku toolbelt
---------------

The Python `webapp is hosted on Heroku`__
It is recommended that you install the Heroku toolbelt, 
but this is not required.
If you're not sure you need this, don't install it just yet.

__ https://impact-spheres-drive-monitor.herokuapp.com/





Link to Google Mind Settlers Add-on document.

Set up environment.

Install requirements.

Get oauth tokens.

Run webapp locally.

Run unit tests.

Run specifications.

Note on CI?