import datetime
import time
import os

class Archivo:
    def __init__(self,_tiempo):
        self.grabacion = []
        self.estadoGrabacion = False
        self.tiempoInicial=_tiempo
        self.inicio=time.time()
        self.estadoReporte=False
        self.datos=[]
        self.tiempos=[]
    
    def crearArchivo(self,_nombre):
        if not self.estadoGrabacion:
            archivo = open(_nombre,"w")
            for i in self.grabacion:
                archivo.write(i + "\n")
            archivo.close()
        else:
            pass

    def iniciarGrabacion(self):
        if not self.estadoGrabacion:
            self.estadoGrabacion = True
            return(str("G 1"))
        else:
            pass

    def detenerGrabacion(self, _nombre):
        _nombre = _nombre + ".txt"
        if self.estadoGrabacion:
            self.estadoGrabacion = False
            self.crearArchivo(_nombre)
            return(str("G 0"))
        else:
            pass
    
    def limpiarGrabacion(self):
        if not self.estadoGrabacion:
            self.grabacion = []
        else:
            pass
    
    def reproducirGrabacion(self,_nombre):
        _nombre = _nombre + ".txt"
        if not self.estadoGrabacion:
            ordenes = []
            try:
                with open(_nombre) as f:
                    ordenes = f.readlines()
                ordenes = [elemento for elemento in ordenes if elemento]
                ordenes=[elemento.strip() for elemento in ordenes]
            except:
                raise Exception("No existe el archivo")
            return ordenes
        else:
            raise Exception("No se puede reproducir una grabacion mientras se esta grabando")
    
    def crearReporte(self):
        indice=0
        fin=time.time()
        self.estadoReporte=True
        reporte = open("Reporte.xml","w")
        reporte.write("<Reporte>\n")
        reporte.write("  <Inicio>"+str(self.tiempoInicial)+"</Inicio>\n")
        for i in self.datos:
            if i[0] == "A":
                if i[2]=="1":
                    reporte.write("\t<Robot>\n"+"\t\t<Estado>Encendido</Estado>\n"+"\t</Robot>\n")
                    reporte.write("\t<Tiempo>"+str(self.tiempos[indice])+"</Tiempo>\n")
                    indice+=1
                elif i[2]=="0":
                    reporte.write("\t<Robot>\n"+"\t\t<Estado>Apagado</Estado>\n"+"\t</Robot>\n")
                    reporte.write("\t<Tiempo>"+str(self.tiempos[indice])+"</Tiempo>\n")
                    indice+=1
            elif i[0] == "G":
                if i[2]=="1":
                    reporte.write("\t<Grabacion>\n"+"\t\t<Estado>Activado</Estado>\n"+"\t</Grabacion>\n")
                    reporte.write("\t<Tiempo>"+str(self.tiempos[indice])+"</Tiempo>\n")
                    indice+=1
                elif i[2]=="0":
                    reporte.write("\t<Grabacion>\n"+"\t\t<Estado>Desactivado</Estado>\n"+"\t</Grabacion>\n")
                    reporte.write("\t<Tiempo>"+str(self.tiempos[indice])+"</Tiempo>\n")
                    indice+=1
            
            elif i[0] == "H":
                reporte.write("\t<Home>\n"+"\t\t<X>0</X>\n"+"\t\t<Y>0</Y>\n"+"\t\t<Z>0</Z>\n"+"\t</Home>\n")
                reporte.write("\t<Tiempo>"+str(self.tiempos[indice])+"</Tiempo>\n")
                indice+=1
            elif i[0] == "E":
                if i[2]=="1":
                    reporte.write("\t<Efector>\n"+"\t\t<Estado>Activado</Estado>\n"+"\t</Efector>\n")
                    reporte.write("\t<Tiempo>"+str(self.tiempos[indice])+"</Tiempo>\n")
                    indice+=1
                elif i[2]=="0":
                    reporte.write("\t<Efector>\n"+"\t\t<Estado>Desactivado</Estado>\n"+"\t</Efector>\n")
                    reporte.write("\t<Tiempo>"+str(self.tiempos[indice])+"</Tiempo>\n")
                    indice+=1
            elif i[0] == "M":
                self.datos = i.split(" ")
                reporte.write("\t<Movimiento>\n"+"\t\t<X>"+self.datos[1]+"</X>\n"+"\t\t<Y>"+self.datos[2]+"</Y>\n"+"\t\t<Z>"+self.datos[3]+"</Z>\n"+"\t\t<Velocidad>"+self.datos[4]+"</Velocidad>\n"+"\t</Movimiento>\n")
                reporte.write("\t<Tiempo>"+str(self.tiempos[indice])+"</Tiempo>\n")
                indice+=1
            elif i[0] == "R":
                self.datos = i.split(" ")
                if self.datos[1]=="1":
                    reporte.write("\t<Rotacion>\n"+"\t\t<Vinculo>1</Vinculo>\n"+"\t\t<Angulo>"+self.datos[2]+"</Angulo>\n"+"\t\t<Sentido>"+self.datos[3]+"</Sentido>\n"+"\t\t<Velocidad>"+self.datos[4]+"</Velocidad>\n"+"\t</Rotacion>\n")
                    reporte.write("\t<Tiempo>"+str(self.tiempos[indice])+"</Tiempo>\n")
                    indice+=1
                elif self.datos[1]=="2":
                    reporte.write("\t<Rotacion>\n"+"\t\t<Vinculo>2</Vinculo>\n"+"\t\t<Angulo>"+self.datos[2]+"</Angulo>\n"+"\t\t<Sentido>"+self.datos[3]+"</Sentido>\n"+"\t\t<Velocidad>"+self.datos[4]+"</Velocidad>\n"+"\t</Rotacion>\n")
                    reporte.write("\t<Tiempo>"+str(self.tiempos[indice])+"</Tiempo>\n")
                    indice+=1
                elif self.datos[1]=="3":
                    reporte.write("\t<Rotacion>\n"+"\t\t<Vinculo>3</Vinculo>\n"+"\t\t<Angulo>"+self.datos[2]+"</Angulo>\n"+"\t\t<Sentido>"+self.datos[3]+"</Sentido>\n"+"\t\t<Velocidad>"+self.datos[4]+"</Velocidad>\n"+"\t</Rotacion>\n")
                    reporte.write("\t<Tiempo>"+str(self.tiempos[indice])+"</Tiempo>\n")
                    indice+=1
        reporte.write("  <Fin>"+str(datetime.datetime.now())+"</Fin>\n")
        elapsed_time = int(fin - self.inicio)
        time_format = datetime.timedelta(seconds=elapsed_time)
        time_str = str(time_format)
        split_time = time_str.split(":")
        reporte.write("  <Tiempo total>"+split_time[0]+" horas "+split_time[1]+" minutos "+split_time[2]+" segundos"+"</Tiempo total>\n")
        reporte.write("</Reporte>\n")
        reporte.close()

    def verReporte(self):
        if os.path.isfile("Reporte.xml"):
            respuesta=[]
            reporte = open("Reporte.xml","r")
            for linea in reporte:
                respuesta.append(linea)
            reporte.close()
            return respuesta
        else:
            self.crearReporte()
            respuesta=[]
            reporte = open("Reporte.xml","r")
            for linea in reporte:
                respuesta.append(linea)
            reporte.close()
            return respuesta