# ============================================================
# PROYECTO FINAL — NIVEL BASICO
# Sistema de Recetas Favoritas
# ============================================================
#
# Instrucciones:
# Lee cada seccion marcada con TODO y completa el codigo.
# Ejecuta el programa seguido para probar que funciona.
#
# Guias de referencia:
#   01 - Introduccion a Python   (print, comentarios)
#   02 - Variables y tipos       (str, int, input, f-strings)
#   03 - Condicionales           (if / elif / else)
#   04 - Ciclos                  (for, while, break)
#   05 - Funciones               (def, parametros, return)
#   06 - Listas y Diccionarios   (list, dict, enumerate)
#   07 - Entrada y Salida        (open, with, csv, try/except)
#   08 - Modulos y Librerias     (import, random, datetime)
# ============================================================


# -------------------------------------------------------
# SECCION 1: Importaciones
# Guia 08 - Modulos y Librerias
# -------------------------------------------------------

# TODO: importa los tres modulos que necesitas:
#   - csv        (para leer y escribir archivos CSV)
#   - random     (para elegir una receta al azar)
#   - datetime desde el modulo datetime (para mostrar la fecha)
#
# Escribe tus imports aqui:




# -------------------------------------------------------
# SECCION 2: Variables globales
# Guia 02 - Variables | Guia 06 - Listas
# -------------------------------------------------------

# TODO: Crea una lista vacia llamada 'recetas'.
#       En esta lista guardaremos todos los diccionarios de recetas.
recetas = ???

# Esta constante ya esta lista — es el nombre del archivo CSV.
ARCHIVO_CSV = 'mis_recetas.csv'


# -------------------------------------------------------
# SECCION 3: Funcion mostrar_bienvenida
# Guia 01 - print() | Guia 08 - datetime
# -------------------------------------------------------

def mostrar_bienvenida():
    '''Muestra el titulo del programa y la fecha de hoy.'''

    # TODO: Obtén la fecha de hoy con datetime.now()
    #       y formatéala con strftime('%A, %d %B %Y')
    hoy = ???

    # TODO: Imprime un encabezado decorativo, el titulo del programa
    #       y la fecha. Por ejemplo:
    #
    #   ===================================
    #      Sistema de Recetas Favoritas
    #      Hoy es: viernes, 07 marzo 2026
    #   ===================================




# -------------------------------------------------------
# SECCION 4: Funcion agregar_receta
# Guia 02 - input | Guia 03 - if | Guia 04 - while
# Guia 05 - funciones | Guia 06 - dict y list
# -------------------------------------------------------

def agregar_receta():
    '''Pide los datos de una nueva receta y la agrega a la lista global.'''

    print('\n--- Agregar nueva receta ---')

    # TODO: Pide el nombre de la receta con input()
    nombre = ???

    # TODO: Pide los ingredientes (como texto, separados por coma)
    ingredientes = ???

    # TODO: Pide el tiempo de preparacion en minutos.
    #       Usa try/except para manejar si el usuario escribe algo
    #       que no sea un numero. Repite la pregunta si es necesario.
    #       El tiempo debe ser un numero entero positivo.
    tiempo = ???

    # TODO: Pide la dificultad. Solo acepta: 'facil', 'media' o 'dificil'.
    #       Usa un ciclo while True con break cuando el valor sea valido.
    #       Convierte la entrada a minusculas con .lower() antes de validar.
    dificultad = ???

    # TODO: Crea un diccionario con las cuatro claves:
    #       'nombre', 'ingredientes', 'tiempo', 'dificultad'
    nueva_receta = ???

    # TODO: Agrega nueva_receta a la lista global 'recetas'
    ???

    # TODO: Imprime un mensaje de confirmacion con el nombre de la receta
    print(???)


# -------------------------------------------------------
# SECCION 5: Funcion mostrar_todas
# Guia 04 - for | Guia 06 - enumerate, dict
# -------------------------------------------------------

