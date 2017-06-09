# ¿DÃ³nde estÃ¡ mi Ã±?

## PyDay Galicia

![PyDay](pyday.svg)

# Miguel Gonz�lez

# ï»¿

# Un poco de historia

## 1836

![](International_Morse_code.png){height=500px}

## Morse

- El primer *wire protocol*
- Por la línea van bits . \_
- Optimiza longitud

    - E: 1 símbolos
    - Q: 4 símbolos

## 1874

![](Baudot_Code_-_from_1888_patent.png){height=500px}

## Baudot

- 5 bits
- Optimiza facilidad de uso
- Código de control *erasure*

## 1900

![](5-holes-tape.png){height=500px}

## Cinta perforada

- Teletipo (TTY)
- Tecla de cambio de función: letras, símbolos, meteorológico

## 1963

![](US-ASCII_code_chart.png){height=500px}

## ASCII

- 7 bits
- 0 a 31: no imprimible
- Optimizado mayúsculas/minúsculas

## Quiz

- 10 LF ¿?
- 7 BEL ¿?

## 1981

![](Codepage-437.png){height=500px}

## Códigos de página

- 8 bits
- Saca partido de los otros 128 caracteres
- Explosión con el OEM: Western, Greek, Russian
- Incluye acentos, caracteres, líneas...

## CP-1252

![](CP-1252.png){height=500px}

## 1991

![](unicode25cake-utc147-design.jpg){height=500px}

## Unicode

- Code points no letras
- 1.114.112 code points de 0 a 10FFFF
- Discusión política
- Codificación... lo vemos después

## Ejemplos de code points

```
A
LATIN CAPITAL LETTER A (U+0041)

☠
SKULL AND CROSSBONES (U+2620)

😀
GRINNING FACE (U+1F600)
```

-----

![](code-points.png){height=500px}

## Ellipsis

… **'HORIZONTAL ELLIPSIS' (U+2026)**

![](horizontal-ellipsis.png){height=500px}

## 2015

![](emoji-examples.png){height=500px}

## Unicode 8

- Emoji

## Fototipos (escala Fitzpatrick)

![](unicode_diversity.png)

# Codificación Unicode

## UCS-2 o UTF-16

- Cualquier carácter Unicode.
- Longitud variable: 2 ó 4 bytes
- Optimizado rango U+0000 a U+FFFF (BMP o *plano básico multilingüe*)
- Resto: planos surrogados: No superposición: Los símbolos de 1 palabra (16 bits) utilizan un subconjunto de valores que no puede utilizarse en símbolos de 2 palabras (32 bits).

## Planos surrogados

![](utf-16.png)

## Problemas UTF-16

- Muchos ceros
- Confusión Little o big endian: Byte Order Mark (BOM)
- Muy complejo

## UTF-8

![](utf-8.png)

## Ventajas UTF-8

- Compatible hacia atrás con ASCII
- Muy eficiente para *code points* más usados: 1 para ASCII, 2 para BMP, 3 en resto
- Auto sincronizable: `0xxxxxxx` y `11xxxxxx` marcan comienzo caracter

## Ejemplo: a (U+0061)

![](letter-a.png)

## Ejemplo: Ñ (U+00D1)

![](N-with-tilde.png)

## Ejemplo: 🐍 (U+1F40D)

![](snake.png)

## En resumen...

- Unicode
- UTF-8

----

![](all-the-things.jpg)

# Python

## Python 2

```
Python 2.7.13 (default, May 10 2017, 20:04:28)
>>> s = 'ñ'
>>> len(s)
2
>>> s = u'ñ'
>>> len(s)
1
```

----

```
Python 2.7.13 (default, May 10 2017, 20:04:28)
>>> s = 'Ñ'
>>> s
'\xc3\x91'
>>> s = u'Ñ'
>>> s
u'\xd1'
```

## Python 3

- Dos tipos: `byte` y *texto* (`str`)

![](encode-decode.png)

----

```python
>>> s = 'Ñ'
>>> s
'Ñ'
>>> s.encode('utf-8')
b'\xc3\x91'
```

----

```
>>> b'Ñ'
  File "<stdin>", line 1
SyntaxError: bytes can only contain ASCII literal characters.
```

```
>>> b'\xd1'
b'\xd1'
>>> b'\xd1'.decode('latin1')
'Ñ'
```

# Mundo exterior

## Archivos

- BOM: no recomendado
- ¿Adivinar?

## chardet

```python
>>> import urllib
>>> rawdata = urllib.urlopen('http://yahoo.co.jp/').read()
>>> import chardet
>>> chardet.detect(rawdata)
{'encoding': 'EUC-JP', 'confidence': 0.99}
```

# Solución

## LF

- Código control **line feed** que avanza el el rodillo de papel un línea

## BEL

- Código control de campana. Inventado por Western Union y recogido en ASCII.

## Gonz�alez

```python
>>> 'á'.encode('latin1').decode('utf8', errors='replace')
'�'
```

## ¿DÃ³nde estÃ¡ mi Ã±?


```
Ã±
```

-----

![ISO-8859-1](latin1.gif){height=500px}

-----

```
       C3        B1
```

```
1100 0011 1011 0001
```

----

![UTF-8](utf-8.png)

----

```
___00011 __110001
```

```
1111 0001
```

```
U+F1
```

**LATIN SMALL LETTER N WITH TILDE**

----

```python
>>> 'Ã±'.encode('latin1')
b'\xc3\xb1'
>>> 'Ã±'.encode('latin1').decode('utf8')
'ñ'
```

## Y por último...

```
 ï  »  ¿
```

Usando *Latin1*:

```
EF BB BF
```

Es el `Byte Order Mark` de UTF-8.

----

```python
>>> 'ï»¿'.encode('latin1')
b'\xef\xbb\xbf'
>>> 'ï»¿'.encode('latin1').decode('utf8')
'\ufeff'
```

```python
>>> import codecs
>>> 'ï»¿'.encode('latin1') == codecs.BOM_UTF8
```

# Saber más

## Enlaces

- http://www.joelonsoftware.com/articles/Unicode.html
- http://nedbatchelder.com/text/unipain.html
- http://www.emojitracker.com/
- http://fsymbols.com/generators/encool/

## ¡Gracias!

![](gracias.png){height=500px}
