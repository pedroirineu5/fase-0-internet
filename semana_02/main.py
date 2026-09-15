
def soma(num1, num2, num3 = None):
    if num3 is not None:
        return num1 + num2 + num3
    else: 
        return num1 + num2

resultado = soma(1,3)
print(resultado)
