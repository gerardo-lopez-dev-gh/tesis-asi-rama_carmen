class HistorialesMedicos:
    def __init__(self, id_historial, id_animal, descripcion, fecha) -> None:
        self.id_historial = id_historial
        self.id_animal = id_animal
        self.descripcion = descripcion
        self.fecha = fecha

    def to_json(self):
        return {
            'id_historial': self.id_historial,
            'id_animal': self.id_animal,
            'descripcion': self.descripcion,
            'fecha': self.fecha
        }
