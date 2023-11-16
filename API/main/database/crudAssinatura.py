def get_assinaturas(conn):
    sql = ''' SELECT * FROM assinatura '''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.fetchall()

def get_assinatura(conn, assinatura):
    sql = ''' SELECT * FROM assinatura 
                WHERE cd_assinatura = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, assinatura)
    conn.commit()
    return cur.fetchall()

def create_assinatura(conn, assinatura):
    sql = ''' INSERT INTO assinatura(nome, descricao, data, valor_proxima, 
                tamanho_ciclo, ativo, cd_tipo_ciclo, cd_metodo_pagamento, cd_usuario)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, assinatura)
    conn.commit()
    return cur.lastrowid

def update_assinatura(conn, assinatura):
    sql = '''UPDATE assinatura
                SET nome = ?, descricao = ?, data = ?, valor_proxima = ?, 
                tamanho_ciclo = ?, ativo = ?, cd_tipo_ciclo = ?, cd_metodo_pagamento = ?,
                cd_usuario = ?
                WHERE cd_assinatura = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, assinatura)
    conn.commit()

def delete_assinatura(conn, assinatura):
    sql = '''DELETE FROM assinatura
                WHERE cd_assinatura = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, (assinatura,))
    conn.commit()

