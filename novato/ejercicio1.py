import math;

a = 3.5
print(math.ceil(a));

n = 0
while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

for i in range(0, 3):
    print(i)
else:
    print(i, "else")
    
    
hat_list = [1, 2, 3, 4, 5]

# Paso 1
hat_list[2] = int(input("Ingresa un número entero: "))
del hat_list[-1]
print(hat_list)
print(len(hat_list))



my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)



# paso 1:
Beatles = []
print("Paso 1:", Beatles)

# paso 2:

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

Beatles.append("Nuevo miembro de la banda: ")
del Beatles[-1]
del Beatles[-1]

my_list = [8, 10, 6, 2, 4]
my_list.sort() #una vez que ejecutas una funcion tu lista original ya queda modificada esto cambia a javascript

list_1 = [1]
list_2 = list_1  ## apunta a list_1 en contra partida en javascript coge ese valor en ese momento
list_1[0] = 2
print(list_2)



my_list = [100, 80, 6, 4, 2]
new_list = my_list[:] #para copiarla entera si se omite un valor pilla el inicio y final
print(new_list)