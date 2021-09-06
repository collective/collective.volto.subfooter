
===============
Volto Subfooter
===============

Add-on for Volto to manage a subfooter (right column) for `Volto Subfooter`_.

.. _Dropdown Menu: https://github.com/collective/volto-subfooter

Features
--------

- Control panel for plone registry to manage subfooter configuration.
- Restapi view that exposes these settings for Volto

Volto endpoint
--------------

Anonymous users can't access registry resources by default with plone.restapi (there is a special permission).

To avoid enabling registry access to everyone, this package exposes a dedicated restapi route with the infos to draw the menu: *@subfooter*::

    > curl -i http://localhost:8080/Plone/@subfooter -H 'Accept: application/json'


Control panel
-------------

You can edit settings directly from Volto because the control has been registered on Plone and available with plone.restapi.


Volto integration
-----------------

To use this product in Volto, your Volto project needs to include a new plugin: https://github.com/collective/volto-subfooter


Translations
------------

This product has been translated into

- Italian


Installation
------------

Install collective.volto.subfooter by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.volto.subfooter


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.volto.subfooter/issues
- Source Code: https://github.com/collective/collective.volto.subfooter


License
-------

The project is licensed under the GPLv2.

Authors
-------

This product was developed by **RedTurtle Technology** team.

.. image:: https://avatars1.githubusercontent.com/u/1087171?s=100&v=4
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
