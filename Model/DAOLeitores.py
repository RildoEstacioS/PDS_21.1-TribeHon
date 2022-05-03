import Leitor, psycopg2
conn = psycopg2.connect("dbname=TribHonbass user=postgres password=Horrivel/10")
cur = conn.cursor()
def adicionar_Leitor( leitor = Leitor ):
    if validar_login(leitor.login):
        cur.execute("INSERT INTO pessoas (nome,cpf,idade) VALUES (%s, %s, %s)",( leitor.nome, leitor.cpf, leitor.idade))
        conn.commit()
        cur.execute("INSERT INTO leitores (login,senha, nivel, id_pessoa) VALUES (%s, %s, %s, %s)", (leitor.login,leitor.senha,leitor.nivel, cur.execute("SELECT id FROM pessoas WHERE cpf LIKE {};".format(leitor.cpf))))
        conn.commit()
# Metodo ainda precisa ser definido melhor como os parametros para aver uma edção

def editar_Leitores(novo_leitor, old_leitor):
    c = cur.execute("SELECT id_pessoa FROM leitores WHERE login LIKE {};".format(old_leitor.login))
    if c != None:
        cur.execute("UPDATE leitores SET login = {}, senha = {}, nivel = {} WHERE login LIKE {}".format(novo_leitor.login, novo_leitor.senha, novo_leitor.nivel, novo_leitor.login))
        cur.execute(
            "UPDATE pessoas SET nome = {}, cpf = {}, idade = {} WHERE id LIKE {}".format(novo_leitor.nome, novo_leitor.cpf, novo_leitor.idade, c))

def remover_leitor(login):
   c = cur.execute("SELECT id_pessoa FROM leitores WHERE login like {};".format(login))
   if c == None:
       cur.execute('DELETE FROM pessoas WHERE id like {}'.format(c))
       cur.execute('DELETE FROM leitores WHERE login like {}'.format(login))
       conn.commit()


def buscar_leitor(login):
    return cur.execute("SELECT * FROM pessoas WHERE login LIKE {};".format(login))

def recompesna():
    pass

def validar_login(login):
    if buscar_leitor(login) == None:
        return True
    return False

def validar_senha(senha):
    if cur.execute("SELECT * FROM pessoas WHERE senha LIKE {};".format(senha)) == None:
        return True
    return False