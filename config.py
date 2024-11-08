from decouple import config as get_config  # Cambia el nombre para evitar conflicto


class Config:
    SECRET_KEY = get_config('SECRET_KEY')  # Usa el nuevo nombre


class DevelopmentConfig(Config):
    DEBUG = True


configurations = {  # Cambia el nombre del diccionario
    'development': DevelopmentConfig
}
