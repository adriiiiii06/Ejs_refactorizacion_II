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
    men = input("Escribe tu mensaje: ")
    id = input("Introduce el codigo de identificacion: ")
    nom = input("Introduce el nombre de usuario: ")
    
    match metodo_envio:
        case "sms":
            n = input("¿A qué número de teléfono quieres enviarlo: ")
            noti = SMS(men, id, nom)
            noti.enviar_mensaje(n)

        case "email":
            direccion_email = input("Destinatario: ")
            asunto = input("Asunto: ")
            noti = Email(men, id, nom, asunto, direccion_email)
            noti.enviar_mensaje()


main()