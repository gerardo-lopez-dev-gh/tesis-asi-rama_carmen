from passlib.hash import pbkdf2_sha256
import jwt
import datetime
from decouple import config

SECRET_KEY = config('SECRET_KEY')  # Load from .env


def hash_password(password):
    return pbkdf2_sha256.hash(password)


def verify_password(password, hashed):
    return pbkdf2_sha256.verify(password, hashed)


def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=24)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')


def verify_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
