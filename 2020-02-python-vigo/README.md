# Distribuir paquetes en Python

## Ejemplo [script rápido](01-scripts/main.py)

## Preparación para empaquetar

- Disposición del código: eliminamos efectos secundarios en el `import`.

- Renombrar para que sea importable (módulo).

## Empaquetar

Añadir:

- [setup.py](03-setup/setup.py)
- [README.rst](03-setup/README.rst)

Creamos el paquete fuente.

```console
$ python3 setup.py sdist
running sdist
running egg_info
writing chove.egg-info/PKG-INFO
writing dependency_links to chove.egg-info/dependency_links.txt
writing top-level names to chove.egg-info/top_level.txt
reading manifest file 'chove.egg-info/SOURCES.txt'
writing manifest file 'chove.egg-info/SOURCES.txt'
running check
creating chove-0.0.1
creating chove-0.0.1/chove.egg-info
copying files to chove-0.0.1...
copying README -> chove-0.0.1
copying chove.py -> chove-0.0.1
copying setup.py -> chove-0.0.1
copying chove.egg-info/PKG-INFO -> chove-0.0.1/chove.egg-info
copying chove.egg-info/SOURCES.txt -> chove-0.0.1/chove.egg-info
copying chove.egg-info/dependency_links.txt -> chove-0.0.1/chove.egg-info
copying chove.egg-info/top_level.txt -> chove-0.0.1/chove.egg-info
Writing chove-0.0.1/setup.cfg
Creating tar archive
removing 'chove-0.0.1' (and everything under it)
```

También


## Alta en PyPI

```console
$ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: migonzalvar-test
Enter your password:
Uploading chove-0.0.1.tar.gz
100%|███████████████████████████████| 4.34k/4.34k [00:01<00:00, 2.37kB/s]

View at:
https://test.pypi.org/project/chove/0.0.1/
```

Lo testamos:

```console
$ podman run -it python:3.6 bash
root@8dae05ae553a:/# pip install -i https://test.pypi.org/simple/ chove==0.0.1
Looking in indexes: https://test.pypi.org/simple/
Collecting chove==0.0.1
Downloading https://test-files.pythonhosted.org/packages/ad/27/a32f56222c1131df2a88555079d4bce66e0576c277231721d2eb139fa556/chove-0.0.1.tar.gz (1.4 kB)
Building wheels for collected packages: chove
Building wheel for chove (setup.py) ... done
Created wheel for chove: filename=chove-0.0.1-py3-none-any.whl size=1803 sha256=a8391babc09ee817bcc2c11741fbe1c3bc15bf42c9cbf49cb388ea9c487d4b35
Stored in directory: /root/.cache/pip/wheels/b3/b0/fe/ad7a1e70a9ed95f928a2fcba2226c9605b136731b66fa487e7
Successfully built chove
Installing collected packages: chove
Successfully installed chove-0.0.1
root@8dae05ae553a:/# python
Python 3.6.10 (default, Feb  2 2020, 09:39:59)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import chove
>>> chove.main()
La predicción para 16/02/2020 es:

Mañana 60%
Tarde 80%
Noche 80%
>>>
```

5. Versiones

6. Otras ayudas para usuarios: README, registro de cambios, documentación...

# Referencias

- PyPI de pruebas https://test.pypi.org/

- Twine https://pypi.org/project/twine/

- Tutorial https://packaging.python.org/tutorials/packaging-projects/

- Proyectos de ejemplo: https://github.com/pypa/sampleproject
  o https://github.com/ionelmc/python-nameless

\_ `src` o no `src` https://hynek.me/articles/testing-packaging/ y
https://blog.ionelmc.ro/2014/05/25/python-packaging/

- Plantillas de cookiecutter:
  https://github.com/ionelmc/cookiecutter-pylibrary/ (`src`)
  y https://github.com/audreyr/cookiecutter-pypackage (no `src`)