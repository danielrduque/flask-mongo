from flask import Flask
from flask_pymongo import PyMongo
from controllers.tareas_controller import tareas_bp

app = Flask(__name__)

# Conexión a Mongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/PARCIAL"
mongo = PyMongo(app)

# mongo a los controladores
app.mongo = mongo

# Registrar blueprint
app.register_blueprint(tareas_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
