def get_tipos_ciclo(conn):
    sql = ''' SELECT * FROM tipo_ciclo '''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.fetchall()

def get_tipo_ciclo(conn, tipo_ciclo):
    sql = ''' SELECT * FROM tipo_ciclo 
                WHERE cd_tipo_ciclo = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, tipo_ciclo)
    conn.commit()
    return cur.fetchall()

def create_tipo_ciclo(conn, tipo_ciclo):
    sql = ''' INSERT INTO tipo_ciclo(descricao)
                VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (tipo_ciclo,))
    conn.commit()
    return cur.lastrowid

def update_tipo_ciclo(conn, tipo_ciclo):
    sql = '''UPDATE tipo_ciclo
                SET descricao = ?
                WHERE cd_tipo_ciclo = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, tipo_ciclo)
    conn.commit()

def delete_tipo_ciclo(conn, tipo_ciclo):
    sql = '''DELETE FROM tipo_ciclo
                WHERE cd_tipo_ciclo = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, (tipo_ciclo,))
    conn.commit()

