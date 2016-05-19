% Python desde la línea de comandos
% Miguel González
% 19 de mayo de 2016

<script type='text/javascript' id="__bs_script__">//<![CDATA[
    document.write("<script async
    src='http://HOST:3000/browser-sync/browser-sync-client.2.7.9.js'><\/script>".replace("HOST", location.hostname));
//]]></script>

# En el principio era la línea de comandos...

---

![](img/teleprinter.jpg)


# Python desde la línea de comandos

---

![](img/miguel-gonzalez.jpg)

- [@migonzalvar](https://twitter.com/migonzalvar)
- Coorganizador Python Vigo
- Miembro junta directiva de Python España
- Trabajo en Initios Desarrollos(http://initios.com)

---

https://bitbucket.org/migonzalvar/talks/src/master/2016-05-python-vigo/

# Disclaimer

---

- POSIX (no Windows... o sí)
- Fundamentos


# Cómo ejecutar un script

## Desde la propia línea de comandos

```
$ python -c 'print("My name is x0")'
My name is x0
```

## Desde un archivo

```python
print('My name is x1')
```

```
$ python x1
My name is x1
```

## Directamente

```python
#!/usr/bin/env python
print('My name is x2')
```

```
$ chmod +x x2
$ ./x2
My name is x2
```


# Argumentos

## argv

- Módulo `sys`
- Una lista de argumentos

---

```python
#!/usr/bin/env python

import sys

print(repr(sys.argv))
```

---

```
$ ./arguments one
['./arguments', 'one']
```

---

```
$ ./arguments one two
['./arguments', 'one', 'two']
```

---

```
$ ./arguments 'only one'
['./arguments', 'only one']
```

---

Cuidado con la expansión de argumentos (`*`, `?`, ...)

```
$ ./arguments *
['./arguments', 'arguments', 'x1', 'x2']
```

---

Las comillas impiden la expansión

```
$ ./arguments '*'
['./arguments', '*']
```

---

BONUS: Ejecución en una subshell

```
$ ./arguments `echo 1`
['./arguments', '1']
```

# Códigos de salida

---

Si es `0` indica éxito.

```
$ python -c 'raise SystemExit()'
$ echo $?
0
```

Si es otra cosa indica error.

```
$ python -c 'raise SystemExit(42)'
$ echo $?
42
```

---

¿Para qué? Encadenar comandos.

```
$ python -c 'raise SystemExit()' || echo ERROR
$ python -c 'raise SystemExit(42)' || echo ERROR
ERROR
```

---

```
$ python -c 'raise SystemExit()' && echo OK
OK
$ python -c 'raise SystemExit(42)' || echo OK
$
```


---


¡Gracias!

![](img/logo-python-vigo-512px.png)

