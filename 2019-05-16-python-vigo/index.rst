:title: El PEP maldito
:css: style.css

----

El PEP maldito
==============

----

572
===

----

Guido lo deja
=============

“Now that PEP 572 is done, I don’t ever want to have to fight so hard
for a PEP and find that so many people despise my decisions.”

.. note::

    https://www.mail-archive.com/python-committers@python.org/msg05628.html

----

Por qué?
========

----

.. code:: python

        a = 1

----

.. code:: python

        a == 1

----

.. code:: python

        a := 1

----

Rompe el zen de python
======================

----


Current:

.. code:: python

    env_base = os.environ.get("PYTHONUSERBASE", None)
    if env_base:
        return env_base

Improved:

.. code:: python

    if env_base := os.environ.get("PYTHONUSERBASE", None):
        return env_base

----

Current:

.. code:: python

    while True:
        line = fp.readline()
        if not line:
           break
        ....

Improved:

.. code:: python

    while line := fp.readline():
        ...

----

Links
-----

- https://www.python.org/dev/peps/pep-0572/
- https://www.mail-archive.com/python-committers@python.org/msg05628.html
