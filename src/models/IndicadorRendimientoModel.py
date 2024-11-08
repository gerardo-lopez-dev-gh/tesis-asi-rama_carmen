class IndicadoresRendimiento:
    def __init__(self, id_indicador, id_capacitacion, tipo_tabla_tipo_indicador,
                 codigo_tabla_tipo_indicador, valor, fecha) -> None:
        self.id_indicador = id_indicador
        self.id_capacitacion = id_capacitacion
        self.tipo_tabla_tipo_indicador = tipo_tabla_tipo_indicador
        self.codigo_tabla_tipo_indicador = codigo_tabla_tipo_indicador
        self.valor = valor
        self.fecha = fecha

    def to_json(self):
        return {
            'id_indicador': self.id_indicador,
            'id_capacitacion': self.id_capacitacion,
            'tipo_tabla_tipo_indicador': self.tipo_tabla_tipo_indicador,
            'codigo_tabla_tipo_indicador': self.codigo_tabla_tipo_indicador,
            'valor': self.valor,
            'fecha': self.fecha
        }
