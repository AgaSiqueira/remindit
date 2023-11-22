def get_notificacoes_renovacao(conn):
    sql = ''' SELECT * FROM notificacao_renovacao '''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.fetchall()

def get_notificacoes_renovacao_por_usuario(conn, cd_usuario):
    sql = ''' SELECT n.nome, n.conteudo, n.visualizado 
                FROM notificacao_renovacao n NATURAL JOIN renovacao r NATURAL JOIN usuario u
                WHERE u.cd_usuario = ?'''
    cur = conn.cursor()
    cur.execute(sql, (cd_usuario,))
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

def visualizar_notificacao_renovacao(conn, notificacao_renovacao):
    sql = '''UPDATE notificacao_renovacao
                SET visualizado = 1
                WHERE cd_notificacao_renovacao = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, (notificacao_renovacao,))
    conn.commit()

def delete_notificacao_renovacao(conn, notificacao_renovacao):
    sql = '''DELETE FROM notificacao_renovacao
                WHERE cd_notificacao_renovacao = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, (notificacao_renovacao,))
    conn.commit()




