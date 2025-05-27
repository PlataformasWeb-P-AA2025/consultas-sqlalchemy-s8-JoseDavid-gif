# 1. Obtener las entregas de todos los estudiantes que pertenecen al departamento de Arte. 
# En función de la entrega, presentar, nombre del tarea, nombre del estudiante, calificación, 
# nombre de instructor y nombre del departamento

from sqlalchemy.orm import sessionmaker
from clases import engine, Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega


Session = sessionmaker(bind=engine)
session = Session()

entregas_v = (
    session.query(Entrega)
    .join(Estudiante)
    .join(Tarea)
    .join(Curso)
    .join(Departamento)
    .filter(Departamento.nombre == 'Arte')
    .all()
)

print(" Entregas ")
for entrega in entregas_v:
    print(f"Nombre de la tarea: {entrega.tarea.titulo}")
    print(f"Nombre del estudiante: {entrega.estudiante.nombre}")
    print(f"Calificacion: {entrega.calificacion}")
    print(f"Nombre del Instructor: {entrega.tarea.curso.instructor.nombre}")
    print(f"Nombre del Departamento: {entrega.tarea.curso.departamento.nombre}")
