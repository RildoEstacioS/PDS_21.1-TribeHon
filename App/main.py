import DAO.DAOLeitores, DAO.DAOLivros, DAO.DAOColecoes
from Model.Leitor import Leitor
from Model.Livro import Livro
from Model.Colecao import Colecao
l = Leitor("victortt", "kkkct", "victor", "10846455439", 0 , 22)
l2 = Leitor("matheuscc", "12345", "matheus", "123455", 1, 21)
#DAO.DAOLeitores.adicionar_Leitor(l2)
genero1 = [0]
autor1 = [0]
id_livros =[1, 5]
#livro =Livro("titulo","sinopse", 20 ,340,1254388874, genero1 , autor1 )
livro1 =Livro("titulo","sinopse", 20 ,340,254136542, genero1 , autor1 )
#DAO.DAOLivros.adicionar_Livro(livro1)
#DAO.DAOColecoes.criar_Colecao(Colecao("Suspense",id_livros),2)
#DAO.DAOLivros.editar_Livro(Livro("titulo","sinopse", 20 ,340,1254388874, genero1 , autor1 ),livro)
#DAO.DAOColecoes.adicionar_livro_a_Colecao(4, id_livros)
print(DAO.DAOLeitores.buscar_leitor(2))
print(DAO.DAOLivros.buscar_livro(1254388874))
print(DAO.DAOColecoes.buscar_Colecao("pense"))
