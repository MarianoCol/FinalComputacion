class TemaMusical():

    def __init__(self, codigo = '', nombre = '', duracion = 0, interprete = ''):
        self._codigo = codigo
        self._nombre = nombre
        self._duracion = duracion
        self._interprete = interprete

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        if codigo == '':
            raise EmptyError()
        self._codigo = codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if nombre == '':
            raise EmptyError()
        self._nombre = nombre

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, duracion):
        if duracion < 0:
            raise EmptyError
        self._duracion = duracion

    @property
    def interprete(self):
        return self._interprete

    @interprete.setter
    def interprete(self, interprete):
        if interprete == '':
            raise EmptyError()
        self._interprete = interprete

    def __str__(self):
        return 'codigo: {}\n\tnombre: {}\n\tduracion: {}\n\tinterprete: {}\n'.format(self._codigo,
         self._nombre, self._duracion, self._interprete)

    def input(self, parametro=''):
        if parametro == '':
            self._codigo = str(input('Ingrese el codigo de la cancion: '))
        self._nombre = str(input('Ingrese el nombre de la cancion: '))
        self._duracion = int(input('Ingrese la duracion de la cancion: '))
        self._interprete = str(input('Ingrese el interprete de la cancion: '))


class EmptyError(ValueError):
    print("Ingrese un valor valido")
