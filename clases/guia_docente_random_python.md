# Guía docente: `random` en Python

## Objetivo de la clase
En esta clase los estudiantes aprenderán a usar el módulo `random` para introducir azar en sus programas. La idea no es profundizar en teoría, sino usar `random` para reforzar lógica de programación con ejemplos divertidos y visualmente fáciles de imaginar.

Al final de la clase, deberían poder:

- importar el módulo `random`
- generar números aleatorios
- elegir elementos al azar de una lista
- usar aleatoriedad junto con `if`, `while`, `for`, funciones y listas
- crear minijuegos simples

---

## Idea principal para explicar
Una buena forma de presentarlo es así:

> `random` es una herramienta que permite que el programa tome decisiones al azar.

Esto sirve para hacer programas menos repetitivos y más interesantes:

- juegos
- sorteos
- simulaciones simples
- decisiones automáticas

---

## Cuándo dar esta clase
Esta clase funciona muy bien después de haber visto:

- variables
- tipos de datos
- condicionales
- bucles
- funciones
- listas

Porque `random` mezcla todo eso de manera natural.

---

# Parte 1: qué es un módulo

Antes de entrar en `random`, conviene explicar brevemente qué es un módulo.

Puedes decirlo así:

> Un módulo es un archivo o conjunto de herramientas ya preparadas que Python nos presta para hacer ciertas cosas sin tener que programarlas desde cero.

Ejemplo:

```python
import random
```

Explicación:

- `import` significa importar
- `random` es el nombre del módulo

---

# Parte 2: primera función importante: `random.randint()`

## Qué hace
Sirve para generar un número aleatorio entero entre dos valores, incluyendo ambos extremos.

```python
import random

numero = random.randint(1, 10)
print(numero)
```

## Cómo explicarlo
Puedes decir:

> `randint(1, 10)` significa: dame un número aleatorio entero entre 1 y 10.

## Partes de esta expresión

```python
random.randint(1, 10)
```

- `random`: el módulo
- `randint`: la función que genera el número entero aleatorio
- `1`: límite inferior
- `10`: límite superior

## Importante recalcar
- puede salir cualquier número entre 1 y 10
- pueden repetirse
- cada vez que se ejecuta, puede cambiar

---

# Parte 3: ejemplos básicos para explicar en clase

## Ejemplo 1: lanzar un dado

```python
import random

dado = random.randint(1, 6)
print("Salió:", dado)
```

### Qué refuerza
- variables
- números enteros
- función del módulo `random`

---

## Ejemplo 2: moneda al aire

```python
import random

moneda = random.randint(0, 1)

if moneda == 0:
    print("Cara")
else:
    print("Cruz")
```

### Qué refuerza
- `if`
- comparación
- azar

---

## Ejemplo 3: número aleatorio y comparación

```python
import random

numero = random.randint(1, 100)

if numero % 2 == 0:
    print(numero, "es par")
else:
    print(numero, "es impar")
```

### Qué refuerza
- operador módulo `%`
- par e impar
- condicionales

---

# Parte 4: `random.choice()`

## Qué hace
Permite elegir un elemento al azar dentro de una lista.

```python
import random

frutas = ["manzana", "pera", "uva", "mango"]
elegida = random.choice(frutas)

print("Fruta elegida:", elegida)
```

## Cómo explicarlo
Puedes decir:

> `choice()` toma una lista y escoge un elemento al azar.

## Qué refuerza
- listas
- variables
- uso práctico de datos guardados

---

# Parte 5: `random.shuffle()`

## Qué hace
Mezcla los elementos de una lista.

```python
import random

cartas = ["A", "B", "C", "D"]
random.shuffle(cartas)

print(cartas)
```

## Explicación sencilla
Puedes decir:

> `shuffle()` desordena una lista al azar.

## Importante
`shuffle()` modifica la lista original.

---

# Parte 6: `random.random()`

## Qué hace
Genera un número decimal aleatorio entre 0 y 1.

```python
import random

numero = random.random()
print(numero)
```

## Recomendación docente
No hace falta profundizar mucho aquí. Basta con mostrarlo como curiosidad útil.

Puedes decir:

> Esta función genera un número decimal aleatorio entre 0 y 1. Se usa mucho en juegos, simulaciones y probabilidades.

---

# Parte 7: ideas clave que deben entender

## 1. aleatorio no significa mágico
El programa sigue reglas. Solo está usando una herramienta que produce valores impredecibles para el usuario.

## 2. aleatorio no significa infinito
Si se pide un número entre 1 y 6, solo saldrán esos números.

## 3. puede repetirse
Muchos estudiantes creen que si ya salió un número, ya no puede volver a salir. Hay que aclarar que sí puede repetirse.

---

# Parte 8: errores comunes de los estudiantes

## Error 1: olvidar importar el módulo

```python
numero = random.randint(1, 10)
```

Esto fallará si no se hizo antes:

```python
import random
```

---

## Error 2: escribir mal el nombre

```python
import ramdom
```

O:

```python
random.radint(1, 10)
```

Recalcar que Python distingue nombres exactos.

---

## Error 3: creer que `randint(1, 10)` excluye el 10
Aclarar que en `randint(a, b)`, ambos extremos están incluidos.

---

## Error 4: usar `choice()` con algo que no es lista

```python
import random

numero = 123
print(random.choice(numero))
```

Eso dará error.

---

## Error 5: pensar que `shuffle()` devuelve una lista nueva
Muchos hacen esto:

```python
mezclada = random.shuffle(cartas)
print(mezclada)
```

