class Contabilidad:
    def __init__(self, id_contabilidad, id_empresa, tipo_tabla_tipo_transaccion,
                 codigo_tabla_tipo_transaccion, monto, fecha, descripcion) -> None:
        self.id_contabilidad = id_contabilidad
        self.id_empresa = id_empresa
        self.tipo_tabla_tipo_transaccion = tipo_tabla_tipo_transaccion
        self.codigo_tabla_tipo_transaccion = codigo_tabla_tipo_transaccion
        self.monto = monto
        self.fecha = fecha
        self.descripcion = descripcion

    def to_json(self):
        return {
            'id_contabilidad': self.id_contabilidad,
            'id_empresa': self.id_empresa,
            'tipo_tabla_tipo_transaccion': self.tipo_tabla_tipo_transaccion,
            'codigo_tabla_tipo_transaccion': self.codigo_tabla_tipo_transaccion,
            'monto': self.monto,
            'fecha': self.fecha,
            'descripcion': self.descripcion
        }
