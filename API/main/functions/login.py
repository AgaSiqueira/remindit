import datetime
import hashlib
import os
import jwt
from database.crudUsuario import get_usuario

def get_token(conn, usuario):
    try:
        sql = ''' SELECT cd_usuario FROM usuario 
                    WHERE nome = ? AND senha = ?
            '''
        cur = conn.cursor()
        cur.execute(sql, (usuario[0], hashlib.md5(usuario[1].encode()).hexdigest()))
        conn.commit()
        resul = cur.fetchone()
        if resul != None:
            token = encode_auth_token(resul[0])
            response = {
                        'status': 200,
                        'message': 'Registrado com sucesso.',
                        'auth_token': token
                    }
            return (response)
        else:
            return ("Usuário ou senha incorretos", 403)
    except Exception as e:
        return e
        
def encode_auth_token(user_id):
    try:
        payload = {
            'username': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=30)
        }
        token = jwt.encode(
            payload,
            os.getenv('SECRET_KEY'),
            algorithm="HS256"
        )
        return token
    except Exception as e:
        return e

def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
        return payload["username"]
    except jwt.ExpiredSignatureError:
        return "Token expirado. Log in novamente."
    except jwt.InvalidTokenError:
        return "Token invalido. Log in novamente."

def analizarToken(conn, auth_header):
    if auth_header:
            auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token:
        resp = decode_auth_token(auth_token)
        if isinstance(resp, int):
            responseObject = {
            'status': 200,
            'message': 'Sucesso na autenticação',
            'userId': resp
            }
            return responseObject
        responseObject = {
            'status': 401,
            'message': 'Falha na autenticação'
        }
        return responseObject
    else:
        responseObject = {
            'status': 401,
            'message': 'Falha na autenticação'
        }
        return responseObject