#pragma once

#include <iostream>
#include <stdlib.h>
#include <cstring>
#include <sstream>
#include "../xmlrpc/XmlRpc.h"

using namespace std;
using namespace XmlRpc;

class Controlador {
private:
    XmlRpcClient cliente;
    XmlRpcValue saludar,kill,estado, tresArgs, cuatroArgs, respuesta;

public:
    Controlador(int port);

    void conectar();

    void apagar_cliente();

    void encenderRobot();

    void apagarRobot();

    void verEstado();

    void home();

    void activarEfector();

    void desactivarEfector();

    void moverRobot(string comando);

    void rotarRobot(string comando);

    void reproducirGrabacion(string comando);

    void verReporte();
};