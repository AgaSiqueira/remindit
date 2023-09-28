import os

from database.db_functions import create_connection, create_table

def main():
    conn = create_connection(os.getenv('DATABASE_PATH'))
    
    sql_create_usuario_table = """
        CREATE TABLE IF NOT EXISTS usuario (
            cd_usuario integer PRIMARY KEY,
            nome text NOT NULL,
            senha text NOT NULL,
            email text
        );
    """
    sql_create_metodo_pagamento_table = """
        CREATE TABLE IF NOT EXISTS metodo_pagamento (
            cd_metodo_pagamento integer PRIMARY KEY,
            nome text NOT NULL,
            apelido text
        );
    """
    sql_create_tipo_ciclo_table = """
        CREATE TABLE IF NOT EXISTS tipo_ciclo (
            cd_tipo_ciclo integer PRIMARY KEY,
            descricao text
        );
    """
    sql_create_notificacao_renovacao_table = """
        CREATE TABLE IF NOT EXISTS notificacao_renovacao (
            cd_notificacao_renovacao integer PRIMARY KEY,
            nome text NOT NULL,
            conteudo text,
            visualizado integer
        );
    """
    sql_create_assinatura_table = """
        CREATE TABLE IF NOT EXISTS assinatura (
            cd_assinatura integer PRIMARY KEY,
            nome text NOT NULL,
            descricao text,
            data text,
            valor_proxima real,
            tamanho_ciclo integer,
            ativo integer,
            cd_tipo_ciclo integer NOT NULL,
            cd_metodo_pagamento integer NOT NULL,
            cd_usuario integer NOT NULL,
            FOREIGN KEY (cd_tipo_ciclo) REFERENCES tipo_ciclo (cd_tipo_ciclo),
            FOREIGN KEY (cd_metodo_pagamento) REFERENCES metodo_pagamento (cd_metodo_pagamento),
            FOREIGN KEY (cd_usuario) REFERENCES usuario (cd_usuario)
        );
    """
    sql_create_renovacao_table = """
        CREATE TABLE IF NOT EXISTS renovacao (
            cd_renovacao integer PRIMARY KEY,
            data text NOT NULL,
            valor real,
            ativo integer,
            cd_assinatura integer NOT NULL,
            cd_notificacao_renovacao integer NOT NULL,
            FOREIGN KEY (cd_assinatura) REFERENCES assinatura (cd_assinatura),
            FOREIGN KEY (cd_notificacao_renovacao) REFERENCES notificacao_renovacao (cd_notificacao_renovacao)
        );
    """

    if conn is not None:
        # Criar tabelas
        create_table(conn, sql_create_usuario_table)
        create_table(conn, sql_create_metodo_pagamento_table)
        create_table(conn, sql_create_tipo_ciclo_table)
        create_table(conn, sql_create_notificacao_renovacao_table)
        create_table(conn, sql_create_assinatura_table)
        create_table(conn, sql_create_renovacao_table)

    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()