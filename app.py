from flask import Flask, render_template, request
import Basedd as dbase
import subprocess
from report import reportes
db = dbase.dbConnection()

app = Flask(__name__)

#Rutas de la aplicación
@app.route('/')
def home():
    lb = db.list_collection_names()
    return render_template('index.html', listadb=lb)
#Method Post

@app.route('/llamar',methods=['POST'])
def llamar():
    try:
        env = request.form['enviar']
        products = db[env.upper()]
        if(products.count_documents({})>0):
            reportes(products,env.upper())
            productsReceived = products.find()
            return render_template('consulta.html', Productos = productsReceived,nom_prod=env,tot=products.count_documents({}))
        else:
            return render_template('error.html')
    except Exception as e:
        return render_template('error.html')

@app.route('/generar',methods=['POST'])
def generar():
    path = f'Reportes\general.pdf'
    subprocess.Popen([path], shell=True)
    return "<h2>Reporte Generado!</h2>"


if __name__ == '__main__':
    app.run(debug=True, port=4000)