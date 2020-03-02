from model.contacto import Contacto
from model.cita import Cita
from model.model import Model
from view.view  import View
from controller.controller import Controller

"""
contactos = []

c1 = Contacto(1, 'Juan Perez', '464-123-1234', 'jp@gmail.com', 'Arteaga No. 5, San Minguel, Salamanca')
c2 = Contacto(2, 'Amanda Leon', '464-987-1234', 'al@gmail.com', 'Villapaldo No.9 Paraiso, Celaya')
d = Cita(1, 1, 'Starbucks', '18-02-2020', '14:00', 'Reunion del trabajo')

contactos.append(c1)
contactos.append(c2)

#guess = input('Dame un nombre: ')
# Buscar si el nombre del contacto esta en la lista
# Imprimir 'sí está' o 'no está'

#for cont in contactos:
#    if (guess.lower() == cont.nombre.lower() ):
#        print('Si esta')
#        break
#    elif(guess != cont.nombre and cont == contactos[-1]):
#else:
#    print('No esta')
       
        



print(c1.id_contacto)
print(c1.nombre)
print(c1.tel)
print(c1.correo)
print(c1.dir)

print("\n\n")
print(d.id_cita)
print(d.id_contacto)
print(d.lugar)
print(d.fecha)
print(d.hora)
print(d.asunto)



m = Model()
m.agregar_contacto(1, 'Juan Perez', '464-123-1234', 'jp@gmail.com', 'Arteaga No. 5, San Minguel, Salamanca')
m.agregar_contacto(2, 'Amanda Leon', '464-987-1234', 'al@gmail.com', 'Villapaldo No.9 Paraiso, Celaya')

s = m.leer_contacto(2)
print(s.nombre)

#m.actualizar_contacto(2, 'Sarah Leon', '1234-123456','sl@gmail.com', 'Girasol No. 12, Jardines, Celaya' )
m.actualizar_contacto(2, 'Jessica Huerta')
s = m.leer_contacto(2)
print(s.nombre)


m.agregar_cita(1, 1, 'Starbucks', '18-02-2020', '14:00', 'Reunion del trabajo')
m.agregar_cita(2, 2, 'Cinepolis', '19-02-2020', '18:00', 'Pelicula de Sonic')


exe = m.leer_cita(1)
print(exe.asunto)

m.actualizar_cita(1, 1, 'Salon 310', '20-02-2020', '16:00', 'Clase de IS')
exe = m.leer_cita(1)
print(exe.asunto)

s = m.leer_todos_contactos()

for c in s:
    print(c.nombre, c.tel)

s = m.leer_contactos_letra('a')
for c in s:
    print(c.nombre, c.tel)

#x = m.borrar_contacto(2)
#print(x)


v = View()
s = m.leer_todos_contactos()
v.mostrar_contactos(s)

c = m.leer_contacto(2)
v.mostrar_contacto(c)

f, c = m.borrar_contacto(1)

if f: 
    v.borrar_contacto(c)

else:
    v.contacto_no_existe(1)

s = m.leer_todos_contactos()
v.mostrar_contactos(s)

print('\n\n\n')
s1 = m.leer
"""

cont = Controller()
cont.start()
cont.menu()
