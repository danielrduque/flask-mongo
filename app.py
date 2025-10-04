from flask import Flask
from flask_pymongo import PyMongo
from controllers.tareas_controller import tareas_bp
from controllers.clientes_controller import clientes_bp
from controllers.ventas_controller import ventas_bp

app = Flask(__name__)


app.config["MONGO_URI_PARCIAL"] = "mongodb://localhost:27017/PARCIAL"
mongo_parcial = PyMongo(app, uri=app.config["MONGO_URI_PARCIAL"])

# Conexión a Mongo (supermarket)
app.config["MONGO_URI_SUPERMARKET"] = "mongodb://localhost:27017/supermarket"
mongo_supermarket = PyMongo(app, uri=app.config["MONGO_URI_SUPERMARKET"])


app.mongo_parcial = mongo_parcial
app.mongo_supermarket = mongo_supermarket

# Registrar blueprints
app.register_blueprint(tareas_bp, url_prefix="/api")
app.register_blueprint(clientes_bp, url_prefix="/api")
app.register_blueprint(ventas_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)