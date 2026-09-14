# EJERCICIO 1 - Básico
# Validador de notas con promedio

# Pasos:
# 1. Crear una lista interna donde se guardarán solo las notas válidas (0-100).
# 2. validar_nota() revisa si una nota está en el rango permitido.
# 3. cargar_notas() recibe varias notas (*args), valida cada una reutilizando
#    validar_nota() y agrega a la lista solo las que sean válidas.
# 4. promedio() suma la lista interna y divide entre su cantidad de elementos.


class Calificador:
    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)


c = Calificador()
print(c.cargar_notas(85, 92, 110, 78, -5, 88))
print(c.promedio())

c2 = Calificador()
c2.cargar_notas(60, 70, 200, -10, 100)
print(c2.notas)
print(c2.promedio())


# EJERCICIO 2 - Básico
# Contador de palabras únicas

# Pasos:
# 1. Usar un conjunto (set) para evitar palabras repetidas.
# 2. Usar una lista para conservar el orden en que se fueron agregando.
# 3. agregar_palabra() guarda en ambas estructuras.
# 4. contar_palabras() retorna el tamaño del conjunto (únicas).
# 5. agregar_multiples() reutiliza agregar_palabra() para varias palabras.


class AnalizadorTexto:
    def __init__(self):
        self.conjunto_palabras = set()
        self.lista_palabras = []

    def agregar_palabra(self, palabra):
        self.conjunto_palabras.add(palabra)
        self.lista_palabras.append(palabra)

    def contar_palabras(self):
        return len(self.conjunto_palabras)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)



at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola")
print(at.contar_palabras())  


at2 = AnalizadorTexto()
at2.agregar_multiples("sol", "luna", "sol", "estrella", "luna")
print(at2.contar_palabras())
print(at2.lista_palabras)  



# EJERCICIO 3 - Básico
# Gestor de compras con totales

# Pasos:
# 1. Guardar los artículos en un diccionario {nombre: precio}.
# 2. total_carrito() suma todos los valores (precios) del diccionario.
# 3. articulos_por_rango() filtra los nombres cuyo precio esté en el rango.


class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        return [nombre for nombre, precio in self.articulos.items()
                if precio_min <= precio <= precio_max]

c = CarroCompras()
c.agregar_articulo("pan", 2.50)
c.agregar_articulo("leche", 3.00)
print(c.total_carrito())  # 5.50

c2 = CarroCompras()
c2.agregar_articulo("arroz", 1.20)
c2.agregar_articulo("aceite", 4.50)
c2.agregar_articulo("azucar", 1.80)
print(c2.articulos_por_rango(1.0, 2.0))  # ['arroz', 'azucar']


# EJERCICIO 4 - Medio
# Inversor de secuencias

# Pasos:
# 1. invertir_lista() recorre la lista de atrás hacia adelante con un bucle
#    (sin usar reversed()) y arma una nueva lista invertida.
# 2. invertir_multiples() recibe varias listas (*listas), invierte cada una
#    reutilizando invertir_lista() y guarda el resultado en un diccionario,
#    usando una tupla de la lista original como clave (las listas no son
#    hashables, por eso se convierten a tupla).


class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            resultado[tuple(lista)] = self.invertir_lista(lista)
        return resultado


inv = InversorSecuencia()
print(inv.invertir_lista([1, 2, 3]))

inv2 = InversorSecuencia()
print(inv2.invertir_multiples([1, 2, 3], ["a", "b", "c"]))


# EJERCICIO 5 - Básico
# Detector de números pares e impares

# Pasos:
# 1. es_par() usa el operador % para saber si un número es par.
# 2. separar() clasifica varios números (*numeros) en un diccionario con
#    claves 'pares' e 'impares', reutilizando es_par(). Se guarda el
#    resultado en un atributo para poder usarlo después.
# 3. cantidad_pares_impares() retorna una tupla con la cantidad de cada uno.


class AnalizadorNumeros:
    def __init__(self):
        self.clasificacion = {'pares': [], 'impares': []}

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        self.clasificacion = {'pares': [], 'impares': []}
        for numero in numeros:
            if self.es_par(numero):
                self.clasificacion['pares'].append(numero)
            else:
                self.clasificacion['impares'].append(numero)
        return self.clasificacion

    def cantidad_pares_impares(self):
        return (len(self.clasificacion['pares']), len(self.clasificacion['impares']))


an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))

