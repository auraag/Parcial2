import random as rd


class Empresa:
    def __init__(self):
        self.camiones = []
        self.conductores = []
        self.asistentes = []
        self.turnosDelDia = []
        self.turnosTotales = 0

    # Función que agrega un camión
    def agregarCamion(self):
        if len(self.conductores) < 1:
            print("XXXX Error: Se requiere al menos 1 conductor registrado XXXX")
            return

        if len(self.asistentes) < 2:
            print("XXXX Error: Se requieren al menos 2 asistentes registrados XXXX")
            return

        print("----- Conductores disponibles -----")
        # Elegir un conductor
        conductoresDisponibles = []
        for i, conductor in enumerate(self.conductores):
            if not conductor.ocupado:
                conductoresDisponibles.append(conductor)
                print(f"{i}. {conductor}")
        conductor = None
        while conductor is None:
            indice = input("Seleccione el número de conductor que desea asignar: ")
            try:
                indice = int(indice)
                if 0 <= indice < len(conductoresDisponibles):
                    conductor = conductoresDisponibles[indice]
                    break
                else:
                    print("Error: Seleccione un número válido de conductor disponible.")
            except ValueError:
                print("Error: Ingrese un número válido.")

        # Cambiar a no disponible
        for i in self.conductores:
            if i.ident == conductor.ident:
                i.ocupado = True

        print("----- Asistentes disponibles -----")
        asistentes_disponibles = []
        for i, asistente in enumerate(self.asistentes):
            if not asistente.ocupado:
                asistentes_disponibles.append(asistente)
                print(f"{i}. {asistente}")

        # Solicitar al usuario que elija dos asistentes
        seleccionados_asistentes = []
        while len(seleccionados_asistentes) < 2:
            indice = input(f"Seleccione el número de asistente {len(seleccionados_asistentes) + 1}: ")
            try:
                indice = int(indice)
                if 0 <= indice < len(asistentes_disponibles):
                    seleccionado_asistente = asistentes_disponibles[indice]
                    seleccionados_asistentes.append(seleccionado_asistente)
                    asistentes_disponibles.pop(indice)
                    print(f"Asistente {len(seleccionados_asistentes)} seleccionado: {seleccionado_asistente}")
                else:
                    print("Error: Seleccione un número válido de asistente disponible.")
            except ValueError:
                print("Error: Ingrese un número válido.")

        asistente1, asistente2 = seleccionados_asistentes
        # Cambiar a no disponible
        for i in self.asistentes:
            if i.ident == asistente1.ident or i.ident == asistente2.ident:
                i.ocupado = True

        id = int(input("Ingrese el código del camión: "))

        # Validar si el camión ya existe en la lista de camiones
        for camion in self.camiones:
            if camion.id == id:
                print("XXXXX Error: El camión ya existe en la empresa XXXXX")
                return
        # Añadirlo a la lista de camiones
        self.camiones.append(Camion(conductor, asistente1, asistente2, id))
        print("----- Camión agregado correctamente -----")

    def agregarConductor(self):
        nombre = input("Ingrese el nombre del conductor: ")
        ident = None

        while not ident:
            try:
                ident = int(input("Ingrese la identificación del conductor: "))
            except ValueError or TypeError:
                print("Error: El identificador debe ser un número entero. Intente nuevamente.")

        # Validar si el conductor ya existe en la lista de conductores
        for conductor in self.conductores:
            if conductor.ident == ident and conductor.id == ident:
                print("XXXXX Error: El conductor ya existe en la empresa XXXXX")
                return

        # Añadirlo a la lista de conductores
        self.conductores.append(Conductor(nombre, ident))
        print("------- Conductor agregado correctamente -------")

    def agregarAsistente(self):
        nombre = input("Ingrese el nombre del asistente: ")
        ident = None
        while not ident:
            try:
                ident = int(input("Ingrese la identificación del asistente: "))
            except ValueError or TypeError:
                print("Error: El identificador debe ser un número entero. Intente nuevamente.")

        # Validar si el asistente ya existe en la lista de conductores
        for asistente in self.asistentes:
            if asistente.ident == ident:
                print("XXXXX Error: El asistente ya existe en la empresa XXXXX")
                return

        # Añadirlo a la lista de asistentes
        self.asistentes.append(Asistente(nombre, ident))
        print("------- Asistente agregado correctamente -------")

    def registrarTurno(self):
        if len(self.camiones) < 1:
            print("XXXX Error: Se requiere al menos 1 camion registrado XXXX")
            return
        elif(self.turnosTotales == len(self.camiones)):
            print("XXXX Error: No hay camiones disponibles para más turnos XXXX")
            return

        print("----- Camiones disponibles -----")
        # Elegir un camion
        camionesDisponibles = []
        for i, camion in enumerate(self.camiones):
            if not camion.ocupado:
                camionesDisponibles.append(camion)
                print(f"{i}. Camión ID: {camion.id}")
        camion = None
        while camion is None:
            indice = input("Seleccione el número de camion que desea asignar: ")
            try:
                indice = int(indice)
                if 0 <= indice < len(camionesDisponibles):
                    camion = camionesDisponibles[indice]
                    break
                else:
                    print("Error: Seleccione un número válido de camion disponible.")
            except ValueError or TypeError:
                print("Error: Ingrese un número válido.")

        # Cambiar a no disponible
        for i in self.camiones:
            if i.id == camion.id:
                i.ocupado = True
        turno = Turno(camion)
        turno.clasificar()
        turno.mostrarResumen()
        respuesta = input("¿Estás seguro de que deseas ingresar el turno? (S/N): ")
        if respuesta.upper() == "S":
            self.turnosDelDia.append(turno)
            print("------- Turno ingresado correctamente -------")
        else:
            print("----- Turno no registrado -----")

    def calcularVidrio(self) -> float:
        totalVidrio = 0
        for i in self.turnosDelDia:
            totalVidrio += i.clasificacion["vidrio"]
        return totalVidrio

    def finalizarDia(self):
        print("----- Finalizar día -----")
        respuesta = input("¿Estás seguro de que deseas finalizar el día? (S/N): ")
        if respuesta.upper() == "S":
            # Calcular vidrio total recogido
            totalVidrio = self.calcularVidrio()
            print("----- Vidrio total recogio en el día en el centro de acopio -----")
            print(f"Vidrio total: {totalVidrio}")
            print("-----------------------------------------------------------------")
            print("------------------------- DÍA FINALIZADO ------------------------")
        else:
            print("...Continuando el día...")

