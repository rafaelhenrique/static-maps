static-maps
===========

This is an example to use google static maps api with Python.

Installation
------------

Create a virtualenv (use ``virtualenvwrapper``): ::

    mkvirtualenv static-maps

Install requirements: ::
  
    pip install -r requirements.txt

Copy env-sample and configure: ::

   cp contrib/env-sample .env

Remember: You need enter with Browser Api Key on .env file.

Create Google Browser Api Key
-----------------------------

Follow instructions: ::

https://developers.google.com/maps/documentation/static-maps/get-api-key

Run
---

Execute script run.py: ::
 
    python3 run.py

The map image will be saved on local directory based on coordinates and address on settings.py

