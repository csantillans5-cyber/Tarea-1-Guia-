#Ejercicio 1
#!Registro y Validador de Velocidades de Vehículos
#*Una empresa de monitoreo de tráfico te pide crear una clase en Python llamada ControlVelocidad 
#*que analice y filtre las mediciones enviadas por los sensores en la vía pública.
#*Requisitos de la clase:Atributo de instancia:Al instanciar la clase, debe inicializarse una lista 
#*interna vacía donde se guardarán las velocidades válidas.Método validar_velocidad(velocidad):Recibe un valor numérico 
#*y retorna True si la velocidad está en el rango permitido de $10$ a $120$ km/h (ambos inclusive). En caso contrario, 
#*retorna False.Método registrar_mediciones(*args):Recibe múltiples valores de velocidad (usando *args), 
#*los valida utilizando validar_velocidad, agrega únicamente las velocidades válidas a la lista interna y 
#*retorna esa lista actualizada.Método promedio_velocidad():Retorna el promedio de las velocidades válidas 
#*que se encuentran almacenadas en la lista interna. Si la lista está vacía, debe retornar 0 para evitar errores.


class Control_de_velocidad:

    def __init__(self):

        self.regis_vel = []

    def validar_velocidad(self, velocidad):
        return 10 <= velocidad <= 120

    def registrar_mediciones(self, *args):

        for velocidad in args:
            if self.validar_velocidad(velocidad):
                self.regis_vel.append(velocidad)
        return self.regis_vel

    def prom(self):

        if not self.regis_vel:
            return 0
        return sum(self.regis_vel) / (len(self.regis_vel))


C = Control_de_velocidad()
print (C.registrar_mediciones(40,57,21,9,88,67,154))
print (C.prom())

#?Ejercicio 2
#!Registro de Usuarios Unicos
#*Escribe una clase en Python llamada RegistroAcceso que cumpla con los siguientes requisitos:
#*Constructor (__init__): Inicializa dos atributos de instancia:
#*Un conjunto vacio para guardar los IDs de usuarios sin duplicados.
#*Una lista vacia para registrar la secuencia histórica de todos los accesos en orden.
#*Método registrar_usuario(usuario_id):
#*Agrega el usuario_id al conjunto de usuarios únicos.
#*Agrega el usuario_id a la lista histórica de accesos.
#*Método total_unicos():
#*Retorna la cantidad de usuarios únicos registrados hasta el momento.
#*Método registrar_lote(*args):
#*Recibe múltiples IDs de usuario mediante *args.
#*Reutiliza el método registrar_usuario para procesar cada uno de los IDs recibidos.

class regi_acc:

    def __init__(self):
        self.id_unicos = set()
        self.id_vacio = []

    def registrar_usuario(self, usuario_id):
        self.id_unicos.add(usuario_id)
        self.id_vacio.append(usuario_id)

    def total_unico(self):
        return len(self.id_unicos)

    def registrar_lote(self, *args):
        for id_unicos in args:
            self.registrar_usuario(id_unicos)

C = regi_acc()
C.registrar_lote("1250844618","0986638789","125084491","1250844618")
print(C.total_unico())


#?Ejercicio 3
#!Registro de Calificaciones de Estudiantes
#*Escribe una clase en Python llamada RegistroEstudiantes que cumpla con los siguientes requisitos:
# *Constructor (__init__): Inicializa un diccionario vacío para almacenar pares de clave-valor con el formato {nombre_estudiante: nota_final}.
# *Método registrar_estudiante(nombre, nota):
# *Guarda o actualiza al estudiante en el diccionario con su respectiva nota.
# *Método promedio_general():
# *Retorna el promedio aritmético de las notas de todos los estudiantes registrados. Si el diccionario está vacío, debe retornar 0.
# *Método filtrar_por_nota(nota_minima):
# *Recibe un valor de nota_minima y retorna una lista con los nombres de los estudiantes que tengan una nota mayor o igual a ese valor.

