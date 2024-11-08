class Cambio:
    def __init__(self, id_cambio, moneda, importe, fecha, confirmado) -> None:
        self.id_cambio = id_cambio
        self.moneda = moneda
        self.importe = importe
        self.fecha = fecha
        self.confirmado = confirmado

    def to_json(self):
        return {
            'id_cambio': self.id_cambio,
            'moneda': self.moneda,
            'importe': self.importe,
            'fecha': self.fecha,
            'confirmado': self.confirmado
        }
