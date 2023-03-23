#ifndef CONSOLA_H
#define CONSOLA_H

#include <string>

using namespace std;

class Consola {
public:
    Consola();
    void mostrarMenu();
    string obtenerComando();
    void mostrarMensaje(string mensaje);
};

#endif /* CONSOLA_H */