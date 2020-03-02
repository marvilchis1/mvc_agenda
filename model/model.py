from .contacto import Contacto
from .cita import Cita

class Model:
    
    def __init__(self):
        self.contactos = []
        self.citas = []

    #Contacto methods
    def esta_id_contacto(self, id_contacto):
        for c in self.contactos:
            if c.id_contacto == id_contacto:
                return True, c
        else:
            return False, 0

    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        if not self.esta_id_contacto(id_contacto)[0]:
            c = Contacto(id_contacto, nombre, tel, correo, dir)
            self.contactos.append(c)
            return True, c
        return False, c

    def leer_contacto(self, id_contacto):
        e, c = self.esta_id_contacto(id_contacto)
        return e, c
        
    def actualizar_contacto(self, id_contacto, n_nombre, n_tel, n_correo, n_dir):
        e, c = self.esta_id_contacto(id_contacto)
        if e:
            if n_nombre != '':
                c.nombre = n_nombre
            if n_tel != '':
                c.tel = n_tel
            if n_correo != '':
                c.correo = n_correo
            if n_dir != '':
                c.dir = n_dir
            return True
        return False

    def borrar_contacto(self, id_contacto):
        e, contacto = self.esta_id_contacto(id_contacto)
        if e:
            self.contactos.remove(contacto)
            lista_temp = [c for c in self.citas if c.id_contacto == id_contacto]

            for c in lista_temp:
                self.citas.remove(c)

            return True, contacto
        return False, 0

    def leer_todos_contactos(self):
        return self.contactos

    #Cita methods
    def esta_id_cita(self, id_cita):
        for d in self.citas:
            if d.id_cita == id_cita:
                return True, d
        else:
            return False, 0
    
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        if not self.esta_id_cita(id_cita)[0]:
            d = Cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
            self.citas.append(d)
            return True
        return False

    def leer_cita(self, id_cita):
        e, d = self.esta_id_cita(id_cita)
        if e:
            return d
        return False  

    def actualizar_cita(self, id_cita, id_contacto, n_lugar, n_fecha, n_hora, n_asunto):
        e, d = self.esta_id_cita(id_cita)
        if e:
            d.id_contacto = id_contacto
            d.lugar = n_lugar
            d.fecha = n_fecha
            d.hora= n_hora
            d.asunto = n_asunto
            return True
        return False

    def borrar_cita(self, id_cita):
        e, d = self.esta_id_cita(id_cita)
        if e:
            self.citas.remove(d)
            return True
        return False

# Busque contactos que empiecen con una letra y devuelva una lista de contactos (pedir letra)
    def leer_contactos_letra(self, letra):
        lista = [c for c in self.contactos if c.nombre.lower().startswith(letra.lower()) ]
        #lista = []
        #for c in self.contactos:
        #    if c.nombre[0].lower() == letra.lower():
            #if c.nombre.lower().startswith(letra):
        #        lista.append(c)       
        return lista

# Buscar las citas de las demas fechas (pedir fecha)

    def leer_citas_fecha(self, fecha):
        lista = [c for c in self.citas if c.fecha == fecha]
        #lista = []
        #for c in self.citas:
        #    if c.fecha == fecha:
        #        lista.append(c)
        return lista