class registro_estudiantes():

    def __init__(self):
        self.dic_estudiantes = {}

    def registrar_est(self, nombre, nota_final):
        self.dic_estudiantes[nombre] = nota_final

    def promedio_general(self):

        if not self.dic_estudiantes:
            return 0
        return sum(self.dic_estudiantes.values()) / (len(self.dic_estudiantes))
    
    def filtrar_nota(self, no_min, no_max):

        filtro = []

        for nombre, nota_final in self.dic_estudiantes.items():
            if no_min <= nota_final <= no_max:
                filtro.append(nombre)
        return filtro


C = registro_estudiantes()
C.registrar_est("Jose", 7)
C.registrar_est("Maria", 10)
C.registrar_est("Abigail", 4)
print(C.promedio_general())

print(C.filtrar_nota(7 , 10))


#?Ejercico 4
#!Contador de Vocales en Palabras
#*Escribe una clase en Python llamada ProcesadorVocales que cumpla con los siguientes requisitos:
#*Método contar_vocales(palabra):
#*Recibe un string (palabra o texto).
#*Recorre el texto mediante un bucle de manera manual y retorna la cantidad total de vocales (a, e, i, o, u, ignorando mayúsculas/minúsculas).
#*Método analizar_palabras(*palabras):
#*Recibe múltiples palabras mediante *palabras.
#*Utiliza un diccionario para almacenar cada palabra original como clave y la cantidad de vocales calculada con contar_vocales como valor.
#*Retorna dicho diccionario.

class Procesador_vocales:
    pass

    def contar_vocales(self, palabra):

        lista =[]

        for i in range(len(palabra)):
            if palabra[i].lower() in ("aeiouáéíóú"):
                lista.append(palabra[i])
        return len(lista)

    def analizar_palabras(self, *palabras):

        resultado = {}
        for lst in palabras:
            tup = tuple(lst)
            resultado[tup] =  self.contar_vocales(lst)

            return resultado 


C = Procesador_vocales()
print(C.contar_vocales("Hola papá"))
print(C.analizar_palabras("Hola", "Python", "Computadora"))


#?Ejercicio 5
#!Clasificador de Temperaturas en Climas
#*#*Escribe una clase en Python llamada ClasificadorClima que cumpla con los siguientes requisitos:
#*Constructor (__init__): Inicializa un diccionario con dos listas vacías:'frio': para temperaturas menores a $18$ °C.
#*'calido': para temperaturas mayores o iguales a $18$ °C.
#*Método es_frio(temperatura):Retorna True si la temperatura es menor a $18$, y False si es mayor o igual a $18$.
#*Método clasificar(*temperaturas):Recibe múltiples temperaturas mediante *temperaturas.
#*Reutiliza el método es_frio para agregar la temperatura a la lista correspondiente en el diccionario ('frio' o 'calido').
#*Retorna el diccionario resultante.Método conteo_climas():
#*Retorna una tupla con la cantidad de mediciones en frío y en cálido con la forma: (cant_frio, cant_calido).

class Clasificador_clima:

    def __init__(self):
        self.clas_clima = {'frio':[], 'calor':[]}

    def es_frio(self, temperatura):
        return temperatura <= 18

    def clasificar(self, *temperaturas):
        for temperatura in temperaturas:
            if self.es_frio(temperatura):
                self.clas_clima['frio'].append(temperatura)
            else:
                self.clas_clima['calor'].append(temperatura)
        return self.clas_clima

    def conteo_climas(self):
        cant_f = len(self.clas_clima['frio'])
        cant_c = len(self.clas_clima['calor'])
        return (cant_f, cant_c)

C = Clasificador_clima()
print(C.clasificar(11,34,37,20,15))
print(C.conteo_climas())


#?Ejercicio 6
#!Registro y Estadísticas de Ventas
#*Escribe una clase en Python llamada GestorVentas que cumpla con los siguientes requisitos:
#*Constructor (__init__): Inicializa una lista vacía para almacenar los montos de cada venta.
#*Método registrar_venta(monto):
#*Agrega un monto individual a la lista interna.
#*Método registrar_lote(*montos):
#*Recibe múltiples montos mediante *montos.
#*Reutiliza el método registrar_venta para guardar cada uno en la lista.
#*Métodos estadísticos:
#*venta_minima(): Retorna la venta con el valor más bajo registrado (usa min()).
#*venta_maxima(): Retorna la venta con el valor más alto registrado (usa max()).
#*total_ventas(): Retorna la suma total recaudada (usa sum()).

