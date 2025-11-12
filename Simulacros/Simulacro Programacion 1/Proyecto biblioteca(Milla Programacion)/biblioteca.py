import mysql.connector

# --- Clase Libro ---
class Libro:
    def __init__(self, id, titulo, autor, anio):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def __str__(self):
        return f"[{self.id}] {self.titulo} - {self.autor} ({self.anio})"


# --- Conexión a la base de datos ---
def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="usuario_diego",       # Cambia por tu usuario de MySQL
            password="1234",             # Cambia por tu contraseña
            database="biblioteca_db"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None


# --- Menú CRUD ---
def mostrar_menu():
    print("\n--- GESTOR DE BIBLIOTECA ---")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Actualizar libro")
    print("4. Eliminar libro")
    print("5. Salir")


def agregar_libro(conexion):
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = input("Año: ")
    cursor = conexion.cursor()
    sql = "INSERT INTO libros (titulo, autor, anio) VALUES (%s, %s, %s)"
    cursor.execute(sql, (titulo, autor, anio))
    conexion.commit()
    print("✅ Libro agregado correctamente.")


def mostrar_libros(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros")
    resultados = cursor.fetchall()
    if not resultados:
        print("No hay libros registrados.")
    else:
        print("\n--- Lista de libros ---")
        for fila in resultados:
            libro = Libro(fila[0], fila[1], fila[2], fila[3])
            print(libro)


def actualizar_libro(conexion):
    id_libro = input("ID del libro a actualizar: ")
    nuevo_titulo = input("Nuevo título: ")
    nuevo_autor = input("Nuevo autor: ")
    nuevo_anio = input("Nuevo año: ")
    cursor = conexion.cursor()
    sql = "UPDATE libros SET titulo=%s, autor=%s, anio=%s WHERE id=%s"
    cursor.execute(sql, (nuevo_titulo, nuevo_autor, nuevo_anio, id_libro))
    conexion.commit()
    print("✅ Libro actualizado correctamente.")


def eliminar_libro(conexion):
    id_libro = input("ID del libro a eliminar: ")
    cursor = conexion.cursor()
    sql = "DELETE FROM libros WHERE id=%s"
    cursor.execute(sql, (id_libro,))
    conexion.commit()
    print("✅ Libro eliminado correctamente.")


# --- Ejecución principal ---
def main():
    conexion = conectar_bd()
    if not conexion:
        print("No se pudo conectar a la base de datos.")
        return

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            agregar_libro(conexion)
        elif opcion == "2":
            mostrar_libros(conexion)
        elif opcion == "3":
            actualizar_libro(conexion)
        elif opcion == "4":
            eliminar_libro(conexion)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

    conexion.close()
    print("Conexión cerrada. Fin del programa.")


if __name__ == "__main__":
    main()
    