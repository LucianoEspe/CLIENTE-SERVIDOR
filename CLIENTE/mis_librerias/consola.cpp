#include "consola.h"
#include <iostream>

using namespace std;

Consola::Consola() {}

void Consola::mostrarMenu() {
    cout << "Bienvenido al sistema de control de robot" << endl;
    cout << "Escriba help para ver los comandos disponibles" << endl;
}

string Consola::obtenerComando() {
    string comando;
    cout << ">> ";
    getline(cin, comando);
    return comando;
}

void Consola::mostrarMensaje(string mensaje) {
    cout << mensaje << endl;
}