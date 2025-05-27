# Todos los departamentos que tengan notas de entregas menores o iguales a 0.3 
# En función de los departamentos, presentar el nombre del departamento 
# y el número de cursos que tiene cada departamento


from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from clases import engine, Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega

Session = sessionmaker(bind=engine)
session = Session()

departamentos_baja_calificacion = (
    session.query(Departamento.nombre, func.count(Curso.id).label('numero_cursos')) # Seleccionamos el nombre del departamento y contamos sus cursos.
    .join(Curso, Departamento.id == Curso.departamento_id) # Unimos Departamentos con Cursos.
    .join(Tarea, Curso.id == Tarea.curso_id)
    .join(Entrega, Tarea.id == Entrega.tarea_id)
    .filter(Entrega.calificacion <= 0.3) # Filtramos las entregas con calificaciones de 0.3 o menos.
    .group_by(Departamento.nombre) # Agrupamos por departamento para obtener un conteo por cada uno.
    .all() # Ejecutamos la consulta y obtenemos los resultados.
)

print("Departamentos notas entregas ")

for nombre_departamento, numero_cursos in departamentos_baja_calificacion:
    print(f"Departamento: {nombre_departamento}, Número de cursos: {numero_cursos}")

session.close()