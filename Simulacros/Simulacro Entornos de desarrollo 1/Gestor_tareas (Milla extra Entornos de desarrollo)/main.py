"""
Sistema de Gestión de Tareas (To-Do List) – Versión Milla Extra
Incluye: creación de tareas, listado, filtrado, marcado de completadas,
validación de entradas, guardado y carga de archivo JSON.
Unidad de Entornos de Desarrollo: POO, control de flujo, ficheros, manejo de errores y documentación.
"""

import json

# --- Clase principal ---

class Tarea:
    """
    Clase que representa una tarea.

    Atributos:
    titulo (str): Nombre de la tarea.
    completada (bool): Indica si la tarea está completada.
    """
    def __init__(self, titulo):
        self.titulo = titulo
        self.completada = False

    def marcar_completada(self):
        """Marca la tarea como completada."""
        self.completada = True

    def __str__(self):
        """Representación de la tarea como cadena."""
        estado = "✔" if self.completada else "✘"
        return f"[{estado}] {self.titulo}"


# --- Funciones del programa ---

def agregar_tarea(lista):
    """
    Agrega una nueva tarea verificando que no esté vacía ni duplicada.
    Unidad/Subunidad: 001 – Desarrollo de software / Estructuras de control
    """
    while True:
        titulo = input("Introduce el título de la tarea: ").strip()
        if not titulo:
            print("Error: el título no puede estar vacío.")
        elif any(t.titulo.lower() == titulo.lower() for t in lista):
            print("Error: ya existe una tarea con ese nombre.")
        else:
            lista.append(Tarea(titulo))
            print("Tarea agregada correctamente.\n")
            break

def listar_tareas(lista, filtro=None):
    """
    Muestra todas las tareas o filtradas por completadas/pendientes.
    Unidad/Subunidad: 001 – Desarrollo de software / Estructuras de control
    """
    if not lista:
        print("No hay tareas registradas.\n")
        return
    
    filtradas = lista
    if filtro == "pendientes":
        filtradas = [t for t in lista if not t.completada]
    elif filtro == "completadas":
        filtradas = [t for t in lista if t.completada]

    if not filtradas:
        print(f"No hay tareas {filtro}.\n")
        return

    print(f"Lista de tareas ({filtro if filtro else 'todas'}):")
    for i, tarea in enumerate(filtradas, 1):
        print(f"{i}. {tarea}")
    print()

def completar_tarea(lista):
    """
    Permite marcar una tarea como completada según su número.
    Unidad/Subunidad: 003 – Diseño y realización de pruebas
    """
    listar_tareas(lista, filtro="pendientes")
    if all(t.completada for t in lista):
        print("No hay tareas pendientes para completar.\n")
        return

    try:
        num = int(input("Número de la tarea a completar: "))
        pendientes = [t for t in lista if not t.completada]
        if 1 <= num <= len(pendientes):
            pendientes[num-1].marcar_completada()
            print("Tarea marcada como completada.\n")
        else:
            print("Error: número inválido.\n")
    except ValueError:
        print("Error: debes introducir un número entero.\n")

def guardar_tareas(lista, archivo="tareas.json"):
    """Guarda las tareas en un archivo JSON."""
    try:
        with open(archivo, "w") as f:
            json.dump([{"titulo": t.titulo, "completada": t.completada} for t in lista], f)
        print("Tareas guardadas correctamente.\n")
    except Exception as e:
        print(f"Error al guardar tareas: {e}\n")

def cargar_tareas(archivo="tareas.json"):
    """Carga las tareas desde un archivo JSON si existe."""
    tareas = []
    try:
        with open(archivo, "r") as f:
            datos = json.load(f)
            for item in datos:
                t = Tarea(item["titulo"])
                t.completada = item["completada"]
                tareas.append(t)
    except FileNotFoundError:
        print("Archivo de tareas no encontrado, se creará uno nuevo.\n")
    except Exception as e:
        print(f"Error al cargar tareas: {e}\n")
    return tareas


# --- Programa principal ---

def main():
    """
    Menú principal del sistema de tareas con opciones de filtrado y gestión.
    Unidad/Subunidad: 002 – Instalación y uso de entornos de desarrollo
    """
    tareas = cargar_tareas()
    
    while True:
        print("=== SISTEMA DE GESTIÓN DE TAREAS – MILLA EXTRA ===")
        print("1. Agregar tarea")
        print("2. Listar todas las tareas")
        print("3. Listar tareas pendientes")
        print("4. Listar tareas completadas")
        print("5. Completar tarea")
        print("6. Guardar y salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            listar_tareas(tareas)
        elif opcion == "3":
            listar_tareas(tareas, filtro="pendientes")
        elif opcion == "4":
            listar_tareas(tareas, filtro="completadas")
        elif opcion == "5":
            completar_tarea(tareas)
        elif opcion == "6":
            guardar_tareas(tareas)
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.\n")


# --- Ejecutar programa ---
if __name__ == "__main__":
    main()