def mostrar_todas():
    '''Muestra todas las recetas guardadas en la lista.'''

    # TODO: Si la lista 'recetas' esta vacia, muestra el mensaje:
    #       "No tienes recetas guardadas todavia."
    #       y termina la funcion con return.
    if ???:
        ???
        return

    print('\n--- Tu recetario ---')

    # TODO: Recorre 'recetas' usando enumerate() para numerar cada receta.
    #       Empieza el conteo desde 1 (usa start=1).
    #       Para cada receta muestra: numero, nombre, dificultad y tiempo.
    #
    #       Ejemplo de salida:
    #       1. Tortilla de papas  |  Dificultad: media  |  Tiempo: 30 min
    for ???:
        print(???)


# -------------------------------------------------------
# SECCION 6: Funcion buscar_por_dificultad
# Guia 03 - if | Guia 04 - for | Guia 06 - listas de dicts
# -------------------------------------------------------

def buscar_por_dificultad():
    '''Filtra y muestra recetas segun la dificultad elegida.'''

    dificultad = input('\nBuscar por dificultad (facil/media/dificil): ').lower()

    # TODO: Recorre 'recetas' y guarda en una nueva lista solo las recetas
    #       cuya clave 'dificultad' coincida con la variable dificultad.
    #       Puedes usar una lista por comprension o un ciclo for con append.
    resultados = ???

    # TODO: Si no se encontro ninguna receta, muestra un mensaje informando.
    #       Si se encontraron, muestra cuantas hay y listalas.
    if ???:
        ???
    else:
        print(f'\nSe encontraron {???} receta(s) de dificultad "{dificultad}":')
        for receta in resultados:
            print(f'  - {receta["nombre"]} ({receta["tiempo"]} min)')


# -------------------------------------------------------
# SECCION 7: Funcion receta_aleatoria
# Guia 08 - random | Guia 03 - if
# -------------------------------------------------------

def receta_aleatoria():
    '''Sugiere una receta elegida al azar.'''

    # TODO: Si 'recetas' esta vacia, muestra un aviso y termina con return.
    if ???:
        ???
        return

    # TODO: Usa random.choice() para elegir una receta al azar.
    sugerencia = ???

    # TODO: Muestra la receta elegida con todos sus datos:
    #       nombre, ingredientes, tiempo y dificultad.
    print('\n--- Sugerencia de hoy ---')
    print(???)


# -------------------------------------------------------
# SECCION 8: Funcion estadisticas
# Guia 04 - for | Guia 05 - return | Guia 06 - dict
# -------------------------------------------------------

def estadisticas():
    '''Calcula y muestra estadisticas del recetario.'''

    # TODO: Si no hay recetas, informa y termina con return.
    if ???:
        ???
        return

    # TODO: Calcula el total de recetas (usa len())
    total = ???

    # TODO: Calcula el tiempo promedio de preparacion.
    #       Suma todos los tiempos con un ciclo for (patron acumulador)
    #       y divídelos entre el total.
    suma_tiempos = 0
    for ???:
        suma_tiempos += ???
    promedio = ???

    # TODO: Cuenta cuantas recetas hay de cada dificultad.
    #       Usa un diccionario con las claves 'facil', 'media', 'dificil'
    #       y un contador como valor. Recorre 'recetas' y suma.
    conteo = {'facil': 0, 'media': 0, 'dificil': 0}
    for ???:
        conteo[???] += 1

    # TODO: Muestra todas las estadisticas de forma clara.
    print('\n--- Estadisticas del recetario ---')
    print(f'Total de recetas: {total}')
    print(f'Tiempo promedio: {promedio:.1f} minutos')
    print(f'Recetas faciles: {conteo["facil"]}')
    print(f'Recetas de dificultad media: {conteo["media"]}')
    print(f'Recetas dificiles: {conteo["dificil"]}')


# -------------------------------------------------------
# SECCION 9: Funcion guardar_en_csv
# Guia 07 - open, with, csv.DictWriter
# -------------------------------------------------------

