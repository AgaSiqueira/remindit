import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from database.crudUsuario import create_usuario, delete_usuario, get_usuarios, update_usuario
from database.db_functions import create_connection
from database.create_tables import main as create_tables

load_dotenv()
conn = create_tables()

app = Flask(__name__)

@app.get("/usuarios")
def receber_usuarios():
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

if __name__ == "__main__":
    app.run(port=5000,host='localhost',debug=True)