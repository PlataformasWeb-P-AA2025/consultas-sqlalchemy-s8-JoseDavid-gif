# 1. Obtener las entregas de todos los estudiantes que pertenecen al departamento de Arte. 
# En función de la entrega, presentar, nombre del tarea, nombre del estudiante, calificación, 
# nombre de instructor y nombre del departamento

from sqlalchemy.orm import sessionmaker 
# modelos de BD 
from clases import engine, Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega 

Session = sessionmaker(bind=engine) 
session = Session() # sesión para interactuar con la BD

entregas_v = (
    session.query(Entrega) # Inicia consulta desde la tabla Entrega
    .join(Estudiante) # Une con Estudiante' para acceder a datos del estudiante
    .join(Tarea) # Une con Tarea para detalles de la tarea
    .join(Curso) # Une con Curso para información del curso
    .join(Departamento) # Une con Departamento para filtrar por su nombre
    .filter(Departamento.nombre == 'Arte') # Filtra: solo entregas de cursos del departamento Arte
    .all() #  trae todos los resultados
)

print(" Entregas ") # Título para la salida
for entrega in entregas_v: # Itera sobre cada entrega encontrada
    print(f"Nombre de la tarea: {entrega.tarea.titulo}")
    print(f"Nombre del estudiante: {entrega.estudiante.nombre}") 
    print(f"Calificacion: {entrega.calificacion}") 
    print(f"Nombre del Instructor: {entrega.tarea.curso.instructor.nombre}")
    print(f"Nombre del Departamento: {entrega.tarea.curso.departamento.nombre}") 
# Cierra la sesión de la base de datos
session.close() 