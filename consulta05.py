# En una consulta, obtener todos los cursos.
# Realizar un ciclo repetitivo para obtener en cada iteración las entregas por cada curso 
#  y presentar el promedio de calificaciones de las entregas

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from clases import *
from config import cadena_base_datos

# Conectar a la base
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta: promedio de calificaciones por curso
resultados = (
    session.query(Curso.titulo, func.avg(Entrega.calificacion).label("promedio"))
    .join(Curso.tareas)
    .join(Tarea.entregas)
    .group_by(Curso.id, Curso.titulo)
    .all()
)

# Mostrar los resultados
print("Promedio de calificaciones por curso:")
for titulo, promedio in resultados:
    print(f"Curso: {titulo} -> Promedio: {promedio:.2f}")