class gestion_ventas:
    pass

    def __init__(self):
        self.lis_vent = []

    def registrar_monto(self, monto):
        self.lis_vent.append(monto)
        return self.lis_vent

    def registrar_lote(self, *montos):
        for monto in montos:
            self.registrar_monto(monto)

    def venta_minima(self):
        if not self.lis_vent:
            return None
        return min(self.lis_vent)

    def venta_maxima(self):
        if not self.lis_vent:
            return None
        return max(self.lis_vent)

    def venta_total(self):
        if not self.lis_vent:
            return 0
        return sum(self.lis_vent)

C = gestion_ventas()

C.registrar_lote(45, 80, 210, 9)

print("Venta mínima:", C.venta_minima())
print("Venta máxima:", C.venta_maxima())
print("Venta total:", C.venta_total())


#?Ejercicio 7
#!Gestor de Inventario de Libros
#*Escribe una clase en Python llamada GestorLibros que cumpla con los siguientes requisitos:
#*Constructor (__init__): Inicializa un diccionario vacío para guardar los pares {titulo: numero_de_paginas}.
#*Método agregar_libro(titulo, paginas):
#*Guarda o actualiza un libro en el diccionario con la cantidad de páginas correspondiente.
#*Método libros_largos(paginas_minimas):
#*Recibe paginas_minimas y retorna una lista con los títulos de los libros que tengan un número de páginas mayor o igual a ese valor (usa .items()).
#*Método paginas_promedio():
#*Retorna el promedio del número de páginas de todos los libros registrados en el diccionario. Si no hay libros, retorna 0.

class Gestor_libros:

    def __init__(self):
        self.dic_lib = {}

    def agregar_libro(self, titulo, paginas):
        self.dic_lib[titulo] = paginas

    def libros_largos(self, paginas_minimas):
        mini = []
        for titulo, paginas in self.dic_lib.items():
            if paginas >= paginas_minimas:
                mini.append(paginas)
        return mini

    def paginas_prom(self):

        if not self.dic_lib:
            return 0
        return sum(self.dic_lib.values())/ len(self.dic_lib)


C = Gestor_libros()
C.agregar_libro("La odidesa", 460)
C.agregar_libro("Don quijote", 1500)

print(C.libros_largos(800))
print(C.paginas_prom())


#?Ejercicio 8
#!Gestor de Proyectos y Colaboradores
#*Escribe una clase en Python llamada GestorProyectos que cumpla con los siguientes requisitos:
#*Constructor (__init__): Inicializa un diccionario vacío para almacenar la estructura {nombre_proyecto: [colaboradores]}.
#*Método crear_proyecto(nombre_proyecto):
#*Inicializa el proyecto con una lista vacía en el diccionario.
#*Método asignar_colaborador(proyecto, colaborador):
#*Agrega el nombre del colaborador a la lista de dicho proyecto.
#*Método proyecto_mas_concurrido():
#*Retorna el nombre del proyecto que tiene asignada la mayor cantidad de colaboradores.

class Gestor_proyectos:
    pass

    def __init__(self):
        self.grupos = {}

    def crear_proyecto(self, nombre_proyecto):
        if nombre_proyecto not in self.grupos:
            self.grupos[nombre_proyecto] = []

    def asignar_colaboradores(self, proyecto, colaborador):
        if proyecto not in self.grupos:
            self.crear_proyecto(proyecto)
        self.grupos[proyecto].append(colaborador)

    def proyecto_mas_concurrido(self):
        if not self.grupos:
            return None
        return max(self.grupos, key=lambda eq: len(self.grupos[eq]))

C = Gestor_proyectos()
C.crear_proyecto("A")
C.asignar_colaboradores("A","Pepe")
C.asignar_colaboradores("A","Tola")
C.crear_proyecto("B")
C.asignar_colaboradores("B","Pdidi")
C.asignar_colaboradores("B","Jeffry")
C.asignar_colaboradores("B","Trmup")

