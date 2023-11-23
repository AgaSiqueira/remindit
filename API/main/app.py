import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from functions.login import analizarToken, decode_auth_token, get_token
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
CORS(app)

import routes.user_routes
import routes.metodo_routes
import routes.tipo_ciclo_routes
import routes.notificacao_renovacao_routes
import routes.assinatura_routes
import routes.renovacao_routes

if __name__ == "__main__":
    app.run(port=5000,host='localhost',debug=True)


