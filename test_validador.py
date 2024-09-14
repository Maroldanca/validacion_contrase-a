import unittest
from validacion import validar_contraseña  
class TestValidarContraseña(unittest.TestCase):
    
    def test_valida_contraseña_correcta(self):

        # Contraseña con todos los criterios
        self.assertTrue(validar_contraseña("Adrimar1416-"))

    def test_corta(self):

        # Contraseña muy corta
        self.assertFalse(validar_contraseña("Adri1-"))

    def test_falta_mayuscula(self):

        # Contraseña que no tiene mayusculas
        self.assertFalse(validar_contraseña("adrimar1416-"))

    def test_falta_minuscula(self):

        # Contraseña sin minusculas
        self.assertFalse(validar_contraseña("ADRIMAR1416-"))

    def test_falta_numero(self):

       # Contraseña sin numeros
        self.assertFalse(validar_contraseña("Adrimar-"))

    def test_falta_caracter_especial(self):
        
        # Contraseña sin caracter especial
        self.assertFalse(validar_contraseña("Adrimar1416"))

if __name__ == "__main__":
    unittest.main()
