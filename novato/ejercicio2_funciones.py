def message(m="default message"):
    print(m)   

message() 
message("esto si")    #identico a cualquier lenguaje programacion


def address(street, city, postal_code):
    print("Tu dirección es:", street, city, postal_code)

#s = input("Calle: ")
#p_c = input("Código Postal: ")
#c = input("Ciudad: ")
#address(s, c, p_c)


a = 'holaa variable global'  #funciona exactamente igual que todos los lenguajes
def hola(a):
    a = "propio escope"
    print(a)
    
hola("jelouu")
print(a)


#Implementación recursiva de la función factorial. Tambien funciona igual que otro lenguaje

def factorial(n):
    if n == 1:    # El caso base (condición de terminación).
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))
