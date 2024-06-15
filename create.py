from datetime import date
from core.models import Period, Note, DetailNote, Student, Teacher, Asignature, ActiveManager, GeneralDelete
from core.models import Period, Note, DetailNote, Student, Teacher, Asignature, ActiveManager, GeneralDelete
from django.contrib.auth.models import User
# ---> DICCIONARIES STUDENTS, TEACHERS, PERIODS, ASIGNATURES
"""""
    periods = {
        "period1": {
            "description": "Primer semestre",
            "start_date": date(2024, 1, 1),
            "end_date": date(2024, 5, 30),
            "user": "davdev"
        },
        "period2": {
            "description": "Segundo semestre",
            "start_date": date(2024, 6, 1),
            "end_date": date(2024, 8, 20),
            "user": "davdev"
        },
        "period3": {
            "description": "Tercer Semestre",
            "start_date": date(2024, 9, 1),
            "end_date": date(2024, 12, 20),
            "user": "davdev"
        },
        "period4": {
            "description": "Cuarto semestre",
            "start_date": date(2025, 1, 15),
            "end_date": date(2025, 5, 30),
            "user": "davdev"
        },
        "period5": {
            "description": "Quinto semestre",
            "start_date": date(2025, 6, 1),
            "end_date": date(2025, 8, 20),
            "user": "davdev"
        },
        "period6": {
            "description": "Sexto semestre",
            "start_date": date(2025, 9, 1),
            "end_date": date(2025, 12, 20),
            "user": "davdev"
        },
        "period7": {
            "description": "Séptimo semestre",
            "start_date": date(2026, 1, 15),
            "end_date": date(2026, 5, 30),
            "user": "davdev"
        },
        "period8": {
            "description": "Octavo semestre",
            "start_date": date(2026, 6, 1),
            "end_date": date(2026, 8, 20),
            "user": "davdev"
        },
        "period9": {
            "description": "Noveno semestre",
            "start_date": date(2026, 9, 1),
            "end_date": date(2026, 12, 20),
            "user": "davdev"
        },
        "period10": {
            "description": "Décimo semestre",
            "start_date": date(2027, 1, 15),
            "end_date": date(2027, 5, 30),
            "user": "davdev"
        }
    }

    # --> ASIGNATURES: REGISTERS
    asignatures = {
                    "asignature1": {
                        "description": "Algoritmo y Logica de Programación",
                        "user": "davdev"
                    },
                    "asignature2": {
                        "description": "Calculo Integral",
                        "user": "davdev"
                    },
                    "asignature3": {
                        "description": "Introducción a la Ingenieria",
                        "user": "davdev"
                    },
                    "asignature4": {
                        "description": "Matematicas Discretas",
                        "user": "davdev"
                    },
                    "asignature5": {
                        "description": "Ecuaciones Diferenciales",
                        "user": "davdev"
                    },
                    "asignature6": {
                        "description": "Fisica I",
                        "user": "davdev"
                    },
                    "asignature7": {
                        "description": "Fisica II",
                        "user": "davdev"
                    },
                    "asignature8": {
                        "description": "Estructura de Datos",
                        "user": "davdev"
                    },
                    "asignature9": {
                        "description": "Modelado de Software",
                        "user": "davdev"
                    },
                    "asignature10": {
                        "description": "Arquitectura de Software",
                        "user": "davdev"
                    },
                }

    # --> TEACHERS: DICCIONARIES
    teachers = {
                    "teachers1" : {
                        "cedula": "0943161372",
                        "first_name": "Juan",
                        "last_name":"Pincay",
                        "user":"davdev"
                    },
                    "teachers2":{
                        "cedula": "0923305627",
                        "first_name": "Mayra",
                        "last_name":"Murillo",
                        "user":"davdev"
                    },
                    "teachers3":{
                        "cedula": "0102030405",
                        "first_name": "Susana",
                        "last_name":"Salan",
                        "user":"davdev"
                    },
                    "teachers4":{
                        "cedula":"0102030413",
                        "first_name":"Gabriel",
                        "last_name":"Asqui",
                        "user":"davdev"
                    },
                    "teachers5":{
                        "cedula":"0203040506",
                        "first_name":"Gabriel",
                        "last_name":"Pincay",
                        "user":"davdev"
                    },
                    "teachers6":{
                        "cedula":"0203040514",
                        "first_name":"Damian",
                        "last_name":"Ordoñez",
                        "user":"davdev"
                    },
                    "teachers7":{
                        "cedula":"0304050607",
                        "first_name":"Valeria",
                        "last_name":"Pincay",
                        "user":"davdev"
                    },
                    "teachers8":{
                        "cedula":"0304050615",
                        "first_name":"Sharon",
                        "last_name":"Virginia",
                        "user":"davdev"
                    },
                    "teachers9":{
                        "cedula":"0405060708",
                        "first_name":"Maria",
                        "last_name":"Aristega",
                        "user":"davdev"
                    },
                    "teachers10":{
                        "cedula":"0405060716",
                        "first_name":"Amelia",
                        "last_name":"Aristega",
                        "user":"davdev"
                    }
                }

    # ---> STUDENTS: DICCIONARIES
    students = {
                    "student1": {
                        "cedula": "1102054981",
                        "first_name": "Carlos",
                        "last_name": "Martínez",
                        "user": "davdev"
                    },
                    "student2": {
                        "cedula": "1102053828",
                        "first_name": "Andrea",
                        "last_name": "Gómez",
                        "user": "davdev"
                    },
                    "student3": {
                        "cedula": "1102056013",
                        "first_name": "Luis",
                        "last_name": "Ramos",
                        "user": "davdev"
                    },
                    "student4": {
                        "cedula": "1102052154",
                        "first_name": "Sofia",
                        "last_name": "Torres",
                        "user": "davdev"
                    },
                    "student5": {
                        "cedula": "1102057809",
                        "first_name": "Miguel",
                        "last_name": "Vargas",
                        "user": "davdev"
                    },
                    "student6": {
                        "cedula": "1102059532",
                        "first_name": "Lucia",
                        "last_name": "Moreno",
                        "user": "davdev"
                    },
                    "student7": {
                        "cedula": "1102054847",
                        "first_name": "David",
                        "last_name": "Ortega",
                        "user": "davdev"
                    },
                    "student8": {
                        "cedula": "1102056740",
                        "first_name": "Valeria",
                        "last_name": "Fernández",
                        "user": "davdev"
                    },
                    "student9": {
                        "cedula": "1102058411",
                        "first_name": "Jorge",
                        "last_name": "Castro",
                        "user": "davdev"
                    },
                    "student10": {
                        "cedula": "1102059263",
                        "first_name": "Elena",
                        "last_name": "Salazar",
                        "user": "davdev"
                    }
                }
"""""
                #-->DETAIL_NOTE (DETALLES) 
