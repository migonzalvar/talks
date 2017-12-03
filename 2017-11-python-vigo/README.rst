:title: Charla sobre entornos virtuales
:author: Miguel González @migonzalvar

.. footer::

    Entornos virtuales, @migonzalvar

----

Entornos virtuales
==================

.. note::

    Ya tenemos Python instalado y con sus pilas incluidas.

    Ahora queremos instalar una librería externa y la documentación nos habla de crear un entorno virtual.
    ¿Qué es? ¿Para qué sirve? ¿Cómo se crea?

    En la charla haremos una introducción histórica.
    Hablaremos de herramientas veteranas como `virtualenv` y `virtualenvwrapper`
    y otras más recientes como `pipsi`, `pew` y `pipenv`.

----

pythons!
========

.. note::

        Hablamos del proyecto `pythonz <https://github.com/saghul/pythonz>`_
        que permite tener varias versiones python instaladas a la vez.

        Exploramos las carpetas y localizamos el ejecutable principal.

        Nos fijamos en la carpeta lib/python donde está la librería estándar.

        Abrimos un módulo al azar y vemos `site-packages`.

----

python es un lenguaje interpretado
==================================

.. note::

        Si creamos un archivo `hello.txt` y lo usamos como parámetro
        del ejecutable de la versión de Python que queramos funciona.

        .. code:: console

                $ ~/.pythonz/pythons/CPython-3.6.3/bin/python3.6 hello.txt
                $ ~/.pythonz/pythons/CPython-2.7.13/bin/python2.7 hello.txt

        Ahora probamos a hacer un módulo (`mimodulo.py`) y lo copiamos en
        la carpeta `lib/pythonX.X/site-packages`.

----

virtualenv
==========


.. note::

        Creamos un entorno virtual con el ejecutable `pyenv`
        incluido desde python 3.6
        (`docs <https://docs.python.org/3/library/venv.html>`_)::

            $ pyvenv mi-entornovirtual

        Lo recomendable es usar `python3.6 -m venv mi-entornovirtual`.

        Volvemos a examinar carpetas: bin, lib y comparamos diferencia
        con una instalación regular.

        QUIZ: `import mimodulo` funcionará?

        PISTA: Opción `--system-site-packages`

        Comentamos el script `activate.(sh|fish|bat)`

----

pip
===

.. note::

        Breve demo uso de pip::

            python -m pip install Django
            pip list
            pip freeze
            pip list --outdated

----

pipsi
=====

.. note::

        `pipsi <https://github.com/mitsuhiko/pipsi>`_
        es **pip** **S** cript **I** nstaller.
        En sus propias palabras:

        > ... pipsi installs each package into ~/.local/venvs/PKGNAME and
        > then symlinks all new scripts into ~/.local/bin (these can be
        > changed by PIPSI_HOME and PIPSI_BIN_DIR env variables respectively)

        Breve demo::

            curl https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py | python
            pipsi install youtube-dl
            pipsi upgrade youtube-dl

----

pew
===

.. note::

        `pew <https://github.com/berdario/pew>`_ es
        una una utilidad que extiende y sustituye la funcionalidad `virtualenv`.
        Se puede instalar con `pipsi`.

        Breve demo::

            pew new mytalk
            which python
            exit
            which python
            pew workon mytalk
            which python
            `Ctrl+D`
            pew rm mytalk
            pew ls

----

pipenv
======

.. note::

        `pipenv <https://docs.pipenv.org/>`_
        es la fusión de la funcionalidad de pip con pew.
        Se puede instalar con `pipsi`.

        Breve demo::

            pipenv install
            pew ls (!!)
            which python
            pipenv shell
            which python
            pipenv install Django
            (examinar Pipfile y Pipfile.loc)
            pipenv graph
            exit
            pipenv --rm
            pipenv install

        Si da tiempo podemos repetir con flask

----

Enlaces
=======

- https://github.com/saghul/pythonz
- https://docs.python.org/3/library/venv.html
- https://github.com/mitsuhiko/pipsi
- https://github.com/berdario/pew
- https://docs.pipenv.org/
