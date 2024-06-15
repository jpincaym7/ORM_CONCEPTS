from datetime import date, datetime, time, timedelta
from core.models import Period, Note, DetailNote, Student, Teacher, Asignature, ActiveManager, GeneralDelete
from myproject.utils import joiners
from django.contrib.auth.models import User
import random
#from create import periods, asignatures, students, teachers, students_data
from django.db.models import Q, F, Sum, Max, Min, Count, ExpressionWrapper, DecimalField
from django.utils import timezone
from django.db.models.functions import Length

def crud_sentences(state):
    if state:
        # Create - details
        user = User.objects.get(id=2)
        student = Student.active_objects.get(id=1)
        print(student.id)
        period = Period.active_objects.last()
        teacher = Teacher.active_objects.first()
        asignature = Asignature.active_objects.get(pk=5)
        print(f"dates: {student.id, period, teacher, asignature}" )
        #create -details for note 
        note = Note.active_objects.create(
            period=period, 
            teacher=teacher, 
            asignature=asignature,
            user=user
        )
        print(f"Nota creada: {note}")
        DetailNote.active_objects.create(
            note=note, 
            estudiante=student,
            note1=random.randint(1,20),
            note2=random.randint(1,20),
            recovery=random.randint(1,20),
            observations="GOOD JOB, STUDENT",
            user=user
        )
        print(f"Detalle creado con exito")
        print(f"\n*3")
        print(f"Nota: {note}")
    else:
        print("ya lo creaste")
crud_sentences(False)

def updated_models_active():
    def updated_notes1_minor(state):
        if state:
            notes_for_updated = DetailNote.active_objects.filter(note1__lt=20).update(note1=15.5)
            notes_updated = DetailNote.active_objects.filter(note1=15.5)
            if notes_updated.exists():
                data_updated = [f"Nota actualizada del Estudiante: {note.estudiante.full_name()} - nota1: {note.note1}"
                                for note in notes_updated]
                joiners(data_updated, "Datos actualizados")
            else:
                print("No hay datos actualizados")
    updated_notes1_minor(True)
    def updated_notes2_minor(state):
        if state:
            notes_for_updated = DetailNote.active_objects.filter(note2__lt=15).update(note2=9.5)
            notes_updated = DetailNote.active_objects.filter(note2=9.5)
            if notes_updated.exists():
                data_updated = [f"Nota actualizada del Estudiante: {note.estudiante.full_name()} - nota2: {note.note2}"
                                for note in notes_updated]
                joiners(data_updated, "Datos actualizados")
            else:
                print("No hay datos actualizados")
    updated_notes2_minor(True)
    def updated_recovery_minor(state):
        if state:
            notes_not_updated = DetailNote.active_objects.filter(recovery__lt=10).update(recovery=16.75)
            notes_updated = DetailNote.active_objects.filter(recovery=16.75)
            if notes_updated.exists():
                data_updated = [f"Recuperación actualizada del Estudiante: {note.estudiante.full_name()} - Recuperación: {note.recovery}" 
                                for note in notes_updated]
                joiners(data_updated, "Datos actualizados")
            else:
                print("No hay datos actualizados")
    updated_recovery_minor(True)
    
    def updated_observations(state):
        if state:
            students_aprobados = DetailNote.active_objects.filter(recovery__isnull=True).update(observations="BUEN RENDIMIENTO, APROBADO")
            update_observation = DetailNote.active_objects.filter(recovery__isnull=True)
            if update_observation.exists():
                data_updated = [f"Observaciones actualizadas del Estudiante: {note.estudiante.full_name()} observación: {note.observations}" 
                                for note in update_observation]
                joiners(data_updated, "Datos actualizados")
            else:
                print("No hay datos actualizados")
    updated_observations(True)
    
    def updated_notes_period(state):
        if state:
            notes_period = DetailNote.active_objects.select_related("note").filter(
                note__period__id=1
            ).update(note1=14.55, note2=13.45, recovery=9.63)
            notes_updated = DetailNote.active_objects.select_related("note").filter(
                note__period__id=1
            )
            if notes_updated.exists():
                data_updated = [f"Notas actualizadas del Estudiante: {note.estudiante.full_name()} - notas: {note.note1} - {note.note2} - recovery: {note.recovery}"
                                for note in notes_updated]
                joiners(data_updated, "Datos actualizados")
            else:
                print("No hay datos actualizados")
    updated_notes_period(True)
    
def delete_logic_models():
    def delete_notes_student(state):
        if state:
            detail_student = DetailNote.active_objects.get(estudiante_id=3)
            detail_student.delete_physical()
            print("Detalle del Estudiante eliminado Fisicamente")
    delete_notes_student(True)
    
    def delete_notes_student_logic(state):
        if state:
            detail_student = DetailNote.active_objects.get(estudiante_id=7)
            detail_student.delete()
            print("Detalle del Estudiante eliminado Logicamente")
    delete_notes_student_logic(True)
    
    def delete_notes_period(state):
        if state:
            detail_student = DetailNote.active_objects.select_related("note").get(
                note__period__id=9
            )
            detail_student.delete_physical()
            print("Detalle del Estudiante eliminado Fisicamente")
    delete_notes_period(True)
    
    def delete_notes_period_logic(state):
        if state:
            detail_student = DetailNote.active_objects.select_related("note").filter(
                note__period__id=10
            )
            detail_student.delete()
            print("Detalle del Estudiante eliminado Logicamente")
    delete_notes_period_logic(True)
    
    def delete_notes_minor(state):
        if state:
            detail_student = DetailNote.active_objects.filter(note1__lt=10)
            for delete_notes in detail_student:
                delete_notes.delete_physical()
            print("Notas menores a 10 eliminado Fisicamente")
    delete_notes_minor(True)
    
#updated_models_active()
#delete_logic_models()