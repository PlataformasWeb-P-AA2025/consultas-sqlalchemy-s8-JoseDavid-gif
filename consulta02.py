# Todos los departamentos que tengan notas de entregas menores o iguales a 0.3 
# En función de los departamentos, presentar el nombre del departamento 
# y el número de cursos que tiene cada departamento

from sqlalchemy.orm import sessionmaker
from sqlalchemy import func # Necesario para usar func.count
from clases import engine, Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega 

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consulta para obtener los departamentos con notas de entregas bajas Y el número de cursos
dep_info_bajas_calificaciones = (
    session.query(
        Departamento.nombre, # Seleccionamos el nombre del departamento
        func.count(Curso.id).label('numero_cursos') # 
    )
    .join(Departamento.cursos) # Unimos Departamento con Curso
    .join(Curso.tareas) # Unimos Curso con Tarea
    .join(Tarea.entregas) # Unimos Tarea con Entrega
    .filter(Entrega.calificacion <= 0.3) # Filtramos por entregas con bajas calificaciones
    .group_by(Departamento.nombre) # ¡Agrupamos por departamento para contar sus cursos!
    .all() # Ejecutamos la consulta
)

# Presentar los departamentos y el número de cursos
print("Departamentos con notas de entregas menores o iguales a 0.3 y su número de cursos:")

# Itera sobre los resultados,
for nombre_dep, num_cursos in dep_info_bajas_calificaciones:
    print(f"Departamento: {nombre_dep}, Número de cursos: {num_cursos}")

session.close() # Cerramos la sesión