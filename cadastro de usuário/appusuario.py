import tkinter as tk
from tkinter import ttk
from Usuario import *  # Supondo que você tenha uma classe Usuario que gerencia os dados


class Usuarios:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.janela = tk.Frame(master)
        self.janela.pack()

        self.msg = tk.Label(self.janela, text="Informe os dados:")
        self.msg["font"] = self.fontePadrao
        self.msg.pack()

        # Frames para entradas de dados
        self.janela2 = tk.Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.janela3 = tk.Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.janela4 = tk.Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.janela5 = tk.Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack()

        self.janela6 = tk.Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.janela7 = tk.Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack()

        self.janela8 = tk.Frame(master)
        self.janela8["padx"] = 20
        self.janela8.pack()

        # Campos de entrada
        self.idLabel = tk.Label(self.janela2, text="IdUsuario:", font=self.fontePadrao, width=10)
        self.idLabel.pack(side=tk.LEFT)
        self.id = tk.Entry(self.janela2)
        self.id["width"] = 12
        self.id["font"] = self.fontePadrao
        self.id.pack(side=tk.LEFT)

        self.bus = tk.Button(self.janela2)
        self.bus["text"] = "Buscar"
        self.bus["font"] = ("Calibri", "12")
        self.bus["width"] = 10
        self.bus["command"] = self.buscarUsuario
        self.bus.pack(side=tk.RIGHT)

        # Outros campos de entrada
        self.nomeLabel = tk.Label(self.janela3, text="Nome:", font=self.fontePadrao, width=10)
        self.nomeLabel.pack(side=tk.LEFT)
        self.nome = tk.Entry(self.janela3)
        self.nome["width"] = 25
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=tk.LEFT)

        self.telLabel = tk.Label(self.janela4, text="Telefone:", font=self.fontePadrao, width=10)
        self.telLabel.pack(side=tk.LEFT)
        self.tel = tk.Entry(self.janela4)
        self.tel["width"] = 25
        self.tel["font"] = self.fontePadrao
        self.tel.pack(side=tk.LEFT)

        self.emailLabel = tk.Label(self.janela5, text="E-mail:", font=self.fontePadrao, width=10)
        self.emailLabel.pack(side=tk.LEFT)
        self.email = tk.Entry(self.janela5)
        self.email["width"] = 25
        self.email["font"] = self.fontePadrao
        self.email.pack(side=tk.LEFT)

        self.usuLabel = tk.Label(self.janela6, text="Usuário:", font=self.fontePadrao, width=10)
        self.usuLabel.pack(side=tk.LEFT)
        self.usu = tk.Entry(self.janela6)
        self.usu["width"] = 25
        self.usu["font"] = self.fontePadrao
        self.usu.pack(side=tk.LEFT)

        self.senhaLabel = tk.Label(self.janela7, text="Senha:", font=self.fontePadrao, width=10)
        self.senhaLabel.pack(side=tk.LEFT)
        self.senha = tk.Entry(self.janela7)
        self.senha["width"] = 25
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=tk.LEFT)

        # Botões de ação
        self.usua = tk.Button(self.janela8)
        self.usua["text"] = "Inserir"
        self.usua["font"] = ("Calibri", "12")
        self.usua["width"] = 14
        self.usua["command"] = self.inserirUsuario
        self.usua.pack(side=tk.LEFT)

        self.cidade = tk.Button(self.janela8)
        self.cidade["text"] = "Alterar"
        self.cidade["font"] = ("Calibri", "12")
        self.cidade["width"] = 14
        self.cidade["command"] = self.alterarUsuario
        self.cidade.pack(side=tk.LEFT)

        self.clie = tk.Button(self.janela8)
        self.clie["text"] = "Excluir"
        self.clie["font"] = ("Calibri", "12")
        self.clie["width"] = 14
        self.clie["command"] = self.excluirUsuario
        self.clie.pack(side=tk.LEFT)

        # Configuração do Treeview
        self.tree = ttk.Treeview(master, columns=("IdUsuario", "Nome", "Telefone", "E-mail", "Usuário"),
                                 show='headings')
        self.tree.heading("IdUsuario", text="IdUsuario")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("E-mail", text="E-mail")
        self.tree.heading("Usuário", text="Usuário")
        self.tree.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Adicionando barra de rolagem
        self.scroll = ttk.Scrollbar(master, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scroll.set)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

    def buscarUsuario(self):
        id = self.id.get()
        user_data = self.selectUser(id)  # Suponha que esta função retorne um dicionário com os dados

        # Limpa os campos de entrada
        self.limparEntradas()

        # Atualiza os campos de entrada com os dados do usuário
        if user_data:
            self.nome.insert(tk.END, user_data['Nome'])
            self.tel.insert(tk.END, user_data['Telefone'])
            self.email.insert(tk.END, user_data['E-mail'])
            self.usu.insert(tk.END, user_data['Usuário'])
            # A senha não deve ser exibida por questões de segurança

    def inserirUsuario(self):
        user_data = {
            'IdUsuario': self.id.get(),
            'Nome': self.nome.get(),
            'Telefone': self.tel.get(),
            'E-mail': self.email.get(),
            'Usuário': self.usu.get(),
        }
        # Aqui você deve inserir o usuário no banco de dados
        self.tree.insert("", "end", values=(
        user_data['IdUsuario'], user_data['Nome'], user_data['Telefone'], user_data['E-mail'], user_data['Usuário']))
        self.limparEntradas()

    def alterarUsuario(self):
        # Implementar a lógica para alterar o usuário
        pass  # Para ser implementado

    def excluirUsuario(self):
        # Implementar a lógica para excluir o usuário
        pass  # Para ser implementado

    def limparEntradas(self):
        self.id.delete(0, tk.END)
        self.nome.delete(0, tk.END)
        self.tel.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.usu.delete(0, tk.END)
        self.senha.delete(0, tk.END)


# Inicialização da aplicação
root = tk.Tk()
root.title("Gerenciamento de Usuários")  # Título da janela
Usuarios(root)
root.geometry("800x600")  # Tamanho inicial da janela
root.mainloop()
