# TrashCity

TrashCity es un sistema de gestión para una empresa de recolección de basura. Permite agregar camiones, conductores y asistentes, registrar turnos del día y finalizar el día de trabajo calculando el total de vidrio recogido en los turnos del día.

## Requisitos

- Python 3.6

## Instrucciones de uso

1. Clona este repositorio o descarga los archivos `main.py` y `clases.py`.

2. Abre una terminal o línea de comandos y navega hasta el directorio donde se encuentran los archivos descargados.

3. Ejecuta el archivo `main.py` en tu entorno de Python.

4. Sigue las instrucciones proporcionadas en la consola para interactuar con el menú de opciones.

## Estructura del proyecto

- `main.py`: Archivo principal del programa que contiene el bucle de ejecución y el menú de opciones.
- `clases.py`: Archivo que define las clases `Empresa`, `Camion`, `Persona`, `Conductor`, `Asistente`, `Turno` y `PuntoGeografico.

## Funcionalidades principales

El código proporcionado ofrece las siguientes funcionalidades principales:

### Agregar Camión

Permite agregar un camión a la empresa. Antes de agregar un camión, se valida que haya al menos 1 conductor y 2 asistentes registrados. Luego, se muestra una lista de los conductores disponibles y se solicita al usuario que seleccione uno. A continuación, se muestra una lista de los asistentes disponibles y se solicita al usuario que seleccione dos. Después de seleccionar el conductor y los asistentes, se solicita al usuario que ingrese el código del camión. Si el camión ya existe en la lista de camiones, se muestra un mensaje de error. Si el camión es nuevo, se agrega a la lista de camiones de la empresa.

### Agregar Conductor

Permite agregar un conductor a la empresa. Se solicita al usuario que ingrese el nombre y la identificación del conductor. Antes de agregarlo, se verifica que el conductor no exista previamente en la lista de conductores.

### Agregar Asistente

Permite agregar un asistente a la empresa. Se solicita al usuario que ingrese el nombre y la identificación del asistente. Antes de agregarlo, se verifica que el asistente no exista previamente en la lista de asistentes.

### Registrar Turno

Permite registrar un turno de recolección. Antes de registrar un turno, se valida que haya al menos 1 camión registrado y que no se haya alcanzado el límite de turnos totales para el día. Se muestra una lista de los camiones disponibles y se solicita al usuario que seleccione uno. Después de seleccionar el camión, se genera automáticamente una ruta de puntos geográficos para el turno y se solicita al usuario que ingrese la cantidad de vidrio, papel, metal y residuos orgánicos recolectados en el turno. Luego se muestra un resumen del turno ingresado y se solicita la confirmación del usuario para registrar el turno.

### Calcular Vidrio Total

Permite calcular la cantidad total de vidrio recolectado en todos los turnos del día.

### Finalizar Día

Permite finalizar el día de trabajo. Antes de finalizar el día, se muestra el total de vidrio recogido en el centro de acopio. Luego se muestra un mensaje indicando que el día ha finalizado.

## Estructura de clases

El código utiliza las siguientes clases:

- `Empresa`: Representa la empresa de recolección de residuos. Contiene los métodos para agregar camiones, conductores, asistentes, registrar turnos, calcular el vidrio total y finalizar el día. También implementa la lógica para garantizar que solo se pueda crear una única instancia de la empresa utilizando el patrón de diseño Singleton.
- `IteradorTurnos`: Implementa un iterador para recorrer los turnos registrados en la empresa.
- `PuntoGeografico`: Representa un punto geográfico con latitud y longitud.
- `Camion`: Representa un camión de recolección de residuos. Contiene el conductor, los asistentes y el ID del camión.
- `Persona`: Clase base para representar una persona con nombre e identificación.
- `Conductor`: Representa un conductor de camión. Hereda de `Persona` y tiene un estado de ocupado o disponible.
- `Asistente`: Representa un asistente de recolección. Hereda de `Persona` y también tiene un estado de ocupado o disponible.
- `Turno`: Representa un turno de recolección. Contiene una ruta de puntos geográficos, un camión asignado, un conductor y asistentes, y una clasificación de la cantidad de vidrio, papel, metal y residuos recolectados.

## Autora

- Aura Guzmán
