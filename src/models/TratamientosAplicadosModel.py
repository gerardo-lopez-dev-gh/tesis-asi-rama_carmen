class TratamientosAplicados:
    def __init__(self, id_tratamiento_apli, id_tratamiento, id_animal, descripcion, fecha_inicio, fecha_fin, resultado) -> None:
        self.id_tratamiento_apli = id_tratamiento_apli
        self.id_tratamiento = id_tratamiento
        self.id_animal = id_animal
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.resultado = resultado

    def to_json(self):
        return {
            'id_tratamiento_apli': self.id_tratamiento_apli,
            'id_tratamiento': self.id_tratamiento,
            'id_animal': self.id_animal,
            'descripcion': self.descripcion,
            'fecha_inicio': self.fecha_inicio,
            'fecha_fin': self.fecha_fin,
            'resultado': self.resultado
        }
