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

## Primero

* Cabecera para hacer un archivo ejecutable. Funciona en Windows!

    ```
    #!/bin/env python3
    ...
    ```

* `chmod +x`

* Alternativamente `python nombre.py`

## ~~tabs~~ 4 espacios

## Vim

```
set shiftwidth=4  " operation >> indents 4 columns; << unindents 4 columns
set tabstop=4     " a hard TAB displays as 4 columns
set expandtab     " insert spaces when hitting TABs
set softtabstop=4 " insert/delete 4 spaces when hitting a TAB/BACKSPACE
set shiftround    " round indent to multiple of 'shiftwidth'
set autoindent    " align the new line indent with the previous line
```

## Sublime

* Preferences > Settings - User

    ```json
    {
        ...,
        "translate_tabs_to_spaces": true
    }
    ```

## PyCharm

----

<iframe width="560" height="315" src="https://www.youtube.com/embed/639hcsfR4vU" frameborder="0" allowfullscreen></iframe>

# Continuar

## Recursos

* https://docs.python.org/3/tutorial/
* https://docs.python.org/3/library/
* http://docs.python-guide.org/en/latest/
* http://migonzalvar.eu/curso-python3/

# Bonus track

## pip

* Gestor de paquetes

* Incluida en Python 3 **salvo Ubuntu**

    ```shell-session
    $ python3 -m pip
    ```

* Instalación en Ubuntu

    ```shell-session
    $ sudo apt-get install python3-pip
    ```

    ```shell-session
    $ curl https://bootstrap.pypa.io/get-pip.py | python3
    ```

* Uso

    ```shell-session
    $ pip3 install youtube-dl
    ...
    $ pip3 install --upgrade youtube-dl
    ...
    $ pip3 uninstall youtube-dl
    ```

## pyenv

* Era una herramienta independiente `virtualenv` ahora incluida en
  la librería estándar como `pyvenv` o `python3 -m venv`

* Uso

    ```shell-session
    $ python3 -m venv /path/to/venv
    $ source /path/to/venv/bin/activate
    (venv)$ 
    ```

* Workaround en Ubuntu trusty 14.04

    ```shell-session
    $ python3 -m venv --without-pip /path/to/venv
    $ curl https://bootstrap.pypa.io/get-pip.py | /path/to/venv/bin/python
    ```

# Gracias!