an2 = AnalizadorNumeros()
an2.separar(10, 15, 20, 25, 30, 33)
print(an2.cantidad_pares_impares())


# EJERCICIO 6 - Medio
# Estadísticas de temperatura

# Pasos:
# 1. registrar_temperatura() guarda cada temperatura en una lista.
# 2. minima(), maxima() y promedio() calculan las estadísticas usando la lista.
# 3. registrar_multiples() reutiliza registrar_temperatura() para varios valores.

class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)


gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
print(gt.promedio())

gt2 = GestorTemperatura()
gt2.registrar_multiples(15, 22, 19, 28, 12)
print(gt2.minima(), gt2.maxima())


# EJERCICIO 7 - Básico
# Mapeador de edades

# Pasos:
# 1. agregar_persona() guarda nombre y edad en un diccionario {nombre: edad}.
# 2. personas_mayores() recorre el diccionario con items() y filtra los
#    nombres cuya edad sea mayor o igual a edad_minima.
# 3. edad_promedio() promedia los valores (edades) del diccionario.

class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        return [nombre for nombre, edad in self.personas.items() if edad >= edad_minima]

    def edad_promedio(self):
        return sum(self.personas.values()) / len(self.personas)


gp = GestorPersonas()
gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
print(gp.personas_mayores(18))

gp2 = GestorPersonas()
gp2.agregar_persona("Luis", 40)
gp2.agregar_persona("Marta", 22)
gp2.agregar_persona("Pedro", 15)
print(gp2.edad_promedio())


# EJERCICIO 8 - Medio
# Asignador de equipos

# Pasos:
# 1. crear_equipo() inicializa un equipo como una lista vacía dentro de un
#    diccionario {nombre_equipo: [jugadores]}.
# 2. agregar_jugador() añade un jugador a la lista de ese equipo.
# 3. equipo_mayor_integrantes() recorre el diccionario y retorna el nombre
#    del equipo cuya lista de jugadores tiene más elementos.

class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        return max(self.equipos, key=lambda equipo: len(self.equipos[equipo]))


eq = Equipos()
eq.crear_equipo("A")
eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")
print(eq.equipos)

eq2 = Equipos()
eq2.crear_equipo("Rojos")
eq2.crear_equipo("Azules")
eq2.agregar_jugador("Rojos", "Ana")
eq2.agregar_jugador("Azules", "Luis")
eq2.agregar_jugador("Azules", "Marta")
print(eq2.equipo_mayor_integrantes())


# EJERCICIO 9 - Básico
# Validador de caracteres

# Pasos:
# 1. solo_vocales() revisa si una letra pertenece a "aeiou" (sin distinguir
#    mayúsculas/minúsculas).
# 2. contar_por_tipo() recorre el texto carácter a carácter, reutiliza
#    solo_vocales() y clasifica en vocales, consonantes o dígitos.
# 3. Se guarda en un atributo el texto más largo analizado hasta el momento.

class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        conteo = {'vocales': 0, 'consonantes': 0, 'digitos': 0}
        for caracter in texto:
            if caracter.isalpha():
                if self.solo_vocales(caracter):
                    conteo['vocales'] += 1
                else:
                    conteo['consonantes'] += 1
            elif caracter.isdigit():
                conteo['digitos'] += 1
        return conteo



astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))


astr2 = AnalizadorString()
astr2.contar_por_tipo("Python")
astr2.contar_por_tipo("Programacion2024")
print(astr2.texto_mas_largo)


# EJERCICIO 10 - Medio
# Gestor de tareas con prioridad

# Pasos:
# 1. agregar_tarea() guarda cada tarea como una tupla (descripcion, prioridad)
#    dentro de una lista.
# 2. tareas_prioritarias() filtra las tuplas cuya prioridad sea "alta".
# 3. eliminar_completada() recorre la lista y elimina la tupla cuya
#    descripción coincida.


class Tareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        return [tarea for tarea in self.tareas if tarea[1] == "alta"]

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                break



t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
print(t.tareas_prioritarias())


t2 = Tareas()
t2.agregar_tarea("Lavar", "media")
t2.agregar_tarea("Cocinar", "alta")
t2.eliminar_completada("Lavar")
print(t2.tareas)


# EJERCICIO 11 - Básico
# Contador de frecuencia

# Pasos:
# 1. agregar_elemento() guarda cada elemento en un diccionario que funciona
#    como contador (clave: elemento, valor: veces que aparece).
# 2. elemento_mas_frecuente() retorna la clave con el valor más alto.
# 3. frecuencia_elemento() retorna cuántas veces apareció un elemento dado.

