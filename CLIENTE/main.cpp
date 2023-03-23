#include <iostream>
#include <stdlib.h>
#include <cstring>
#include <vector>
#include <sstream>
#include <cctype>
#include "xmlrpc/XmlRpc.h"
#include "mis_librerias/controlador.h"
#include "mis_librerias/consola.h"
using namespace std;
using namespace XmlRpc;

int main() {
    bool estado = true;
    Controlador controlador(8000);
    Consola consola;

    consola.mostrarMenu();

    string comando;
    while (estado) {
        comando = consola.obtenerComando();

        if (comando == "help") {
            consola.mostrarMensaje("(C)onectar     (A)pagar");
            consola.mostrarMensaje("(EN)cender Robot  (AP)agar Robot");
            consola.mostrarMensaje("(M)over Robot  (EF)ector");
            consola.mostrarMensaje("(H)ome         (E)stado");
            consola.mostrarMensaje("(R)otar Robot  (V)er Reporte");
            consola.mostrarMensaje("(G)rabacion");
            consola.mostrarMensaje("(S)alir");
        }
        else if (comando == "conectar" || comando == "C" || comando == "c") {
            controlador.conectar();
        }
        else if (comando == "apagar" || comando == "A" || comando == "a") {
            controlador.apagar_cliente();
        }
        else if (comando == "encender robot" || comando == "EN" || comando == "en") {
            controlador.encenderRobot();
        }
        else if (comando == "apagar robot" || comando == "AP" || comando == "ap") {
            controlador.apagarRobot();
        }
        else if (comando == "estado" || comando == "E" || comando == "e") {
            controlador.verEstado();
        }
        else if (comando == "ver reporte" || comando == "V" || comando == "v") {
            controlador.verReporte();
        }
        else if (comando[0] == 'G' || comando[0] == 'g') {
            controlador.reproducirGrabacion(comando);
        }
        else if (comando[0] == 'M' || comando[0] == 'm') {
            controlador.moverRobot(comando);
        }
        else if (comando[0] == 'R' || comando[0] == 'r') {
            controlador.rotarRobot(comando);
        }
        else if (comando == "efector" || comando == "EF" || comando == "ef") {
            controlador.activarEfector();
        }
        else if (comando == "home" || comando == "H" || comando == "h") {
            controlador.home();
        }
        else if (comando == "salir" || comando == "S" || comando == "s") {
            estado = false;
        }
        else {
            cout << "Comando no reconocido. Escriba help para ver los comandos disponibles." << endl;
        }
    }

    cout << "Saliendo del sistema de control de robot." << endl;

    return 0;
}