print(C.proyecto_mas_concurrido())

#?Ejercico 9
#!Validador de Complejidad de Texto
#*Escribe una clase en Python llamada ValidadorTexto que cumpla con los siguientes requisitos:
#*Constructor (__init__): Inicializa una variable self.ultimo_texto en "" para guardar el último texto procesado.
#*Método es_mayuscula(letra):
#*Retorna True si el carácter es una letra mayúscula (puedes usar .isupper()).
#*Método analizar_caracteres(texto):
#*Guarda el valor en self.ultimo_texto.
#*Retorna un diccionario con las siguientes claves y sus conteos:
#*'mayusculas': cantidad de letras mayúsculas (reutilizando es_mayuscula).
#*'minusculas': cantidad de letras minúsculas (.islower()).
#*'especiales': cantidad de caracteres que no son ni letras ni números (puedes usar not char.isalnum()).

class ValidadorTexto:
    def __init__(self):
        self.ultimo_texto = ""

    def es_mayuscula(self, letra):
        return letra.isupper()

    def analizar_caracteres(self, texto):
        self.ultimo_texto = texto
        mayusculas = 0
        minusculas = 0
        especiales = 0

        for char in texto:
            if self.es_mayuscula(char):
                mayusculas += 1
            elif char.islower():
                minusculas += 1
            elif not char.isalnum():
                especiales += 1

        return {
            'mayusculas': mayusculas,
            'minusculas': minusculas,
            'especiales': especiales
        }


C = ValidadorTexto()
print(C.analizar_caracteres("¡Hola Mundo! 123"))


#?Ejercico 10
#!Gestor de Inventario con Estado
#*Escribe una clase en Python llamada Inventario que cumpla con los siguientes requisitos:
#*Constructor (__init__): Inicializa una lista vacía para almacenar tuplas del tipo (producto, estado).
#*Método agregar_producto(producto, estado):
#*Guarda una nueva tupla (producto, estado) en la lista.
#*Método productos_agotados():
#*Retorna una lista con las tuplas cuya propiedad estado sea igual a "agotado".
#*Método retirar_producto(producto):
#*Elimina del inventario las tuplas cuyo nombre coincida con el parámetro producto.

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, estado):
        self.productos.append((producto, estado))

    def productos_agotados(self):
        return [item for item in self.productos if item[1] == "agotado"]

    def retirar_producto(self, producto):
        self.productos = [item for item in self.productos if item[0] != producto]


# Demostración:
C = Inventario()
C.agregar_producto("Pan", "disponible")
C.agregar_producto("Leche", "agotado")
C.agregar_producto("Arroz", "agotado")
print(C.productos_agotados())
C.retirar_producto("Pan")
print(C.productos)


#?Ejercico 11
#!Contador de Votos
#*Escribe una clase en Python llamada UrnaVotos que cumpla con los siguientes requisitos:
#*Constructor (__init__): Inicializa un diccionario vacío self.votos = {}.
#*Método registrar_voto(candidato):
#*Incrementa en 1 la cantidad de votos del candidato recibido.
#*Método obtener_ganador():
#*Retorna el nombre del candidato con mayor número de votos acumulados.
#*Método total_votos_candidato(candidato):
#*Retorna la cantidad exacta de votos que recibió el candidato (retorna 0 si no recibió ningún voto).

class UrnaVotos:
    def __init__(self):
        self.votos = {}

    def registrar_voto(self, candidato):
        self.votos[candidato] = self.votos.get(candidato, 0) + 1

    def obtener_ganador(self):
        if not self.votos:
            return None
        return max(self.votos, key=self.votos.get)

    def total_votos_candidato(self, candidato):
        return self.votos.get(candidato, 0)


# Demostración:
C = UrnaVotos()
C.registrar_voto("Alice")
C.registrar_voto("Bob")
C.registrar_voto("Alice")

print(C.obtener_ganador())
print(C.total_votos_candidato("Alice"))
print(C.total_votos_candidato("Charlie"))


