from datetime import date

print('Hello, World!')
sum = 1 + 2 # 3
product = sum * 2
print(product)

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

print(type (planets_in_solar_system))
print(type (distance_to_alpha_centauri))
print(type (can_liftoff))

x = 2
x *=  2
print(x)

date.today()
print(date.today())
print("Today's date is: " + str(date.today()))


parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")


a = 55
b = 97
# test expression
if a < b:
    # statement to be run
    print(b)



a = 24
b = 44
if a <= 0:
    print(a)
print(b)


while True:
    print("1primer numero: ")
    a = input()
    print("1primer numero: ")
    b = input()
    if a < b:
        print("a is less than b")
    elif a > b:
       print("a is greater than b")
    else: 
        print ("a is equal to b")
        break
 
while True:
     print("Tamaño de objeto identificado:")
     objeto = int(input())
     if objeto >= 5:
         print("objeto identificado como peligroso para la nave")
     else:
        print("objeto descartado nave a salvo")
     print("Tienes mas objetos si / no")
     R = input()
     if R == "no":
     	    break
 