from datetime import date, datetime, time, timedelta
from core.models import Period, Note, DetailNote, Student, Teacher, Asignature, ActiveManager, GeneralDelete
from myproject.utils import joiners
from django.contrib.auth.models import User
import random
from create import periods, asignatures, students, teachers, students_data
from django.db.models import Q, F, Sum, Max, Min, Count, ExpressionWrapper, DecimalField
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

# ---> GENERAL BASIC CONSULTATION <---
def consult_basic():
    # ---> CONSULT STUDENTS WHERE FIRST_NAME START IN "EST" <---
    def consult_student(state):
        if state:
            students = Student.active_objects.filter(first_name__istartswith="est")
            joiners(students, "Estudiantes cuyo nombre empieza con 'Est'")
    consult_student(False)
    # ---> CONSULT TEACHERS WHERE FIRST_NAME START IN "OR" <---
    def consult_teacher(state):
        if state:
            teachers = Teacher.active_objects.filter(first_name__icontains="or")
            joiners(teachers, "Profesores cuyo nombre contiene 'or'")
    consult_teacher(False)
    # ---> CONSULT STUDENTS WHERE DESCRIPTION END IN "10" <---
    def consult_asignatures_end10(state):
        if state:
            asignatures = Asignature.active_objects.filter(description__endswith="10")
            joiners(asignatures, "Asignaturas cuya descripción termina en '10'")
    consult_asignatures_end10(False)
    # ---> SEE NOTES WHERE THEY ARE GRATHER THAN 8.0 <---
    def consult_notes_elderly(states):
        if states:
            note1 = DetailNote.active_objects.filter(note1__gt=8.0) 
            lister = [[note.estudiante.full_name(), note.note1] for note in note1]
            print("Listado de Estudiantes y Notas:\n" + "-"*77)
            joiners([f"Nombre del Estudiante: {estudiante:<30} | Nota1 ->: {nota}" for estudiante, nota in lister], "Notas mayores a 8.0")
            print("-"*77)
    consult_notes_elderly(False)
    # ---> SEE NOTES WHERE THEY ARE LESS THAN 9.0 <---
    def consult_notes_minor(states):
        if states:
            note2 = DetailNote.active_objects.filter(note2__lt=9.0)
            lister = [[note.estudiante.full_name(), note.note2] for note in note2]
            print("Listado de Estudiantes y Notas:\n" + "-"*77)
            joiners([f"Nombre del Estudiante: {estudiante:<30} | Nota2 ->: {nota}" for estudiante, nota in lister], "Notas menores a 9.0")
            print("-"*77)
    consult_notes_minor(False)

# ---> CALL THE FUNCTION TO SEE ITS FUNCTIONALITY <---

def consult_logic():
    def student_consult(state):
        if state:
            students = Student.active_objects.filter(Q(first_name__istartswith="Est") & Q(cedula__endswith=1)).values_list("first_name", "cedula")
            student_entries = [f"{student[0]} - {student[1]}" for student in students]
            joiners(student_entries, "Estudiantes que comienzan por 'Est' y terminan en '1'")
    student_consult(False)
    def asignature_consult(state):
        if state:
            asignatures = Asignature.active_objects.filter(Q(description__icontains="Asig") | Q(description__iendswith="5"))
            joiners(asignatures, f"Asignaturas que contienen 'Asig' o terminan en '5' (Total: {asignatures.count()})")
    asignature_consult(False)
    def teachers_consult(state):
        if state:
            teachers = Teacher.active_objects.filter(~Q(first_name__icontains="or") & ~Q(last_name__icontains="or"))
            joiners(teachers, "Profesores que no contienen 'or'")
    teachers_consult(False)
    def notes_consult_elderly_minor(state):
        if state:
            notes = DetailNote.active_objects.filter(Q(note1__gt=7.0) & Q(note2__lt=8.0))
            note_entries = [f"{note.estudiante.full_name()} - Nota1: {note.note1}, Nota2: {note.note2}" for note in notes]
            joiners(note_entries, "Notas con Nota1 > 7.0 y Nota2 < 8.0")
    notes_consult_elderly_minor(False)
    def notes_consult_elderly_nulls(state):
        if state:
            notes = DetailNote.active_objects.filter(Q(recovery__isnull=True) | Q(note2__gt=9.0))
            note_entries = [f"{note.estudiante.full_name()} - Recovery: {note.recovery}, Nota2: {note.note2}" for note in notes]
            joiners(note_entries, "Recovery con None o Nota2 > 9.0")
    notes_consult_elderly_nulls(False)

