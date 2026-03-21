# Guía docente: clase de listas en Python

> Material pensado para ti como profesor. Está escrito para leerlo rápido desde el teléfono mientras das la clase.

---

## Objetivo de esta clase

Que el estudiante entienda que una **lista** sirve para guardar varios valores dentro de una sola variable, y que pueda:

- crear listas,
- acceder a elementos,
- modificar elementos,
- recorrer listas con `for`,
- usar operaciones básicas frecuentes,
- resolver pequeños ejercicios de lógica con listas.

---

## Qué deben saber antes de esta clase

Idealmente ya deben haber visto:

- variables,
- tipos de datos,
- `if`,
- `for`,
- `while`,
- funciones básicas o al menos llamadas de funciones.

Si no dominan todavía el `for`, esta clase se vuelve más pesada.

---

## Idea principal para explicar

Una lista es como una **caja con varios espacios** donde guardamos varios datos en orden.

Ejemplo mental:

- una variable normal guarda **un valor**,
- una lista guarda **muchos valores**.

Ejemplo:

```python
nombre = "Ana"
```

Aquí hay un solo dato.

```python
nombres = ["Ana", "Luis", "Pedro"]
```

Aquí hay varios datos dentro de una sola variable.

---

## Definición sencilla para decir en clase

> Una lista es una estructura de datos que permite guardar varios elementos en una sola variable y acceder a ellos por posición.

No hace falta complicarlo mucho más al principio.

---

## Primera explicación visual

Puedes dibujar esto en la pizarra:

```text
nombres = ["Ana", "Luis", "Pedro"]
            0       1        2
```

Y explicar:

- cada elemento tiene una posición,
- en Python la primera posición es **0**,
- eso se llama **índice**.

Esto suele ser una de las cosas que más confunde al principio.

---

## Primer ejemplo de la clase

```python
nombres = ["Ana", "Luis", "Pedro"]

print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[2])
```

### Qué explicar aquí

- la lista completa se imprime con `print(nombres)`
- un elemento específico se obtiene con corchetes: `nombres[0]`
- los índices empiezan en cero

---

## Partes clave de una lista

### 1. Nombre de la variable

```python
nombres = ["Ana", "Luis", "Pedro"]
```

Aquí el nombre es:

```python
nombres
```

### 2. Corchetes

Los corchetes `[]` indican que estamos creando una lista.

### 3. Elementos

Son los valores que hay dentro:

```python
"Ana", "Luis", "Pedro"
```

### 4. Comas

Separan los elementos.

### 5. Índice

La posición de cada elemento:

- `"Ana"` está en índice `0`
- `"Luis"` está en índice `1`
- `"Pedro"` está en índice `2`

---

## Tipos de listas que puedes mostrar

### Lista de enteros

```python
numeros = [10, 20, 30, 40]
```

### Lista de cadenas

```python
colores = ["rojo", "azul", "verde"]
```

### Lista de booleanos

```python
estados = [True, False, True]
```

### Lista mezclada

```python
datos = ["Ana", 20, True]
```

### Recomendación docente

Puedes decir que Python permite mezclar tipos, pero que **al empezar** es mejor usar listas con elementos parecidos para evitar confusión.

---

## Acceder a elementos

```python
frutas = ["manzana", "pera", "uva"]

print(frutas[0])
print(frutas[1])
print(frutas[2])
```

### Explicación importante

Acceder significa **leer** un valor de una posición específica.

---

## Modificar elementos

```python
frutas = ["manzana", "pera", "uva"]
frutas[1] = "sandía"

print(frutas)
```

Resultado:

```python
['manzana', 'sandía', 'uva']
```

### Qué explicar

- una lista se puede cambiar,
- eso la hace muy útil,
- estamos reemplazando el elemento que está en la posición `1`.

---

## Ver cuántos elementos tiene una lista

```python
frutas = ["manzana", "pera", "uva"]
print(len(frutas))
```

### Explicación

`len()` devuelve la cantidad de elementos.

Esto es muy útil para:

- contar,
- recorrer,
- validar posiciones,
- saber si una lista está vacía o no.

---

## Agregar elementos

```python
frutas = ["manzana", "pera"]
frutas.append("uva")

print(frutas)
```

