import serial
import csv
import time

def configure_serial_connection(serial_port, baud_rate):
    """
    Esta función configura la comunicación seria con el arduino nano 33 ble sense

    Parameters:
    - serial_port (str): esto es el pin al que está conectado el arduino.
    - baud_rate (int): esto representa la velocidad de transmisión de datos en baudios.
    
    Return:
    - serial.Serial: devuelva la conexión configurada.
    """
    return serial.Serial(serial_port, baud_rate, timeout=1)

def read_serial_data(serial_connection):
    """
    Esta función lee los datos del serial monitor y los muestra como una lista.

    Parameters:
    - serial_connection (serial.Serial): esta conexión lee los datos.

    Return:
    - list: retorna los valores registrados en el serial monitor.
    """
    return serial_connection.readline().decode("utf-8").replace('\r', "").replace('\n', "").split(',')

def write_data_to_csv(data, csv_file):
    """
    Esta función toma los datos del serial monitor y los pasa a un archivo csv.

    Parameters:
    - data (list): toma las 6 coordenadas (aceleración y giroscopio) y los escribe en el csv.
    - csv_file (csv.writer): archivo donde se guardarán todos los movimientos realizados.
    """
    csv_file.writerow(data)

def main():
    """
    En la función main se hace la comunicación, leen los datos y se escriben en el csv.
    
    Parameters:
    - serial_port (str): nombre del dispositivo
    - baud_port (int): velocidad de transmisión
    - samples (int): cantidad de muestras por movimiento
    - archivo_csv (csv.writer): nombre archivo del movimiento actual
    - ser: configuración de la conexión.
    """
    serial_port = "/dev/ttyACM0"
    baud_rate = 9600
    primer_linea = ['aX', 'aY', 'aZ', 'gX', 'gY', 'gZ']
    samples = 1500
    archivo_csv = 'circle.csv'
    
    ser = configure_serial_connection(serial_port, baud_rate)
    print("NanoBLE 33 Sense conectado")

    with open(archivo_csv, 'w', newline='', encoding='UTF8') as file:
        writeFile = csv.writer(file)
        writeFile.writerow(primer_linea)

        counter = 0
        while counter < samples:
            movimiento = read_serial_data(ser)
            if len(movimiento) == 6:
                write_data_to_csv(movimiento, writeFile)
                counter += 1

if __name__ == "__main__":
    main()
