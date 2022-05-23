import psycopg2
from  Model.Colecao import Colecao
from  Model.Leitor import Leitor
conn = psycopg2.connect("dbname=TribHonbass user=postgres password=Horrivel/10")
cur = conn.cursor()

def adicionar_livro_a_Colecao( id_colecao, colecao ):
    cur.execute("UPDATE colecao SET id_livro = ARRAY[{}] WHERE id = {} ".format(colecao, id_colecao))
    conn.commit()

def remover_Colecao(id_nome):
    #cur.execute("DELETE * FROM colecao WHERE nome LIKE {}".format(id_nome))
    cur.execute("DELETE * FROM colecao WHERE id = {}".format(id_nome))
    conn.commit()

def criar_Colecao( colecao = Colecao, id_leitor = int):
    cur.execute("INSERT INTO colecao (nome ,id_leitor, id_livro) VALUES (%s,%s, %s)", (colecao.nome ,id_leitor, colecao.id_livro))
    conn.commit()

def buscar_Colecao(id_nome):
     cur.execute("SELECT * FROM colecao WHERE nome LIKE '%{}%'".format(id_nome))
     #cur.execute("SELECT * FROM colecao WHERE nome LIKE {}".format(id_nome))
     return cur.fetchone()

