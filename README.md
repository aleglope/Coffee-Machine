# ☕ Proyecto de Máquina de Café 🖥️

## 📜 Descripción

Este proyecto es un simulador interactivo de máquina de café desarrollado en Python. El programa permite a los usuarios elegir de un menú de bebidas, pagar por ellas y obtener un informe de los recursos y dinero en la máquina.

## 📋 Requisitos

Antes de ejecutar el simulador de máquina de café, asegúrate de tener Python instalado en tu sistema. Puedes descargar Python desde el [sitio web oficial](https://www.python.org/).

## 📁 Archivos Necesarios

Para que la máquina de café funcione correctamente, necesitarás los siguientes archivos:

1. `main.py`: El archivo principal para ejecutar el programa de la máquina de café.
2. `coffee_maker.py`: Contiene la clase `CoffeeMaker` que gestiona los recursos de la máquina.
3. `menu.py`: Contiene las clases `Menu` y `MenuItem` para definir y gestionar las opciones de bebidas.
4. `money_machine.py`: Contiene la clase `MoneyMachine` para gestionar las transacciones de dinero.

## 🛠️ Instrucciones de Uso

### Paso 1: Configuración del Entorno

1. Asegúrate de que todos los archivos necesarios estén en el mismo directorio.
2. Abre una terminal o símbolo del sistema y navega al directorio donde se encuentran los archivos.

### Paso 2: Ejecutar la Máquina de Café

Para iniciar el programa de la máquina de café, ejecuta el archivo `main.py`:

```sh
python main.py
```

### Paso 3: Usar la Máquina de Café

- **Elegir una Bebida**: Cuando se te pida, ingresa el nombre de la bebida que deseas (por ejemplo, `latte`, `espresso`, `cappuccino`). También puedes escribir `report` para ver los recursos y dinero actuales, o `off` para apagar la máquina.
- **Insertar Monedas**: Si eliges una bebida, se te pedirá que insertes monedas. Ingresa el número de cada tipo de moneda cuando se te pregunte.
- **Disfruta tu Bebida**: Si has insertado suficiente dinero, se preparará tu bebida y se te devolverá cualquier cambio.

## 📂 Resumen de Archivos

### `main.py`
Este es el script principal para ejecutar el simulador de la máquina de café. Crea objetos para el menú, la máquina de café y la máquina de dinero, y maneja el bucle principal del programa.

### `coffee_maker.py`
Contiene la clase `CoffeeMaker`, que gestiona:
- Informar sobre los recursos actuales.
- Comprobar si hay suficientes recursos para hacer una bebida.
- Preparar el café deduciendo los recursos utilizados.

### `menu.py`
Contiene las clases `Menu` y `MenuItem`:
- `MenuItem` modela cada elemento del menú, incluyendo sus ingredientes y costo.
- `Menu` proporciona la lista de bebidas disponibles y métodos para obtener detalles de las bebidas.

### `money_machine.py`
Contiene la clase `MoneyMachine`, que gestiona:
- Procesar las monedas insertadas por el usuario.
- Comprobar si el pago es suficiente.
- Devolver el cambio y actualizar las ganancias.

## 🤝 Contribuciones

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio 🍴.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`) 🌿.
3. Realiza tus cambios y haz commit de los mismos (`git commit -m 'Añadir nueva característica'`) ✨.
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`) 🚀.
5. Abre un Pull Request 📬.
