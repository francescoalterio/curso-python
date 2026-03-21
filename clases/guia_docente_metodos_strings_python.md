# Guía docente: métodos de strings en Python

## Objetivo de la clase
Que los estudiantes entiendan que un `string` es texto y que Python trae herramientas ya hechas para manipularlo. La meta no es memorizar todos los métodos, sino aprender a usar los más útiles en ejercicios reales.

---

## Qué debería saber el estudiante antes de esta clase
Idealmente ya debería conocer:

- variables
- tipos de datos básicos
- `if`
- `for`
- `while`
- funciones básicas

Si además ya vio listas, mejor, pero no es obligatorio.

---

## Objetivos concretos de la clase
Al final de la clase deberían poder:

- guardar texto en variables
- usar métodos comunes de strings
- limpiar texto ingresado por el usuario
- cambiar mayúsculas y minúsculas
- buscar texto dentro de otro texto
- dividir texto en partes
- unir texto
- resolver ejercicios prácticos con cadenas

---

## Idea clave para explicar
Un `string` es una cadena de texto.

Ejemplo:

```python
nombre = "Carlos"
mensaje = "Hola mundo"
```

Y Python trae funciones especiales llamadas **métodos** que ya vienen preparadas para trabajar con texto.

Ejemplo:

```python
texto = "hola"
print(texto.upper())
```

Resultado:

```python
HOLA
```

---

## Cómo explicarlo de forma sencilla
Puedes decirlo así en clase:

> Un método es una acción que un dato sabe hacer.
> Por ejemplo, un texto puede pasarse a mayúsculas, a minúsculas, separarse en partes o limpiarse.

Comparación útil:

- variable: la caja donde guardo el texto
- string: el texto en sí
- método: la acción que puedo hacerle a ese texto

---

## Estructura de la clase

### Parte 1: repaso rápido
Repasa en 5 minutos:

- qué es un string
- cómo se guarda en una variable
- cómo se imprime
- concatenación básica

Ejemplo:

```python
nombre = "Ana"
print("Hola " + nombre)
```

---

## Parte 2: métodos más importantes de strings

### 1. `upper()`
Convierte el texto a mayúsculas.

```python
texto = "hola"
print(texto.upper())
```

Resultado:

```python
HOLA
```

Uso práctico:
- títulos
- comparar respuestas sin importar mayúsculas/minúsculas

---

### 2. `lower()`
Convierte el texto a minúsculas.

```python
texto = "HoLa"
print(texto.lower())
```

Resultado:

```python
hola
```

Muy útil para validar entradas del usuario.

```python
respuesta = input("Escribe sí o no: ").lower()
if respuesta == "sí":
    print("Correcto")
```

---

### 3. `strip()`
Elimina espacios al inicio y al final.

```python
texto = "   hola   "
print(texto.strip())
```

Resultado:

```python
hola
```

Muy útil porque mucha gente mete espacios sin querer.

```python
nombre = input("Escribe tu nombre: ").strip()
print("Hola", nombre)
```

---

### 4. `replace()`
Reemplaza una parte del texto por otra.

```python
texto = "Me gusta Python"
print(texto.replace("Python", "programar"))
```

Resultado:

```python
Me gusta programar
```

Uso práctico:
- corregir texto
- cambiar palabras
- limpiar caracteres

---

### 5. `find()`
Busca la posición de un texto dentro de otro.

```python
texto = "Hola mundo"
print(texto.find("mundo"))
```

Resultado:

```python
5
```

Si no lo encuentra, devuelve `-1`.

```python
texto = "Hola mundo"
print(texto.find("Python"))
```

Resultado:

```python
-1
```

---

### 6. `startswith()`
Sirve para saber si un texto empieza con algo.

```python
texto = "Python es fácil"
print(texto.startswith("Python"))
```

Resultado:

```python
True
```

---

### 7. `endswith()`
Sirve para saber si un texto termina con algo.

```python
correo = "usuario@gmail.com"
print(correo.endswith(".com"))
```