class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        self.frecuencias[elemento] = self.frecuencias.get(elemento, 0) + 1

    def elemento_mas_frecuente(self):
        return max(self.frecuencias, key=self.frecuencias.get)

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)


cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
print(cf.elemento_mas_frecuente())

cf2 = ContadorFrecuencia()
for letra in "abracadabra":
    cf2.agregar_elemento(letra)
print(cf2.frecuencia_elemento("a"))


# EJERCICIO 12 - Medio
# Selector de rango con tuplas

# Pasos:
# 1. crear_rango() genera una tupla con todos los números entre inicio y fin.
# 2. elementos_en_multiples_rangos() recibe varias tuplas (inicio, fin),
#    genera cada rango reutilizando crear_rango(), y une todo en un
#    conjunto para eliminar duplicados.


class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        elementos = set()
        for inicio, fin in rangos:
            elementos.update(self.crear_rango(inicio, fin))
        return sorted(elementos)


sr = SelectorRango()
print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))


sr2 = SelectorRango()
print(sr2.elementos_en_multiples_rangos((1, 2), (5, 7), (2, 3)))


# EJERCICIO 13 - Básico
# Combinador de listas

# Pasos:
# 1. intercalar() recorre ambas listas por índice y va alternando elementos.
# 2. intercalar_multiples() generaliza el proceso para varias listas
#    (*listas), recorriendo por posición y agregando el elemento de cada
#    lista que exista en esa posición.


class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        largo = max(len(lista1), len(lista2))
        for i in range(largo):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        resultado = []
        largo = max(len(lista) for lista in listas)
        for i in range(largo):
            for lista in listas:
                if i < len(lista):
                    resultado.append(lista[i])
        return resultado


cl = CombinadorListas()
print(cl.intercalar([1, 2], [3, 4]))

cl2 = CombinadorListas()
print(cl2.intercalar_multiples([1, 4], [2, 5], [3, 6]))


# EJERCICIO 14 - Medio
# Mapeo de estudiantes a notas

# Pasos:
# 1. registrar() guarda estudiante y nota en un diccionario.
# 2. estudiantes_aprobados() recorre el diccionario con items() y filtra
#    los nombres cuya nota sea mayor o igual a nota_minima.
# 3. mejor_estudiante() busca la clave con el valor más alto y retorna
#    una tupla (nombre, nota).


class RegistroNotas:
    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        return [nombre for nombre, nota in self.notas.items() if nota >= nota_minima]

    def mejor_estudiante(self):
        nombre = max(self.notas, key=self.notas.get)
        return (nombre, self.notas[nombre])


rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
print(rn.mejor_estudiante())

rn2 = RegistroNotas()
rn2.registrar("Luis", 55)
rn2.registrar("Marta", 80)
rn2.registrar("Pedro", 40)
print(rn2.estudiantes_aprobados(60))



# EJERCICIO 15 - Básico
# Divisores de un número

# Pasos:
# 1. encontrar_divisores() recorre desde 1 hasta el número y guarda en una
#    tupla los que dividen exactamente (sin residuo).
# 2. es_perfecto() reutiliza encontrar_divisores(), suma todos menos el
#    número mismo, y compara si esa suma es igual al número.
# 3. encontrar_multiples_divisores() recibe varios números (*numeros) y
#    arma un diccionario {numero: tupla_divisores}.


class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma_propios = sum(d for d in divisores if d != numero)
        return suma_propios == numero

    def encontrar_multiples_divisores(self, *numeros):
        return {numero: self.encontrar_divisores(numero) for numero in numeros}


df = DivisorFinder()
print(df.encontrar_divisores(12))

df2 = DivisorFinder()
print(df2.es_perfecto(28))
print(df2.encontrar_multiples_divisores(6, 12))


# EJERCICIO 16 - Medio
# Codificador/Decodificador (Cifrado César)

# Pasos:
# 1. codificar_letra() usa ord()/chr() y el operador % para desplazar una
#    letra dentro del alfabeto, respetando mayúsculas y minúsculas.
# 2. codificar_palabra() reutiliza codificar_letra() para toda la palabra,
#    y guarda el resultado en un diccionario historial {palabra: codificada}.


class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            return chr((ord(letra) - base + desplazamiento) % 26 + base)
        return letra

    def codificar_palabra(self, palabra, desplazamiento):
        codificada = "".join(self.codificar_letra(letra, desplazamiento) for letra in palabra)
        self.historial[palabra] = codificada
        return codificada


