from flask import Blueprint, jsonify, current_app
# 🔽 ¡Importa tu nuevo modelo!
from models.reporte_model import ReporteModel

tareas_bp = Blueprint("PARCIAL", __name__)

@tareas_bp.route("/reporte", methods=["GET"])
def get_reporte():
    # 1. Obtén la conexión a la BD
    mongo = current_app.mongo
    
    # 2. Pídele al modelo que genere el reporte (¡toda la complejidad está oculta!)
    reporte = ReporteModel.generar_reporte_completo(mongo)
    
    # 3. Devuelve el resultado
    return jsonify(reporte)