### Explicación

`append()` agrega un elemento al final de la lista.

Esta es una de las operaciones más útiles y más fáciles de enseñar.

---

## Eliminar elementos

### Opción simple para enseñar: `remove()`

```python
frutas = ["manzana", "pera", "uva"]
frutas.remove("pera")

print(frutas)
```

### Explicación

`remove()` elimina el valor que le indiques.

No hace falta entrar hoy en demasiadas variantes de borrado si no quieres complicar.

---

## Recorrer una lista con `for`

Este es probablemente el punto más importante de la clase.

```python
frutas = ["manzana", "pera", "uva"]

for fruta in frutas:
    print(fruta)
```

### Qué decir

- `for` va elemento por elemento,
- cada vez guarda temporalmente uno en la variable `fruta`,
- así podemos trabajar con todos sin escribirlos uno por uno.

### Idea clave

Aquí es donde la lista se conecta con la lógica de programación.

---

## Recorrer una lista y tomar decisiones

```python
numeros = [3, 8, 1, 10, 5]

for numero in numeros:
    if numero > 5:
        print(numero, "es mayor que 5")
```

### Qué trabajas aquí

- listas,
- `for`,
- `if`,
- comparación,
- lectura de datos en secuencia.

Este tipo de ejercicio vale mucho pedagógicamente.

---

## Acumular resultados con listas

Puedes introducir una idea básica de construcción de lista:

```python
pares = []

for numero in [1, 2, 3, 4, 5, 6]:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)
```

### Explicación simple

- empezamos con una lista vacía,
- revisamos cada número,
- si cumple la condición, lo guardamos.

Muy útil para enseñar lógica real.

---

## Operaciones básicas recomendadas para esta clase

Yo me quedaría con estas y no metería demasiadas más:

- crear lista: `[]`
- acceder por índice: `lista[0]`
- modificar: `lista[1] = valor`
- contar elementos: `len(lista)`
- agregar: `append()`
- eliminar: `remove()`
- recorrer con `for`

Con eso ya tienen una base bastante buena.

---

## Cosas que yo no complicaría demasiado hoy

No profundizaría todavía en:

- listas anidadas,
- `insert()`,
- `pop()`,
- slicing,
- list comprehensions,
- métodos avanzados,
- ordenar con muchas variantes,
- copias profundas o superficiales.

Todo eso puede esperar.

---

## Errores comunes que debes advertir

### 1. Pensar que el primer índice es 1

Error común:

```python
nombres = ["Ana", "Luis", "Pedro"]
print(nombres[1])
```

Muchos creerán que sale `Ana`, pero sale `Luis`.

### 2. Salirse del rango

```python
nombres = ["Ana", "Luis", "Pedro"]
print(nombres[3])
```

Esto da error porque solo existen los índices `0`, `1` y `2`.

### 3. Confundir elemento con índice

A veces creen que `frutas["pera"]` funciona. No funciona así.

### 4. Olvidar los corchetes

```python
numeros = 1, 2, 3
```

Eso no está creando una lista de la forma que quieres enseñarles hoy.

### 5. Escribir mal `append()`

Por ejemplo:

```python
frutas.append["uva"]
```

Eso está mal. Lo correcto es:

```python
frutas.append("uva")
```

---

## Forma sencilla de explicar `append()`

Puedes decir:

> `append()` es como decirle a la lista: “guárdame este nuevo valor al final”.

---

## Ejemplos listos para usar en clase

### Ejemplo 1: lista de nombres

```python
nombres = ["Ana", "Luis", "Pedro"]

for nombre in nombres:
    print("Hola", nombre)
```

### Ejemplo 2: sumar elementos manualmente

```python
numeros = [10, 20, 30, 40]
suma = 0

for numero in numeros:
    suma = suma + numero

print("La suma es:", suma)
```

### Ejemplo 3: contar aprobados

```python
notas = [80, 45, 70, 30, 90]
aprobados = 0

for nota in notas:
    if nota >= 60:
        aprobados = aprobados + 1

print("Cantidad de aprobados:", aprobados)
```

### Ejemplo 4: encontrar el mayor

```python
numeros = [3, 9, 2, 15, 7]
mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

print("El número mayor es:", mayor)
```

