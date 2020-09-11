from flask import Flask
from flask import jsonify, render_template, request
from biblioteca import MiBiblioteca
from controller import Controller

app=Flask(__name__)

controller_libros = MiBiblioteca()
libros_diego = controller_libros.libros
controller_biblio = Controller()

#Muestra libros en HTML
@app.route('/Biblioteca', methods=['GET'])
def getLibros():
    mi_json = jsonify({"Biblioteca": controller_libros.libros})
    return mi_json
    #return render_template('index.html', data=mi_json)
#Fin de la Funcion

#Agrega libros en Insomnia
@app.route('/AddLibro', methods=['POST'])
def AddLibro():
    new_libro = {
        
        "id_libro": request.json['id_libro'],
        "nombre_libro": request.json['nombre_libro'],
        "paginas": request.json['paginas']   
    }
    controller_libros.libros.append(new_libro)
    return jsonify({"Libro agregado...!!!": new_libro})
    #Fin de la Funcion

#Edita Libros
@app.route('/editBiblio/<string:id_libro>', methods=['PUT'])
def editBiblio(id_libro):
    biblio = controller_biblio.busca_libro(id_libro)

   #si el libro no es encontrado
    if biblio==None:
        return jsonify({"Message":"Libro no existente!"})
    else:
        #guardamos los valores originales para comparar
        id_libro=biblio['id_libro']
        nombre_libro=biblio['nombre_libro']
        paginas=biblio['paginas']
        data = (id_libro, nombre_libro, paginas)

        id =  request.json['id_libro']
        nom = request.json['nombre_libro']
        pag = request.json['paginas']

    #envia parametros para actualizar al controlador desde el request
        resultado = controller_biblio.actualiza_libros(int(id),str(nom),int(pag))

        if resultado != None:
            #si el libro es encontrado
            return jsonify({"Message":resultado,
                            "Data" : data,
                            "Biblioteca Actualizada" : biblio})
#Fin de la Funcion

"""#Actualizar Biblioteca
@app.route('/editBiblioteca/<string:id_libro>', methods=['PUT'])
def editBiblioteca(id):
    biblioFound = [item for item in libros_diego] 
    for item in biblioFound:
        if item == id:
            pass

    if(len(biblioFound) > 0):
        biblioFound[0]['id_libro'] = request.json['id_libro']
        biblioFound[0]['nombre_libro'] = request.json['nombre_libro']
        biblioFound[0]['paginas'] = request.json['paginas']
        return jsonify({"Biblioteca Actualizada": biblioFound[0]})
    return jsonify({"Message": "Biblioteca No encontrada..."})"""


#Elimina Libros
@app.route('/deleteBiblio/<string:id_libro>', methods=["'DELETE'"])
def deleteLibros():
    biblio = controller_biblio.busca_libro(id)
    if biblio!=None:
        #si el libro existe, entonces procedemos a eliminarlo
        resultado=controller_biblio.elimina_libro(id)
        
        return jsonify({"Message":resultado,
                                "Biblioteca" : biblio})
#Fin de la Funcion


if __name__=='__main__':
    app.run(debug=True, port=4000)