Resultado:

```python
True
```

---

### 8. `split()`
Divide un string en varias partes y devuelve una lista.

```python
texto = "rojo,verde,azul"
colores = texto.split(",")
print(colores)
```

Resultado:

```python
['rojo', 'verde', 'azul']
```

Muy bueno para enlazar con listas.

---

### 9. `join()`
Une varios strings en uno solo.

```python
palabras = ["Hola", "mundo"]
resultado = " ".join(palabras)
print(resultado)
```

Resultado:

```python
Hola mundo
```

---

### 10. `len()`
No es un método, pero conviene enseñarlo aquí porque se usa mucho con strings.

```python
texto = "Python"
print(len(texto))
```

Resultado:

```python
6
```

Sirve para saber cuántos caracteres tiene un texto.

---

## Resumen rápido para enseñar en clase

| Herramienta | Para qué sirve |
|---|---|
| `upper()` | poner en mayúsculas |
| `lower()` | poner en minúsculas |
| `strip()` | quitar espacios al inicio y al final |
| `replace()` | reemplazar texto |
| `find()` | buscar una parte dentro del texto |
| `startswith()` | comprobar cómo empieza |
| `endswith()` | comprobar cómo termina |
| `split()` | dividir el texto |
| `join()` | unir textos |
| `len()` | contar caracteres |

---

## Cómo conectarlo con lógica
Esta clase no debe sentirse como “memorizar comandos”.

Cada método debe conectarse con problemas reales:

- limpiar respuestas del usuario
- validar nombres
- revisar correos simples
- buscar palabras
- separar datos
- unir frases

---

## Ejemplos sencillos para explicar en vivo

### Ejemplo 1: limpiar nombre del usuario
```python
nombre = input("Escribe tu nombre: ").strip().title()
print("Hola", nombre)
```

Nota docente: `title()` también puede mencionarse como extra. Convierte la primera letra de cada palabra en mayúscula.

---

### Ejemplo 2: comparar respuestas sin problemas de mayúsculas
```python
respuesta = input("Escribe si o no: ").strip().lower()

if respuesta == "si":
    print("Elegiste sí")
else:
    print("Elegiste otra cosa")
```

---

### Ejemplo 3: verificar dominio simple de correo
```python
correo = input("Escribe tu correo: ").strip().lower()

if correo.endswith("@gmail.com"):
    print("Es un correo de Gmail")
else:
    print("No es un correo de Gmail")
```

---

### Ejemplo 4: separar palabras
```python
frase = input("Escribe una frase: ")
palabras = frase.split(" ")
print(palabras)
print("La frase tiene", len(palabras), "palabras")
```

---

### Ejemplo 5: reemplazar palabras
```python
frase = "Me gusta Java"
nueva_frase = frase.replace("Java", "Python")
print(nueva_frase)
```

---

## Ejercicios guiados para clase

### Ejercicio 1
Pide al usuario su nombre y muéstralo en mayúsculas.

```python
nombre = input("Escribe tu nombre: ")
print(nombre.upper())
```

---

### Ejercicio 2
Pide una frase y muéstrala en minúsculas.

```python
frase = input("Escribe una frase: ")
print(frase.lower())
```

---

### Ejercicio 3
Pide al usuario una palabra con espacios al principio y al final. Luego quita esos espacios.

```python
palabra = input("Escribe una palabra con espacios: ")
print(palabra.strip())
```

---

### Ejercicio 4
Pide una frase y reemplaza una palabra por otra.

```python
frase = input("Escribe una frase: ")
print(frase.replace("a", "@"))
```

---

### Ejercicio 5
Pide una palabra y muestra cuántas letras tiene.

```python
palabra = input("Escribe una palabra: ")
print(len(palabra))
```

---

## Ejercicios un poco más completos

### 1. Validador simple de respuesta
```python
respuesta = input("¿Quieres continuar? (si/no): ").strip().lower()

if respuesta == "si":
    print("Continuando...")
elif respuesta == "no":
    print("Saliendo...")
else:
    print("Respuesta no válida")
```