Este ejemplo es muy bueno para trabajar lógica.

---

## Ejercicios para hacer en clase

### Ejercicio 1
Crea una lista con 5 colores e imprime el primero y el último.

### Ejercicio 2
Crea una lista con 4 números y cambia el tercero por otro valor.

### Ejercicio 3
Recorre una lista de nombres e imprime un saludo para cada uno.

### Ejercicio 4
Dada una lista de números, imprime solo los números mayores que 10.

### Ejercicio 5
Crea una lista vacía y agrega 3 frutas con `append()`.

### Ejercicio 6
Dada una lista de notas, cuenta cuántos estudiantes aprobaron con 60 o más.

### Ejercicio 7
Dada una lista de números, encuentra el número mayor.

---

## Mini dinámica guiada para la clase

Puedes hacer esta progresión:

### Paso 1
Mostrar una lista sencilla:

```python
numeros = [5, 8, 2, 10]
```

### Paso 2
Preguntar:

- ¿cuántos elementos tiene?
- ¿cuál es el primer elemento?
- ¿cuál es el índice del `2`?

### Paso 3
Modificar un elemento:

```python
numeros[2] = 99
```

### Paso 4
Recorrerla con `for`

```python
for numero in numeros:
    print(numero)
```

### Paso 5
Aplicar condición

```python
for numero in numeros:
    if numero > 6:
        print(numero)
```

Con eso conviertes una clase teórica en una clase dinámica.

---

## Cómo conectar listas con funciones

Si ya viste funciones o vas a verlas, puedes unir ambos temas con algo así:

```python
def mostrar_nombres(lista):
    for nombre in lista:
        print(nombre)

nombres = ["Ana", "Luis", "Pedro"]
mostrar_nombres(nombres)
```

### Qué ganas con esto

- refuerzas funciones,
- refuerzas listas,
- muestras que una función puede recibir una lista.

---

## Cómo conectar listas con Turtle más adelante

Cuando luego llegues a `turtle`, puedes explicar que las listas servirán para guardar:

- colores,
- posiciones,
- nombres de jugadores,
- puntajes,
- enemigos,
- objetos.

Eso les hace ver que no es un tema aislado.

---

## Estructura sugerida de la clase

### Parte 1: introducción
- qué es una lista,
- para qué sirve,
- ejemplos cotidianos.

### Parte 2: crear listas y acceder a elementos
- índices,
- lectura,
- modificación.

### Parte 3: operaciones básicas
- `len()`,
- `append()`,
- `remove()`.

### Parte 4: recorrer listas
- `for`,
- imprimir,
- condicionales.

### Parte 5: ejercicios
- saludos,
- contar,
- mayor,
- aprobados.

### Parte 6: cierre
- explicar que listas + funciones + condicionales + bucles ya permiten resolver problemas bastante reales.

---

## Frases útiles para explicar en clase

- “Una lista es una variable que puede guardar muchos valores.”
- “Cada valor tiene una posición llamada índice.”
- “En Python, el primer índice es 0.”
- “Con `for` podemos recorrer la lista sin ir posición por posición manualmente.”
- “Las listas son muy útiles cuando tenemos muchos datos del mismo tipo.”
- “Programar muchas veces consiste en guardar datos, recorrerlos y tomar decisiones.”

---

## Resumen corto para cerrar la clase

Hoy aprendimos que:

- una lista guarda varios valores,
- cada valor tiene un índice,
- podemos leer y cambiar elementos,
- podemos agregar y eliminar,
- podemos recorrer listas con `for`,
- y podemos usar listas para resolver ejercicios de lógica.

---

## Mini reto final opcional

```python
numeros = [4, 7, 2, 9, 12, 1]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print("Números pares:", pares)
```

### Qué trabaja este reto

- listas,
- lista vacía,
- `for`,
- `if`,
- operador módulo,
- `append()`.

Muy buen ejercicio de cierre.

---

## Recomendación docente final

Para esta clase, prioriza que entiendan bien:

1. qué es una lista,
2. cómo acceder a elementos,
3. cómo recorrerla con `for`,
4. cómo usarla con `if`.

Eso vale mucho más que intentar cubrir veinte métodos distintos.

Si el grupo va bien, luego amplías.
