from xmlrpc.server import SimpleXMLRPCServer,SimpleXMLRPCRequestHandler

class MyRequestHandler(SimpleXMLRPCRequestHandler):
    def log_request(self, code='-', size='-'):
        mensaje = 'El cliente ejecuto un comando'
        SimpleXMLRPCRequestHandler.log_message(self, mensaje)

class MyServer(SimpleXMLRPCServer):
    def __init__(self, *args, **kwargs):
        self.quit = 0
        kwargs["requestHandler"] = MyRequestHandler
        SimpleXMLRPCServer.__init__(self, *args, **kwargs)
    
    def serve_forever(self):
        while not self.quit:
            self.handle_request()

class Servidor(SimpleXMLRPCServer):
    def __init__(self,_robot,_archivo):
        self.servidor=MyServer(("localhost", 8000),requestHandler=MyRequestHandler, allow_none=True)
        self.robot=_robot
        self.archivo=_archivo

    def decodificar(self,comando):
        comando= comando.split(" ")
        comando.pop(0)
        args = comando[0].split(",")
        return args

    def saludar(self):
        mensaje = "Conexión establecida"
        print(mensaje)
        return mensaje
    
    def kill(self):
        self.servidor.quit = 1
        self.servidor.server_close()
        return 1
    
    def encenderRobot(self):
        return(self.robot.encenderRobot())
    def apagarRobot(self):
        return(self.robot.apagarRobot())
    def verEstado(self):
        return(self.robot.verEstado())
    def home(self):
        return(self.robot.home())
    def activarEfector(self):
        return(self.robot.activarEfector())
    def desactivarEfector(self):
        return(self.robot.desactivarEfector())
    def moverRobot(self,comando):
        args=self.decodificar(comando)
        return(self.robot.moverRobot(args))
    def rotarRobot(self,comando):
        args=self.decodificar(comando)
        return(self.robot.rotarRobot(args))
    def reproducirGrabacion(self,comando):
        comando=self.decodificar(comando)
        return(self.archivo.reproducirGrabacion(comando[0]))
    def verReporte(self):
        return(self.archivo.verReporte())
        
    
    def iniciar(self):
        self.servidor.register_function(self.saludar, "saludar")
        self.servidor.register_function(self.kill, "kill")
        self.servidor.register_function(self.encenderRobot, "encenderRobot")
        self.servidor.register_function(self.apagarRobot, "apagarRobot")
        self.servidor.register_function(self.verEstado, "verEstado")
        self.servidor.register_function(self.home, "home")
        self.servidor.register_function(self.activarEfector, "activarEfector")
        self.servidor.register_function(self.desactivarEfector, "desactivarEfector")
        self.servidor.register_function(self.moverRobot, "moverRobot")
        self.servidor.register_function(self.rotarRobot, "rotarRobot")
        self.servidor.register_function(self.reproducirGrabacion, "reproducirGrabacion")
        self.servidor.register_function(self.verReporte, "verReporte")
        self.servidor.serve_forever()