def consult_notes_between():
    def consult_notes_elderly_range(state):
        if state:
            notes = DetailNote.active_objects.filter(note1__range = (7.0, 9.0))
            note_entries = [f"{note.estudiante.full_name()} - Nota1: {note.note1}" for note in notes]
            joiners(note_entries, "Notas con Nota1 entre 7.0 y 9.0")
    consult_notes_elderly_range(False)
    def consult_notes_outside_range(state):
        if state:
            notes = DetailNote.active_objects.filter(~Q(note2__range= (6.0, 8.0)))
            note_entries = [f"{note.estudiante.full_name()} - Nota2: {note.note2}" for note in notes]
            joiners(note_entries, "Notas con Nota2 fuera del rango entre 6.0 y 8.0")
    consult_notes_outside_range(False)
    def consult_notes_null_filter(state):
        if state:
            notes = DetailNote.active_objects.filter(recovery__isnull=False)
            note_entries = [f"{note.estudiante.full_name()} - Recuperación: {note.recovery}, Nota1: {note.note1}, Nota2: {note.note2}" for note in notes]
            joiners(note_entries, "Notas cuya recuperación no es None")
    consult_notes_null_filter(False)

def consult_models_date():
    def consult_models_last_year(state):
        if state:
            year_end = timezone.now() - timedelta(days=365)
            notes = DetailNote.active_objects.filter(created__gte=year_end)
            note_entries = [f"Year: {note.created.year} - Recuperación: {note.recovery}, Nota1: {note.note1}, Nota2: {note.note2}" for note in notes]
            joiners(note_entries, "Creación de las notas en el último año")
    
    def consult_models_last_month(state):
        if state:
            month_end = timezone.now() - timedelta(days=30)
            notes = DetailNote.active_objects.filter(created__gte=month_end)
            note_entries = [f"Mes: {note.created.strftime('%B')} - Recuperación: {note.recovery}, Nota1: {note.note1}, Nota2: {note.note2}" for note in notes]
            joiners(note_entries, "Creación de las notas en el último mes")
    
    def consult_models_last_day(state):
        if state:
            now = timezone.now()
            last_day = now - timedelta(days=1)
            notas_ultimo_dia = DetailNote.active_objects.filter(created__gte=last_day)
            note_entries = [f"Fecha: {note.created} - Recuperación: {note.recovery}, Nota1: {note.note1}, Nota2: {note.note2}" for note in notas_ultimo_dia]
            joiners(note_entries, "Notas creadas en el ultimo dia")
    def consult_models_before_2023(state):
        if state:
            start_of_2023 = timezone.make_aware(datetime(year=2023, month=1, day=1))
            notes = DetailNote.active_objects.filter(created__lt=start_of_2023)
            note_entries = [f"Fecha: {note.created.strftime('%Y-%m-%d')} - Recuperación: {note.recovery}, Nota1: {note.note1}, Nota2: {note.note2}" for note in notes]
            joiners(note_entries, "Creación de las notas antes del año 2023")
    
    def consult_models_march_any_year(state):
        if state:
            notes = DetailNote.active_objects.filter(created__month=3)
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
            students = Student.active_objects.annotate(
                first_name_length=Length('first_name'),
                last_name_length=Length('last_name')
            ).filter(Q(first_name_length=10) | Q(last_name_length=10))
            
            note_entries = [f"Estudiante: {student.full_name()}" for student in students]
            joiners(note_entries, "todos los estudiantes cuyo nombre o apellido tiene exactamente 10 caracteres")
    
    def consult_note1_and_note2_elderly(state):
        if state:
            elderly_notes = DetailNote.active_objects.filter(Q(note1__gt=7.5) & Q(note2__gt=7.5))
            note_entries = [f"{note.estudiante.full_name()} - Nota1: {note.note1}, Nota2: {note.note2}" for note in elderly_notes]
            joiners(note_entries,"Nota1 y nota2 mayores a 7.5")
    
    def consult_note_null_note1_elderly(state):
        if state:
            notes = DetailNote.active_objects.filter(Q(recovery__isnull=False) & Q(note1__gt=F('note2')))
            note_entries = [f"{note.estudiante.full_name()} - Recuperación: {note.recovery} - note1: {note.note1} > note2: {note.note2}" for note in notes]
            joiners(note_entries, "Recuperación no nula y nota1 mayor que nota2")
    
    def consult_notes_elderly(state):
        if state:
            notes = DetailNote.active_objects.filter(Q(note1__gt=8.0) | Q(note2=7.5))
            note_entries = [f"{note.estudiante.full_name()} - Nota1: {note.note1} note2: {note.note2}" for note in notes]
            joiners(note_entries, "Nota1 mayor a 8.0 o nota2 igual a 7.5")

    def consult_recovery_elderly_notes(state):
        if state:
            notes = DetailNote.active_objects.filter(Q(recovery__gt=F("note1")) & Q(recovery__gt=F("note2")))
            note_entries = [f"{note.estudiante.full_name()} - Recuperación: {note.recovery} > note1: {note.note1} - note2: {note.note2}" for note in notes]
            joiners(note_entries, "Recuperación mayor que nota1 y nota2")
    
    consult_recovery_elderly_notes(True)
    consult_notes_elderly(False)
    consult_note_null_note1_elderly(False)
    consult_note1_and_note2_elderly(False)
    consult_students_length(False)

