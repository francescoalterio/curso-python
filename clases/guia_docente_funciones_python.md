# Guía docente: clase de funciones en Python

> Material de apoyo para el profesor. Pensado para leer desde el teléfono durante la clase.

---

## Objetivo de esta clase

Que los estudiantes entiendan que una **función** es un bloque de código reutilizable que sirve para:

- organizar instrucciones,
- evitar repetir código,
- dividir problemas grandes en partes pequeñas,
- preparar el camino para trabajar luego con cosas visuales como `turtle`.

---

## Qué deben saber antes de esta clase

Los estudiantes ya vieron:

- variables,
- tipos de datos (`str`, `int`, `float`, `bool`),
- condicionales (`if`),
- `match`,
- bucle `while`,
- bucle `for`.

Eso es suficiente para entrar a funciones.

---

# Idea principal para explicar

Una función se puede presentar como:

- una **receta**,
- una **máquina** que recibe datos y devuelve un resultado,
- o una **acción con nombre** que se puede reutilizar.

Frase útil para decir en clase:

> Una función es un bloque de instrucciones que guardamos con un nombre para poder usarlo varias veces sin repetir el código.

---

# Qué problema resuelven las funciones

Antes de enseñar sintaxis, conviene mostrar por qué existen.

## Ejemplo sin función

```python
print("Hola, Ana")
print("Bienvenida al sistema")
print("--------------------")

print("Hola, Luis")
print("Bienvenido al sistema")
print("--------------------")
```

### Explicación para el profesor

Aquí hay repetición. Si quisiéramos cambiar el mensaje, habría que editar varias líneas.

## Ejemplo con función

```python
def saludar(nombre):
    print("Hola,", nombre)
    print("Bienvenido al sistema")
    print("--------------------")

saludar("Ana")
saludar("Luis")
```

### Mensaje clave

La función permite **reutilizar** el mismo bloque con datos diferentes.

---

# Definición simple de función

```python
def nombre_de_la_funcion():
    instrucciones
```

---

# Partes de una función

Esta es una de las secciones más importantes de la clase.

## Ejemplo base

```python
def sumar(a, b):
    resultado = a + b
    return resultado
```

## Partes que debes explicar

### 1. `def`
Es la palabra reservada que le dice a Python que vamos a crear una función.

### 2. nombre de la función
En el ejemplo:

```python
sumar
```

Es el nombre que usamos para identificar esa función.

### 3. paréntesis `()`
Ahí van los datos que la función puede recibir.

### 4. parámetros
En el ejemplo:

```python
a, b
```

Son variables que la función recibe al ser llamada.

### 5. dos puntos `:`
Indican que empieza el bloque de código de la función.

### 6. bloque indentado
Todo lo que está indentado pertenece a la función.

```python
resultado = a + b
return resultado
```

### 7. `return`
Sirve para devolver un resultado.

En este caso devuelve:

```python
resultado
```

---

# Diferencia entre parámetro y argumento

Esto suele confundir al alumno, así que conviene decirlo simple.

## Parámetro
Es la variable que aparece en la definición.

```python
def saludar(nombre):
    print("Hola", nombre)
```

Aquí `nombre` es un **parámetro**.

## Argumento
Es el valor real que mandamos cuando usamos la función.

```python
saludar("Carlos")
```

Aquí `"Carlos"` es el **argumento**.

### Forma breve de explicarlo

- parámetro = variable de entrada,
- argumento = dato real que enviamos.

---

# Estructura general para enseñar funciones

## Caso 1: función sin parámetros y sin return

```python
def saludar():
    print("Hola")

saludar()
```

### Qué explicar

- la función existe,
- se llama con su nombre,
- ejecuta instrucciones,
- no recibe datos,
- no devuelve nada.

---

## Caso 2: función con parámetros y sin return

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("María")
```

### Qué explicar

- ahora la función recibe información,
- se puede reutilizar con distintos nombres.

---

## Caso 3: función con parámetros y con return

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)
```

### Qué explicar

- la función no solo hace algo,
- también puede producir un valor que luego guardamos en una variable.

---

# Diferencia entre `print()` y `return`

Esto hay que dejarlo clarísimo.

## Con `print()`

