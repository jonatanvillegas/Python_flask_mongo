from flask import Flask, render_template, request, jsonify, redirect,url_for, Response
import database as dbase
from producto import Producto

db = dbase.conection_db()

app = Flask(__name__)

@app.route('/')
#buscando el archivo en la carpeta template importada de flask 
def inicio():
    TablaP = db['productos']
    TodoslosProductos = TablaP.find()
    return render_template('index.html', productos=TodoslosProductos)


#Metodo POST
@app.route('/products', methods=['POST'])
def agregarProducto():
    #creanndo la coleccion en la base de datos 
    TablaP = db['productos']
    #obteniendo los datos de un Form 
    name = request.form['name']
    description = request.form['description']
    price = request.form['price']

    #validando si los datos existen
    if name and description and price:
        #creando el objeto  
        producto = Producto(name, description, price)
        #agregando el producto en la tabla con su esquema
        TablaP.insert_one(producto.__dict__)

        response = jsonify({
            'name': name,
            'description': description,
            'price': price
        })
        return redirect(url_for('inicio'))
    else :
        return notFound()
    
#Metodo DELETE
@app.route('/delete/<string:product_name>')
def eliminarProducto(product_name):
    TablaP = db['productos']
    TablaP.delete_one({'name': product_name})
    return redirect(url_for('inicio'))

#Metodo PUT
@app.route('/edit/<string:product_name>', methods=['POST'])
def EditarProducto(product_name):
    productos = db['productos']
    name = request.form['name']
    description = request.form['description']
    price = request.form['price']

    if name and description and price:
        productos.update_one({'name': product_name}, {'$set': {'name': name, 'description': description, 'price': price}})
        response = jsonify({'message': 'Producto' + product_name + 'Actualizado Correctamente'})
        return redirect(url_for('inicio'))
    else :
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado' + request.url,
        'status': '404'
    }
    response = jsonify(message)
    response.status_code = 404
    return Response



#evaluando si el archivo actual se esta ejecutando como archivo principal si es asi que se ejecute en el puerto 3000
if __name__ == '__main__':
    print('el servidor esta corriendo en el puerto 3000')
    app.run(debug=True, port=3000)