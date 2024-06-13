from datetime import date, datetime, time, timedelta
from core.models import Period, Note, DetailNote, Student, Teacher, Asignature, ActiveManager, GeneralDelete
from django.contrib.auth.models import User
import random
from create import periods, asignatures, students, teachers, students_data
from django.db.models import Q, F
from django.utils import timezone
from django.db.models.functions import Length
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
    consult_notes_null_filter(False)

def consult_models_date():
    def consult_models_last_year(state):
        if state:
            year_end = timezone.now() - timedelta(days=365)
            notes = DetailNote.objects.filter(created__gte=year_end)
            note_entries = [f"Year: {note.created.year} - Recuperación: {note.recovery}, Nota1: {note.note1}, Nota2: {note.note2}" for note in notes]
            joiners(note_entries, "Creación de las notas en el último año")
    
    def consult_models_last_month(state):
        if state:
            month_end = timezone.now() - timedelta(days=30)
            notes = DetailNote.objects.filter(created__gte=month_end)
            note_entries = [f"Mes: {note.created.strftime('%B')} - Recuperación: {note.recovery}, Nota1: {note.note1}, Nota2: {note.note2}" for note in notes]
            joiners(note_entries, "Creación de las notas en el último mes")
    
    def consult_models_last_day(state):
        if state:
            now = timezone.now()
            last_day = now - timedelta(days=1)
            notas_ultimo_dia = DetailNote.objects.filter(created__gte=last_day)
            note_entries = [f"Fecha: {note.created} - Recuperación: {note.recovery}, Nota1: {note.note1}, Nota2: {note.note2}" for note in notas_ultimo_dia]
            joiners(note_entries, "Notas creadas en el ultimo dia")
    def consult_models_before_2023(state):
        if state:
            start_of_2023 = timezone.make_aware(datetime(year=2023, month=1, day=1))
            notes = DetailNote.objects.filter(created__lt=start_of_2023)
            note_entries = [f"Fecha: {note.created.strftime('%Y-%m-%d')} - Recuperación: {note.recovery}, Nota1: {note.note1}, Nota2: {note.note2}" for note in notes]
            joiners(note_entries, "Creación de las notas antes del año 2023")
    
    def consult_models_march_any_year(state):
        if state:
            notes = DetailNote.objects.filter(created__month=3)
            note_entries = [f"Fecha: {note.created.strftime('%Y-%m-%d')} - Recuperación: {note.recovery}, Nota1: {note.note1}, Nota2: {note.note2}" for note in notes]
            joiners(note_entries, "Creación de las notas en marzo de cualquier año")
    
    consult_models_last_year(False)
    consult_models_last_month(False)
    consult_models_last_day(False)
    consult_models_before_2023(False)
    consult_models_march_any_year(False)


def consult_avanced_notes():
    def consult_students_length(state):
        if state:
            students = Student.objects.annotate(
                first_name_length=Length('first_name'),
                last_name_length=Length('last_name')
            ).filter(Q(first_name_length=10) | Q(last_name_length=10))
            
            note_entries = [f"Estudiante: {student.full_name()}" for student in students]
            joiners(note_entries, "todos los estudiantes cuyo nombre o apellido tiene exactamente 10 caracteres")
    
    def consult_note1_and_note2_elderly(state):
        if state:
            elderly_notes = DetailNote.objects.filter(Q(note1__gt=7.5) & Q(note2__gt=7.5))
            note_entries = [f"{note.estudiante_id.full_name()} - Nota1: {note.note1}, Nota2: {note.note2}" for note in elderly_notes]
            joiners(note_entries,"Nota1 y nota2 mayores a 7.5")
    
    def consult_note_null_note1_elderly(state):
        if state:
            notes = DetailNote.objects.filter(Q(recovery__isnull=False) & Q(note1__gt=F('note2')))
            note_entries = [f"{note.estudiante_id.full_name()} - Recuperación: {note.recovery} - note1: {note.note1} > note2: {note.note2}" for note in notes]
            joiners(note_entries, "Recuperación no nula y nota1 mayor que nota2")
    
    def consult_notes_elderly(state):
        if state:
            notes = DetailNote.objects.filter(Q(note1__gt=8.0) | Q(note2=7.5))
            note_entries = [f"{note.estudiante_id.full_name()} - Nota1: {note.note1} note2: {note.note2}" for note in notes]
            joiners(note_entries, "Nota1 mayor a 8.0 o nota2 igual a 7.5")

    def consult_recovery_elderly_notes(state):
        if state:
            notes = DetailNote.objects.filter(Q(recovery__gt=F("note1")) & Q(recovery__gt=F("note2")))
            note_entries = [f"{note.estudiante_id.full_name()} - Recuperación: {note.recovery} > note1: {note.note1} - note2: {note.note2}" for note in notes]
            joiners(note_entries, "Recuperación mayor que nota1 y nota2")
    
    consult_recovery_elderly_notes(True)
    consult_notes_elderly(False)
    consult_note_null_note1_elderly(False)
    consult_note1_and_note2_elderly(False)
    consult_students_length(False)

def subconsult_models():
    def consult_recovery(state):
        if state:
            recovery_notes = DetailNote.objects.filter(recovery__isnull=False).distinct()
            note_entries = [f"{note.estudiante_id.full_name()} - Recuperación: {note.recovery}" for note in recovery_notes]
            joiners(note_entries, "Recuperación no nula")
    
    def consult_teacher_asignature_distinct(state):
        asignature_name = "Algoritmo y Logica de Programación"
        if state:
        # Obtenemos la asignatura específica por su nombre
            try:
                asignature = Asignature.objects.get(description=asignature_name)
            except Asignature.DoesNotExist:
                print(f"No existe una asignatura con la descripción '{asignature_name}'")
                return
            
            # Obtenemos los profesores que han dado la asignatura específica
            teacher_ids = Note.objects.filter(asignature=asignature).values_list('teacher_id', flat=True).distinct()
            
            # Usamos una lista de comprensión para obtener los nombres completos de los profesores
            note_entries = [
                f"Profesor: {Teacher.objects.get(id=teacher_id).full_name()} - Asignatura: {asignature.description}"
                for teacher_id in teacher_ids
            ]
            
            # Llamar a la función joiners con las entradas formadas
            joiners(note_entries, f"Profesores que han dado la asignatura '{asignature_name}'")
    consult_teacher_asignature_distinct(True)
    consult_recovery(False)
    
    
"""""    
consult_basic()
consult_logic()
consult_notes_between()
consult_models_date()
consult_avanced_notes()

"""""
subconsult_models()