#?Ejercico 12
#!Combinador de Números Únicos
#*Escribe una clase en Python llamada CombinadorNumeros que cumpla con los siguientes requisitos:
#*Método generar_secuencia(paso, limite):
#*Retorna una tupla con los números múltiplos de paso comenzando desde paso hasta llegar a limite inclusive.
#*Ejemplo: generar_secuencia(2, 6) debe retornar (2, 4, 6).
#*Método unir_unicos(*secuencias):
#*Recibe múltiples secuencias o tuplas.
#*Utiliza un conjunto (set) para unirlas todas eliminando los valores duplicados.
#*Retorna una lista ordenada con todos los números únicos obtenidos.

class CombinadorNumeros:
    def __init__(self):
        pass

    def generar_secuencia(self, paso, limite):
        secuencia = tuple(range(paso, limite + 1, paso))
        return secuencia

    def unir_unicos(self, *secuencias):
        conjunto_unicos = set()
        for secuencia in secuencias:
            conjunto_unicos.update(secuencia)
        return sorted(list(conjunto_unicos))


C = CombinadorNumeros()
sec1 = C.generar_secuencia(2, 6) # (2, 4, 6)
sec2 = C.generar_secuencia(3, 9) # (3, 6, 9)

print(sec1)
print(C.unir_unicos(sec1, sec2, (4, 5, 10)))

#?Ejercico 13
#!Intercalador de Cadenas
#*Escribe una clase en Python llamada CombinadorCadenas que cumpla con los siguientes requisitos:
#*Método intercalar_textos(texto1, texto2):
#*Recibe dos cadenas de texto y retorna una nueva cadena intercalando un carácter de cada una.
#*Ejemplo: intercalar_textos("abc", "123") debe retornar "a1b2c3".
#*Método intercalar_multiples_textos(*textos):
#*Recibe múltiples cadenas de texto e intercala sus caracteres manteniendo el orden posicional.

#?Ejercico 14
#!Registro de Tiempos Deportivo
#*Escribe una clase en Python llamada RegistroTiempos que cumpla con los siguientes requisitos:
#*Constructor (__init__): Inicializa un diccionario vacío self.tiempos = {}.
#*Método registrar_tiempo(atleta, segundos):
#*Guarda o actualiza el tiempo en segundos asociado al atleta en el diccionario.
#*Método atletas_rapidos(tiempo_maximo):
#*Itera usando .items() y retorna una lista de nombres de los atletas cuyo tiempo sea menor o igual a tiempo_maximo.
#*Método ganador():
#*Retorna una tupla (atleta, segundos) correspondiente al atleta con el menor tiempo registrado.

class CombinadorCadenas:
    def __init__(self):
        pass

    def intercalar_textos(self, texto1, texto2):
        resultado = []
        max_len = max(len(texto1), len(texto2))
        for i in range(max_len):
            if i < len(texto1):
                resultado.append(texto1[i])
            if i < len(texto2):
                resultado.append(texto2[i])
        return "".join(resultado)

    def intercalar_multiples_textos(self, *textos):
        if not textos:
            return ""
        resultado = []
        max_len = max(len(t) for t in textos)
        for i in range(max_len):
            for texto in textos:
                if i < len(texto):
                    resultado.append(texto[i])
        return "".join(resultado)

C = CombinadorCadenas()
print(C.intercalar_textos("abc", "123"))
print(C.intercalar_multiples_textos("abc", "123", "XYZ"))


#?Ejercico 15
#!Analizador de Múltiplos
#*Escribe una clase en Python llamada AnalizadorMultiplos que cumpla con los siguientes requisitos:
#*Método obtener_multiplos(numero, limite):
#*Retorna una tupla con todos los múltiplos positivos de numero menores o iguales a limite.
#*Ejemplo: obtener_multiplos(3, 10) debe retornar (3, 6, 9).
#*Método es_multiplo_comun(num1, num2, candidato):
#*Retorna True si candidato es múltiplo tanto de num1 como de num2 (es decir, el resto del módulo % para ambos es 0).
#*Método mapear_multiplos(limite, *numeros):
#*Recibe un limite seguido de varios números enteros.
#*Retorna un diccionario con la estructura {numero: tupla_multiplos} reutilizando obtener_multiplos.

