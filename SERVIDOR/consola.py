from cmd import Cmd

class Consola(Cmd):

    doc_header = (
        "Ayuda de comandos (escriba 'help <comando>' para obtener mas información)"
    )
    prompt = ">> "

    def __init__(self,_controlador):
        Cmd.__init__(self)
        self.controlador = _controlador

    def precmd(self, args):
        args = args.lower()
        return args

    def preloop(self):
        print(
            "Iniciando entrada de comandos...\nUtilice el comando 'help' para obtener ayuda del sistema."
        )

    def default(self, args):
        print('\nComando " ' + args + '"  no encontrado\n')

    def do_robot(self, args):
        """\nAccede al menu de control del robot\n"""
        menurobot = menuRobot(self.controlador)
        menurobot.cmdloop()
    
    def do_archivo(self, args):
        """\nAccede al menu de archivos\n"""
        menuarchivo = menuArchivo(self.controlador)
        menuarchivo.cmdloop()
    
    def do_servidor(self, args):
        """\nInicia o apaga el servidor, utilice \'servidor [on/off]\'\n"""
        print("Servidor iniciando...")
        self.controlador.iniciarServidor()
        print("Conexion terminada")
        

    def do_salir(self, args):
        """\nFinaliza el programa\n"""
        raise SystemExit

class menuRobot(Cmd):

    prompt = "ROBOT>> "

    def __init__(self,_controlador):
        Cmd.__init__(self)
        self.controlador = _controlador

    def precmd(self, args):
        args = args.lower()
        return args

    def default(self, args):
        print('\nComando " ' + args + '"  no encontrado\n')

    def do_encender(self, args):
        """\nEnciende el robot\n"""
        print(self.controlador.encenderRobot())
    
    def do_apagar(self, args):
        """\nApaga el robot\n"""
        print(self.controlador.apagarRobot())

    def do_estado(self, args):
        """\nMuestra el estado del robot\n"""
        print(self.controlador.verEstado())
    
    def do_home(self, args):
        """\nVuelve al home\n"""
        print(self.controlador.home())
    
    def do_efector(self, args):
        """\nActiva o desactiva el efector, utilice efector [on/off] \n"""
        try:
            if args == "on":
                print(self.controlador.activarEfector())
            elif args == "off":
                print(self.controlador.desactivarEfector())
            else:
                print("Argumento invalido")
        except Exception as error:
            print(error)

    def do_mover(self, args):
        """\nMueve el robot a la posicion indicada, utilice mover [X,Y,Z,velocidad]\n"""
        comando = args
        args = args.split(",")
        try:
            print(self.controlador.moverRobot(comando,args))
        except Exception as error:
            print(error)

    def do_rotar(self, args):
        """\nRota un vinculo del robot un angulo indicado, utilice rotar [vinculo,angulo,sentido,velocidad]\n"""
        comando = args
        args = args.split(",")
        try:
            print(self.controlador.rotarRobot(comando,args))
        except Exception as error:
            print(error)

    def do_volver(self, args):
        """\nVuelve al menu principal\n"""
        return Consola

    def do_salir(self, args):
        """\nFinaliza el programa\n"""
        raise SystemExit
    
class menuArchivo(Cmd):

    prompt = "ARCHIVO>> "

    def __init__(self,_controlador):
        Cmd.__init__(self)
        self.controlador = _controlador

    def precmd(self, args):
        args = args.lower()
        return args

    def default(self, args):
        print('\nComando " ' + args + '"  no encontrado\n')

    def do_iniciar(self, args):
        """\nInicia la grabacion de una rutina\n"""
        print(self.controlador.iniciarGrabacion())
    
    def do_detener(self, args):
        """\nDetiene la grabacion de una rutina y guarda el archivo, utilice detener [nombre_archivo]\n"""
        print(self.controlador.detenerGrabacion(args))
    
    def do_borrar(self, args):
        """\nLimpia la grabacion\n"""
        print(self.controlador.limpiarGrabacion())
    
    def do_reproducir(self, args):
        """\nReproduce un archivo, utilice reproducir [nombre_archivo]\n"""
        try:
            print(self.controlador.reproducirGrabacion(args))
        except Exception as error:
            print(error)
    
    def do_reporte(self, args):
        """\nGenera un reporte de la rutina\n"""
        reporte=self.controlador.verReporte()
        for linea in reporte:
            print(linea)

    def do_volver(self, args):
        """\nVuelve al menu principal\n"""
        return Consola

    def do_salir(self, args):
        """\nFinaliza el programa\n"""
        raise SystemExit