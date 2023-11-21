import hashlib

def get_usuarios(conn):
    
    sql = ''' SELECT * FROM usuario '''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.fetchall()

def get_usuario(conn, usuario):
    sql = ''' SELECT * FROM usuario 
                WHERE cd_usuario = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, (usuario,))
    conn.commit()
    return cur.fetchall()

def create_usuario(conn, usuario):
    sql = ''' INSERT INTO usuario(nome, senha, email)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (usuario[0], hashlib.md5(usuario[1].encode()).hexdigest(), usuario[2]))
    conn.commit()
    return cur.lastrowid

def update_usuario(conn, usuario):
    sql = '''UPDATE usuario
                SET nome = ?, senha = ?, email = ?
                WHERE cd_usuario = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, usuario)
    conn.commit()

def delete_usuario(conn, usuario):
    sql = '''DELETE FROM usuario
                WHERE cd_usuario = ?
        '''
    cur = conn.cursor()
    cur.execute(sql, (usuario,))
    conn.commit()