class AnalizadorMultiplos:
    def __init__(self):
        pass

    def obtener_multiplos(self, numero, limite):
        multiplos = [i for i in range(numero, limite + 1, numero)]
        return tuple(multiplos)

    def es_multiplo_comun(self, num1, num2, candidato):
        return (candidato % num1 == 0) and (candidato % num2 == 0)

    def mapear_multiplos(self, limite, *numeros):
        return {num: self.obtener_multiplos(num, limite) for num in numeros}

C = AnalizadorMultiplos()
print(C.obtener_multiplos(3, 10))
print(C.es_multiplo_comun(3, 4, 12))
print(C.mapear_multiplos(10, 2, 5))


#?Ejercico 16
#!Codificador por Reemplazo de Vocales
#*Escribe una clase en Python llamada CodificadorVocales que cumpla con los siguientes requisitos:
#*Constructor (__init__): Inicializa un diccionario vacío self.historial = {} y define un mapa de conversión de vocales, por ejemplo:
#*{'a': '@', 'e': '3', 'i': '1', 'o': '0', 'u': 'v'}.
#*Método transformar_caracter(caracter):
#*Retorna el símbolo sustituto si el carácter es una vocal (minúscula o mayúscula); si no es vocal, retorna el carácter original sin cambios.
#*Método codificar_texto(texto):
#*Recibe una cadena de texto, aplica la conversión carácter por carácter reutilizando transformar_caracter y guarda en el diccionario self.historial la entrada {texto_original: texto_transformado}.
#*Retorna la cadena de texto transformada.

class CodificadorVocales:
    def __init__(self):
        self.historial = {}
        self.mapa_vocales = {
            'a': '@', 'e': '3', 'i': '1', 'o': '0', 'u': 'v',
            'A': '@', 'E': '3', 'I': '1', 'O': '0', 'U': 'v'
        }

    def transformar_caracter(self, caracter):
        return self.mapa_vocales.get(caracter, caracter)

    def codificar_texto(self, texto):
        texto_transformado = "".join([self.transformar_caracter(c) for c in texto])
        self.historial[texto] = texto_transformado
        return texto_transformado

C = CodificadorVocales()
print(C.codificar_texto("hola"))
print(C.codificar_texto("python"))
print(C.historial)



#?Ejercico 17
#!: Clasificador de Temperaturas
#*
#*Escribe una clase en Python llamada ClasificadorClima que cumpla con los siguientes requisitos:
#*Constructor (__init__): Inicializa un diccionario vacío self.mediciones = {} para guardar {categoria: [temperaturas]}.
#*Método clasificar_temperatura(temp):
#*Retorna "frio" si temp < 15.
#*Retorna "templado" si 15 <= temp <= 25.
#*Retorna "caluroso" si temp > 25.
#*Método agrupar_temperaturas(*temperaturas):
#*Clasifica y agrupa cada temperatura en la lista del diccionario self.mediciones.
#*Retorna el diccionario resultante.
#*Método promedio_clima(categoria):
#*Retorna la temperatura promedio registrada dentro de la categoría especificada.

class ClasificadorClima:
    def __init__(self):
        self.mediciones = {}

    def clasificar_temperatura(self, temp):
        if temp < 15:
            return "frio"
        elif temp <= 25:
            return "templado"
        else:
            return "caluroso"

    def agrupar_temperaturas(self, *temperaturas):
        self.mediciones = {}
        for temp in temperaturas:
            cat = self.clasificar_temperatura(temp)
            if cat not in self.mediciones:
                self.mediciones[cat] = []
            self.mediciones[cat].append(temp)
        return self.mediciones

    def promedio_clima(self, categoria):
        temps = self.mediciones.get(categoria, [])
        if not temps:
            return 0.0
        return sum(temps) / len(temps)


C = ClasificadorClima()
print(C.agrupar_temperaturas(10, 20, 30, 22))
print(C.promedio_clima("templado"))

