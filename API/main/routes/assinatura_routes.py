from __main__ import app, conn

import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from functions.login import analizarToken, decode_auth_token, get_token
from database.crudAssinatura import create_assinatura, delete_assinatura, get_assinaturas, get_assinatura, get_assinaturas_por_usuario, update_assinatura
from database.crudMetodoPagamento import create_metodo_pagamento, delete_metodo_pagamento, get_metodos_pagamento, get_metodo_pagamento, update_metodo_pagamento
from database.crudNotificacaoRenovacao import create_notificacao_renovacao, delete_notificacao_renovacao, get_notificacoes_renovacao, get_notificacao_renovacao, update_notificacao_renovacao
from database.crudTipoCiclo import create_tipo_ciclo, delete_tipo_ciclo, get_tipos_ciclo, get_tipo_ciclo, update_tipo_ciclo
from database.crudRenovacao import create_renovacao, delete_renovacao, get_renovacoes, get_renovacao, update_renovacao
from database.db_functions import create_connection


@app.get("/assinaturas")
def receber_assinaturas():
    auth_header = request.headers.get('Authorization')
    resp = analizarToken(conn, auth_header)
    if(resp['status'] == 200):
        return jsonify(get_assinaturas_por_usuario(conn, resp["userId"]))
    else:
        return resp, 403
    
@app.post("/assinatura")
def adicionar_assinatura():
    if request.is_json:
        req_assinatura = request.get_json()
        
        auth_header = request.headers.get('Authorization')
        resp = analizarToken(conn, auth_header)
        if(resp['status'] == 200):
            assinaturaSql = (req_assinatura["nome"], req_assinatura["descricao"], req_assinatura["valor_proxima"],
                          req_assinatura["tamanho_ciclo"], req_assinatura["ativo"], req_assinatura["cd_tipo_ciclo"],
                          req_assinatura["cd_metodo_pagamento"], resp["userId"])
            id_assinatura = create_assinatura(conn, assinaturaSql)
            return f'Assinatura {id_assinatura} criada', 201
        else:
            return resp, 403
    return {"error": "A requisição deve ser JSON"}, 415

@app.put("/assinatura/<int:cd_assinatura>")
def editar_assinatura(cd_assinatura):
    if request.is_json:
        req_assinatura = request.get_json()

        auth_header = request.headers.get('Authorization')
        resp = analizarToken(conn, auth_header)
        if(resp['status'] == 200):
            assinaturaSql = (req_assinatura["nome"], req_assinatura["descricao"], req_assinatura["valor_proxima"],
                          req_assinatura["tamanho_ciclo"], req_assinatura["ativo"], req_assinatura["cd_tipo_ciclo"],
                          req_assinatura["cd_metodo_pagamento"], resp["userId"], cd_assinatura)
            update_assinatura(conn, assinaturaSql)
            return f'Assinatura {cd_assinatura} atualizada', 201
        else:
            return resp, 403
    return {"error": "A requisição deve ser JSON"}, 415

@app.delete("/assinatura/<int:cd_assinatura>")
def deletar_assinatura(cd_assinatura):
    auth_header = request.headers.get('Authorization')
    resp = analizarToken(conn, auth_header)
    if(resp['status'] == 200):
        delete_assinatura(conn, cd_assinatura)
        return f'Assinatura {cd_assinatura} deletada', 200
    else:
        return resp, 403