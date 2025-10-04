# controllers/ventas_controller.py

from flask import Blueprint, jsonify, current_app
from models.venta_model import VentaModel

ventas_bp = Blueprint("ventas", __name__)

@ventas_bp.route("/ventas", methods=["GET"])
def get_ventas_detalle():
    # 1. Obtén la conexión a la BD 'supermarket'
    mongo = current_app.mongo_supermarket
    
    # 2. Pídele al modelo que ejecute la consulta de agregación
    ventas = VentaModel.obtener_ventas_con_productos(mongo)
    
    # 3. Devuelve el resultado
    return jsonify(ventas)