students_data = {
    "detail1": {
        "student": Student.objects.get(id=1),
        "note": Note.objects.get(id=1),
        "note1": 8.5,
        "note2": 9.0,
        "recovery": 10.50,
        "observations": "Sigue mejorando"
    },
    "detail2": {
        "student": Student.objects.get(id=2),
        "note": Note.objects.get(id=2),
        "note1": 15.0,
        "note2": 18.0,
        "recovery": None,
        "observations": "Excelente desempeño."
    },
    "detail3": {
        "student": Student.objects.get(id=3),
        "note": Note.objects.get(id=3),
        "note1": 16.0,
        "note2": 17.5,
        "recovery": None,
        "observations": "Excelente desempeño."
    },
    "detail4": {
        "student": Student.objects.get(id=4),
        "note": Note.objects.get(id=4),
        "note1": 12.0,
        "note2": 11.5,
        "recovery": None,
        "observations": "Rendimiento promedio."
    },
    "detail5": {
        "student": Student.objects.get(id=5),
        "note": Note.objects.get(id=5),
        "note1": 9.0,
        "note2": 8.5,
        "recovery": None,
        "observations": "Rendimiento promedio."
    },
    "detail6": {
        "student": Student.objects.get(id=6),
        "note": Note.objects.get(id=6),
        "note1": 6.5,
        "note2": 7.0,
        "recovery": 8.0,
        "observations": "Necesita mejorar."
    },
    "detail7": {
        "student": Student.objects.get(id=7),
        "note": Note.objects.get(id=7),
        "note1": 3.0,
        "note2": 2.5,
        "recovery": 4.0,
        "observations": "Necesita mejorar."
    },
    "detail8": {
        "student": Student.objects.get(id=8),
        "note": Note.objects.get(id=8),
        "note1": 16.5,
        "note2": 17.0,
        "recovery": None,
        "observations": "Excelente desempeño."
    },
    "detail9": {
        "student": Student.objects.get(id=9),
        "note": Note.objects.get(id=9),
        "note1": 13.0,
        "note2": 12.5,
        "recovery": None,
        "observations": "Rendimiento promedio."
    },
    "detail10": {
        "student": Student.objects.get(id=10),
        "note": Note.objects.get(id=10),
        "note1": 5.5,
        "note2": 6.0,
        "recovery": 7.5,
        "observations": "Necesita mejorar."
    },
    "detail11": {
        "student": Student.objects.get(id=10),
        "note": Note.objects.get(id=1),
        "note1": 19.5,
        "note2":14.4,
        "recovery": None,
        "observations": "Good Job"
    }
}

