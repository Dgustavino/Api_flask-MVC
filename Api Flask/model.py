import json

class Biblioteca():

    def __init__(self, nombre_biblio, id_libro, nombre_libro, paginas, lista_libros):
        self.nombre_biblio = nombre_biblio
        self.id_libro = id_libro
        self.nombre_libro = nombre_libro
        self.paginas = paginas
        self.lista_libros = lista_libros
    #Fin del metodo

    def biblioteca(self):
        return ("%s %s %s %s %s" % (self.nombre_biblio, self.id_libro, self.nombre_libro, self.paginas, self.lista_libros))
    #Fin del metodo

    #Funcion para jalar datos desde el txt
    def getBiblio(self):
        database = open('data/db.txt', 'r')
        result = []
        json_list = json.loads(database.read())
        for item in json_list:
            item = json.loads(item)
            biblioteca = Biblioteca(item['nombre_biblio'], item['id_libro'], 
            item['nombre_libro'], item['paginas'], item['lista_libros'])
            result.append(biblioteca)
        return result
    #Fin del metodo

#Fin de la clase Biblioteca

