# models/venta_model.py
from bson import ObjectId

class VentaModel:
    @staticmethod
    def obtener_ventas_con_productos(mongo):
        """
        Ejecuta una consulta de agregación para obtener las ventas
        con los detalles de los productos incluidos.
        """
        pipeline = [
            {
                "$unwind": "$items"
            },
            {
                "$lookup": {
                    "from": "productos",
                    "localField": "items.producto_id",
                    "foreignField": "_id",
                    "as": "producto"
                }
            },
            {
                "$unwind": "$producto"
            },
            {
                "$group": {
                    "_id": "$_id",
                    "cliente_id": { "$first": "$cliente_id" },
                    "fecha": { "$first": "$fecha" },
                    "total": { "$first": "$total" },
                    "productos": {
                        "$push": {
                            "nombre": "$producto.nombre",
                            "precio": "$producto.precio",
                            "cantidad": "$items.cantidad"
                        }
                    }
                }
            },
            {
                "$project": {
                    # "_id" se incluye por defecto, lo mantenemos
                    "cliente_id": 1,
                    "fecha": 1,
                    "total": 1,
                    "productos": 1
                }
            }
        ]
        
        ventas_data = list(mongo.db.ventas.aggregate(pipeline))
        
        # Convertimos los ObjectId a string para que sean compatibles con JSON
        for venta in ventas_data:
            venta["_id"] = str(venta["_id"])
            if "cliente_id" in venta and isinstance(venta["cliente_id"], ObjectId):
                venta["cliente_id"] = str(venta["cliente_id"])
                
        return ventas_data