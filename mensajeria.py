from abc import ABC, abstractmethod

class Notificacion(ABC):
    def __init__(self, mensaje, identificacion, nombre):
      self.mensaje = mensaje
      self.identificacion = identificacion
      self.nombre = nombre

    @abstractmethod
    def mostrar_info(self):
      pass

class SMS(Notificacion):
    
    sms_enviados = 0

    def __init__(self, mensaje, identificacion, nombre):
      super().__init__(mensaje, identificacion, nombre)

    def enviar_mensaje(self, num):
      sms_enviados += 1
      print(f"Enviando SMS al número {num}...")

  
class Email(Notificacion):
    
    email_enviados = 0

    def __init__(self, mensaje, identificacion, nombre, asunto, direccion_email):
      super().__init__(mensaje, identificacion, nombre)
      self.asunto = asunto
      self.direccion_email = direccion_email

    def enviar_mensaje(self):
      email_enviados += 1
      print(f"Enviando email con asunto: {self.asunto} a {self.direccion_email}...")


def main():
    
    metodo_envio = input("¿Qué método de envío quieres utilizar? SMS/Email: ").lower()
    mensaje = input("Escribe tu mensaje: ")
    identificacion = input("Introduce el codigo de identificacion: ")
    nombre = input("Introduce el nombre de usuario: ")
    
    match metodo_envio:
        case "sms":
            num_telefono = input("¿A qué número de teléfono quieres enviarlo: ")
            notificacion = SMS(mensaje, identificacion, nombre)
            notificacion.enviar_mensaje(num_telefono)

        case "email":
            direccion_email = input("Destinatario: ")
            asunto = input("Asunto: ")
            notificacion = Email(mensaje, identificacion, nombre, asunto, direccion_email)
            notificacion.enviar_mensaje()


main()  