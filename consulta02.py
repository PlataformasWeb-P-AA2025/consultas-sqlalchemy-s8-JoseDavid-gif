# Todos los departamentos que tengan notas de entregas menores o iguales a 0.3 
# En función de los departamentos, presentar el nombre del departamento 
# y el número de cursos que tiene cada departamento

from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from clases import engine, Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega 

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consulta para obtener solo los nombres de los departamentos con notas de entregas bajas
dep_notas = (
    session.query(Departamento.nombre) # Seleccionamos el nombre del departamento
    .join(Departamento.cursos) # Unimos Departamento con Curso a través de la relación
    .join(Curso.tareas) # Unimos Curso con Tarea a través de la relación
    .join(Tarea.entregas) # Unimos Tarea con Entrega a través de la relación
    .filter(Entrega.calificacion <= 0.3) # Filtramos por entregas con calificaciones de 0.3 o menos
    .distinct() # Aseguramos que cada nombre de departamento aparezca solo una vez
    .all() # Ejecutamos la consulta
)

# Presentar los departamentos
print("Departamentos que tienen notas menores o iguales a 0.3:")

for nombre_dep, in dep_notas: # Iteramos sobre los resultados
    print(f"Departamento: {nombre_dep}")

session.close() # Cerramos la sesión