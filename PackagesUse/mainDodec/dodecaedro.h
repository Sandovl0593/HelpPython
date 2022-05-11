#pragma once

#ifdef __dodecaedro
#endif // DODECAEDRO_H

extern "C" { 
	__declspec(dllexport) float minor_rest(float num1, float num2) {}
}

extern "C" { 
	__declspec(dllexport) float* med_Dodecaedro(int arista) {}
}

#ifdef __dodecaedro
#endif // DODECAEDRO_H