```python
def sumar(a, b):
    print(a + b)
```

Esto **muestra** el resultado en pantalla.

## Con `return`

```python
def sumar(a, b):
    return a + b
```

Esto **devuelve** el resultado para usarlo después.

## Ejemplo comparativo

```python
def suma_con_print(a, b):
    print(a + b)


def suma_con_return(a, b):
    return a + b

x = suma_con_return(2, 3)
print(x)
```

### Frase útil

> `print()` enseña el valor. `return` entrega el valor.

---

# Orden recomendado para explicar en clase

## Paso 1. Función más simple posible

```python
def saludar():
    print("Hola")

saludar()
```

## Paso 2. Función con un parámetro

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Lucía")
```

## Paso 3. Función con dos parámetros

```python
def sumar(a, b):
    print(a + b)

sumar(4, 7)
```

## Paso 4. Función con `return`

```python
def sumar(a, b):
    return a + b

resultado = sumar(4, 7)
print("La suma es:", resultado)
```

## Paso 5. Función con condicional

```python
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par(4))
print(es_par(7))
```

---

# Ejemplos listos para usar en clase

## Ejemplo 1: saludo

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Ana")
saludar("Pedro")
```

## Ejemplo 2: suma

```python
def sumar(a, b):
    return a + b

print(sumar(10, 5))
```

## Ejemplo 3: mayor de edad

```python
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

print(es_mayor_de_edad(20))
print(es_mayor_de_edad(15))
```

## Ejemplo 4: número mayor

```python
def mayor(a, b):
    if a > b:
        return a
    else:
        return b

print(mayor(8, 3))
```

## Ejemplo 5: tabla de multiplicar

```python
def tabla(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

tabla(5)
```

## Ejemplo 6: convertir temperatura

```python
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_a_fahrenheit(30))
```

---

# Errores típicos que van a cometer

## 1. Olvidar llamar la función

```python
def saludar():
    print("Hola")
```

Si no escriben:

```python
saludar()
```

no pasa nada.

---

## 2. Mala indentación

```python
def saludar():
print("Hola")
```

Eso da error. El bloque debe ir indentado.

Correcto:

```python
def saludar():
    print("Hola")
```

---

## 3. Confundir `print` con `return`

Muchos alumnos creen que imprimir equivale a devolver.

Conviene mostrar que no es lo mismo.

---

## 4. Llamar la función con menos o más argumentos de los necesarios

```python
def sumar(a, b):
    return a + b

sumar(5)
```

Eso da error porque falta un argumento.

---

## 5. Creer que las variables internas existen fuera de la función

```python
def prueba():
    x = 10

print(x)
```

Esto da error porque `x` solo existe dentro de la función.

---

# Cómo explicarlo de forma intuitiva

Puedes usar esta analogía:

## Analogía de la licuadora

- La función es la licuadora.
- Los parámetros son los ingredientes.
- El `return` es el batido que sale.

Ejemplo:

```python
def licuar(fruta, leche):
    return "Batido de " + fruta
```

No hace falta que sea técnicamente perfecto; sirve para que entiendan la idea.

---

# Mini ejercicios para hacer en clase

## Ejercicio 1
Crear una función que imprima:

```python
Hola mundo
```

### Solución

```python
def hola():
    print("Hola mundo")

hola()
```

---

## Ejercicio 2
Crear una función que reciba un nombre y lo salude.

### Solución

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Carlos")
```

---

## Ejercicio 3
Crear una función que reciba dos números y devuelva la resta.

### Solución

```python
def restar(a, b):
    return a - b

print(restar(10, 4))
```

---

## Ejercicio 4
Crear una función que diga si una nota está aprobada.

### Solución

```python
def aprobado(nota):
    if nota >= 60:
        return True
    else:
        return False

