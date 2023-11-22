from __main__ import app, conn

import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from functions.login import analizarToken, decode_auth_token, get_token
from database.crudAssinatura import create_assinatura, delete_assinatura, get_assinaturas, get_assinatura, update_assinatura
from database.crudMetodoPagamento import create_metodo_pagamento, delete_metodo_pagamento, get_metodos_pagamento, get_metodo_pagamento, update_metodo_pagamento
from database.crudNotificacaoRenovacao import create_notificacao_renovacao, delete_notificacao_renovacao, get_notificacoes_renovacao, get_notificacao_renovacao, update_notificacao_renovacao
from database.crudTipoCiclo import create_tipo_ciclo, delete_tipo_ciclo, get_tipos_ciclo, get_tipo_ciclo, update_tipo_ciclo
from database.crudRenovacao import create_renovacao, delete_renovacao, get_renovacoes, get_renovacao, update_renovacao
from database.db_functions import create_connection


@app.get("/metodos")
def receber_metodos():
    auth_header = request.headers.get('Authorization')
    resp = analizarToken(conn, auth_header)
    if(resp['status'] == 200):
        return jsonify(get_metodos_pagamento(conn))
    else:
        return resp, 403
    
@app.post("/metodo")
def adicionar_metodo():
    if request.is_json:
        req_metodo = request.get_json()
        
        auth_header = request.headers.get('Authorization')
        resp = analizarToken(conn, auth_header)
        if(resp['status'] == 200):
            metodoSql = (req_metodo["nome"], req_metodo["apelido"])
            id_metodo = create_metodo_pagamento(conn, metodoSql)
            return f'Metodo de pagamento {id_metodo} criado', 201
        else:
            return resp, 403
    return {"error": "A requisição deve ser JSON"}, 415

@app.put("/metodo/<int:cd_metodo_pagamento>")
def editar_metodo(cd_metodo_pagamento):
    if request.is_json:
        req_metodo = request.get_json()

        auth_header = request.headers.get('Authorization')
        resp = analizarToken(conn, auth_header)
        if(resp['status'] == 200):
            metodoSql = (req_metodo["nome"], req_metodo["apelido"], cd_metodo_pagamento)
            update_metodo_pagamento(conn, metodoSql)
            return f'Metodo de pagamento {cd_metodo_pagamento} atualizado', 201
        else:
            return resp, 403
    return {"error": "A requisição deve ser JSON"}, 415

@app.delete("/metodo/<int:cd_metodo_pagamento>")
def deletar_metodo(cd_metodo_pagamento):
    auth_header = request.headers.get('Authorization')
    resp = analizarToken(conn, auth_header)
    if(resp['status'] == 200):
        delete_metodo_pagamento(conn, cd_metodo_pagamento)
        return f'Metodo de pagamento {cd_metodo_pagamento} deletado', 200
    else:
        return resp, 403