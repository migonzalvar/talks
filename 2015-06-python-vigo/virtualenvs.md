% Virtualenvs
% Miguel González
% 18 de junio de 2015

<script type='text/javascript' id="__bs_script__">//<![CDATA[
    document.write("<script async
    src='http://HOST:3000/browser-sync/browser-sync-client.2.7.9.js'><\/script>".replace("HOST", location.hostname));
//]]></script>

![](img/logo-python-vigo-512px.png)

# Entornos virtuales

## Ventajas

1. Entorno independiente con posibilidad de tener distintas
   versiones a las del sistema (paquetes e intérprete).

2. No son necesarios permisos de administrador.

3. Herramientas para recrear el entorno en otros equipos.

# Por el principio

## Pythons

- Es un lenguaje interpretado

```
$ python hola.py
Hola mundo!
```

---

- Se puede hacer un pseudo ejecutable

*Linux*

```
$ cat hola.py
#!/usr/bin/python
print('Hola mundo!')
$ chmod +x hola.py
$ ./hola.py
Hola mundo!
```

*Windows*

. . .

<span style='color:red'>¡Doble click!</span>

# Entonces...

## Creación de un entorno virtual

```
$ virtualenv
```

# Herramientas

## virtualenvwrapper

Comandos

## autoenv

## pythonz

## Enlaces

- [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/index.html)
- [autoenv](https://github.com/kennethreitz/autoenv)
- [pythonz](https://github.com/saghul/pythonz)

## Bootstraping

- Ejemplo Ubuntu 14.04

### pip

```
$ sudo apt-get install python-pip python-virtualenv
$ pip install --user pip --upgrade
$ export PATH=$HOME/.local/bin:$PATH
```

### virtualenvwrapper

```
$ pip install --user virtualenvwrapper
```

### pythonz

```
$ sudo apt-get install build-essential zlib1g-dev libbz2-dev libssl-dev libreadline-dev \
  libncurses5-dev libsqlite3-dev libgdbm-dev libdb-dev libexpat-dev libpcap-dev liblzma-dev \
  libpcre3-dev
$ curl -kL https://raw.github.com/saghul/pythonz/master/pythonz-install | bash
```

    3
    4  echo $PATH
    5  vim .bashrc
    6  pip install --user pip
    7  sudo apt-get install python-pip python-virtualenv
    8  pip install --user pip
    9  pip install --user pip --upgrade
   10  ls -la
   11  .local/bin/pip --version
   12  vim .bashrc
   13  echo $PATH
   14  vim .bashrc
   15  history


# Gracias
