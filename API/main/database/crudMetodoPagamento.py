def get_metodos_pagamento(conn):
    sql = ''' SELECT * FROM metodo_pagamento '''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.fetchall()

def get_metodo_pagamento(conn, metodo_pagamento):
    sql = ''' SELECT * FROM metodo_pagamento 
                WHERE cd_metodo_pagamento = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, metodo_pagamento)
    conn.commit()
    return cur.fetchall()

def create_metodo_pagamento(conn, metodo_pagamento):
    sql = ''' INSERT INTO metodo_pagamento(nome, apelido)
                VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, metodo_pagamento)
    conn.commit()
    return cur.lastrowid

def update_metodo_pagamento(conn, metodo_pagamento):
    sql = '''UPDATE metodo_pagamento
                SET nome = ?, apelido = ?
                WHERE cd_metodo_pagamento = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, metodo_pagamento)
    conn.commit()

def delete_metodo_pagamento(conn, metodo_pagamento):
    sql = '''DELETE FROM metodo_pagamento
                WHERE cd_metodo_pagamento = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, (metodo_pagamento,))
    conn.commit()

