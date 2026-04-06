from conexao_post import conn

cursor_obj = conn.cursor()

sql = """
    UPDATE games
    SET NAME = %s
    WHERE ID = %s
"""

cursor_obj.execute(sql, ("Fifa 23", 2))
conn.commit()
print("Dados atualizados com sucesso")
conn.close()
