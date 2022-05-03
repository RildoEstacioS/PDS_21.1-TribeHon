import Livro ,psycopg2
conn = psycopg2.connect("dbname=TribHonbass user=postgres password=Horrivel/10")
cur = conn.cursor()
def editar_Livro(new_livro = Livro, old_livro = Livro):
    if new_livro.sbn == old_livro.sbn:
        if cur.execute("SELECT * FROM livros WHERE sbn LIKE {};".format(old_livro.sbn)):
            cur.execute(
                "UPDATE livros SET titulo= {}, data_Publicavao= {}, sbn= {}, paginas= {}, genero={}, autor= {} WHERE sbn LIKE {} "
                (new_livro.titulo, new_livro.data_Publicavao, new_livro.sbn, new_livro.paginas, new_livro.genero, new_livro.autor, new_livro.sbn))
            
def buscar_Livro(genero):
        return  cur.execute("SELECT * FROM livros WHERE genero LIKE {};".format(genero))

def buscar_Livro(titulo):
    return  cur.execute("SELECT * FROM livros WHERE titulo LIKE {};".format(titulo))

def buscar_livro(nome_artistico):
    return cur.execute("SELECT * FROM livros WHERE nome_Artistico LIKE {};".format(nome_artistico))
def indicar_Livro():
    pass
def remover_Livro():
    pass
def adicionar_Livro(livro = Livro ):
    if cur.execute("SELECT * FROM livros WHERE sbn LIKE {};".format(livro.sbn)):
        cur.execute("INSERT INTO livros (titulo, data_Publicavao, sbn, paginas, genero, autor) VALUES (%s, %s, %s,%s, %s, %s)",(livro.titulo, livro.data_Publicavao, livro.sbn, livro.paginas, livro.genero, livro.autor))
