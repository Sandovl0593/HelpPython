"""Un ejemplo del uso del paquete 'cmd':
-- Personalizacion de objetos que genera un framework con el soporte
de interpretes en la interfaz de linea de comandos"""
import cmd

def parse(arg):
    'Convierte los argumentos en una tupla de números'
    return tuple(map(int, arg.split()))

def identify(arg, number):
    if len(arg) == 1:
        return number, int(arg)
    return parse(arg)

class Operator(cmd.Cmd):
    intro = "Calculator progresivo, tipear ? para mas información\n"
    prompt = "-Escribe.- "
    number = 0

    def do_sum(self, args):
        "Realiza la suma de dos números, decir: SUM"
        num1, num2 = identify(args, self.number)
        self.number = num1 + num2
        print("Suma: %d\n" %(self.number) )

    def do_rest(self, args):
        "Realiza la resta de dos números, decir: REST"
        num1, num2 = identify(args, self.number)
        self.number = num1 - num2
        print("Resta: %d\n" %(self.number) )

    def do_mult(self, args):
        "Realiza la multiplicación de dos números, decir: MULT"
        num1, num2 = identify(args, self.number)
        self.number = num1 * num2
        print("Producto: %d\n" %(self.number) )
    
    def do_div(self, args):
        "Realiza la división de dos números, decir: DIV"
        num1, num2 = identify(args, self.number)
        self.number = num1 // num2
        print("Cociente: %d\n" %(self.number) )

    def do_EOF(self, args):
        "Finaliza la ejecución, pulsar: Crt + Z"
        print(f"Resultado final: {self.number}")
        return True

if __name__ == "__main__":
    Operator().cmdloop()