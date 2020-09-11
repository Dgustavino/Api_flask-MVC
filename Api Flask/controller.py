from model import Biblioteca
from biblioteca import MiBiblioteca


class Controller():

    biblioteca = MiBiblioteca()
    libritos = biblioteca.libros

    def busca_libro(self, id):
        for dictionario in self.libritos:   #Esta funcion no me la esta reconociendo en PUT y DELETE
            if dictionario['id_libro']==id:
                return dictionario
    #Fin de la Funcion
    
    def actualiza_libros(self, id, nom, pag):
        biblio = self.busca_libro(id)

        id_libro = id
        nombre_libro = nom
        paginas = pag

        if biblio==None:
            return None
        else:
            biblio['id_libro']= id_libro
            biblio['nombre_libro']= nombre_libro
            biblio['paginas']= paginas
            return "Biblioteca actualizada!" 
    #Fin de la Funcion

    def elimina_libro(self,id_libro):
        biblio = self.busca_libro(id_libro)
        self.libritos.pop(self.libritos.index(biblio))
        return "Libro eliminado!"
    #Fin de la Funcion

#Fin de la clase Controller


    

        