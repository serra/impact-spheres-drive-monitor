.. _deployment:

==========
Deployment
==========

Component overview
==================

In ASCII art::


  Google Docs Add-On ---> webapp ---> Google Drive
                            ^
                            |
                            +--->  Slack Impact Spheres App
  
  Key:
  A --> B: component A calls component B
  

Webapp
======

The Python `webapp is hosted on Heroku`__.
The app is managed through Marijn's Heroku account. 

__ https://impact-spheres-drive-monitor.herokuapp.com/

The app requires access to the Impact Spheres folder on Gooogle Drive.
It uses the impactspheres@gmail.com credentials to access this folder.

Credentials are set as environment variables; see :ref:`development` 
for a list of environment variables to set.

It is recommended that you install the `Heroku toolbelt`__, 
but this is not required.
If you're not sure you need this, don't install it just yet.

__ https://devcenter.heroku.com/articles/using-the-cli


Slack Impact Spheres App
========================


The webapp requires access to agilityscales.slack.com.
It gets this access as the `Impact Spheres App`__ there.

__ https://agilityscales.slack.com/apps/A7RHUFQ90-impact-spheres-app

You can manage this app on the `Impact Spheres App management page`_.


Google docs add-on
==================

The Google Docs Add-On is `deployed form the document here`__.
Users can install the Add-On from `the Google Chrome webstore`__

__ https://docs.google.com/document/d/1ISqiBCOewgPYycaId4vUCFuARObpr5eg9XNWb0_oCVQ/edit
__ https://chrome.google.com/webstore/detail/mind-settlers/dcaffcejnkpkgiggodipjbcgdiioemnp


.. references

.. _Impact Spheres App management page: https://api.slack.com/apps/A7RHUFQ90

