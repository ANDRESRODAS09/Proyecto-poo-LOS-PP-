class Usuario:
    def __init__(self, username, password, nombres, apellidos, documento, correo, tipo_de_usuario):
        self.username = username
        self.password = password
        self.nombres = nombres
        self.apellidos = apellidos
        self.documento = documento
        self.correo = correo
        self.tipo_de_usuario = tipo_de_usuario

class Administrador(Usuario):
    def __init__(self, username, password, nombres, apellidos, documento, correo):
        super().__init__(username, password, nombres, apellidos, documento, correo, "Administrador")
    
    def crear_usuario(self, username, password, nombres, apellidos, documento, correo, tipo_de_usuario):
        nuevo_usuario = Usuario(username, password, nombres, apellidos, documento, correo, tipo_de_usuario)
        # Base de datos
        return nuevo_usuario

    def registrar_usuario(self, username, password, nombres, apellidos, documento, correo, tipo_de_usuario):
        nuevo_usuario = self.crear_usuario(username, password, nombres, apellidos, documento, correo, tipo_de_usuario)
        #Para guardar el nuevo usuario
        return nuevo_usuario

class UsuarioFinal(Usuario):
    def __init__(self, username, password, nombres, apellidos, documento, correo):
        super().__init__(username, password, nombres, apellidos, documento, correo, "Usuario Final")
    
    def registrarse(self, username, password, nombres, apellidos, documento, correo):
        nuevo_usuario = UsuarioFinal(username, password, nombres, apellidos, documento, correo)
        #Para guardar el nuevo usuario
        return nuevo_usuario

class Imagen:
    def __init__(self):
        self.datos_imagen = None
        self.formato = None
        self.tamano = None
    
    def cargar_desde_archivo(self, ruta_archivo):
        pass
    
    def exportar_con_mensaje(self, mensaje):
        pass
    
    def obtener_datos_imagen(self):
        #datos de la imagen (píxeles, formato, tamaño)
        return self.datos_imagen, self.formato, self.tamaño

class Mensaje:
    def __init__(self, texto):
        self.texto = texto
    
    def cifrar(self, clave):
        pass
    
    def descifrar(self, clave):
        pass

username = input("Ingrese su nombre de usuario: ")
password = input("Ingrese su contraseña: ")
nombres = input("Ingrese sus nombres: ")
apellidos = input("Ingrese sus apellidos: ")
documento = input("Ingrese su número de documento: ")
correo = input("Ingrese su correo electrónico: ")

usuario1 = Administrador(username, password, nombres, apellidos, documento, correo)
nuevo_usuario = usuario1.registrar_usuario(username, password, nombres, apellidos, documento, correo, "Usuario Final")
print("Nuevo usuario registrado:", nuevo_usuario.username)