def subconsult_models():
    def consult_recovery(state):
        if state:
            recovery_notes = DetailNote.active_objects.filter(recovery__isnull=False).distinct()
            note_entries = [f"{note.estudiante.full_name()} - Recuperación: {note.recovery}" for note in recovery_notes]
            joiners(note_entries, "Recuperación no nula")
    
    def consult_teacher_asignature_distinct(state):
        asignature_id = 1
        if state:
            asignature = Asignature.active_objects.get(id=asignature_id)
            teacher_ids = Note.objects.filter(asignature=asignature).values_list('teacher_id', flat=True).distinct()
            note_entries = [
                f"Profesor: {Teacher.active_objects.get(id=teacher_id).full_name()} - Asignatura: {asignature.description}"
                for teacher_id in teacher_ids
            ]
            joiners(note_entries, f"Profesores que han dado la asignatura '{asignature.description}'")
    
    def subconsult_asignature_not_notes(state):
        if state:
            asignature_not = Asignature.active_objects.get(id=11)
            details_notes = DetailNote.active_objects.filter(note__asignature=asignature_not).exists()
            if not details_notes:
                data_asignature = f"La asignatura que no contiene registros de notas es: {asignature_not}"
                print(data_asignature)
    
    def subconsult_studentes_recovery_not_null(state):
        if state:
            
            estudiantes_sin_recuperacion = Student.objects.exclude(
            student_detail__in=DetailNote.objects.filter(recovery__isnull=False)
            )
            
            if estudiantes_sin_recuperacion.exists():
                data_recovery_null = [f"Estudiante: {student.first_name} - sin nota de recuperación" for student in estudiantes_sin_recuperacion]
                joiners(data_recovery_null, "Estudiantes sin nota de recuperación")
            else:
                print("No hay estudiantes sin nota de recuperación")
    
    def subconsult_notes_elderly(state):
        if state:
            notes_elderly = DetailNote.active_objects.filter(Q(note1__gt=8.0) & Q(note2__gt=8.0))
            data_notes_elderly = [f"nota1 {subconsult.note1} - note2 {subconsult.note2}" for subconsult in notes_elderly]
            if notes_elderly.exists():
                joiners(data_notes_elderly, "Notas con promedio mayor a 8.")
                
    def subconsult_notes_minor(state):
        if state:
            notes_minor = DetailNote.active_objects.filter(Q(note1__lt=6.0) & Q(note2__gt=7.0))
            data_notes_minor = [f"nota1 {subconsult.note1} - note2 {subconsult.note2}" for subconsult in notes_minor]
            if notes_minor.exists():
                joiners(data_notes_minor, "Nota 1 menor a 6.0 y nota 2 mayor a 7.0")
    
    #Seleccionar todas las notas con nota1 en la lista [7.0, 8.0, 9.0]:
    def subconsult_notes_list(state):
        if state:
            notes_list = DetailNote.active_objects.filter(note1__in=[7.0, 8.0, 9.0])
            data_notes_list = [f"nota1: {subconsult.note1} del estudiante: {subconsult.estudiante.full_name()} en la lista" for subconsult in notes_list ]
            if notes_list.exists():
                joiners(data_notes_list, "Notas con nota1 en la lista [7.0, 8.0, 9-0]")
    
    def subconsult_notes_range(state):
        if state:
            notes_id = DetailNote.active_objects.filter(id__range=(1,5)).order_by("id")
            data_notes_id = [f"id: {subconsult.id} nota1: {subconsult.note1} nota2: {subconsult.note2}" for subconsult in notes_id]
            if notes_id.exists():
                joiners(data_notes_id, "Notas con id en el rango [entre el 1 al 5]")
    
    def subconsult_recovery_not_list(state):
        if state:
            recovery_not_list = DetailNote.active_objects.filter(
            ~Q(recovery__in=[8.0, 9.0, 10.0]) & ~Q(recovery__isnull=True)
            )
            data_recovery_not_list = [f"recovery: {subconsult.recovery} del estudiante {subconsult.estudiante.full_name()}" for subconsult in recovery_not_list]
            if recovery_not_list.exists():
                joiners(data_recovery_not_list, "Recuperaciones no en la lista [8.0, 9.0, 10.0]")
    
    def subconsult_notes_students(state):
        if state:
            notes_sum = DetailNote.active_objects.filter(estudiante=1).annotate(sum_notes=Sum(F("note1") + F("note2")))
            data_notes_sum = [f"suma de notas: (note1: {subconsult.note1} + note2: {subconsult.note2}) es: {subconsult.sum_notes} el total del estudiante: {subconsult.estudiante.full_name()}" for subconsult in notes_sum ]
            if notes_sum.exists():
                joiners(data_notes_sum, "Suma de notas de los estudiantes")
    
    #36. Nota máxima obtenida por un estudiante:
    def subconsult_max_note(state):
        if state:
            max_note = DetailNote.active_objects.values('estudiante').annotate(
                max_total_note=Max(F('note1') + F('note2')),
                student_name=F('estudiante_id__first_name')
            ).order_by('-max_total_note').first()
            if max_note is not None:
                max_total_note = max_note['max_total_note']
                student_name = max_note['student_name']
                message = f"Nota máxima obtenida por el estudiante {student_name}: {max_total_note}"
                joiners([message], "Nota máxima obtenida por un estudiante")
            else:
                print("No se encontraron notas registradas")
    
    def subconsult_min_note(state):
        if state:
            min_note = DetailNote.active_objects.values(
                'estudiante_id__first_name',
                "observations"
            ).annotate(
                min_total_note=Min(F('note1') + F('note2'))
            ).order_by('min_total_note').first()
            
            if min_note is not None:
                student_name = min_note['estudiante_id__first_name']
                min_total_note = min_note['min_total_note']
                observations = min_note["observations"]
                message = f"Nota mínima obtenida por el estudiante {student_name}: {min_total_note} la observacion es: {observations}"
                joiners([message], "Nota mínima obtenida por cualquier estudiante")
            else:
                print("No se encontraron notas registradas")
    
    def count_total_notes_student(state):
        if state:
            count_notes = DetailNote.active_objects.filter(estudiante=5).annotate(count_note=Count("id"))
            data_count_notes = [f"El estudiante {subconsult.estudiante.full_name()} tiene {subconsult.count_note}" 
                                for subconsult in count_notes]
            joiners(data_count_notes, "Total de notas registradas")

    def avg_total_notes_students(state):
        if state:
            avg_notes = DetailNote.active_objects.filter(estudiante=5).annotate(
                    avg_notes=ExpressionWrapper(
                        (F('note1') + F('note2')) / 2.0,
                        output_field=DecimalField(max_digits=5, decimal_places=2)
                    )
                )
            data_avg_notes = [f"El estudiante {subconsult.estudiante.full_name()} tiene de promedio entre las dos notas: {subconsult.avg_notes}" 
                              for subconsult in avg_notes]
            joiners(data_avg_notes, "Promedio de las dos notas de los estudiantes")

    avg_total_notes_students(True)
    count_total_notes_student(False)
    subconsult_min_note(False)
    subconsult_max_note(False)
    subconsult_notes_students(False)
    subconsult_recovery_not_list(False)
    subconsult_notes_range(False)
    subconsult_notes_list(False)
    subconsult_notes_minor(False)
    subconsult_notes_elderly(False)
    subconsult_studentes_recovery_not_null(False)
    subconsult_asignature_not_notes(False)
    consult_teacher_asignature_distinct(False)
    consult_recovery(False)
    

