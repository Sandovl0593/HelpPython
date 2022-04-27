"Un ejemplo del uso del paquete 'array'"
import array

cater = input("Una frase: ")

def distLetters(frase):
    for palabar in frase.split():
        arr = array.array("u", palabar)
    print("Orden de letras:", sorted(arr.tolist()))
    
def comparacion(frase):
    i = 0
    for palabra in frase.split():
        arr = array.array("u", palabra)
        bits = str(arr.tobytes())
        for let in bits:
            if let == '0':
                i+=1
    
    if len("".join(palabra for palabra in frase.split())) >= round(i/2):
        print("The phrase is very cool in bits")
    else:
        print("The phrase has low coolness cool in bits")