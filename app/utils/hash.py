from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# print(f'este es el password: {hash_password("123456")}')
# print(f'la verificacion es: {verify_password(
#     "123456", # contraseña en texto plano
#     "$2b$12$t6CJ3n2QoX/vFbk7gwE24.cyW5RYTI2qjRQ3kasiTghxsi5VCiJ3W" # contraseña encriptada
#     )}')

