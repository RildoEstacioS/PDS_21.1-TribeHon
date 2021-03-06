import Model.Livro ,psycopg2
conn = psycopg2.connect("dbname=TribHonbass user=postgres password=Horrivel/10")
cur = conn.cursor()
def editar_Livro(new_livro = Model.Livro, old_livro = Model.Livro):
    if new_livro.sbn == old_livro.sbn:
        if cur.execute("SELECT * FROM livros WHERE sbn = {};".format(old_livro.sbn)):
            cur.execute(
                "UPDATE livros SET titulo= {},sinopse ={} , data_Publicavao= {}, paginas= {}, genero= ARRAY[{}], autor= ARRAY[{}] WHERE sbn = {} "
                (new_livro.titulo,new_livro.sinopse , new_livro.data_Publicavao, new_livro.paginas, new_livro.genero, new_livro.autor, new_livro.sbn))
            conn.commit()

#def buscar_Livro(genero):
    #Estamos passando para base listas contendo os id's dos generos e n os seu nomes . Fiz assim pq achei que seria mais pratico
 #   return cur.execute("SELECT * FROM livros WHERE genero[:] LIKE {};".format(cur.execute("SELECT id FROM generos WHERE genero LIKE {};".format(genero))))

def buscar_livro(sbn):
    cur.execute("SELECT * FROM livros WHERE sbn = {};".format(sbn))
    return cur.fetchone()

#def buscar_livro(nome_artistico):
#    return cur.execute("SELECT * FROM livros WHERE id_autor[:] LIKE {};".format(cur.execute("SELECT id FROM autores WHERE nome_artistico LIKE {};".format(nome_artistico))))

def remover_Livro(livro = Model.Livro):
   cur.execute("DELETE FROM livros WHERE sbn = {};".format(livro.sbn))
   conn.commit()

def adicionar_Livro(livro = Model.Livro ):
    if cur.execute("SELECT * FROM livros WHERE sbn = {};".format(livro.sbn)) == None:
        cur.execute("INSERT INTO livros (titulo, data_publicacao, sbn, paginas, id_genero, id_autor, sinopse) VALUES (%s, %s, %s,%s, ARRAY [%s], ARRAY[%s],%s)",(livro.titulo, livro.data_publicacao, livro.sbn, livro.paginas, livro.genero, livro.autor, livro.sinopse))
        conn.commit()
