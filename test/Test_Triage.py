import unittest
import csv
from src.Interfaz import cambiar_gravedad,asignar_gravedad

with open("DATOS.csv", "r") as tabla:
    csv_reader = csv.DictReader(tabla)  # lee por columnas
    # Passing the cav_reader object to list() to get a list of lists
    lista_pacientes = list(csv_reader)

class MyTestCase(unittest.TestCase):
    def test_asignar_paciente(self):
        paciente = lista_pacientes[0]
        self.assertEqual(paciente["gravedad"], '4')

    def test_cambiar_gravedad(self):
        # Caso de prueba con un paciente en estado azul (gravedad 1)
        pacientes = [{"gravedad": 1, "tiempo_espera": 240}]
        cambiar_gravedad(pacientes)
        assert pacientes[0]["gravedad"] == 2
    def test_cambiar_gravedad_1(self):
        # Caso de prueba con un paciente en estado azul (gravedad 1)
        pacientes = [{"gravedad": 1, "tiempo_espera": 0}]
        cambiar_gravedad(pacientes)
        assert pacientes[0]["gravedad"] == 1 #mantiene la gravedad

    def test_asignar_gravedad_1(self):
        pacientes = [{"sintomas": 'politraumatismo grave',"gravedad": 0, "tiempo_espera": 0}]
        asignar_gravedad(pacientes)
        assert pacientes[0]["gravedad"] ==  5 # mantiene la gravedad

    def test_asignar_gravedad_1(self):
        pacientes = [{"sintomas": 'asdsd', "gravedad": 0, "tiempo_espera": 0}, {"sintomas": 'politraumatismo grave', "gravedad": 0, "tiempo_espera": 0}]
        longitud_inicial = len(pacientes)# la longitud inicial de la lista de pacientes
        asignar_gravedad(pacientes) # Llama a la función que borra el paciente si tiene basura en el sintoma
        longitud_despues = len(pacientes) # la longitud después de la llamada a la función
        assert longitud_despues < longitud_inicial




if __name__ == '__main__':
    unittest.main()
