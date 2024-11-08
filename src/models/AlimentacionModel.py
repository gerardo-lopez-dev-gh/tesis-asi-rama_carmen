class Alimentacion:
    def __init__(self, id_alimentacion, id_dieta, tipo_tabla_tipo_alimento, codigo_tabla_tipo_alimento,
                 cantidad, fecha) -> None:
        self.id_alimentacion = id_alimentacion
        self.id_dieta = id_dieta
        self.tipo_tabla_tipo_alimento = tipo_tabla_tipo_alimento
        self.codigo_tabla_tipo_alimento = codigo_tabla_tipo_alimento
        self.cantidad = cantidad
        self.fecha = fecha

    def to_json(self):
        return {
            'id_alimentacion': self.id_alimentacion,
            'id_dieta': self.id_dieta,
            'tipo_tabla_tipo_alimento': self.tipo_tabla_tipo_alimento,
            'codigo_tabla_tipo_alimento': self.codigo_tabla_tipo_alimento,
            'cantidad': self.cantidad,
            'fecha': self.fecha
        }
