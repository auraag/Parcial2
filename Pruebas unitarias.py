import unittest
import clases as cl


class TrashCityTests(unittest.TestCase):

    def setUp(self):
        self.empresa = cl.Empresa()

    def test_agregarConductor(self):
        self.empresa.agregarConductor()
        self.assertEqual(len(self.empresa.conductores), 1)

    def test_agregarAsistente(self):
        self.empresa.agregarAsistente()
        self.assertEqual(len(self.empresa.asistentes), 1)
    def test_calcularVidrio(self):
        # Registrar algunos turnos con clasificaciones de vidrio
        self.empresa.agregarConductor()
        self.empresa.agregarAsistente()
        self.empresa.agregarAsistente()
        self.empresa.agregarCamion()
        self.empresa.registrarTurno()
        self.empresa.registrarTurno()

        vidrio_total = self.empresa.calcularVidrio()

        self.assertEqual(vidrio_total,
            self.empresa.turnosDelDia[0].clasificacion["vidrio"] +
            self.empresa.turnosDelDia[1].clasificacion["vidrio"])


if __name__ == '__main__':
    unittest.main()
