from os import stat
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk

class AdminJanela():

    def ItensPedidoBackEnd(self):
        IdPedido = self.IdPedido

        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                db='comprasonline',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro ao conectar ao banco de dados')


        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidoitem where fk_id_pedido = {}'.format(IdPedido))
                conexao.commit()
                resultados = cursor.fetchall()
        except:
            print('erro ao fazer a consulta')

        self.tree2.delete(*self.tree2.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['fk_id_pedido'])
            linhaV.append(linha['fk_id_produto'])
            
            self.tree2.insert("", END, values=linhaV, tag='1')

            linhaV.clear()

    def ItensPedido(self):
        self.itenspedido = Tk()
        self.itenspedido.title('Itens')
        self.itenspedido['bg'] = '#524f4f'
        self.itenspedido.resizable(False, False)

        Label(self.itenspedido, text='Itens', bg='#524f4f', fg='white').grid(row=0, column=4, columnspan=4, padx=5, pady=5)

        self.IdPedido = int(self.tree.selection()[0])

        self.tree2 = ttk.Treeview(self.itenspedido, selectmode="browse", column=("column1", "column2"), show='headings')

        self.tree2.column("column1", width=80, minwidth=500, stretch=NO)
        self.tree2.heading('#1', text='Id Pedido')

        self.tree2.column("column2", width=80, minwidth=500, stretch=NO)
        self.tree2.heading('#2', text='Id Produto')

        self.tree2.grid(row=1, column=4, padx=10, pady=10, columnspan=3, rowspan=6)

        self.ItensPedidoBackEnd()

        self.itenspedido.mainloop()




    def PedidosClienteBackEnd(self):
        CodigoPedido = self.CodigoPedido

        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                db='comprasonline',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro ao conectar ao banco de dados')


        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidos where fk_nome = "{}"'.format(CodigoPedido))
                conexao.commit()
                resultados = cursor.fetchall()
        except:
            print('erro ao fazer a consulta')

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['id_pedido'])
            linhaV.append(linha['fk_nome'])
            linhaV.append(linha['status_pedido'])
            
            self.tree.insert("", END, values=linhaV, iid=linha['id_pedido'], tag='1')

            linhaV.clear()

    def PedidosCliente(self):
        self.pedidoscliente = Tk()
        self.pedidoscliente.title('Pedidos')
        self.pedidoscliente['bg'] = '#524f4f'
        self.pedidoscliente.resizable(False, False)

        Label(self.pedidoscliente, text='Pedidos', bg='#524f4f', fg='white').grid(row=0, column=4, columnspan=4, padx=5, pady=5)

        Button(self.pedidoscliente, text='Ver itens do pedido', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.ItensPedido).grid(row=5, column=0, padx=5, pady=5)

        self.CodigoPedido = self.tree1.selection()[0]

        self.tree = ttk.Treeview(self.pedidoscliente, selectmode="browse", column=("column1", "column2", "column3"), show='headings')

        self.tree.column("column1", width=50, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='id')

        self.tree.column("column2", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Nome Cliente')

        self.tree.column("column3", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Status')

        self.tree.grid(row=1, column=4, padx=10, pady=10, columnspan=3, rowspan=6)

        self.PedidosClienteBackEnd()

        self.pedidoscliente.mainloop()

    def PedidosBackEnd(self):

        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                db='comprasonline',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro ao conectar ao banco de dados')


        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultados = cursor.fetchall()
        except:
            print('erro ao fazer a consulta')

        self.tree1.delete(*self.tree1.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])
            linhaV.append(linha['status_cliente'])
            
            self.tree1.insert("", END, values=linhaV, iid=linha['nome'], tag='1')

            linhaV.clear()

    def Pedidos(self):
        self.pedidos = Tk()
        self.pedidos.title('Gerenciar pedidos')
        self.pedidos['bg'] = '#524f4f'

        self.pedidos.resizable(False, False)
        Label(self.pedidos, text='Selecione o cliente para ver os pedidos', bg='#524f4f', fg='white').grid(row=0, column=4, columnspan=4, padx=5, pady=5)

        Button(self.pedidos, text='Ver pedidos', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.PedidosCliente).grid(row=5, column=0, padx=5, pady=5)

        self.tree1 = ttk.Treeview(self.pedidos, selectmode="browse", column=("column1", "column2"), show='headings')

        self.tree1.column("column1", width=100, minwidth=500, stretch=NO)
        self.tree1.heading('#1', text='Nome')

        self.tree1.column("column2", width=100, minwidth=500, stretch=NO)
        self.tree1.heading('#2', text='Status')

        self.tree1.grid(row=1, column=4, padx=10, pady=10, columnspan=3, rowspan=6)

        self.PedidosBackEnd()

        self.pedidos.mainloop()

    def CadastrarProduto(self):
        self.cadastrar = Tk()
        self.cadastrar.title('Gerenciar produtos')
        self.cadastrar['bg'] = '#524f4f'

        Label(self.cadastrar, text='Cadastre produtos', bg='#524f4f', fg='white').grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        Label(self.cadastrar, text='Nome', bg='#524f4f', fg='white').grid(row=1, column=0, columnspan=1,padx=5, pady=5)
        self.nome = Entry(self.cadastrar)
        self.nome.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Marca', bg='#524f4f', fg='white').grid(row=2, column=0, columnspan=1,padx=5, pady=5)
        self.marca = Entry(self.cadastrar)
        self.marca.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Departamento', bg='#524f4f', fg='white').grid(row=3, column=0, columnspan=1,padx=5, pady=5)
        self.departamento = Entry(self.cadastrar)
        self.departamento.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

        Label(self.cadastrar, text='Preço', bg='#524f4f', fg='white').grid(row=4, column=0, columnspan=1,padx=5, pady=5)
        self.preco = Entry(self.cadastrar)
        self.preco.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

        Button(self.cadastrar, text='Cadastrar', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.CadastrarProdutoBackEnd).grid(row=5, column=0, padx=5, pady=5)
        Button(self.cadastrar, text='Excluir', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.RemoverCadastrosBackEnd).grid(row=5, column=1, padx=5, pady=5)
        Button(self.cadastrar, text='Atualizar', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.CadastrarProdutoBackEnd).grid(row=6, column=0, padx=5, pady=5)

        self.tree = ttk.Treeview(self.cadastrar, selectmode="browse", column=("column1", "column2", "column3", "column4", "column5", "column6"), show='headings')
        
        self.tree.column("column1", width=200, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("column2", width=200, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Marca')

        self.tree.column("column3", width=200, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Departamento')

        self.tree.column("column4", width=60, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Preço')

        self.tree.grid(row=0, column=4, padx=10, pady=10, columnspan=3, rowspan=6)

        self.MostrarProdutosBackEnd()

        self.cadastrar.mainloop()

    def __init__(self):
        self.root = Tk()
        self.root.title('ADMIN')

        Button(self.root, text='Pedidos', width=20, bg='#A29E9E', command=self.Pedidos).grid(row=0, column=0, padx=10, pady=10)
        Button(self.root, text='Editar produtos', width=20, bg='#A29E9E', command=self.CadastrarProduto).grid(row=1, column=0, padx=10, pady=10)

        self.root.mainloop()

    def MostrarProdutosBackEnd(self):
        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                db='comprasonline',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro ao conectar ao banco de dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from produtos')
                resultados = cursor.fetchall()
        except:
            print('erro ao fazer a consulta')

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])
            linhaV.append(linha['marca'])
            linhaV.append(linha['departamento'])
            linhaV.append(linha['preco'])
        
            self.tree.insert("", END, values=linhaV, iid=linha['id_produto'], tag='1')

            linhaV.clear()

    def CadastrarProdutoBackEnd(self):
        nome = self.nome.get()
        marca = self.marca.get()
        departamento = self.departamento.get()
        preco = self.preco.get()

        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                db='comprasonline',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro ao conectar ao banco de dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('insert into produtos (nome, marca,departamento, preco) values (%s, %s, %s, %s)', (nome, marca,departamento, preco))
                conexao.commit()
        except:
            print('erro ao fazer a consulta')
        
        self.MostrarProdutosBackEnd()

    def RemoverCadastrosBackEnd(self):
        idDeletar = int(self.tree.selection()[0])

        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                db='comprasonline',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro ao conectar ao banco de dados')

        try:
            with conexao.cursor() as cursor:
                cursor.execute('delete from produtos where id_produto = {}'.format(idDeletar))
                conexao.commit()
        except:
            print('erro ao fazer a consulta')
        
        self.MostrarProdutosBackEnd()


class JanelaLogin():

    def VerificaLogin(self):
        autenticado = False
        usuarioMaster = False


        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                db='comprasonline',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro ao conectar ao banco de dados')

        usuario = self.login.get()
        senha = self.senha.get()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultados = cursor.fetchall()
        except:
            print('erro ao fazer a consulta')
        
        for linha in resultados:
            if usuario == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False
        
        if not autenticado:
            messagebox.showinfo('login', 'Email ou senha invalido')

        if autenticado:
            #self.root.destroy()
            if usuarioMaster:
                AdminJanela()
            else:
                self.UsuarioJanela()
            

    def CadastroBackEnd(self):
        if len(self.login.get()) <= 20:
            if(len(self.senha.get())) <= 50:
                nome = self.login.get()
                senha = self.senha.get()
                usuarioweb = self.usuarioWeb.get()
                autorizado = 1

                try:
                    conexao = pymysql.connect(

                        host='localhost',
                        user='root',
                        db='comprasonline',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor
                    )
                except:
                    print('erro ao conectar ao banco de dados')

                try:
                    with conexao.cursor() as cursor:
                        cursor.execute('select * from cadastros')
                        resultados = cursor.fetchall()

                    for linha in resultados:
                        if linha['nome'] == nome:
                            autorizado = 0
                            break

                    with conexao.cursor() as cursor:
                        if autorizado == 1:
                            cursor.execute('Insert into cadastros (nome, senha, usuarioweb, status_cliente, nivel) values (%s, %s, %s, "novo", %s)', (nome, senha, usuarioweb, 1))
                            cursor.execute('Insert into carrinho (fk_nome_carrinho) values (%s)', (nome))
                            global FkIdCarrinho
                            FkIdCarrinho = cursor.lastrowid
                            conexao.commit()
                            messagebox.showinfo('Cadastro', 'Usuário cadastrado com sucesso')
                        else:
                            messagebox.showinfo('Cadastro', 'Esse nome já existe')
                    

                except:
                    print('erro ao inserir dados')
            else:
                messagebox.showinfo('ERRO', 'Senha grande de mais')
        else:
            messagebox.showinfo('ERRO', 'Nome grande de mais')

    def Cadastro(self):
        Label(self.root, text='É usuário Web?').grid(row=3, column=0, padx=5, pady=5)
        listusuarioWeb = ["sim", "não"]
        self.usuarioWeb = StringVar()
        self.usuarioWeb.set(listusuarioWeb[0])
        OptionMenu(self.root, self.usuarioWeb, *listusuarioWeb).grid(row=3, column=1)

        Button(self.root, text='confirmar cadastro', width=15, bg='blue1', command=self.CadastroBackEnd).grid(row=5, column=0, columnspan=3, padx=10, pady=5)
    
    def UpdateBackEnd(self):
        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                db='comprasonline',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro ao conectar ao banco de dados')


        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from cadastros')
                resultados = cursor.fetchall()
        except:
            print('erro ao fazer a consulta')

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])
            linhaV.append(linha['senha'])
            linhaV.append(linha['usuarioweb'])
            linhaV.append(linha['status_cliente'])
            linhaV.append(linha['nivel'])
            
            self.tree.insert("", END, values=linhaV, iid=linha['nome'], tag='1')

            linhaV.clear()

    def VisualizarCadastros(self):
        self.vc = Toplevel()
        self.vc.resizable(False, False)
        self.vc.title('Visualizar cadastros')

        self.tree = ttk.Treeview(self.vc, selectmode="browse", column=("column1", "column2", "column3", "column4", "column5"), show='headings')

        self.tree.column("column1", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("column2", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Senha')

        self.tree.column("column3", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Usuário Web')
        
        self.tree.column("column4", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='status')

        self.tree.column("column5", width=40, minwidth=500, stretch=NO)
        self.tree.heading('#5', text='Nível')

        self.tree.grid(row=0, column=0, padx=10, pady=10)

        self.UpdateBackEnd()

        self.vc.mainloop()

    def __init__(self):
        self.root = Tk()
        self.root.title('Login')
        Label(self.root, text = 'Faça o login').grid(row=0, column=0, columnspan=2)

        Label(self.root, text = 'Usuário').grid(row=1, column=0)

        self.login = Entry(self.root)
        self.login.grid(row=1, column=1, padx=5, pady=5)

        Label(self.root, text = 'Senha').grid(row=2, column=0)

        self.senha = Entry(self.root, show='*')
        self.senha.grid(row=2, column=1, padx=5, pady=5)

        Button(self.root, text='login', bg='blue1', width=8, command=self.VerificaLogin).grid(row=6, column=0, padx=5, pady=5)
        Button(self.root, text='cadastre-se', bg='green1', width=8, command=self.Cadastro).grid(row=6, column=1, padx=5, pady=5)
        
        Button(self.root, text='Visualizar cadastros', bg='white', command=self.VisualizarCadastros).grid(row=7, column=0, columnspan=2,padx=5, pady=5)
        self.root.mainloop()


    def TabelaProdutosBackEnd(self):
        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                db='comprasonline',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro ao conectar ao banco de dados')


        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from produtos')
                resultados = cursor.fetchall()
        except:
            print('erro ao fazer a consulta')

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])
            linhaV.append(linha['marca'])
            linhaV.append(linha['departamento'])
            linhaV.append(linha['preco'])
            
            self.tree.insert("", END, values=linhaV, iid=linha['id_produto'], tag='1')

            linhaV.clear()

    def AdicionarCarrinhoBackEnd(self):

        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                db='comprasonline',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro ao conectar ao banco de dados')

        idAdicionar = int(self.tree.selection()[0])
        nome = self.login.get()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from carrinho')
                resultados = cursor.fetchall()
                for linha in resultados:
                    if nome == linha['fk_nome_carrinho']:
                        IdCarrinho = linha['id_carrinho']
                        break
                cursor.execute('Insert into carrinhoitem (fk_id_carrinho, fk_id_produto_carrinho) values (%s, %s)', (IdCarrinho, idAdicionar))
                conexao.commit()
            messagebox.showinfo('Usuário', 'Item inserido no carrinho.')
        except:
            print('erro ao fazer a consulta')

    def VisualizarCarrinhoBackEnd(self):
        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                db='comprasonline',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro ao conectar ao banco de dados')

        nome = self.login.get()


        try:
            with conexao.cursor() as cursor:

                cursor.execute('select * from carrinho')
                resultados = cursor.fetchall()
                for linha in resultados:
                    if nome == linha['fk_nome_carrinho']:
                        IdCarrinho = linha['id_carrinho']
                        break

                cursor.execute('select * from carrinhoitem where fk_id_carrinho = {}'.format(IdCarrinho))
                resultados = cursor.fetchall()
        except:
            print('erro ao fazer a consulta')

        self.tree3.delete(*self.tree3.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['fk_id_carrinho'])
            linhaV.append(linha['fk_id_produto_carrinho'])
            
            self.tree3.insert("", END, values=linhaV, tag='1')

            linhaV.clear()

    def Comprar(self):
        try:
            conexao = pymysql.connect(

                host='localhost',
                user='root',
                db='comprasonline',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('erro ao conectar ao banco de dados')

        nome = self.login.get()

        try:
            with conexao.cursor() as cursor:

                cursor.execute('select * from carrinho')
                resultados = cursor.fetchall()
                for linha in resultados:
                    if nome == linha['fk_nome_carrinho']:
                        IdCarrinho = linha['id_carrinho']
                        break

                cursor.execute('insert into pedidos (fk_nome, status_pedido) values (%s, "Confirmado")', (self.login.get()))
                lastid = cursor.lastrowid
                cursor.execute('select * from carrinhoitem where fk_id_carrinho = {}'.format(FkIdCarrinho))
                resultados = cursor.fetchall()
                for linha in resultados:
                    cursor.execute('Insert into pedidoitem values (%s, %s)', (lastid, linha['fk_id_produto_carrinho']))

                cursor.execute('delete from carrinhoitem where fk_id_carrinho = {}'.format(IdCarrinho))
                conexao.commit()
            messagebox.showinfo('Compra', 'Compra feita com sucesso!')
            self.visualizar.destroy()
        except:
            print('erro ao fazer a consulta')

    def VisualizarCarrinho(self):
        self.visualizar = Tk()
        self.visualizar.title('Carrinho')

        Button(self.visualizar, text='Comprar', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.Comprar).grid(row=5, column=0, padx=5, pady=5)

        self.tree3 = ttk.Treeview(self.visualizar, selectmode="browse", column=("column1", "column2"), show='headings')

        self.tree3.column("column1", width=100, minwidth=500, stretch=NO)
        self.tree3.heading('#1', text='Id Carrinho')

        self.tree3.column("column2", width=100, minwidth=500, stretch=NO)
        self.tree3.heading('#2', text='Id produto')

        self.tree3.grid(row=0, column=0, padx=10, pady=10)

        self.VisualizarCarrinhoBackEnd()

    def UsuarioJanela(self):
        
        self.usuario = Tk()
        self.usuario.title('Conta')
        Button(self.usuario, text='Adicionar no carrinho', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.AdicionarCarrinhoBackEnd).grid(row=5, column=0, padx=5, pady=5)
        Button(self.usuario, text='Ver carrinho', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.VisualizarCarrinho).grid(row=6, column=0, padx=5, pady=5) 

        self.tree = ttk.Treeview(self.usuario, selectmode="browse", column=("column1", "column2", "column3", "column4"), show='headings')

        self.tree.column("column1", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("column2", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Marca')

        self.tree.column("column3", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Departamento')

        self.tree.column("column4", width=50, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Preço')

        self.tree.grid(row=0, column=0, padx=10, pady=10)

        self.TabelaProdutosBackEnd()

        self.usuario.mainloop()

JanelaLogin()