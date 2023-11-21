import datetime
import hashlib
import os
import jwt

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
            print(token)
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
            # os.getenv('SECRET_KEY')
            "123",
            algorithm="HS256"
        )
        return token
    except Exception as e:
        return e

def decode_auth_token(auth_token):
    try:
        # payload = jwt.decode(auth_token, os.getenv('SECRET_KEY'))
        payload = jwt.decode(auth_token, "123", algorithms=["HS256"])
        return payload["username"]
    except jwt.ExpiredSignatureError:
        return 'Token expirado. Log in novamente.'
    except jwt.InvalidTokenError:
        return 'Token invalido. Log in novamente.'