def guardar_en_csv():
    '''Guarda todas las recetas en un archivo CSV.'''

    # TODO: Usa 'with open(ARCHIVO_CSV, ...)' en modo escritura ('w').
    #       Usa csv.DictWriter con los campos: nombre, ingredientes, tiempo, dificultad.
    #       Escribe el encabezado con writeheader() y luego todas las recetas
    #       con writerows().
    #
    #       Recuerda usar: newline='', encoding='utf-8'

    with open(???, ???, newline='', encoding='utf-8') as f:
        campos = ['nombre', 'ingredientes', 'tiempo', 'dificultad']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        # TODO: escribe todas las recetas de la lista
        ???

    print(f'Recetario guardado en {ARCHIVO_CSV} ({len(recetas)} recetas).')


# -------------------------------------------------------
# SECCION 10: Funcion cargar_desde_csv
# Guia 07 - open, with, csv.DictReader, try/except
# -------------------------------------------------------

def cargar_desde_csv():
    '''Carga recetas desde el archivo CSV si existe.'''

    # Necesitamos modificar la lista global 'recetas'
    global recetas

    # TODO: Usa try/except para manejar el caso de que el archivo no exista.
    #       Dentro del try, abre ARCHIVO_CSV en modo lectura ('r')
    #       y usa csv.DictReader para leer cada fila como diccionario.
    #
    #       Importante: el campo 'tiempo' se guarda como texto en el CSV.
    #       Convierte cada valor 'tiempo' a entero con int() al cargarlo.
    #
    #       En el except (FileNotFoundError), no hagas nada (puedes usar pass).

    try:
        with open(???, ???, encoding='utf-8') as f:
            lector = csv.DictReader(f)
            recetas = []
            for fila in lector:
                # TODO: convierte fila['tiempo'] a int antes de agregar
                fila['tiempo'] = ???
                recetas.append(fila)
        if recetas:
            print(f'Recetario cargado desde {ARCHIVO_CSV} ({len(recetas)} recetas encontradas).')
    except ???:
        pass  # Si el archivo no existe, empezamos con la lista vacia


# -------------------------------------------------------
# SECCION 11: Funcion mostrar_menu
# Guia 01 - print | Ya esta completa, no necesitas cambiarla
# -------------------------------------------------------

def mostrar_menu():
    '''Muestra las opciones del menu principal.'''
    print('\n=== MENU ===')
    print('1. Agregar receta')
    print('2. Ver todas las recetas')
    print('3. Buscar por dificultad')
    print('4. Receta aleatoria')
    print('5. Ver estadisticas')
    print('6. Guardar en archivo')
    print('7. Cargar desde archivo')
    print('8. Salir')


# -------------------------------------------------------
# SECCION 12: Funcion main — menu principal
# Guia 04 - while | Guia 03 - if/elif/else
# -------------------------------------------------------

def main():
    '''Funcion principal: muestra el menu y procesa las opciones.'''

    mostrar_bienvenida()
    cargar_desde_csv()

    # TODO: Crea un ciclo while True que:
    #       1. Llame a mostrar_menu()
    #       2. Pida una opcion al usuario con input()
    #       3. Use if/elif para llamar a la funcion correcta segun la opcion:
    #            '1' -> agregar_receta()
    #            '2' -> mostrar_todas()
    #            '3' -> buscar_por_dificultad()
    #            '4' -> receta_aleatoria()
    #            '5' -> estadisticas()
    #            '6' -> guardar_en_csv()
    #            '7' -> cargar_desde_csv()
    #            '8' -> imprime "Hasta luego!" y rompe el ciclo con break
    #            else -> imprime "Opcion no valida."

    while ???:
        mostrar_menu()
        opcion = input('Elige una opcion: ')

        if opcion == '1':
            ???
        elif opcion == '2':
            ???
        elif opcion == '3':
            ???
        elif opcion == '4':
            ???
        elif opcion == '5':
            ???
        elif opcion == '6':
            ???
        elif opcion == '7':
            ???
        elif opcion == '8':
            print('Hasta luego!')
            ???
        else:
            print('Opcion no valida. Elige un numero del 1 al 8.')


# -------------------------------------------------------
# Punto de entrada del programa
# Guia 05 - llamar funciones
# -------------------------------------------------------

# Esta linea llama a main() cuando ejecutas el archivo.
# No la modifiques.
main()
