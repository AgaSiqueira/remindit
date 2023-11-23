from __main__ import app, conn

import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from functions.login import analizarToken, decode_auth_token, get_token
from database.crudAssinatura import create_assinatura, delete_assinatura, get_assinaturas, get_assinatura, get_assinaturas_por_usuario, update_assinatura
from database.crudMetodoPagamento import create_metodo_pagamento, delete_metodo_pagamento, get_metodos_pagamento, get_metodo_pagamento, update_metodo_pagamento
from database.crudNotificacaoRenovacao import create_notificacao_renovacao, delete_notificacao_renovacao, get_notificacoes_renovacao, get_notificacao_renovacao, update_notificacao_renovacao
from database.crudTipoCiclo import create_tipo_ciclo, delete_tipo_ciclo, get_tipos_ciclo, get_tipo_ciclo, update_tipo_ciclo
from database.crudRenovacao import create_renovacao, delete_renovacao, get_renovacoes, get_renovacao, get_renovacoes_por_usuario, update_renovacao
from database.db_functions import create_connection


@app.get("/renovacoes")
def receber_renovacoes():
    auth_header = request.headers.get('Authorization')
    resp = analizarToken(conn, auth_header)
    if(resp['status'] == 200):
        return jsonify(get_renovacoes_por_usuario(conn, resp["userId"]))
    else:
        return resp, 403
    
@app.post("/renovacao")
def adicionar_renovacao():
    if request.is_json:
        req_renovacao = request.get_json()
        
        auth_header = request.headers.get('Authorization')
        resp = analizarToken(conn, auth_header)
        if(resp['status'] == 200):
            renovacaoSql = (req_renovacao["data"], req_renovacao["valor"], req_renovacao["ativo"],
                             req_renovacao["cd_assinatura"], req_renovacao["cd_notificacao_renovacao"])
            id_renovacao = create_renovacao(conn, renovacaoSql)
            return f'Renovacao {id_renovacao} criada', 201
        else:
            return resp, 403
    return {"error": "A requisição deve ser JSON"}, 415

@app.put("/renovacao/<int:cd_renovacao>")
def editar_renovacao(cd_renovacao):
    if request.is_json:
        req_renovacao = request.get_json()

        auth_header = request.headers.get('Authorization')
        resp = analizarToken(conn, auth_header)
        if(resp['status'] == 200):
            assinaturaSql = (req_renovacao["data"], req_renovacao["valor"], req_renovacao["ativo"],
                             req_renovacao["cd_assinatura"], req_renovacao["cd_notificacao_renovacao"], cd_renovacao)
            update_renovacao(conn, assinaturaSql)
            return f'Renovacao {cd_renovacao} atualizada', 201
        else:
            return resp, 403
    return {"error": "A requisição deve ser JSON"}, 415

@app.delete("/renovacao/<int:cd_renovacao>")
def deletar_renovacao(cd_renovacao):
    auth_header = request.headers.get('Authorization')
    resp = analizarToken(conn, auth_header)
    if(resp['status'] == 200):
        delete_renovacao(conn, cd_renovacao)
        return f'Renovacao {cd_renovacao} deletada', 200
    else:
        return resp, 403
