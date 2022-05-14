#include "dodecaedro.h"
#include <math.h>
// #include "pch.h"

float minor_rest(float num1, float num2) {
    float red;
    if (num1 < num2) {
        red = num2 - num1; }
    else {
        red = num1 - num2; }
    return red;
}

float med_Dodecaedro(float arista) {
    float apotema = 3 * sqrt(25 + 10 * sqrt(5)) * pow(arista, 2);
    float volumen = 0.25 * (15 + 7 * sqrt(5)) * pow(arista, 3);
    float respuest[2] = {apotema, volumen};
    return respuest[2];
}