from datetime import date, time
from core.models import Period, Note, DetailNote, Student, Teacher, Asignature, ActiveManager, GeneralDelete
from django.contrib.auth.models import User
import random
from create import periods, asignatures, students, teachers, students_data

"""
    ----------------------------------------------------------------------------------------------
            |PERIODS | TEACHERS | STUDENTS | NOTES |                                                      
            
            ORM: OBJECT RELATIONAL MAPPING (SENTENCES |CRUD|)
                                                                                                
        -----> REGISTRANDO OBJETOS A PARTIR DE LOS MODELOS MEDIANTE CREATE_BULKS <-----      
                        CREA MULTIPLES REGISTROS DE MANERA EFICIENTE        
                                                                                                
    ----------------------------------------------------------------------------------------------
    
"""

def create_bulks(state):
    if state:
        #---->INSERT PERIODOS
        periodos = []
        for key, value in periods.items():
            periodo = Period(description=value["description"], start_date=value["start_date"], end_date=value["end_date"], user=User.objects.get(username=value["user"]))
            periodos.append(periodo)

        Period.objects.bulk_create(periodos)

        #---->INSERT Asignaturas
        asignaturas = []
        for key, value in asignatures.items():
            asignatura = Asignature(description=value["description"], user=User.objects.get(username=value["user"]))
            asignaturas.append(asignatura)

        Asignature.objects.bulk_create(asignaturas)

        #---->INSERT Profesores
        profesores = []
        for key, value in teachers.items():
            profesor = Teacher(cedula=value["cedula"], first_name=value["first_name"], last_name=value["last_name"], user=User.objects.get(username=value["user"]))
            profesores.append(profesor)

        Teacher.objects.bulk_create(profesores)

        #---->INSERT Estudiantes
        estudiantes = []
        for key, value in students.items():
            estudiante = Student(cedula=value["cedula"], first_name=value["first_name"], last_name=value["last_name"], user=User.objects.get(username=value["user"]))
            estudiantes.append(estudiante)

        Student.objects.bulk_create(estudiantes)
    else:
        print("No se puede crear la base de datos")
create_bulks(False)


# ---> RELACIONES ONE TO MANY FOR NOTES, CREATE OBJECT FOR NOTES <---
def note_create(state):
    user = User.objects.get(username="davdev")
    if state:
        for i in range(1,11):
            periodo = Period.objects.get(id=i)
            profesor = Teacher.objects.get(id=i)
            asignatura = Asignature.objects.get(id=i)
            note = Note.objects.create(
                period=periodo,
                teacher=profesor,
                asignature=asignatura,
                user=user
            )
    else:
        print("No se puede crear la base de datos")
note_create(False)

#---> RELACION ONE TO MANY FOR DETAILS_NOTE (SENTENCE: CREATE) <---
def create_detail(state):
    user = User.objects.get(username="davdev")
    if state:
        for data_detail in students_data.values():
            detail_note = DetailNote(
                note = data_detail["note"],
                estudiante_id=data_detail["student"],
                note1=data_detail["note1"],
                note2=data_detail["note2"],
                recovery=data_detail["recovery"],
                observations=data_detail["observations"],
                user=user
            )
            detail_note.save()
            print("REGISTROS GUARDADOS CON EXITO")
    else:
        print("NO SE GUARDARON LOS REGISTROS")
create_detail(False)

# ---> FUNCTION JOIN FOR CONSULTS GENERALS <---
def joiners(listers):
    return print(f"\n".join([f" ==> {context}" for i, context in enumerate(listers)]))

# ---> GENERAL BASIC CONSULTATION <---
def consult_basic():
    # ---> CONSULT STUDENTS WHERE FIRST_NAME START IN "EST" <---
    def consult_student(state):
        if state:
            students = Student.objects.filter(first_name__istartswith="est")
            joiners(students)
    consult_student(False)
    # ---> CONSULT TEACHERS WHERE FIRST_NAME START IN "OR" <---
    def consult_teacher(state):
        if state:
            teachers = Teacher.objects.filter(first_name__icontains="or")
            joiners(teachers)
    consult_teacher(False)
    # ---> CONSULT STUDENTS WHERE DESCRIPTION END IN "10" <---
    def consult_asignatures_end10(state):
        if state:
            asignatures = Asignature.objects.filter(description__endswith="10")
            joiners(asignatures)
    consult_asignatures_end10(False)
    # ---> SEE NOTES WHERE THEY ARE GRATHER THAN 8.0 <---
    def consult_notes_elderly(states):
        if states:
            note1 = DetailNote.objects.filter(note1__gt=8.0) 
            lister = [[note.estudiante_id.full_name(), note.note1] for note in note1]
            print("Listado de Estudiantes y Notas:\n" + "-"*77)
            joiners([f"Nombre del Estudiante: {estudiante:<30} | Nota1 ->: {nota}" for estudiante, nota in lister])
            print("-"*77)
    consult_notes_elderly(True)
    # ---> SEE NOTES WHERE THEY ARE LESS THAN 9.0 <---
    def consult_notes_minor(states):
        if states:
            note2 = DetailNote.objects.filter(note2__lt=9.0)
            lister = [[note.estudiante_id.full_name(), note.note2] for note in note2]
            print("Listado de Estudiantes y Notas:\n" + "-"*77)
            joiners([f"Nombre del Estudiante: {estudiante:<30} | Nota2 ->: {nota}" for estudiante, nota in lister])
            print("-"*77)
    consult_notes_minor(True)

# ---> CALL THE FUNCTION TO SEE ITS FUNCTIONALITY <---
consult_basic()