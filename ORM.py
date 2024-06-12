from datetime import date, time
from core.models import Period, Note, DetailNote, Student, Teacher, Asignature, ActiveManager, GeneralDelete
from django.contrib.auth.models import User
import random
from create import periods, asignatures, students, teachers, students_data
from django.db.models import Q
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
def joiners(listers, title):
    print(f"\n{title}\n" + "="*len(title))
    for i, context in enumerate(listers, start=1):
        print(f"{i:02d}. {context}")
    print("="*len(title) + "\n")

# ---> GENERAL BASIC CONSULTATION <---
def consult_basic():
    # ---> CONSULT STUDENTS WHERE FIRST_NAME START IN "EST" <---
    def consult_student(state):
        if state:
            students = Student.objects.filter(first_name__istartswith="est")
            joiners(students, "Estudiantes cuyo nombre empieza con 'Est'")
    consult_student(False)
    # ---> CONSULT TEACHERS WHERE FIRST_NAME START IN "OR" <---
    def consult_teacher(state):
        if state:
            teachers = Teacher.objects.filter(first_name__icontains="or")
            joiners(teachers, "Profesores cuyo nombre contiene 'or'")
    consult_teacher(False)
    # ---> CONSULT STUDENTS WHERE DESCRIPTION END IN "10" <---
    def consult_asignatures_end10(state):
        if state:
            asignatures = Asignature.objects.filter(description__endswith="10")
            joiners(asignatures, "Asignaturas cuya descripción termina en '10'")
    consult_asignatures_end10(False)
    # ---> SEE NOTES WHERE THEY ARE GRATHER THAN 8.0 <---
    def consult_notes_elderly(states):
        if states:
            note1 = DetailNote.objects.filter(note1__gt=8.0) 
            lister = [[note.estudiante_id.full_name(), note.note1] for note in note1]
            print("Listado de Estudiantes y Notas:\n" + "-"*77)
            joiners([f"Nombre del Estudiante: {estudiante:<30} | Nota1 ->: {nota}" for estudiante, nota in lister], "Notas mayores a 8.0")
            print("-"*77)
    consult_notes_elderly(False)
    # ---> SEE NOTES WHERE THEY ARE LESS THAN 9.0 <---
    def consult_notes_minor(states):
        if states:
            note2 = DetailNote.objects.filter(note2__lt=9.0)
            lister = [[note.estudiante_id.full_name(), note.note2] for note in note2]
            print("Listado de Estudiantes y Notas:\n" + "-"*77)
            joiners([f"Nombre del Estudiante: {estudiante:<30} | Nota2 ->: {nota}" for estudiante, nota in lister], "Notas menores a 9.0")
            print("-"*77)
    consult_notes_minor(False)

# ---> CALL THE FUNCTION TO SEE ITS FUNCTIONALITY <---
consult_basic()

def consult_logic():
    def student_consult(state):
        if state:
            students = Student.objects.filter(Q(first_name__istartswith="Est") & Q(cedula__endswith=1)).values_list("first_name", "cedula")
            student_entries = [f"{student[0]} - {student[1]}" for student in students]
            joiners(student_entries, "Estudiantes que comienzan por 'Est' y terminan en '1'")
    student_consult(False)
    def asignature_consult(state):
        if state:
            asignatures = Asignature.objects.filter(Q(description__icontains="Asig") | Q(description__iendswith="5"))
            joiners(asignatures, f"Asignaturas que contienen 'Asig' o terminan en '5' (Total: {asignatures.count()})")
    asignature_consult(False)
    def teachers_consult(state):
        if state:
            teachers = Teacher.objects.filter(~Q(first_name__icontains="or") & ~Q(last_name__icontains="or"))
            joiners(teachers, "Profesores que no contienen 'or'")
    teachers_consult(False)
    def notes_consult_elderly_minor(state):
        if state:
            notes = DetailNote.objects.filter(Q(note1__gt=7.0) & Q(note2__lt=8.0))
            note_entries = [f"{note.estudiante_id.full_name()} - Nota1: {note.note1}, Nota2: {note.note2}" for note in notes]
            joiners(note_entries, "Notas con Nota1 > 7.0 y Nota2 < 8.0")
    notes_consult_elderly_minor(False)
    def notes_consult_elderly_nulls(state):
        if state:
            notes = DetailNote.objects.filter(Q(recovery__isnull=True) | Q(note2__gt=9.0))
            note_entries = [f"{note.estudiante_id.full_name()} - Recovery: {note.recovery}, Nota2: {note.note2}" for note in notes]
            joiners(note_entries, "Recovery con None o Nota2 > 9.0")
    notes_consult_elderly_nulls(False)
consult_logic()

def consult_notes_between():
    def consult_notes_elderly_range(state):
        if state:
            notes = DetailNote.objects.filter(note1__range = (7.0, 9.0))
            note_entries = [f"{note.estudiante_id.full_name()} - Nota1: {note.note1}" for note in notes]
            joiners(note_entries, "Notas con Nota1 entre 7.0 y 9.0")
    consult_notes_elderly_range(False)
    def consult_notes_outside_range(state):
        if state:
            notes = DetailNote.objects.filter(~Q(note2__range= (6.0, 8.0)))
            note_entries = [f"{note.estudiante_id.full_name()} - Nota2: {note.note2}" for note in notes]
            joiners(note_entries, "Notas con Nota2 fuera del rango entre 6.0 y 8.0")
    consult_notes_outside_range(False)
    def consult_notes_null_filter(state):
        if state:
            notes = DetailNote.objects.filter(recovery__isnull=False)
            note_entries = [f"{note.estudiante_id.full_name()} - Recuperación: {note.recovery}, Nota1: {note.note1}, Nota2: {note.note2}" for note in notes]
            joiners(note_entries, "Notas cuya recuperación no es None")
    consult_notes_null_filter(True)
consult_notes_between()