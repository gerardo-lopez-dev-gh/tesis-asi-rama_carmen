class Tratamientos:
    def __init__(self, id_tratamiento, descripcion, duracion) -> None:
        self.id_tratamiento = id_tratamiento
        self.descripcion = descripcion
        self.duracion = duracion

    def to_json(self):
        return {
            'id_tratamiento': self.id_tratamiento,
            'descripcion': self.descripcion,
            'duracion': self.duracion
        }
