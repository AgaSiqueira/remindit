from __main__ import app, conn

import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from functions.login import analizarToken, decode_auth_token, get_token
from database.crudAssinatura import create_assinatura, delete_assinatura, get_assinaturas, get_assinatura, update_assinatura
from database.crudMetodoPagamento import create_metodo_pagamento, delete_metodo_pagamento, get_metodos_pagamento, get_metodo_pagamento, update_metodo_pagamento
from database.crudNotificacaoRenovacao import create_notificacao_renovacao, delete_notificacao_renovacao, get_notificacoes_renovacao, get_notificacao_renovacao, update_notificacao_renovacao
from database.crudTipoCiclo import create_tipo_ciclo, delete_tipo_ciclo, get_tipos_ciclo, get_tipo_ciclo, popular_tipo_ciclo, update_tipo_ciclo
from database.crudRenovacao import create_renovacao, delete_renovacao, get_renovacoes, get_renovacao, update_renovacao
from database.db_functions import create_connection

@app.get("/tipos_ciclo")
def receber_tipos():
    auth_header = request.headers.get('Authorization')
    resp = analizarToken(conn, auth_header)
    if(resp['status'] == 200):
        return jsonify(get_tipos_ciclo(conn))
    else:
        return resp, 403