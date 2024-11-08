from src.models.AnimalModel import Animal
from src.repositories.AnimalRepository import AnimalRepository


class AnimalService:

    @staticmethod
    def get_all_animals():
        return AnimalRepository.get_all()

    @staticmethod
    def get_animal_by_id(id_animal):
        return AnimalRepository.get_by_id(id_animal)

    @staticmethod
    def create_animal(id_empresa, codigo_tabla_tipo_animal, fecha_nacimiento, peso, codigo_tabla_estado_salud, codigo_tabla_estado_registro, tipo_tabla_tipo_animal=12, tipo_tabla_estado_salud=5, tipo_tabla_estado_registro=13):
        animal = Animal(
            id_animal=None,  # Será generado por la base de datos
            id_empresa=id_empresa,
            tipo_tabla_tipo_animal=tipo_tabla_tipo_animal,
            codigo_tabla_tipo_animal=codigo_tabla_tipo_animal,
            fecha_nacimiento=fecha_nacimiento,
            peso=peso,
            tipo_tabla_estado_salud=tipo_tabla_estado_salud,
            codigo_tabla_estado_salud=codigo_tabla_estado_salud,
            tipo_tabla_estado_registro=tipo_tabla_estado_registro,
            codigo_tabla_estado_registro=codigo_tabla_estado_registro
        )
        return AnimalRepository.create(animal)

    @staticmethod
    def update_animal(id_animal, id_empresa, codigo_tabla_tipo_animal, fecha_nacimiento, peso, codigo_tabla_estado_salud, tipo_tabla_tipo_animal=12, tipo_tabla_estado_salud=5):
        animal = Animal(
            id_animal=id_animal,
            id_empresa=id_empresa,
            tipo_tabla_tipo_animal=tipo_tabla_tipo_animal,
            codigo_tabla_tipo_animal=codigo_tabla_tipo_animal,
            fecha_nacimiento=fecha_nacimiento,
            peso=peso,
            tipo_tabla_estado_salud=tipo_tabla_estado_salud,
            codigo_tabla_estado_salud=codigo_tabla_estado_salud,
            tipo_tabla_estado_registro=None,  # No se actualiza este campo
            codigo_tabla_estado_registro=None  # No se actualiza este campo
        )
        return AnimalRepository.update(animal)

    @staticmethod
    def delete_animal(id_animal):
        return AnimalRepository.delete(id_animal)
