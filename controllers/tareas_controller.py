from flask import Blueprint, jsonify, current_app
from models.reporte_model import ReporteModel

tareas_bp = Blueprint("PARCIAL", __name__)

@tareas_bp.route("/reporte", methods=["GET"])
def get_reporte():
    # 1. Obtén la conexión a la BD 'PARCIAL'
    mongo = current_app.mongo_parcial
    
    reporte = ReporteModel.generar_reporte_completo(mongo)
    
    # 3. Devuelve el resultado
    return jsonify(reporte)