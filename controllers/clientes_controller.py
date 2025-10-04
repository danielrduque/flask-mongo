# controllers/clientes_controller.py

from flask import Blueprint, jsonify, current_app
# 🔽 ¡Importa tu nuevo modelo!
from models.cliente_model import ClienteModel

clientes_bp = Blueprint("supermarket", __name__)

@clientes_bp.route("/clientes", methods=["GET"])
def get_clientes():
    # 1. Obtén la conexión a la BD 'supermarket'
    mongo = current_app.mongo_supermarket
    
    # 2. Pídele al modelo que obtenga los clientes
    clientes = ClienteModel.obtener_clientes(mongo)
    
    # 3. Devuelve el resultado
    return jsonify(clientes)