def get_notificacoes_renovacao(conn):
    sql = ''' SELECT * FROM notificacao_renovacao '''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.fetchall()

def get_notificacao_renovacao(conn, notificacao_renovacao):
    sql = ''' SELECT * FROM notificacao_renovacao 
                WHERE cd_notificacao_renovacao = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, notificacao_renovacao)
    conn.commit()
    return cur.fetchall()

def create_notificacao_renovacao(conn, notificacao_renovacao):
    sql = ''' INSERT INTO notificacao_renovacao(nome, conteudo, visualizado)
                VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, notificacao_renovacao)
    conn.commit()
    return cur.lastrowid

def update_notificacao_renovacao(conn, notificacao_renovacao):
    sql = '''UPDATE notificacao_renovacao
                SET nome = ?, conteudo = ?, visualizado = ?
                WHERE cd_notificacao_renovacao = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, notificacao_renovacao)
    conn.commit()

def delete_notificacao_renovacao(conn, notificacao_renovacao):
    sql = '''DELETE FROM notificacao_renovacao
                WHERE cd_notificacao_renovacao = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, (notificacao_renovacao,))
    conn.commit()




