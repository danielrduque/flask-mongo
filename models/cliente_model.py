# models/cliente_model.py

class ClienteModel:
    @staticmethod
    def obtener_clientes(mongo):
        """
        Obtiene todos los documentos de la colección 'clientes'.
        """
        clientes_data = list(mongo.db.clientes.find())
        
        for cliente in clientes_data:
            cliente["_id"] = str(cliente["_id"])
            
        return clientes_data