#?Ejercico 18
#!Calculador de Distancia 1D
#*Escribe una clase en Python llamada CalculadorDistancia1D que cumpla con los siguientes requisitos:
#*Constructor (__init__): Inicializa una lista vacía self.registro_distancias = [].
#*Método distancia_absoluta(x1, x2):
#*Calcula la distancia absoluta entre dos valores numéricos usando abs(x2 - x1).
#*Agrega el valor a self.registro_distancias y lo retorna.
#*Método numero_mas_cercano(referencia, *numeros):
#*Retorna el número de la tupla *numeros cuya distancia absoluta con referencia sea la menor.

class CalculadorDistancia1D:
    def __init__(self):
        self.registro_distancias = []

    def distancia_absoluta(self, x1, x2):
        dist = abs(x2 - x1)
        self.registro_distancias.append(dist)
        return dist

    def numero_mas_cercano(self, referencia, *numeros):
        if not numeros:
            return None
        return min(numeros, key=lambda num: self.distancia_absoluta(referencia, num))

C = CalculadorDistancia1D()
print(C.distancia_absoluta(10, 25))
print(C.numero_mas_cercano(10, 50, 12, 30))


#?Ejercico 19
#!Billetera Digita
#*Escribe una clase en Python llamada BilleteraDigital que cumpla con los siguientes requisitos:
#*Constructor (__init__): Inicializa un diccionario vacío self.cuentas = {} para guardar {usuario: saldo}.
#*Método depositar(usuario, monto):
#*Agrega o suma el monto al saldo del usuario.
#*Método retirar(usuario, monto):
#*Si el usuario existe y su saldo es mayor o igual al monto, descuenta dicho monto y retorna True.
#*Si no hay suficiente saldo o el usuario no existe, retorna False.
#*Método usuarios_con_saldo_bajo(limite):
#*Retorna una lista con los nombres de los usuarios cuyo saldo actual sea menor que limite.

class BilleteraDigital:
    def __init__(self):
        self.cuentas = {}

    def depositar(self, usuario, monto):
        self.cuentas[usuario] = self.cuentas.get(usuario, 0) + monto

    def retirar(self, usuario, monto):
        if usuario in self.cuentas and self.cuentas[usuario] >= monto:
            self.cuentas[usuario] -= monto
            return True
        return False

    def usuarios_con_saldo_bajo(self, limite):
        return [usuario for usuario, saldo in self.cuentas.items() if saldo < limite]


C = BilleteraDigital()
C.depositar("Ana", 100)
C.depositar("Carlos", 50)
print(C.retirar("Ana", 70))
print(C.usuarios_con_saldo_bajo(40))

#?Ejercico 20
#!Analizador de Sufijos
#*Escribe una clase en Python llamada AnalizadorSufijos que cumpla con los siguientes requisitos:
#*Método encontrar_por_sufijo(texto, sufijo):
#*Recibe una cadena texto y una terminación sufijo.
#*Utiliza .endswith() para retornar una lista con todas las palabras que terminan con dicho sufijo.
#*Método agrupar_por_letra_inicial(texto):
#*Retorna un diccionario {letra_inicial: [palabras]} agrupando las palabras según el primer carácter con el que empiezan.
#*Método obtener_caracteres_unicos(texto):
#*Retorna un conjunto (set) con todos los caracteres individuales presentes en el texto (sin duplicados).

class AnalizadorSufijos:
    def __init__(self):
        pass

    def encontrar_por_sufijo(self, texto, sufijo):
        return [palabra for palabra in texto.split() if palabra.endswith(sufijo)]

    def agrupar_por_letra_inicial(self, texto):
        resultado = {}
        for palabra in texto.split():
            inicial = palabra[0]
            if inicial not in resultado:
                resultado[inicial] = []
            resultado[inicial].append(palabra)
        return resultado

    def obtener_caracteres_unicos(self, texto):
        return set(texto)


C = AnalizadorSufijos()
print(C.encontrar_por_sufijo("correr saltar comer programar", "er"))
print(C.agrupar_por_letra_inicial("sol saco luna libre"))
print(C.obtener_caracteres_unicos("hola"))