# controllers/clientes_controller.py

from flask import Blueprint, jsonify, current_app
# 🔽 ¡Importa tu nuevo modelo!
from models.cliente_model import ClienteModel

clientes_bp = Blueprint("supermarket", __name__)

@clientes_bp.route("/clientes", methods=["GET"])
def get_clientes():

    mongo = current_app.mongo_supermarket
    
    clientes = ClienteModel.obtener_clientes(mongo)
    
    return jsonify(clientes)