---

### 2. Contar cuántas veces aparece una letra
Aquí puedes introducir `count()` como extra.

```python
texto = input("Escribe una frase: ").lower()
letra = input("Escribe una letra: ").lower()
print("La letra aparece", texto.count(letra), "veces")
```

---

### 3. Separar nombres
```python
nombres = input("Escribe varios nombres separados por coma: ")
lista_nombres = nombres.split(",")
print(lista_nombres)
```

Puedes luego recorrer la lista:

```python
for nombre in lista_nombres:
    print(nombre.strip())
```

---

## Extras útiles si sobra tiempo

### `title()`
Pone la primera letra de cada palabra en mayúscula.

```python
nombre = "juan perez"
print(nombre.title())
```

Resultado:

```python
Juan Perez
```

### `capitalize()`
Pone en mayúscula solo la primera letra del texto.

```python
texto = "hola mundo"
print(texto.capitalize())
```

Resultado:

```python
Hola mundo
```

### `count()`
Cuenta cuántas veces aparece algo.

```python
texto = "banana"
print(texto.count("a"))
```

Resultado:

```python
3
```

---

## Errores comunes de los estudiantes

### 1. Olvidar los paréntesis
Incorrecto:

```python
print(texto.upper)
```

Correcto:

```python
print(texto.upper())
```

---

### 2. Pensar que `len()` es un método
Incorrecto:

```python
texto.len()
```

Correcto:

```python
len(texto)
```

---

### 3. Confundir strings con números
A veces intentan sumar texto con número sin convertir.

Incorrecto:

```python
edad = 20
print("Tu edad es " + edad)
```

Correcto:

```python
edad = 20
print("Tu edad es " + str(edad))
```

O más simple:

```python
print("Tu edad es", edad)
```

---

### 4. Creer que los métodos cambian siempre la variable original
Ejemplo:

```python
texto = "hola"
texto.upper()
print(texto)
```

Resultado:

```python
hola
```

Porque hay que guardar el resultado si quieres conservar el cambio.

Correcto:

```python
texto = "hola"
texto = texto.upper()
print(texto)
```

---

## Preguntas para hacer en clase
Puedes ir preguntando:

- ¿Qué diferencia hay entre `upper()` y `lower()`?
- ¿Para qué sirve `strip()` en un programa real?
- ¿Qué devuelve `split()`?
- ¿Qué pasa si `find()` no encuentra el texto?
- ¿Por qué `len()` no lleva punto antes?

---

## Mini reto final
Haz un programa que:

1. pida al usuario una frase
2. la limpie con `strip()`
3. la convierta a minúsculas
4. muestre cuántos caracteres tiene
5. muestre cuántas palabras tiene

Solución posible:

```python
frase = input("Escribe una frase: ").strip().lower()
print("Frase limpia:", frase)
print("Cantidad de caracteres:", len(frase))
print("Cantidad de palabras:", len(frase.split()))
```

---

## Cierre de la clase
Al cerrar, resume algo así:

> Hoy vimos que los strings no son solo texto guardado en una variable. También tienen herramientas muy útiles para limpiarlo, transformarlo, buscar partes y separarlo.

Y conecta con lo siguiente:

- esto sirve para validaciones
- esto sirve para formularios
- esto sirve para juegos
- esto sirve para programas que reciben texto del usuario

---

## Orden recomendado para enseñar en clase
Si vas con el tiempo justo, enseña en este orden:

1. `upper()`
2. `lower()`
3. `strip()`
4. `replace()`
5. `len()`
6. `split()`
7. `find()`
8. extras si sobra tiempo

---

## Resumen docente final
Si te sobra poco tiempo y quieres ir a lo esencial, quédate con estos seis:

- `upper()`
- `lower()`
- `strip()`
- `replace()`
- `split()`
- `len()`

Con eso ya tienen una clase muy útil, muy práctica y fácil de conectar con ejercicios reales.
