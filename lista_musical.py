class ListaMusical():
    
    def __init__(self):
        self._listaMusical = dict()

    def add(self, tema):
        cod = tema.codigo
        if cod in self._listaMusical:
            raise KeyError()
        self._listaMusical[cod] = tema

    def update(self, tema, codigo):
        if codigo not in self._listaMusical:
            raise KeyError()
        self._listaMusical[codigo] = tema

    def delete(self, codigo):
        if codigo not in self._listaMusical:
            raise KeyError()
        self._listaMusical.pop(codigo)

    def find_by_id(self, codigo):
        if codigo not in self._listaMusical:
            raise KeyError()
        return self._listaMusical[codigo]

    def find_all(self):
        lista = list()
        for i in self._listaMusical:
            lista.append(self._listaMusical[i])
        return lista


    @property
    def temas(self):
        return self._listaMusical

    #@temas.setter
    #def temas(self, tema):
    #    self._temas = tema