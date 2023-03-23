class Robot:
    def __init__(self):
        self.posicion = [0, 0, 0]
        self.posicion_max = [50, 50, 50]
        self.posicion_min = [-50, -50, 0]
        self.velocidad_max = 60
        self.vinculos = [0, 0, 0]
        self.angulo_max = [90, 90, 90]
        self.angulo_min = [-90, 0, 0]
        self.vel_ang_max = 20
        self.efector = False
        self.estado = False
        self.ultimo_modo = "L"

    def encenderRobot(self):
        if not self.estado:
            self.estado = True
            self.home()
            return("A 1")
        else:
            pass
        
    def apagarRobot(self):
        if self.estado:
            self.estado = False
            return("A 0")
        else:
            pass

    def verEstado(self):
        if self.ultimo_modo == "R":
            return (
                "Vinculo 1: "
                + str(self.vinculos[0])
                + "°\nVinculo 2: "
                + str(self.vinculos[1])
                + "°\nVinculo 3: "
                + str(self.vinculos[2])
                + "°\nEfector: "
                + ("encendido" if self.efector else "apagado")
                if self.estado
                else "Robot apagado"
            )
        elif self.ultimo_modo == "L":
            return (
                "Posicion x: "
                + str(self.posicion[0])
                + "\nPosicion y: "
                + str(self.posicion[1])
                + "\nPosicion z: "
                + str(self.posicion[2])
                + "\nEfector: "
                + ("encendido" if self.efector else "apagado")
                if self.estado
                else "Robot apagado"
            )
        
    def home(self):
        if self.estado:
            self.vinculos = [0, 0, 0]
            self.posicion = [0, 0, 0]
            self.desactivarEfector()
            return("H")
        else:
            raise Exception("El robot esta apagado")
        
    def activarEfector(self):
        if self.estado:
            self.efector = True
            return("E 1")
        else:
            raise Exception("El robot esta apagado")

    def desactivarEfector(self):
        if self.estado:
            self.efector = False
            return("E 0")
        else:
            raise Exception("El robot esta apagado")

    def moverRobot(self, _argumentos):
        _argumentos = [int(i) for i in _argumentos]
        if self.estado:
            if _argumentos[0] > self.posicion_max[0] or _argumentos[0] < self.posicion_min[0]:
                raise Exception("Posicion x fuera de rango")
            if _argumentos[1] > self.posicion_max[1] or _argumentos[1] < self.posicion_min[1]:
                raise Exception("Posicion y fuera de rango")
            if _argumentos[2] > self.posicion_max[2] or _argumentos[2] < self.posicion_min[2]:
                raise Exception("Posicion z fuera de rango")
            if _argumentos[3] > self.velocidad_max:
                raise Exception("Velocidad fuera de rango")
            self.posicion = [_argumentos[0], _argumentos[1], _argumentos[2]]
            self.ultimo_modo = "L"
            return(str("M" + str(_argumentos[0]) + " " + str(_argumentos[1]) + " " + str(_argumentos[2]) + " " + str(_argumentos[3])))
        else:
            raise Exception("El robot esta apagado")

    def rotarRobot(self, _argumentos):
        for i in [0, 1, 3]:
            _argumentos[i] = int(_argumentos[i])
        if self.estado:
            if _argumentos[2]== "h":
                _angaux = _argumentos[1] + self.vinculos[_argumentos[0]-1]
            if _argumentos[2] == "a":
                _angaux = -_argumentos[1] + self.vinculos[_argumentos[0]-1]
            if _argumentos[3] > self.vel_ang_max:
                raise Exception("Velocidad fuera de rango")
            if _angaux > self.angulo_max[_argumentos[0]-1] or _angaux < self.angulo_min[_argumentos[0]-1]:
                raise Exception("Angulo fuera de rango")
            else:
                self.vinculos[_argumentos[0]-1] = _angaux
                self.ultimo_modo = "R"
            return(str("R " + str(_argumentos[0]) + " " + str(_argumentos[1]) + " " + str(_argumentos[2]) + " " + str(_argumentos[3])))
        else:
            raise Exception("El robot esta apagado")