print(aprobado(75))
```

---

## Ejercicio 5
Crear una función que reciba un número y muestre su tabla de multiplicar.

### Solución

```python
def tabla(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

tabla(7)
```

---

# Propuesta de dinámica de clase

## Parte 1: repaso breve
Duración estimada: 10 a 15 minutos.

Repasar rápidamente:

- variables,
- `if`,
- `for`,
- `while`.

Ejemplo de repaso:

```python
numero = 5
if numero > 0:
    print("Es positivo")
```

---

## Parte 2: introducir funciones
Duración estimada: 20 a 30 minutos.

Secuencia sugerida:

1. función sin parámetros,
2. función con parámetros,
3. función con `return`,
4. función con condicional.

---

## Parte 3: práctica guiada
Duración estimada: 20 a 30 minutos.

Haz que escriban:

- un saludo,
- una suma,
- una función que diga si un número es par,
- una tabla de multiplicar.

---

## Parte 4: mini reto final
Duración estimada: 10 a 15 minutos.

Reto:

Crear una función que reciba una edad y devuelva si la persona es:

- menor de edad,
- mayor de edad.

Ejemplo:

```python
def clasificar_edad(edad):
    if edad < 18:
        return "Menor de edad"
    else:
        return "Mayor de edad"
```

---

# Sección extra para alargar la clase: listas

Si la clase es larga, puedes enlazar funciones con listas sin complicarlo mucho.

## Qué es una lista

Una lista es una estructura que permite guardar varios valores en una sola variable.

```python
nombres = ["Ana", "Luis", "Pedro"]
```

## Acceder a elementos

```python
print(nombres[0])
print(nombres[1])
```

## Recorrer una lista con `for`

```python
nombres = ["Ana", "Luis", "Pedro"]

for nombre in nombres:
    print(nombre)
```

## Función que use una lista

```python
def mostrar_nombres(lista):
    for nombre in lista:
        print(nombre)

nombres = ["Ana", "Luis", "Pedro"]
mostrar_nombres(nombres)
```

### Idea pedagógica

Así muestras que una función también puede recibir una lista como parámetro.

---

# Ejercicios simples con listas

## Ejercicio 1
Crear una lista con 5 frutas e imprimirlas.

```python
frutas = ["manzana", "pera", "uva", "mango", "fresa"]

for fruta in frutas:
    print(fruta)
```

## Ejercicio 2
Crear una función que reciba una lista de números y los imprima.

```python
def mostrar_numeros(lista):
    for numero in lista:
        print(numero)

numeros = [1, 2, 3, 4, 5]
mostrar_numeros(numeros)
```

## Ejercicio 3
Crear una función que sume todos los números de una lista.

```python
def sumar_lista(lista):
    total = 0
    for numero in lista:
        total = total + numero
    return total

numeros = [2, 4, 6]
print(sumar_lista(numeros))
```

---

# Puente hacia la próxima clase visual

Frase para cerrar la clase:

> Ahora que sabemos crear funciones, luego podremos hacer funciones para dibujar figuras, mover objetos y crear cosas visuales en pantalla.

Ejemplos de nombres que puedes mencionar para sembrar la idea:

- `dibujar_cuadrado()`
- `mover_derecha()`
- `cambiar_color()`

Eso hace que vean que funciones no es teoría aislada, sino una herramienta real para construir programas visuales.

---

# Resumen final para el profesor

## Qué deben llevarse de esta clase

Los estudiantes deberían salir entendiendo que:

- una función sirve para reutilizar código,
- una función puede recibir datos,
- una función puede devolver un resultado,
- `print` no es lo mismo que `return`,
- las funciones ayudan a organizar mejor los programas.

## Prioridad real de la clase

No hace falta que dominen todo perfecto.

La meta principal es que puedan:

- leer una función sencilla,
- escribir una función sencilla,
- llamar una función con parámetros,
- entender un `return` básico.

---

# Chuleta rápida para consultar durante la clase

## Sintaxis mínima

```python
def nombre(parametro1, parametro2):
    instrucciones
    return resultado
```

## Ejemplo corto

```python
def sumar(a, b):
    return a + b

print(sumar(3, 4))
```

## Ideas clave

- `def` crea la función.
- Los parámetros son datos de entrada.
- El bloque indentado es el cuerpo de la función.
- `return` devuelve un valor.
- Para usar la función hay que llamarla.

---

# Cierre sugerido para decir en voz alta

> Hoy aprendimos a crear funciones. Las funciones nos ayudan a no repetir código y a organizar mejor nuestros programas. Más adelante, esto nos va a servir para hacer programas visuales de una forma mucho más clara.