def related_models_invers():
    def students_notes_detail(state):
        if state:
            student = Student.active_objects.prefetch_related('student_detail').get(id=5)
            detalles_notas = student.student_detail.all()
            data_details = [f"Estudiante: {student.full_name()} - Asignatura: {detalle.note.asignature.description}, Nota1: {detalle.note1}, Nota2: {detalle.note2}, Recuperación: {detalle.recovery}, Observaciones: {detalle.observations}" for detalle in detalles_notas]
            joiners(data_details, "Detalles del estudiante")

    students_notes_detail(False)

    def notes_periods_especific(state):
        if state:
            notas = Note.active_objects.filter(asignature_id=1, period_id=1).prefetch_related('Notas')
            data_details = [f"Periodo: {nota.period.description}\nProfesor: {nota.teacher.full_name()}\nAsignatura: {nota.asignature.description}\n" + "\n".join([f"Nota 1: {detalle.note1}, Nota 2: {detalle.note2}, Recuperación: {detalle.recovery}, Observaciones: {detalle.observations}" for detalle in nota.Notas.all()]) for nota in notas]
            joiners(data_details, "Notas del periodo específico")

    notes_periods_especific(False)

    def notes_teacher_especific(state):
        if state:
            notas = Note.active_objects.filter(teacher_id=2).prefetch_related('Notas')
            data_details = [f"Profesor: {nota.teacher.full_name()}\n" + "\n".join([f"Estudiante: {detalle.estudiante.full_name()}\nPeriodo: {detalle.note.period.description}\nAsignatura: {detalle.note.asignature.description}\nNota 1: {detalle.note1}\nNota 2: {detalle.note2}\nRecuperación: {detalle.recovery}\nObservaciones: {detalle.observations}" for detalle in nota.Notas.all()]) for nota in notas]
            joiners(data_details, "Notas del profesor específico")

    notes_teacher_especific(False)

    def notes_student_elderly(state):
        if state:
            student = Student.active_objects.prefetch_related('student_detail').get(id=8)
            detalles_notas = student.student_detail.filter(note1__gt=16.00)
            data_details = [f"Estudiante: {student.full_name()} - Asignatura: {detalle.note.asignature.description}, Nota1: {detalle.note1}, Nota2: {detalle.note2}, Recuperación: {detalle.recovery}, Observaciones: {detalle.observations}" for detalle in detalles_notas]
            joiners(data_details, "Detalles del estudiante")

    notes_student_elderly(True)

    def student_notes_period(state):
        if state:
            student = Student.objects.get(id=5)
            student_notes = DetailNote.active_objects.filter(estudiante=student).select_related('note__period', 'note__teacher', 'note__asignature').order_by('note__period__description', 'note__teacher__first_name', 'note__asignature__description')
            data_details = [f"Estudiante: {student.full_name()}\nPeriodo: {detail_note.note.period.description}\nProfesor: {detail_note.note.teacher.full_name()}\nAsignatura: {detail_note.note.asignature.description}\nNota1: {detail_note.note1}, Nota2: {detail_note.note2}, Recuperación: {detail_note.recovery}, Observaciones: {detail_note.observations}\n" for detail_note in student_notes]
            joiners(data_details, "Notas del estudiante en periodo")

    student_notes_period(False)

    def average_notes_student_period(state, student_id, period_id):
        if state:
            student = Student.active_objects.get(id=student_id)
            detail_notes = student.student_detail.filter(note__period_id=period_id)
            total_notes = detail_notes.count()
            if total_notes > 0:
                sum_notes = sum(detalle.note1 + detalle.note2 for detalle in detail_notes)
                average = sum_notes / (2 * total_notes)
                print(f"El promedio de las notas del estudiante {student.full_name()} en el periodo {period_id} es {average:.2f}")
            else:
                print(f"No hay notas para el estudiante {student.full_name()} en el periodo {period_id}")

    average_notes_student_period(False, student_id=5, period_id=5)

    def notes_with_specific_observation(state, observation):
        if state:
            detail_notes = DetailNote.active_objects.filter(observations__icontains=observation).select_related('note__asignature', 'note__period', 'note__teacher', 'estudiante')
            data_details = [f"Estudiante: {detail_note.estudiante.full_name()}\nPeriodo: {detail_note.note.period.description}\nProfesor: {detail_note.note.teacher.full_name()}\nAsignatura: {detail_note.note.asignature.description}\nNota1: {detail_note.note1}, Nota2: {detail_note.note2}, Recuperación: {detail_note.recovery}, Observaciones: {detail_note.observations}\n" for detail_note in detail_notes]
            joiners(data_details, "Notas con observación específica")

    notes_with_specific_observation(False, observation="Necesita mejorar.")

    def notes_student_ordered_by_asignature(state, student_id):
        if state:
            student = Student.active_objects.get(id=student_id)
            detail_notes = student.student_detail.select_related('note__asignature').order_by('note__asignature__description')
            data_details = [f"Estudiante: {student.full_name()}\nAsignatura: {detail_note.note.asignature.description}\nNota1: {detail_note.note1}, Nota2: {detail_note.note2}, Recuperación: {detail_note.recovery}, Observaciones: {detail_note.observations}\n" for detail_note in detail_notes]
            joiners(data_details, "Notas del estudiante ordenadas por asignatura")

    notes_student_ordered_by_asignature(False, student_id=5)

    
    
      
consult_basic()
consult_notes_between()
consult_models_date()
consult_avanced_notes()
consult_logic()
subconsult_models()
related_models_invers()