from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="El número de teléfono debe contener entre 9 y 15 dígitos.")
 
# ---> FUNCTION JOIN FOR CONSULTS GENERALS <---
def joiners(listers, title):
    print(f"\n{title}\n" + "="*len(title))
    for i, context in enumerate(listers, start=1):
        print(f"{i:02d}. {context}")
    print("="*len(title) + "\n") 
 
def valida_cedula(value):
    cedula = str(value)
    if not cedula.isdigit():
        raise ValidationError('La cédula debe contener solo números.')

    longitud = len(cedula)
    if longitud != 10:
        raise ValidationError('La cédula debe tener 10 dígitos.')

    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    total = 0
    for i in range(9):
        digito = int(cedula[i])
        coeficiente = coeficientes[i]
        producto = digito * coeficiente
        if producto > 9:
            producto -= 9
        total += producto

    digito_verificador = (total * 9) % 10
    if digito_verificador != int(cedula[9]):
        raise ValidationError('La cédula no es válida.')
      