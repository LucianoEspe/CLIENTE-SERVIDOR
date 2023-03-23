from servidor import Servidor
import datetime
class Controlador():
    def __init__(self,_robot,_archivo,_validador):
        self.robot = _robot
        self.archivo=_archivo
        self.validador=_validador

    def decodificar(self,_ordenes):
        for i in _ordenes:
                print(i)
                if i[0] == "A":
                    if i[2] == "1":
                        self.encenderRobot()
                    elif i[2] == "0":
                        self.apagarRobot()
                elif i[0] == "H":
                    self.home()
                elif i[0] == "E":
                    if i[2] == "1":
                        self.activarEfector()
                    elif i[2] == "0":
                        self.desactivarEfector()
                elif i[0] == "M":
                    datos = i.split(" ")
                    datos.pop(0)
                    self.robot.moverRobot(datos)
                elif i[0] == "R":
                    datos = i.split(" ")
                    datos.pop(0)
                    self.robot.rotarRobot(datos)
                else:
                    pass

    def encenderRobot(self):
        if self.archivo.estadoGrabacion:
            self.robot.encenderRobot()
            self.archivo.grabacion.append("A 1")
            return "Robot encendido"
        elif self.archivo.estadoReporte:
            self.robot.encenderRobot()
            self.archivo.datos.append("A 1")
            self.archivo.tiempos.append(datetime.datetime.now())
            return "Robot encendido"
        else:
            self.robot.encenderRobot()
            return "Robot encendido"
    
    def apagarRobot(self):
        if self.archivo.estadoGrabacion:
            self.robot.apagarRobot()
            self.archivo.grabacion.append("A 0")
            return "Robot apagado"
        elif self.archivo.estadoReporte:
            self.robot.apagarRobot()
            self.archivo.datos.append("A 0")
            self.archivo.tiempos.append(datetime.datetime.now())
            return "Robot apagado"
        else:
            self.robot.apagarRobot()
            return "Robot apagado"
    
    def home(self):
        if self.archivo.estadoGrabacion:
            self.robot.home()
            self.archivo.grabacion.append("H")
            return "Robot en home"
        elif self.archivo.estadoReporte:
            self.robot.home()
            self.archivo.datos.append("H")
            self.archivo.tiempos.append(datetime.datetime.now())
            return "Robot en home"
        else:
            self.robot.home()
            return "Robot en home"

    def activarEfector(self):
        if self.archivo.estadoGrabacion:
            self.robot.activarEfector()
            self.archivo.grabacion.append("E 1")
            return "Efector activado"
        elif self.archivo.estadoReporte:
            self.robot.activarEfector()
            self.archivo.datos.append("E 1")
            self.archivo.tiempos.append(datetime.datetime.now())
            return "Efector activado"
        else:
            self.robot.activarEfector()
            return "Efector activado"

    def desactivarEfector(self):
        if self.archivo.estadoGrabacion:
            self.robot.desactivarEfector()
            self.archivo.grabacion.append("E 0")
            return "Efector desactivado"
        elif self.archivo.estadoReporte:
            self.robot.desactivarEfector()
            self.archivo.datos.append("E 0")
            self.archivo.tiempos.append(datetime.datetime.now())
            return "Efector desactivado"
        else:
            self.robot.desactivarEfector()
            return "Efector desactivado"

    def moverRobot(self,_comando,_argumentos):
        self.validador.validarLineal(_comando)
        if self.archivo.estadoGrabacion:
            self.robot.moverRobot(_argumentos)
            self.archivo.grabacion.append("M "+_argumentos[0]+" "+_argumentos[1]+" "+_argumentos[2]+" "+_argumentos[3])
            return "El robot se movio a la posicion: X:"+_argumentos[0]+" Y:"+_argumentos[1]+" Z:"+_argumentos[2]+" con velocidad: "+_argumentos[3]
        elif self.archivo.estadoReporte:
            self.robot.moverRobot(_argumentos)
            self.archivo.datos.append("M "+_argumentos[0]+" "+_argumentos[1]+" "+_argumentos[2]+" "+_argumentos[3])
            self.archivo.tiempos.append(datetime.datetime.now())
            return "El robot se movio a la posicion: X:"+_argumentos[0]+" Y:"+_argumentos[1]+" Z:"+_argumentos[2]+" con velocidad: "+_argumentos[3]
        else:
            self.robot.moverRobot(_argumentos)
            return "El robot se movio a la posicion: X:"+_argumentos[0]+" Y:"+_argumentos[1]+" Z:"+_argumentos[2]+" con velocidad: "+_argumentos[3]

    def rotarRobot(self,_comando,_argumentos):
        self.validador.validarRotacion(_comando)
        if self.archivo.estadoGrabacion:
            self.robot.rotarRobot(_argumentos)
            self.archivo.grabacion.append("R "+str(_argumentos[0])+" "+str(_argumentos[1])+" "+str(_argumentos[2])+" "+str(_argumentos[3]))
            return "El vinculo "+str(_argumentos[0])+" roto "+str(_argumentos[1])+"° en sentido "+str(_argumentos[2])+" y con velocudad angular "+str(_argumentos[3])
        elif self.archivo.estadoReporte:
            self.robot.rotarRobot(_argumentos)
            self.archivo.datos.append("R "+str(_argumentos[0])+" "+str(_argumentos[1])+" "+str(_argumentos[2])+" "+str(_argumentos[3]))
            self.archivo.tiempos.append(datetime.datetime.now())
            if _argumentos[2] == "h":
                _argumentos[2] = "horario"
            else:
                _argumentos[2] = "antihorario"   
            return "El vinculo "+str(_argumentos[0])+" roto "+str(_argumentos[1])+"° en sentido "+str(_argumentos[2])+" y con velocudad angular "+str(_argumentos[3])
        else:
            self.robot.rotarRobot(_argumentos)
            if _argumentos[2] == "h":
                _argumentos[2] = "horario"
            else:
                _argumentos[2] = "antihorario"   
            return "El vinculo "+str(_argumentos[0])+" roto "+str(_argumentos[1])+"° en sentido "+str(_argumentos[2])+" y con velocudad angular "+str(_argumentos[3])


    def verEstado(self):
        return(self.robot.verEstado())
    
    def iniciarGrabacion(self):
        self.archivo.iniciarGrabacion()
        return("Grabacion iniciada")

    def detenerGrabacion(self,_nombre):
        self.archivo.detenerGrabacion(_nombre)
        return("Grabacion detenida")
    
    def limpiarGrabacion(self):
        self.archivo.limpiarGrabacion()
        return("Grabacion limpiada")
    
    def reproducirGrabacion(self,_nombre):
        self.encenderRobot()
        self.home()
        ordenes=self.archivo.reproducirGrabacion(_nombre)
        self.decodificar(ordenes)
        return("Repoduciendo secuencia")
        
    def verReporte(self):
        return(self.archivo.verReporte())
    def iniciarServidor(self):
        servidor = Servidor(self.robot,self.archivo)
        servidor.iniciar()