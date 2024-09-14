import string

def validar_contraseña(contraseña):

    # Criterios
    # False significa que no cumple con los requisitos
    caracteres_especiales = set(string.punctuation)
    
    # Verificaciones
    # Mayusculas, minusculas, numero y caracter especial
    # Se inician en False para verificar luego si cumple
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_especial = False

    # Si la contraseña es menor a la longitud minima de los requisitos (8 caracteres) cancela de inmediato
    if len(contraseña) < 8:
        return False
    
    # For para recorrer toda la contraseña, verificando los requisitos 
    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        elif caracter in caracteres_especiales:
            tiene_especial = True
    
    # Devuelve el valor True de todos los requisitos luego de recorrer la contraseñac
    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial

# Solicita la contraseña al usuario
contraseña_usuario = input("Ingrese una contraseña: ")

# Mensaje de validacion
if validar_contraseña(contraseña_usuario):
    print("La contraseña es válida.")
else:
    print("La contraseña no es válida.")
