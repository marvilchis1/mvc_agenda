class View:
    # Contactos
    def mostrar_contacto(self, contacto):
        print('********** Datos del contacto ***********')
        print('Nombre: ', contacto.nombre)
        print('Telefono: ', contacto.tel)
        print('Correo: ', contacto.correo)
        print('Direccion:', contacto.dir)
        print('*****************************************')

    def mostrar_contactos(self, contactos):
        print('******** Contactos Definidos ************')
        for c in contactos:
            print(c.nombre, c.tel, c.correo, c.dir)
        print('*****************************************')

    def crear_contacto(self, contacto):
        print(contacto.nombre,'se ha agregado a la base de datos')

    def borrar_contacto(self, contacto):
        print(contacto.nombre,'se ha borrado de la base de datos')

    def actualizar_contacto(self, contacto_o, contacto_n):
        print(contacto_o.nombre, 'se ha modificado correctamente')

    def contacto_ya_existe(self, contacto):
        print(contacto.id_contacto, 'YA EXISTE EN LA BASE DE DATOS')

    def contacto_no_existe(self, id_contacto):
        print(id_contacto, 'NO EXISTE EN LA BASE DE DATOS')

    def start(self):
        print('Esto es un ejemplo de vista sencilla')

    def end(self):
        print('Hasta la vista!')

    # Citas

    def mostrar_cita(self, cita):
        print('********** Datos de la cita ***********')
        print('ID contacto: ', cita.id_contacto)
        print('Lugar: ', cita.id_lugar)
        print('Fecha: ', cita.fecha)
        print('Hora:', cita.hora)
        print('*****************************************')
    
    def mostrar_citas(self, citas):
        print('********** Citas definidas ***********')
        for d in citas:
            print(d.id_contacto, d.lugar, d.fecha, d.hora, d.asunto)
        print('**************************************')

    def crear_cita(self, cita):
        print(cita.fecha, cita.asunto, 'se ha agregado a la base de datos')

    def borrar_cita(self, cita):
        print(cita.fecha, cita.asunto, 'se ha borrado de la base de datos')
    
    def modificar_cita(self, cita):
        print(cita.fecha, cita.asunto, 'se ha modificado correctamente')

    def cita_ya_existe(self, cita):
        print(cita.id_cita, 'YA EXISTE EN LA BASE DE DATOS')

    def cita_no_existe(self, cita):
        print(cita.id_cita, 'NO EXISTE EN LA BASE DE DATOS')

    def menu(self):
        print('1. Agregar contacto')
        print('2. Buscar contacto')
        print('3. Actualizar contacto')
        print('4. Borrar contacto')
        print('5. Crear cita')
        print('6. Buscar cita')
        print('7. Modificar cita')
        print('8. Borrar cita')

    def opcion_no_valida(self):
        print('Opcion no valida')