cc = CodificadorCesar()
print(cc.codificar_palabra("hola", 3))

cc2 = CodificadorCesar()
cc2.codificar_palabra("Python", 5)
print(cc2.historial)


# EJERCICIO 17 - Básico
# Grupo de edades

# Pasos:
# 1. clasificar_edad() usa if/elif para retornar la categoría según la edad.
# 2. agrupar_por_categoria() recibe varias edades (*edades), reutiliza
#    clasificar_edad() y arma un diccionario {categoria: [edades]}. Se
#    guarda el resultado en un atributo para reutilizarlo.
# 3. edad_promedio_categoria() promedia las edades de una categoría dada.


class AgrupadorEdades:
    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):
        if edad < 13:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.grupos = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.grupos.setdefault(categoria, []).append(edad)
        return self.grupos

    def edad_promedio_categoria(self, categoria):
        edades = self.grupos.get(categoria, [])
        if not edades:
            return 0
        return sum(edades) / len(edades)


ae = AgrupadorEdades()
print(ae.agrupar_por_categoria(5, 15, 30, 70))


ae2 = AgrupadorEdades()
ae2.agrupar_por_categoria(10, 12, 40, 50, 80)
print(ae2.edad_promedio_categoria("adulto"))


# EJERCICIO 18 - Medio
# Matriz de distancias

# Pasos:
# 1. distancia_euclidiana() recibe dos tuplas (x, y), calcula la distancia
#    con la fórmula sqrt((x2-x1)^2 + (y2-y1)^2) y guarda el resultado en
#    una lista interna.
# 2. punto_mas_cercano() reutiliza distancia_euclidiana() para comparar
#    cada punto contra la referencia y retorna el más cercano.

import math

class CalculadorDistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        distancia = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        self.distancias.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        return min(puntos, key=lambda punto: self.distancia_euclidiana(referencia, punto))


cd = CalculadorDistancia()
print(cd.distancia_euclidiana((0, 0), (3, 4)))

cd2 = CalculadorDistancia()
print(cd2.punto_mas_cercano((0, 0), (10, 10), (1, 1), (5, 5)))



# EJERCICIO 19 - Básico
# Inventario de productos

# Pasos:
# 1. agregar_stock() guarda o suma cantidad en un diccionario {producto: cantidad}.
# 2. restar_stock() valida que haya suficiente stock antes de restar y
#    retorna True/False.
# 3. productos_bajo_stock() filtra los productos cuya cantidad sea menor
#    al mínimo indicado.


class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        self.stock[producto] = self.stock.get(producto, 0) + cantidad

    def restar_stock(self, producto, cantidad):
        if self.stock.get(producto, 0) >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        return [producto for producto, cantidad in self.stock.items() if cantidad < minimo]


inv = Inventario()
inv.agregar_stock("pan", 50)
print(inv.restar_stock("pan", 30))
print(inv.productos_bajo_stock(15))

inv2 = Inventario()
inv2.agregar_stock("leche", 10)
inv2.agregar_stock("huevos", 5)
print(inv2.restar_stock("huevos", 20))
print(inv2.productos_bajo_stock(8))


# EJERCICIO 20 - Avanzado
# Analizador de patrones en textos

# Pasos:
# 1. encontrar_palabras() separa el texto con split() y filtra las palabras
#    que empiecen con el patrón dado (startswith).
# 2. agrupar_por_longitud() separa el texto y arma un diccionario
#    {longitud: [palabras]}. También actualiza un conjunto interno con
#    todas las palabras vistas.
# 3. palabras_unicas() retorna las palabras únicas guardadas en el conjunto.


class AnalizadorPatrones:
    def __init__(self):
        self.todas_palabras = set()

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        self.todas_palabras.update(palabras)
        return [palabra for palabra in palabras if palabra.startswith(patron)]

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        self.todas_palabras.update(palabras)
        grupos = {}
        for palabra in palabras:
            grupos.setdefault(len(palabra), []).append(palabra)
        return grupos

    def palabras_unicas(self):
        return list(self.todas_palabras)


ap = AnalizadorPatrones()
print(ap.agrupar_por_longitud("el gato está aquí"))


ap2 = AnalizadorPatrones()
print(ap2.encontrar_palabras("el perro y el pato corren en el parque", "p"))
print(ap2.palabras_unicas())