class ResultadosExamenes:
    def __init__(self, id_historial, id_animal, tipo_tabla_tipo_examen, codigo_tabla_tipo_examen,
                 resultado, fecha) -> None:
        self.id_historial = id_historial
        self.id_animal = id_animal
        self.tipo_tabla_tipo_examen = tipo_tabla_tipo_examen
        self.codigo_tabla_tipo_examen = codigo_tabla_tipo_examen
        self.resultado = resultado
        self.fecha = fecha

    def to_json(self):
        return {
            'id_historial': self.id_historial,
            'id_animal': self.id_animal,
            'tipo_tabla_tipo_examen': self.tipo_tabla_tipo_examen,
            'codigo_tabla_tipo_examen': self.codigo_tabla_tipo_examen,
            'resultado': self.resultado,
            'fecha': self.fecha
        }
