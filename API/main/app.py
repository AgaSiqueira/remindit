import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from functions.login import decode_auth_token, get_token
from database.crudUsuario import create_usuario, delete_usuario, get_usuarios, get_usuario, update_usuario
from database.crudAssinatura import create_assinatura, delete_assinatura, get_assinaturas, get_assinatura, update_assinatura
from database.crudMetodoPagamento import create_metodo_pagamento, delete_metodo_pagamento, get_metodos_pagamento, get_metodo_pagamento, update_metodo_pagamento
from database.crudNotificacaoRenovacao import create_notificacao_renovacao, delete_notificacao_renovacao, get_notificacoes_renovacao, get_notificacao_renovacao, update_notificacao_renovacao
from database.crudTipoCiclo import create_tipo_ciclo, delete_tipo_ciclo, get_tipos_ciclo, get_tipo_ciclo, update_tipo_ciclo
from database.crudRenovacao import create_renovacao, delete_renovacao, get_renovacoes, get_renovacao, update_renovacao
from database.db_functions import create_connection
from database.create_tables import main as create_tables

load_dotenv()
conn = create_tables()

app = Flask(__name__)

# @app.get("/usuarios")
# def receber_usuarios():
#     return jsonify(get_usuarios(conn))

# @app.post("/usuario")
# def adicionar_usuario():
#     if request.is_json:
#         req_usuario = request.get_json()

#         usuarioSql = (req_usuario["nome"], req_usuario["senha"], req_usuario["email"])
#         id_usuario = create_usuario(conn, usuarioSql)
#         return f'Usuário {id_usuario} criado', 201
#     return {"error": "A requisição deve ser JSON"}, 415

# @app.put("/usuario/<int:cd_usuario>")
# def editar_usuario(cd_usuario):
#     if request.is_json:
#         req_usuario = request.get_json()
        
#         usuarioSql = (req_usuario["nome"], req_usuario["senha"], req_usuario["email"], cd_usuario)
#         update_usuario(conn, usuarioSql)
#         return f'Usuário {cd_usuario} atualizado', 201
#     return {"error": "A requisição deve ser JSON"}, 415

# @app.delete("/usuario/<int:cd_usuario>")
# def deletar_usuario(cd_usuario):
#     delete_usuario(conn, cd_usuario)
#     return f'Usuário {cd_usuario} deletado', 200

@app.get("/usuarios")
def receber_usuarios():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token:
        resp = decode_auth_token(auth_token)
        print(resp)
        if not isinstance(resp, str):
            user = get_usuario(conn, resp)
            responseObject = {
            'status': 200,
            'message': 'Sucesso na autenticação'
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

    return jsonify(get_usuarios(conn))

@app.post("/usuario")
def adicionar_usuario():
    if request.is_json:
        req_usuario = request.get_json()

        usuarioSql = (req_usuario["nome"], req_usuario["senha"], req_usuario["email"])
        id_usuario = create_usuario(conn, usuarioSql)
        return f'Usuário {id_usuario} criado', 201
    return {"error": "A requisição deve ser JSON"}, 415

@app.put("/usuario/<int:cd_usuario>")
def editar_usuario(cd_usuario):
    if request.is_json:
        req_usuario = request.get_json()
        
        usuarioSql = (req_usuario["nome"], req_usuario["senha"], req_usuario["email"], cd_usuario)
        update_usuario(conn, usuarioSql)
        return f'Usuário {cd_usuario} atualizado', 201
    return {"error": "A requisição deve ser JSON"}, 415

@app.delete("/usuario/<int:cd_usuario>")
def deletar_usuario(cd_usuario):
    delete_usuario(conn, cd_usuario)
    return f'Usuário {cd_usuario} deletado', 200

@app.post("/login")
def realizar_login():
    if request.is_json:
        req_usuario = request.get_json()

        usuarioSql = (req_usuario["nome"], req_usuario["senha"])
        result = get_token(conn, usuarioSql)
        if result['status'] == 200: 
            return result
        else:
            return f'Usuário ou senha incorretos', result[1]
    return {"error": "A requisição deve ser JSON"}, 415

if __name__ == "__main__":
    app.run(port=5000,host='localhost',debug=True)


