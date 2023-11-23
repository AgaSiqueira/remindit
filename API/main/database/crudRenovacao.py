def get_renovacoes(conn):
    sql = ''' SELECT * FROM renovacao '''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.fetchall()

def get_renovacoes_por_usuario(conn, cd_usuario):
    sql = ''' SELECT r.cd_renovacao, r.data, r.valor, r.ativo, r.cd_assinatura, r.cd_notificacao_renovacao, a.nome FROM renovacao r NATURAL JOIN assinatura a
            WHERE a.cd_usuario = ?'''
    cur = conn.cursor()
    cur.execute(sql, (cd_usuario,))
    conn.commit()
    return cur.fetchall()

def get_renovacoes_por_assinatura(conn, cd_assinatura):
    sql = ''' SELECT * FROM renovacao
            WHERE cd_assinatura = ?'''
    cur = conn.cursor()
    cur.execute(sql, (cd_assinatura,))
    conn.commit()
    return cur.fetchall()

def get_renovacao(conn, renovacao):
    sql = ''' SELECT * FROM renovacao 
                WHERE cd_renovacao = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, renovacao)
    conn.commit()
    return cur.fetchall()

def create_renovacao(conn, renovacao):
    sql = ''' INSERT INTO renovacao(data, valor, ativo, 
                cd_assinatura, cd_notificacao_renovacao)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, renovacao)
    conn.commit()
    return cur.lastrowid

def update_renovacao(conn, renovacao):
    sql = '''UPDATE assinatura
                SET data = ?, valor = ?, ativo = ?, 
                cd_assinatura = ?, cd_notificacao_renovacao = ?
                WHERE cd_renovacao = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, renovacao)
    conn.commit()

def delete_renovacao(conn, renovacao):
    sql = '''DELETE FROM renovacao
                WHERE cd_renovacao = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, (renovacao,))
    conn.commit()