"""""
def create_bulks(state):
    if state:
        insert_periods()
        insert_asignatures()
        insert_teachers()
        insert_students()
    else:
        print("No se puede crear la base de datos")

def insert_periods():
    periods = []
    for key, value in periods.items():
        periodo = Period(description=value["description"], start_date=value["start_date"], end_date=value["end_date"], user=User.objects.get(username=value["user"]))
        periods.append(periodo)
    
    Period.objects.bulk_create(periods)

def insert_asignatures():
    asignaturas = []
    for key, value in asignatures.items():
        asignatura = Asignature(description=value["description"], user=User.objects.get(username=value["user"]))
        asignaturas.append(asignatura)
    
    Asignature.objects.bulk_create(asignaturas)

def insert_teachers():
    teachers = []
    for key, value in teachers.items():
        profesor = Teacher(cedula=value["cedula"], first_name=value["first_name"], last_name=value["last_name"], user=User.objects.get(username=value["user"]))
        teachers.append(profesor)
    
    Teacher.objects.bulk_create(teachers)

def insert_students():
    students = []
    for key, value in students.items():
        estudiante = Student(cedula=value["cedula"], first_name=value["first_name"], last_name=value["last_name"], user=User.objects.get(username=value["user"]))
        students.append(estudiante)
    
    Student.objects.bulk_create(students)
"""""
def Create_Register():
# ---> RELACIONES ONE TO MANY FOR NOTES, CREATE OBJECT FOR NOTES <---
    def note_create(state):
        if state:
            user = User.objects.get(username="davdev")
            for i in range(1, 11):
                try:
                    periodo = Period.objects.get(id=i)
                    profesor = Teacher.objects.get(id=i)
                    asignatura = Asignature.objects.get(id=i)
                    note = Note.objects.create(
                        period=periodo,
                        teacher=profesor,
                        asignature=asignatura,
                        user=user
                    )
                    print(f"Nota creada para Periodo {periodo}, Profesor {profesor}, Asignatura {asignatura}")
                except (Period.DoesNotExist, Teacher.DoesNotExist, Asignature.DoesNotExist) as e:
                    print(f"Error al crear la nota para el ID {i}: {e}")
        else:
            print("No se puede crear la base de datos")
    note_create(False)
    #---> RELACION ONE TO MANY FOR DETAILS_NOTE (SENTENCE: CREATE) <---
    def create_detail_notes(state):
        if state:
            user = User.objects.get(username="davdev")  # Asegúrate de obtener el usuario adecuado

            for key, data in students_data.items():
                try:
                    student_instance = data['student']
                    note_instance = data['note']

                    detail_note = DetailNote.objects.create(
                        note=note_instance,
                        estudiante=student_instance,
                        note1=data['note1'],
                        note2=data['note2'],
                        recovery=data['recovery'],
                        observations=data['observations'],
                        user=user  # Asigna el usuario a la instancia de DetailNote
                    )
                    print(f"Creado: {detail_note}")
                except (Student.DoesNotExist, Note.DoesNotExist) as e:
                    print(f"No se pudo crear DetailNote para {key}: {e}")
        else:
            print("No se puede crear la base de datos")
    create_detail_notes(False)
Create_Register()