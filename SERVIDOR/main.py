from robot import Robot
from archivos import Archivo
from validador import Validador
from controlador import Controlador
from consola import Consola
import datetime

def main():
    robot = Robot()
    tiempoInicial = datetime.datetime.now()
    archivo = Archivo(tiempoInicial)
    archivo.estadoReporte=True
    validador = Validador()
    controlador = Controlador(robot,archivo,validador)
    consola= Consola(controlador)
    consola.cmdloop()

if __name__ == "__main__":
    main()