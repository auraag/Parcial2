import clases as cl

TrashCity = cl.Empresa()

while True:
    print("------------- Menú -------------")
    print("1. Agregar camión")
    print("2. Agregar trabajador")
    print("3. Registrar turnos del día")
    print("4. Finalizar día")
    print("--------------------------------")

    opcion = int(input("Selecciona una opción (1-4): "))

    if opcion == 1:
        print("----- Agregar camión -----")
        TrashCity.agregarCamion()

    elif opcion == 2:
        print("----- Menú Agregar -----")
        print("1. Agregar conductor")
        print("2. Agregar asistente")
        print("------------------------")

        opcion = int(input("Selecciona una opción (1-2): "))

        if opcion == 1:
            TrashCity.agregarConductor()
        elif opcion == 2:
            TrashCity.agregarAsistente()
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

    elif opcion == 3:
        TrashCity.registrarTurno()
    elif opcion == 4:
        TrashCity.finalizarDia()
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
