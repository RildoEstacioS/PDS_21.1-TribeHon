from tkinter import *

tela = Tk()
tela.title("TribHon")  # Titulo da tela
tela.geometry("290x260+610+153")  # Tamanho e possição
tela.resizable(width=1, height=1)
#tela.iconbitmap('imagem\\TribHonIcone.ico')

class Tela:
    def __init__(self):
        # Criação da tela

        img_fundo = PhotoImage(file="./view/imagem/Tela.png")
        img_botaoL = PhotoImage(file="imagem\\botaoL.png")
        img_botaoC = PhotoImage(file="imagem\\botaoC.png")
        
        #Adicionar a imagem no fundo
        lab_fundo = Label(tela, image=img_fundo)
        lab_fundo.pack()

        # Adicionar botões e posição
        botaoL = Button(tela, bd=0, image=img_botaoL, command=self.TelaLogin)
        botaoL.place(width=139, height=42, x=74, y=144)

        botaoC = Button(tela, bd=0, image=img_botaoC, command=self.TelaCadastro)
        botaoC.place(width=139, height=42, x=74, y=201)
        
        tela.mainloop()  # Deixar a tela aberta

    def TelaLogin(self):

        tela.destroy()

        telaL = Tk()
        telaL.title("TribHon")  # Titulo da tela
        telaL.geometry("260x230+610+153")  # Tamanho e possição
        telaL.iconbitmap('imagem/TribHonIcone.ico')

        titulo = Label(telaL, text="Tela de Login")
        titulo["font"] = ("Arial", "20", "bold")
        titulo.pack()

        loginLabel = Label(telaL, text="Login")
        loginLabel["font"] = ("Arial", "10")
        loginLabel.pack()

        login = Entry(telaL)
        login["width"] = 25
        login.pack()

        senhaLabel = Label(telaL, text="Senha")
        senhaLabel["font"] = ("Arial", "10")
        senhaLabel.pack()

        senha = Entry(telaL, show="*")
        senha["width"] = 25
        senha.pack()

        botaoLogin = Button(telaL, text="Fazer Login", command=self.TelaPrincipal)
        botaoLogin.place(width=139, height=42, x=60, y=144)
        # botaoLogin.pack()

    def TelaCadastro(self):
        telaLivro = Tk()
        telaLivro.title("TribHon")  # Titulo da tela
        telaLivro.geometry("290x330+610+153")  # Tamanho e possição
        telaLivro.iconbitmap('imagem/TribHonIcone.ico')

        titulo = Label(telaLivro, text="Cadastrar usuário")
        titulo["font"] = ("Arial", "20", "bold")
        titulo.pack()

        loginLabel = Label(telaLivro, text="Login")
        loginLabel["font"] = ("Arial", "10")
        loginLabel.pack()

        login = Entry(telaLivro)
        login["width"] = 25
        login.pack()

        nomeLabel = Label(telaLivro, text="Nome")
        nomeLabel["font"] = ("Arial", "10")
        nomeLabel.pack()

        nome = Entry(telaLivro)
        nome["width"] = 25
        nome.pack()

        cpfLabel = Label(telaLivro, text="CPF")
        cpfLabel["font"] = ("Arial", "10")
        cpfLabel.pack()

        cpf = Entry(telaLivro)
        cpf["width"] = 25
        cpf.pack()

        idadeLabel = Label(telaLivro, text="Idade")
        idadeLabel["font"] = ("Arial", "10")
        idadeLabel.pack()

        idade = Entry(telaLivro)
        idade["width"] = 25
        idade.pack()

        senhaLabel = Label(telaLivro, text="Senha")
        senhaLabel["font"] = ("Arial", "10")
        senhaLabel.pack()

        senha = Entry(telaLivro, show="*")
        senha["width"] = 25
        senha.pack()

        botaoLogin = Button(telaLivro, text="Fazer Login")
        botaoLogin.place(width=139, height=42, x=75, y=260)
        # botaoLogin.pack()

        tela.destroy()

    def TelaPrincipal(self):

        telaMenu = Tk()
        telaMenu.title("TribHon")  # Titulo da tela
        telaMenu.geometry("290x330+610+153")  # Tamanho e possição
        telaMenu.iconbitmap('imagem/TribHonIcone.ico')

        titulo = Label(telaMenu, text="Menu")
        titulo["font"] = ("Arial", "20", "bold")
        titulo.pack()

        senhaLabel = Label(telaMenu, text="Buscar Livro")
        senhaLabel["font"] = ("Arial", "10")
        senhaLabel.pack()

        senha = Entry(telaMenu)
        senha["width"] = 25
        senha.pack()

        botaoLogin = Button(telaMenu, text="Buscar")
        botaoLogin.place(width=100, height=25, x=95, y=82)

        botaoLogin = Button(telaMenu, text="Criar Coleção")
        botaoLogin.place(width=139, height=42, x=75, y=132)

        botaoLogin = Button(telaMenu, text="Manter Leitor")
        botaoLogin.place(width=139, height=42, x=75, y=182)

        botaoLogin = Button(telaMenu, text="Atualizar Livro")
        botaoLogin.place(width=139, height=42, x=75, y=232)


