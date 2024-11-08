class Capacitacion:
    def __init__(self, id_capacitacion, id_capacitor, descripcion, fecha_inicio, fecha_fin, resultado) -> None:
        self.id_capacitacion = id_capacitacion
        self.id_capacitor = id_capacitor
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.resultado = resultado

    def to_json(self):
        return {
            'id_capacitacion': self.id_capacitacion,
            'id_capacitor': self.id_capacitor,
            'descripcion': self.descripcion,
            'fecha_inicio': self.fecha_inicio,
            'fecha_fin': self.fecha_fin,
            'resultado': self.resultado
        }
