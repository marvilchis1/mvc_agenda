from model.model import Model
from view.view import View

class Controller:
    #Constructor
    def __init__(self):
        self.model = Model()
        self.view = View()

    #Contracto controllers
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        b, c = self.model.agregar_contacto(id_contacto, nombre, tel, correo, dir)
        if b:
            self.view.crear_contacto(c)
        else:
            self.view.contacto_ya_existe(c)

    def leer_contacto(self, id_contacto):
        e, c = self.model.leer_contacto(id_contacto)
        if e:
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_todos_contactos(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)

    def actualizar_contacto(self, id_contacto, n_nombre = '', n_tel = '', n_correo = '', n_dir = ''):
        e = self.model.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_dir)
        
        if e:
            self.view.actualizar_contacto(id_contacto)
        else:
            self.view.contacto_no_existen(id_contacto)

    def borrar_contacto(self, id_contacto):
        e, c = self.model.borrar_contacto(id_contacto)
        
        if e:
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)
            

    def leer_contactos_letra(self, letra):
        c = self.model.leer_contactos_letra(letra)
        self.view.mostrar_contactos(c)
    

    # Citas
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        pass

    def leer_cita(self, id_cita):
        pass

    def actualizar_cita(self, id_cita, id_contacto, n_lugar, n_fecha, n_hora, n_asunto):
        pass

    def borrar_cita(self, id_cita):
        pass


    def insertar_contactos(self):
        self.agregar_contacto(1, 'Juan Perez', '464-123-1234', 'jp@gmail.com', 'Arteaga No. 5, San Miguel, Salamanca')
        self.agregar_contacto(2, 'Amanda Leon', '464-987-1234', 'al@gmail.com', 'Villapaldo No.9 Paraiso, Celaya')
        self.agregar_contacto(3, 'Jessica Mendoza', '461-912-1234', 'jm@gmail.com', 'Girasol No.12 Manzanos, Guanajuato')

    def insertar_citas(self): 
        self.agregar_cita(1, 1, 'Starbucks', '18-03-2020', '19:00', 'Break del trabajo')
        self.agregar_cita(1, 3, 'Cinepolis', '02-03-2020', '14:00', 'Pelicula Mulan')
        self.agregar_cita(1, 2, 'DICIS', '16-04-2020', '12:00', 'Clase de programacion')
        self.agregar_cita(1, 3, 'Soriana', '30-04-2020', '15:00', 'Compras para la fiesta')
        self.agregar_cita(1, 2, 'McDonalds', '19-03-2020', '16:00', 'Comida con Amanda')

    #Cita controllers
    def start(self):
        #Display a welcome message
        self.view.start()
        #Insert data in model
        self.insertar_contactos()
        self.insertar_citas()
        # Show all contacts in DB
        self.leer_todos_contactos()
        self.leer_contactos_letra('a')

    def menu(self):
        #Display menu
        self.view.menu()
        o = input('Seleciona una opcion (1-9)')
        if o == '1':
            id_con = input('ID Contacto: ')
            nombre = input('Nombre: ')
            tel = input('Telefono: ')
            correo = input('Correo: ')
            dire = input('Direccion: ')
            self.agregar_contacto(id_con, nombre, tel, correo, dire)

        elif o == '2':
            id_con = input('ID Contacto: ')
            self.leer_contacto(id_con)
            
        elif o == '3':
            id_con = input('ID Contacto: ')
            nombre = input('Nombre: ')
            tel = input('Telefono: ')
            correo = input('Correo: ')
            dire = input('Direccion: ')
            self.actualizar_contacto(id_con, nombre, tel, correo, dire)
    
        elif o == '4':
            pass

        elif o == '5':
            pass
        elif o == '6':
            pass
        elif o == '7':
            pass
        elif o == '8':
            pass
        elif o == '9':
            self.view.end()
        
        else:
            self.view.opcion_no_valida()
