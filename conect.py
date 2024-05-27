import mysql.connector

db_config = {
    'user': 'root',  # Reemplaza con tu usuario de MySQL correcto
    'password': '',  # Reemplaza con tu contraseña de MySQL correcta
    'host': 'localhost',  # O la IP donde se aloja tu servidor MySQL
    'database': 'gato'
}

# Función para conectarse a la base de datos
def connect_to_db():
    try:
        conn = mysql.connector.connect(**db_config)
        print("Conexión a la base de datos exitosa")  # Mensaje de depuración
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
