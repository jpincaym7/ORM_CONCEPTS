from django.contrib import admin
from .models import Period, Asignature, Teacher, Student, Note, DetailNote

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('description', 'start_date', 'end_date', 'state')
    list_filter = ('start_date', 'end_date', 'state')
    search_fields = ('description',)

@admin.register(Asignature)
class AsignatureAdmin(admin.ModelAdmin):
    list_display = ('description', 'state')
    list_filter = ('state',)
    search_fields = ('description',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'cedula', 'state')
    list_filter = ('state',)
    search_fields = ('first_name', 'last_name', 'cedula')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'cedula', 'state')
    list_filter = ('state',)
    search_fields = ('first_name', 'last_name', 'cedula')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('period', 'teacher', 'asignature')
    list_filter = ('period', 'teacher', 'asignature')
    search_fields = ('period__description', 'teacher__first_name', 'teacher__last_name', 'asignature__description')

@admin.register(DetailNote)
class DetailNoteAdmin(admin.ModelAdmin):
    list_display = ('note', 'estudiante', 'note1', 'note2', 'recovery')
    list_filter = ('note__period', 'estudiante', 'recovery')
    search_fields = ('note__period__description', 'estudiante__first_name', 'estudiante__last_name')

