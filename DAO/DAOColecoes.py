import Model.Colecao, Model.Leitor, psycopg2
conn = psycopg2.connect("dbname=TribHonbass user=postgres password=Horrivel/10")
cur = conn.cursor()

def adicionar_livro_a_Colecao(colecao = Model.Colecao):
    cur.execute("UPDATE colecao SET nome = {}, id_leitor = {}, id_livro = ARRAY[{}] WHERE nome LIKE {} ".format(colecao.nome, colecao.id_leitor, colecao.id_livro))
    conn.commit()

def remover_Colecao(nome):
    return cur.execute("DELETE * FROM colecao WHERE nome LIKE {}".format(nome))

def criar_Colecao( colecao = Model.Colecao, leitor = Model.Leitor):
    cur.execute("INSERT INTO colecao (nome ,id_leitor, id_livro) VALUES (%s,%s, %s)", (colecao.nome, colecao.id_livros, cur.execute("SELECT id FROM leitor WHERE login LIKE {}".format(leitor.login))))
    conn.commit()

def buscar_Colecao(nome):
    return cur.execute("SELECT * FROM colecao WHERE nome LIKE {}".format(nome))
