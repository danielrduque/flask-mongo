# models/reporte_model.py

class ReporteModel:
    @staticmethod
    def generar_reporte_completo(mongo):
        """
        Ejecuta una consulta de agregación para generar un reporte detallado de tareas,
        proyectos y responsables, filtrado por un grupo de edad específico.
        """
        
        pipeline = [
            {
                "$lookup": {
                    "from": "estado_tarea",
                    "localField": "id_estado_tarea",
                    "foreignField": "_id",
                    "as": "result"
                }
            },
            {"$unwind": "$result"},
            {
                "$lookup": {
                    "from": "proyecto",
                    "localField": "id_proyecto",
                    "foreignField": "_id",
                    "as": "proyect"
                }
            },
            {"$unwind": "$proyect"},
            {
                "$lookup": {
                    "from": "responsable",
                    "localField": "id_responsable",
                    "foreignField": "_id",
                    "as": "respon"
                }
            },
            {"$unwind": "$respon"},
            {
                "$project": {
                    "_id": 0,
                    "nombre_tarea": 1,
                    "estado_tarea": "$result.estado_tarea",
                    "nombre_proyecto": "$proyect.nombre_proyecto",
                    "nombre_responsable": "$respon.nombre_responsable",
                    "apellido_responsable": "$respon.apellido_responsable",
                    "edad": "$respon.edad",
                    "grupo_etareo": {
                        "$cond": {
                            "if": {"$and": [{"$gt": ["$respon.edad", 17]}, {"$lte": ["$respon.edad", 30]}]},
                            "then": "adulto_joven",
                            "else": {
                                "$cond": {
                                    "if": {"$and": [{"$gt": ["$respon.edad", 30]}, {"$lte": ["$respon.edad", 50]}]},
                                    "then": "adulto_medio",
                                    "else": "adulto_mayor"
                                }
                            }
                        }
                    }
                }
            },
            {
                "$match": {
                    "grupo_etareo": "adulto_medio"
                }
            },
            {
                "$sort": {
                    "nombre_responsable": 1
                }
            }
        ]
        
        reporte_data = list(mongo.db.tarea.aggregate(pipeline))
        return reporte_data