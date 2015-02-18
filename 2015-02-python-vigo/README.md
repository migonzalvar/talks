% Python 3, primeros pasos
% Miguel González @migonzalvar
% 19 Febrero 2015

# Instalación

## Linux

* Ya está!

    ```bash-session
    vagrant@vagrant-ubuntu-trusty-64:~$ python3
    Python 3.4.0 (default, Apr 11 2014, 13:05:11) 
    [GCC 4.8.2] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
    vagrant@vagrant-ubuntu-trusty-64:~$ which python3
    /usr/bin/python3
    ```

## Windows

* [Instalador MSI](https://www.python.org/ftp/python/3.4.2/python-3.4.2.amd64.msi)

    Más info en https://www.python.org/downloads/windows/

## Mac OS X

* [Instalador pkg](https://www.python.org/ftp/python/3.4.2/python-3.4.2-macosx10.6.pkg)

* [Homebrew](http://brew.sh/)

    ```shell-session
    $ brew install python3
    ```

## Intérpretes

## Estándar

```shell-session
$ python
>>>
```

## bpython

* Instalación

    ```shell-session
    $ sudo apt-get install bpython3
    ```

    [Más info](http://www.bpython-interpreter.org/)

* Demo

## Otros

* [ipython notebook](http://ipython.org/)
* [repl.it](http://repl.it/languages/Python3)

# Escribir programas

## Vim

## Sublime

## PyCharm

----

<iframe width="560" height="315" src="https://www.youtube.com/embed/639hcsfR4vU" frameborder="0" allowfullscreen></iframe>

# Bonus track

## pyenv

* Era una herramienta independiente `virtualenv` ahora incluida en
  la librería estándar como `pyvenv` o `python3 -m venv`

* Workaround en Ubuntu trusty 14.04

    ```shell-session
    $ python3 -m venv --without-pip /path/to/venv
    $ curl https://bootstrap.pypa.io/get-pip.py | /path/to/venv/bin/python
    ```