class PuntoGeografico:
    def __init__(self, latitud: int, longitud: int):
        self.latitud = latitud
        self.longitud = longitud


class Camion:
    def __init__(self, conductor, asistente1, asistente2, id: int):
        self.conductor = conductor
        self.asistentes = [asistente1, asistente2]
        self.id = id
        self.ocupado = False

    def __repr__(self):
        return f"Camión ID: {self.id}\nConductor: {self.conductor}\nAsistentes: {self.asistentes}"

# La clase Persona almacena informacion de la persona (nombre e identificacíón)
class Persona:
    def __init__(self, nombre: str, ident: int):
        self.nombre = nombre
        self.ident = ident


# La clase Conductor hereda de persona nombre e ident(indentificación) y almacena su cargo
class Conductor(Persona):
    def __init__(self, nombre: str, ident: int):
        super().__init__(nombre, ident)
        self.cargo = "Conductor"
        self.ocupado = False

    def __repr__(self):
        estado = "disponible" if not self.ocupado else "no disponible"
        return f"{self.nombre} ({self.ident}), Estado: {estado}"


# La clase Asistente hereda de persona nombre e ident(indentificación) y almacena su cargo
class Asistente(Persona):
    def __init__(self, nombre: str, ident: int):
        super().__init__(nombre, ident)
        self.cargo = "Asistente de recolección"
        self.ocupado = False

    def __repr__(self):
        estado = "disponible" if not self.ocupado else "no disponible"
        return f"{self.nombre} ({self.ident}), Estado: {estado}"

class Turno:
    def __init__(self, camion: Camion):
        self.ruta = []
        self.generarRuta()
        self.camion = camion
        self.conductor = self.camion.conductor
        self.asistentes = self.camion.asistentes
        self.clasificacion = {"vidrio": 0.0, "papel": 0.0, "metal": 0.0, "residuos": 0.0}

    def generarRuta(self):
        for _ in range(5):
            latitud = rd.randint(-90, 90)  # Generar latitud aleatoria entre -90 y 90
            longitud = rd.randint(-180, 180)  # Generar longitud aleatoria entre -180 y 180
            self.ruta.append(PuntoGeografico(latitud, longitud))

    def clasificar(self) -> None:
        vidrio = float(input("¿Cuánto vidrio se recogió en el turno?: "))
        papel = float(input("¿Cuánto papel se recogió en el turno?: "))
        metal = float(input("¿Cuánto metal se recogió en el turno?: "))
        residuos = float(input("¿Cuánto residuos se recogió en el turno?: "))
        self.clasificacion.update({"vidrio":vidrio, "papel":papel, "metal": metal, "residuos":residuos})

    def mostrarResumen(self) -> None:
        print("----- Resumen de turno ingresado ------------------------------")
        print(self.camion)
        print("Cantidad de vidrio: ", self.clasificacion["vidrio"])
        print("Cantidad de papel: ", self.clasificacion["vidrio"])
        print("Cantidad de metal: ", self.clasificacion["vidrio"])
        print("Cantidad de residuos organicos: ", self.clasificacion["vidrio"])
        print("---------------------------------------------------------------")
