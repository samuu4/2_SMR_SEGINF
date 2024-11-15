
# Criptografía: métodos clásicos

El gran valor de la escritura, la universalización del acceso al conocimiento, es, a la vez, su gran debilidad cuando las informaciones escritas son, por unas u otras causas, de carácter confidencial.

Lo primero que inventamos para evitar que ciertos mensajes llegasen a ojos no deseados fue la **esteganografía**, consistente en ocultar el mensaje a las miradas curiosas, como cuando escribían el texto en la cabeza rapada del mensajero y esperaban a que le creciese el pelo.

Sin embargo, pronto se vio que los métodos de ocultación tenían el gran inconveniente de que una vez el engaño era descubierto el mensaje quedaba completamente expuesto. Por eso surgió la **criptografía**, "el arte de escribir con clave secreta", que consiste en ocultar no el mensaje en sí, sino el significado. De esta manera, aunque el mensaje fuese interceptado, su contenido aún estaría a salvo.

Muchos son los sistemas de encriptación. Los clásicos pueden clasificarse en **sistemas de transposición** y de **sustitución**, siendo estos últimos de dos tipos: **códigos** y **cifrados**.

## TRANSPOSICIÓN

El significado se oculta cambiando simplemente el orden de las letras del mensaje. Por ejemplo, podemos coger primero todas las letras que ocupan posiciones pares y después escribir las de las posiciones impares. De esta manera, la frase `esto es un mensaje de ejemplo` se convertiría en `SOE NMNAED JMLET SU ESJ EEEPO`.

## SUSTITUCIÓN

La idea es sustituir los elementos del texto plano (el mensaje original) por otros que formen el texto encriptado. Si lo que se sustituyen son las letras se llama **cifrado**, mientras que si lo que se sustituyen son palabras o expresiones enteras, se llama **código**.

### Cifrado César

Utilizado, de ahí su nombre, por Julio César para comunicarse con sus oficiales, consiste en sustituir cada letra del mensaje por la que está *n* posiciones más adelante o atrás en el alfabeto. Si *n* = 3, la `a` se sustituiría por la `D`, la `b` por `E`, la `c` por `F` y así sucesivamente. De este modo, la palabra `epsilones` se transforma en `HSVLÑRPHV`.

En los sistemas de encriptación se suele distinguir entre el **algoritmo** o procedimiento general y la **clave**, que sirve para singularizar el resultado del algoritmo. En el caso del cifrado César, el algoritmo sería la regla por la cual cambiamos cada carácter por uno que está *n* posiciones más adelante, mientras que la clave sería el valor concreto utilizado para *n*.

Lo malo de este sistema es que, si se sabe que se está utilizando, solo permite 27 sustituciones distintas (tantas como letras tiene el alfabeto), con lo que su descifrado es trivial. Para complicar un poco la cosa se puede utilizar, en vez de una cifra, dos, o más. Así, si la clave es 31, se sustituirá la primera letra por la que esté tres posiciones por delante, la segunda por la que esté una posición más avanzada, la tercera por la que esté tres posiciones por delante, y así sucesivamente.

El cifrado César es fácilmente matematizable: ver el Apéndice.

### Sustitución monoalfabética

A cada letra del alfabeto se le asigna un signo distinto, que puede ser otra letra o cualquier otra cosa. Por ejemplo, según la tabla siguiente, la palabra `matematicas` se transformaría en `9XD?9XD3RXM`:

| a | b | c | d | e | f | g | h | i | j | k | l | m | n | ñ | o | p | q | r | s | t | u | v | w | x | y | z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X | 5 | R | A | ? | P | 2 | U | 3 | Ñ | $ | * | 9 | E | 6 | I | W | ¿ | & | M | D | 7 | Z | T | 4 | B | @ |

Está claro que lo mejor es que la tabla sea completamente aleatoria, pero esto obliga a conocer la tabla completa. Una alternativa es la utilización de una clave para formar las equivalencias. Por ejemplo, si la clave es `EPSILON`, se escribirían a continuación el resto de las palabras del alfabeto en su orden habitual pero sin repetir las ya utilizadas. La tabla quedaría de la siguiente manera:

| a | b | c | d | e | f | g | h | i | j | k | l | m | n | ñ | o | p | q | r | s | t | u | v | w | x | y | z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E | P | S | I | L | O | N | Ñ | Q | R | T | U | V | W | X | Y | Z | A | B | C | D | F | G | H | J | K | M |

La palabra `matematicas` se cifraría como `VEDLVEDQSEC`.

### Análisis de frecuencias

Podría pensarse que tales sistemas son eficientes, pero resultan tremendamente fáciles de descifrar mediante una técnica llamada **análisis de frecuencias**, desarrollada primeramente por los árabes...

...

## MÁQUINAS Y ORDENADORES

Con la Segunda Guerra Mundial la criptografía se mecaniza. Máquinas como Enigma proporcionan códigos segurísimos que máquinas como la Bomba de Turing se encargan de descifrar...

## Apéndice: las matemáticas del cifrado César

Si *x* es la posición de la letra que queremos cifrar, la posición de la nueva letra vendrá dada por la fórmula:

**f(x) = (x + n) mod p**,

donde:

- **p** = longitud del alfabeto (27 para el castellano, por ejemplo),
- **x** = número asociado a la letra (1 para la *a*, 2 para la *b*, etc.),
- **n** = clave, dependiendo de la cual cambiará el código.

Por ejemplo, si codificamos la palabra `clave` tomando *a* como la posición 1 y haciendo *n* = 5, se tiene:

- c → f(3) = (3 + 5) mod 27 = 8 → h
- l → f(12) = (12 + 5) mod 27 = 17 → p
- a → f(1) = (1 + 5) mod 27 = 6 → f
- v → f(23) = (23 + 5) mod 27 = 1 → a
- e → f(5) = (5 + 5) mod 27 = 10 → j

Para descifrar algo tan sencillo, utilizamos la fórmula inversa de aquella que hemos utilizado para cifrar (estas funciones siempre han de ser inyectivas): **f(x) = (x - n) mod p**.