Y luego se confunden. Mejor usar:

```python
random.shuffle(cartas)
print(cartas)
```

---

# Parte 9: ejercicios guiados en clase

## Ejercicio 1: dado
Pide al estudiante que genere un número aleatorio entre 1 y 6.

```python
import random

dado = random.randint(1, 6)
print(dado)
```

---

## Ejercicio 2: moneda
Pide que el programa imprima `Cara` o `Cruz`.

```python
import random

moneda = random.randint(0, 1)

if moneda == 0:
    print("Cara")
else:
    print("Cruz")
```

---

## Ejercicio 3: adivina el número
El programa genera un número y el usuario intenta adivinar.

```python
import random

secreto = random.randint(1, 10)
adivinanza = int(input("Adivina el número del 1 al 10: "))

if adivinanza == secreto:
    print("¡Correcto!")
else:
    print("No. El número era", secreto)
```

### Qué trabaja
- `input()`
- conversión con `int()`
- condicionales
- azar

---

## Ejercicio 4: elegir nombre al azar

```python
import random

nombres = ["Ana", "Luis", "Pedro", "María"]
ganador = random.choice(nombres)

print("El ganador es:", ganador)
```

---

## Ejercicio 5: piedra, papel o tijera

```python
import random

opciones = ["piedra", "papel", "tijera"]
maquina = random.choice(opciones)
usuario = input("Escribe piedra, papel o tijera: ")

print("La máquina eligió:", maquina)

if usuario == maquina:
    print("Empate")
elif usuario == "piedra" and maquina == "tijera":
    print("Ganaste")
elif usuario == "papel" and maquina == "piedra":
    print("Ganaste")
elif usuario == "tijera" and maquina == "papel":
    print("Ganaste")
else:
    print("Perdiste")
```

### Qué trabaja
- listas
- `choice()`
- `if` y `elif`
- comparación de textos

---

# Parte 10: ejercicios de refuerzo si sobra tiempo

## Opción A: lanzar dos dados y sumarlos

```python
import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print("Dado 1:", dado1)
print("Dado 2:", dado2)
print("Suma:", dado1 + dado2)
```

---

## Opción B: generar 5 números aleatorios con `for`

```python
import random

for i in range(5):
    numero = random.randint(1, 10)
    print(numero)
```

---

## Opción C: escoger varias veces un elemento de una lista

```python
import random

colores = ["rojo", "azul", "verde", "amarillo"]

for i in range(3):
    print(random.choice(colores))
```

---

# Parte 11: cómo conectar esta clase con lógica

Esta clase no debe sentirse solo como “cosas al azar”.

El objetivo real es mostrar que `random` sirve para combinar conceptos ya vistos.

Puedes recalcar que aquí estamos usando:

- variables
- funciones
- listas
- condicionales
- bucles
- entradas del usuario

Es una clase muy buena para consolidar conocimientos.

---

# Parte 12: propuesta de estructura de clase

## Bloque 1: introducción
- qué es un módulo
- qué es `random`
- por qué sirve

## Bloque 2: `randint()`
- explicar qué hace
- ejemplo del dado
- ejemplo de la moneda

## Bloque 3: `choice()`
- introducir lista
- elegir un elemento al azar

## Bloque 4: ejercicios guiados
- dado
- adivina el número
- nombre al azar

## Bloque 5: minijuego
- piedra, papel o tijera

## Bloque 6: cierre
- repaso
- preguntas
- ejercicio extra si sobra tiempo

---

# Parte 13: frases útiles para explicar en clase

- “`random` le da variedad al programa.”
- “El programa sigue reglas, pero ahora algunas decisiones las toma al azar.”
- “`randint` sirve para números enteros aleatorios.”
- “`choice` sirve para elegir un elemento de una lista.”
- “Esto se usa muchísimo en juegos.”
- “No hace falta memorizar todo; lo importante es entender para qué sirve.”

---

# Parte 14: mini resumen para cerrar la clase

Al final puedes resumir así:

> Hoy aprendimos a usar `random` para que nuestros programas puedan generar números al azar, elegir elementos de listas y hacer juegos sencillos. Este tema es importante porque mezcla muchas cosas que ya conocemos: variables, condicionales, listas, bucles y funciones.

---

# Parte 15: ideas para la clase siguiente

Después de `random`, puedes seguir con cualquiera de estas opciones:

- strings más a fondo
- funciones + listas + random en un miniproyecto
- introducción a `turtle`

Una muy buena transición sería:

- usar `random` para mover objetos o elegir colores en `turtle`

---

# Ejercicios propuestos para dejar preparados

## Nivel fácil
1. simular un dado
2. simular una moneda
3. mostrar 3 números aleatorios

## Nivel medio
4. elegir un nombre al azar de una lista
5. pedir al usuario que adivine un número
6. mostrar 5 colores aleatorios

## Nivel un poco más desafiante
7. piedra, papel o tijera
8. lanzar dos dados y decir cuál fue mayor
9. crear una función que devuelva un número aleatorio entre dos valores

---

# Ejemplo extra con función

```python
import random

def lanzar_dado():
    return random.randint(1, 6)

resultado = lanzar_dado()
print("El dado cayó en:", resultado)
```

Esto viene muy bien para enlazar la clase de `random` con la de funciones.

---

# Cierre para el profesor

Si la clase va muy rápido, no hace falta meter todas las funciones del módulo. Con estas basta:

- `random.randint()`
- `random.choice()`
- `random.shuffle()`
- `random.random()` como extra

La prioridad debe ser que entiendan el uso práctico y no saturarlos.
