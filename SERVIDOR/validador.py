import re
class Validador():
    def __init__(self):
        pass
    def validarLineal(self, _comando):
        patron= r'^-?\d{1,2},-?\d{1,2},-?\d{1,2},\d{1,2}$'
        if re.match(patron, _comando):
            pass
        else:
            raise ValueError("Debe ingresar cuatro valores numericos (dos digitos)")
    def validarRotacion(self,_comando):
        patron= r'^[1-3],\d{1,3},[ha],\-?[1-9]\d?$'
        if re.match(patron, _comando):
            pass
        else:
            raise ValueError("El comando no es valido")