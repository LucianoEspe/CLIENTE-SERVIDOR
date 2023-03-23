#include "controlador.h"

Controlador::Controlador(int port) : cliente("localhost", port) {}

void Controlador::conectar() {
    cout << "Estableciendo conexión..." << endl;
    cliente.execute("saludar",saludar, respuesta);
    cout << respuesta << endl;
}

void Controlador::apagar_cliente() {
    cout << "Cerrando conexión..." << endl;
    cliente.execute("kill", kill, respuesta);
}

void Controlador::encenderRobot() {
    XmlRpcValue encenderRobot;
    cliente.execute("encenderRobot", encenderRobot, respuesta);
    cout << respuesta << endl;
}

void Controlador::apagarRobot() {
    XmlRpcValue apagarRobot;
    cliente.execute("apagarRobot", apagarRobot, respuesta);
    cout << respuesta << endl;
}

void Controlador::verEstado() {
    cliente.execute("verEstado", estado, respuesta);
    cout << respuesta << endl;
}

void Controlador::home() {
    XmlRpcValue home;
    cliente.execute("home", home, respuesta);
    cout << respuesta << endl;
}

void Controlador::activarEfector() {
    XmlRpcValue activarEfector;
    cliente.execute("activarEfector", activarEfector, respuesta);
    cout << respuesta << endl;
}

void Controlador::desactivarEfector() {
    XmlRpcValue desactivarEfector;
    cliente.execute("desactivarEfector", desactivarEfector, respuesta);
    cout << respuesta << endl;
}

void Controlador::moverRobot(string comando) {
    XmlRpcValue posicionXml;
    posicionXml = comando;
    cliente.execute("moverRobot", posicionXml, respuesta);
    cout << respuesta << endl;
}

void Controlador::rotarRobot(string comando) {
    XmlRpcValue vinculosXml;
    vinculosXml = comando;
    cliente.execute("rotarRobot", vinculosXml, respuesta);
    cout << respuesta << endl;
}

void Controlador::reproducirGrabacion(string comando) {
    XmlRpcValue grabacionXml;
    grabacionXml = comando;
    cliente.execute("reproducirGrabacion", grabacionXml, respuesta);
    cout << respuesta << endl;
}

void Controlador::verReporte() {
    XmlRpcValue verReporte;
    cliente.execute("verReporte", verReporte, respuesta);
    //mostrar el reporte que tiene multilines
    for (int i = 0; i < respuesta.size(); i++) {
        cout << respuesta[i] << endl;
    }
}