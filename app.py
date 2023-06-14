from flask import Flask, render_template , request,jsonify, redirect, url_for 
import database as dbase
from products import Product

db = dbase.dbconecction()

app = Flask(__name__)
#rutas de la app
@app.route('/')
def home():
    Products = db['Product']
    productsRecibidos = Products.find()
    return render_template('index.html',products = productsRecibidos)






#metodo get para obtener los productos

#metodo post para agregar productos
@app.route('/products', methods=["POST"])
def addproducts():
    Products = db['Product']
    name = request.form ('name')
    price = request.form ('price')
    quantity = request.form ('quantity')
    
    if name and price and quantity:
        new_product = Product(name, price, quantity)
        Products.insert_one(Products.toDBcollection())
        response = jsonify({
            'name' : name,
            'price' : price,
            'quantity' : quantity
        })
        return redirect(url_for('home'))
    else:
       return notfound()
    
#metodo para eliminar productos(delete)
@app.route('/delete/<string:product_name>')
def delete(product_name):
        Products = db['Product']
        Products.delete_one({'name':product_name})
        return redirect(url_for('home'))

#metodo para editar los productos(put)
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    Products = db['Product']
    name = request.form ('name')
    price = request.form ('price')
    quantity = request.form ('quantity')
    
    if name and price and quantity:
        Products.update_one({'name': product_name}, {'$set': {'name': name, 'price': price, 'quantity': quantity}})
        responsive = jsonify({'message': 'producto '+ product_name + 'actualizado'})
        return redirect(url_for('home'))
    else:
        return notfound()

        

#metodo para redirecionar a la pagina de inicio por errores   
@app.errorhandler(404)
def notfound(error=None):
    message = {
        'message': 'Resource not found' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response  

if __name__ == '__main__':
    app.run(debug=True, port= 4000)






