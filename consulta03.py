# Obtener todas las tareas asignadas a los siguientes estudiantes 

 #   Jennifer Bolton 
 #   Elaine Perez
 #   Heather Henderson
 #   Charles Harris
 # En función de cada tarea, presentar el número de entregas que tiene


from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, or_
from clases import engine, Estudiante, Tarea, Entrega

Session = sessionmaker(bind=engine)
session = Session()

estudiantes = ['Jennifer Bolton', 'Elaine Perez', 'Heather Henderson', 'Charles Harris']

tareas_con_entregas = (
    session.query(Tarea) # Selecciona el título de la tarea y cuenta las entregas.
    .join(Entrega)  # Une con la tabla Estudiante.
    .join(Estudiante)     # Une con la tabla Entrega.
    .filter(Estudiante.nombre.in_(estudiantes)) # Filtra: busca nombres de estudiantes *exactamente* como están en la lista 'estudiantes'.
    .all() # Ejecuta la consulta.
)

resultado = {}

for tarea in tareas_con_entregas:
	resultado [tarea.titulo] =  len(tarea.entregas)

for titulo, num_entregas in resultado.items():
	print(f"{titulo} - {num_entregas} entregas")


