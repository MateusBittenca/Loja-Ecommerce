from prettytable import PrettyTable
import mysql.connector

def abrebanco():
    try:
    
        global conexao
        conexao = mysql.connector.Connect(host='localhost',database='loja',
        user='root', password='')
            # testando se estamos conectado ao banco de dados
        if conexao.is_connected():
            informacaobanco = conexao.get_server_info()
            print(f'Conectado ao servidor banco de dados - Versão {informacaobanco}')
            print('Conexão ok')
            # criando objeto cursor, responsável para trabalharmos com registros retornados pela tabela fisica
            
            global comandosql
            comandosql = conexao.cursor()
            # Criando uma QUERY para mostrar as informações do banco de dados ao qual nos conectamos
            
            comandosql.execute('select database();')
            # usando método fetchone para buscar um dado do banco de dados e armazenálo na variável nomebanco
            
            nomebanco = comandosql.fetchone()
            print(f'Banco de dados acessado = {nomebanco}')
            print('='*80)
            return 1
        else:
            print('Conexão não realizada com banco')
        return 0
    except Exception as erro:
        print(f'Erro : {erro}')
        return 0 
    




    
def mostraCliente():
   
    grid = PrettyTable(['ID do Cliente', "Nome", "Email", "Endereço" , "Telefone" ])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from clientes')
        
        tabela = comandosql.fetchall()
    
       
        if comandosql.rowcount > 0:

            for registro in tabela:
      
                grid.add_row([registro[0], registro[1] , registro[2] , registro[3], registro[4]])
         
            print(grid)
        else:
            print('Não existem informações cadastradas nessa tabela !!!')
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')




def consultarCliente(idcliente = 0):
    try:
        grid = PrettyTable(['ID do Cliente', "Nome", "Email", "Endereço","Telefone" ])
        comandosql = conexao.cursor()
       
        comandosql.execute(f'select * from  clientes  where cliente_id = {idcliente};')
           
        tabelaconsulta = comandosql.fetchall()
        for registro in tabelaconsulta:
            grid.add_row([registro[0], registro[1] , registro[2] , registro[3],registro[4]])
         
            print(grid)
     
        conexao.commit()


    except Exception as erro :
        print(f'Erro: {erro}')
        return 'Não foi possível consultar  !!!'
    

  

def cadastrarCliente(idcliente = 0, nome = ' ', email = '' , endereco = '' , telefone = 0):
    try:
        comandosql = conexao.cursor()
      

        comandosql.execute(f'insert into clientes (cliente_id, nome , email , endereco, telefone) values({idcliente}, "{nome}", "{email}", "{endereco}", {telefone})')


        conexao.commit()
        return 'Cadastro realizado com sucesso !!!! '
    except Exception as erro :
        print(f'Erro: {erro}')
        return 'Não foi possível realizar o cadastro !!!'
    
    


def alterarCliente(idcliente = 0, nome = ' ', email = '' , endereco = '' , telefone = 0):
    try:
        comandosql = conexao.cursor()
       
        comandosql.execute(f'UPDATE clientes SET nome ="{nome}", email="{email}", endereco="{endereco}", telefone={telefone} WHERE cliente_id ={idcliente};')

        
        conexao.commit()
        return 'Cliente  alterado com sucesso !!!'
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível alterar o cliente '




def excluirCliente(idcliente = 0):
    try:
        conexao.cursor()

        comandosql.execute(f'delete from clientes where cliente_id = {idcliente};')

        conexao.commit()
        return 'Cliente excluido com sucesso'
    except Exception as erro:
        print (f'Erro: {erro}')
    return 'Não foi possível excluir !!' 



    















def mostraProdutos():
   
    grid = PrettyTable(['ID do Produto', "Nome", "Preço", "Quantidade - Estoque" , " ID da Categoria" ])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from produtos')
        
        tabela = comandosql.fetchall()
    
       
        if comandosql.rowcount > 0:

            for registro in tabela:
      
                grid.add_row([registro[0], registro[1] , registro[2] , registro[3] , registro[4]])
         
            print(grid)
        else:
            print('Não existem produtos cadastrados nessa tabela !!!')
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')



def consultarProdutos(idproduto = 0):
    try:
        
        comandosql = conexao.cursor()
       
        comandosql.execute(f'select * from  produtos  where produto_id = {idproduto};')
           
        tabelaconsulta = comandosql.fetchall()
        for registro in tabelaconsulta:
            grid = PrettyTable(['ID do Produto', "Nome", "Preço", "Quantidade - Estoque" , " ID da Categoria" ])
            grid.add_row([registro[0], registro[1] , registro[2] , registro[3] , registro[4]])
         
            print(grid)
        conexao.commit()


    except Exception as erro :
        print(f'Erro: {erro}')
        return 'Não foi possível consultar  !!!'
    

def cadastrarProduto(idproduto = 0, nomeproduto = ' ', preco = 0 , qtd = 0 , idcategoria = 0):
    try:
        comandosql = conexao.cursor()
      

        comandosql.execute(f'insert into produtos (produto_id, nome , preco , quantidade_estoque,categoria_id) values({idproduto}, "{nomeproduto}", {preco}, {qtd}, {idcategoria})')



        conexao.commit()
        return 'Produto cadastrado com sucesso !!!! '
    except Exception as erro :
        print(f'Erro: {erro}')
        return 'Não foi possível realizar o cadastro !!!'
    


def alterarProduto(idproduto = 0, nomeproduto = ' ', preco = 0 , qtd = 0 , idcategoria = 0):
    try:
        comandosql = conexao.cursor()
       
        comandosql.execute(f'UPDATE produtos SET nome = "{nomeproduto}", preco={preco}, quantidade_estoque = {qtd}, categoria_id = {idcategoria} WHERE produto_id = {idproduto};')

        
        conexao.commit()
        return 'Produto  alterado com sucesso !!!'
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível alterar o produto '






    
def excluirProduto(idproduto = 0):
    try:
        comandosql = conexao.cursor()

        comandosql.execute(f'delete from produtos where produto_id = {idproduto};')

        conexao.commit()
        return 'Produto excluido com sucesso'
    except Exception as erro:
        print (f'Erro: {erro}')
    return 'Não foi possível excluir !!' 


    















def mostraCategoria():
   
    grid = PrettyTable(['ID da Categoria', "Nome", "Descrição" ])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from categorias')
        
        tabela = comandosql.fetchall()
    
       
        if comandosql.rowcount > 0:

            for registro in tabela:
      
                grid.add_row([registro[0], registro[1] , registro[2]])
         
            print(grid)
        else:
            print('Não existem categorias cadastradas nessa tabela !!!')
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')


def consultarCategoria(idcategoria = 0):
    try:
        
        comandosql = conexao.cursor()
       
        comandosql.execute(f'select * from  categorias  where categoria_id = {idcategoria};')
           
        tabelaconsulta = comandosql.fetchall()
        for registro in tabelaconsulta:
            grid = PrettyTable(['ID da Categoria', "Nome", " Descrição" ])
            grid.add_row([registro[0], registro[1] , registro[2]])
         
            print(grid)
     
        conexao.commit()


    except Exception as erro :
        print(f'Erro: {erro}')
        return 'Não foi possível consultar  !!!'
    

    
def cadastrarCategoria (idcategoria = 0 , nomecategoria = '' , descricao = ''):
    try:
        comandosql = conexao.cursor()
      

        comandosql.execute(f'insert into categorias (categoria_id, nome, descricao) values({idcategoria}, "{nomecategoria}", "{descricao}")')



        conexao.commit()
        return ' Categoria cadastrada com sucesso !!!! '
    except Exception as erro :
        print(f'Erro: {erro}')
        return 'Não foi possível realizar o cadastro !!!'
    


def alterarCategoria(idcategoria = 0 , nomecategoria = '' , descricao = ''):
    try:
        comandosql = conexao.cursor()
       
        comandosql.execute(f'UPDATE produtos SET nome ="{nomecategoria}", descricao = "{descricao}" WHERE categoria_id ={idcategoria};')

        
        conexao.commit()
        return 'Categoria  alterado com sucesso !!!'
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível alterar o cliente '



    

def excluirCategoria(idcategoria = 0):
    try:
        comandosql = conexao.cursor()

        comandosql.execute(f'delete from categorias where categoria_id = {idcategoria}')

        conexao.commit()
        return ' Categoria excluida com sucesso !!!! '
    except Exception as erro :
        print(f'Erro: {erro}')
        return 'Não foi possível realizar a exclusão !!!'
    

    











def mostraPedidos():
   
    grid = PrettyTable(['ID do Pedido', "ID do Cliente", "Data" , "Status" ])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'select * from pedidos')
        
        tabela = comandosql.fetchall()
    
       
        if comandosql.rowcount > 0:

            for registro in tabela:
      
                grid.add_row([registro[0], registro[1] , registro[2] , registro[3]])
         
            print(grid)
        else:
            print('Não existem  pedidos cadastrados nessa tabela !!!')
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')



def consultarPedidos(idpedido = 0):
    try:
        
        comandosql = conexao.cursor()
       
        comandosql.execute(f'select * from  pedidos  where pedido_id = {idpedido};')
           
        tabelaconsulta = comandosql.fetchall()
        for registro in tabelaconsulta:
            grid = PrettyTable(['ID do Pedido', "ID do Cliente ", "Data" , "Status " ])
            grid.add_row([registro[0], registro[1] , registro[2],registro [3]])
         
            print(grid)
     
        conexao.commit()


    except Exception as erro :
        print(f'Erro: {erro}')
        return 'Não foi possível consultar  !!!'
    
def cadastrarPedidos (idpedido = 0 , idcliente = 0 , data = '', status = ''):
    try:
        comandosql = conexao.cursor()
      

        comandosql.execute(f'insert into pedidos (pedido_id, cliente_id, data_pedido, status) values({idpedido}, {idcliente}, "{data}", "{status}")')



        conexao.commit()
        return ' Pedido cadastrado com sucesso !!!! '
    except Exception as erro :
        print(f'Erro: {erro}')
        return 'Não foi possível realizar o cadastro !!!'
    


def alterarPedidos(idpedido = 0 , idcliente = 0 , data = '', status = ''):
    try:
        comandosql = conexao.cursor()
       
        comandosql.execute(f'UPDATE produtos SET cliente_id = {idcliente} , data_pedido = "{data}" , status = "{status}" WHERE pedido_id ={idpedido};')

        
        conexao.commit()
        return 'Pedido alterado com sucesso !!!'
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível alterar o cliente '
    


def excluirPedidos(idpedido = 0):
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'delete from pedidos where pedido_id = {idpedido}')
        conexao.commit()
        
        return ' Categoria excluida com sucesso !!!! '
    except Exception as erro :
        print(f'Erro: {erro}')
        return 'Não foi possível realizar a exclusão !!!'



#'''
#========================================= JOINS
#===============================================
#'''


def join1(id_pedido = 0):

    grid = PrettyTable(['pedido_ID', "Data_pedido", "Status", "nome_cliente", "email" ])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'SELECT P.pedido_id, P.data_pedido, P.status, C.nome AS cliente_nome,C.email FROM Pedidos P INNER JOIN Clientes C ON P.cliente_id = C.cliente_id WHERE C.cliente_id = {id_pedido};')
        
        tabela = comandosql.fetchall()
    
       
        if comandosql.rowcount > 0:

            for registro in tabela:
      
                grid.add_row([registro[0], registro[1] , registro[2],registro[3], registro[4]])
         
            print(grid)
        else:
            print('Não exite nenhum pedido com este ID !!!')
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')


def join2(id_categoria = 0):

    grid = PrettyTable(['produto_id', "produto_nome", "preço", "categoria" ])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'SELECT P.produto_id, P.nome AS produto_nome, P.preco, C.nome AS categoria_nome FROM Produtos P INNER JOIN Categorias C ON P.categoria_id = C.categoria_id WHERE C.categoria_id ={id_categoria};')
        
        tabela = comandosql.fetchall()
    
       
        if comandosql.rowcount > 0:

            for registro in tabela:
      
                grid.add_row([registro[0], registro[1] , registro[2],registro[3]])
         
            print(grid)
        else:
            print('Não exite nenhuma categoria com este ID !!!')
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')
        
            
def join3(id_cliente = 0):
    
    grid = PrettyTable(['produto_id', "data_pedido", "status", "cliente_nome", "produto_nome" ])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'SELECT P.pedido_id, P.data_pedido, P.status, C.nome AS cliente_nome, Pr.nome AS produto_nome FROM Pedidos P INNER JOIN Clientes C ON P.cliente_id = C.cliente_id INNER JOIN Produtos Pr ON P.pedido_id = Pr.produto_id WHERE C.cliente_id = {id_cliente};')
        
        tabela = comandosql.fetchall()
    
       
        if comandosql.rowcount > 0:

            for registro in tabela:
      
                grid.add_row([registro[0], registro[1] , registro[2],registro[3] , registro[4]])
         
            print(grid)
        else:
            print('Não existe nenhum cliente com este ID !!!')
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')

def join4(id_categoria = 0):

    grid = PrettyTable(['produto_nome', "preco", "quantidade_estoque", "categoria_nome" ])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'SELECT Pr.nome AS produto_nome, Pr.preco, Pr.quantidade_estoque, C.nome AS categoria_nome FROM Produtos Pr INNER JOIN Categorias C ON Pr.categoria_id = C.categoria_id WHERE C.categoria_id = {id_categoria} AND Pr.quantidade_estoque > 0;')
        
        tabela = comandosql.fetchall()
    
       
        if comandosql.rowcount > 0:

            for registro in tabela:
      
             grid.add_row([registro[0],registro[1],registro[2],registro[3]])
         
            print(grid)
        else:
            print('Não existe nenhuma categoria com este ID !!!')
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')

def join5():

    grid = PrettyTable(['pedido_id', "data_pedido", "status", "cliente_nome", "produto_nome"])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'SELECT P.pedido_id, P.data_pedido, P.status, C.nome AS cliente_nome, Pr.nome AS produto_nome FROM Pedidos P INNER JOIN Clientes C ON P.cliente_id = C.cliente_id INNER JOIN Produtos Pr ON P.pedido_id = Pr.produto_id WHERE P.status <> "Entregue"')
        
        tabela = comandosql.fetchall()
    
       
        if comandosql.rowcount > 0:

            for registro in tabela:
      
                grid.add_row([registro[0],registro[1],registro[2],registro[3], registro[4]])
         
            print(grid)
       
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')

def join6():
    
    grid = PrettyTable(['categoria_nome', "media_precos"])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'SELECT C.nome AS categoria_nome, AVG(Pr.preco) AS média_preços FROM Produtos Pr INNER JOIN Categorias C ON Pr.categoria_id = C.categoria_id GROUP BY C.nome;')
        
        tabela = comandosql.fetchall()
    
       
        if comandosql.rowcount > 0:

            for registro in tabela:
      
                grid.add_row([registro[0],registro[1]])
         
            print(grid)
       
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')

def join7(data = ''):

    grid = PrettyTable(['pedido_id',"data_pedido","status","cliente_nome","produto_nome"])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'SELECT P.pedido_id, P.data_pedido, P.status, C.nome AS cliente_nome, Pr.nome AS produto_nome FROM Pedidos P INNER JOIN Clientes C ON P.cliente_id = C.cliente_id INNER JOIN Produtos Pr ON P.pedido_id = Pr.produto_id WHERE P.data_pedido = "{data}" ;')
        
        tabela = comandosql.fetchall()
    
       
        if comandosql.rowcount > 0:

            for registro in tabela:
      
                grid.add_row([registro[0],registro[1],registro[2],registro[3],registro[4]])

                print(grid)
        else:
            print("data inexistente")                 
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')

def join8():

    grid = PrettyTable(['produto_nome', "categoria_nome"])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'SELECT Pr.nome AS produto_nome, C.nome AS categoria_nome FROM Produtos Pr INNER JOIN Categorias C ON Pr.categoria_id = C.categoria_id WHERE Pr.quantidade_estoque = 0;')
        
        tabela = comandosql.fetchall()
    
       
        if comandosql.rowcount > 0:

            for registro in tabela:
      
                grid.add_row([registro[0],registro[1]])
         
            print(grid)
       
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')

def join9():

    grid = PrettyTable(['cliente_nome', "quantidade_pedidos"])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'SELECT C.nome AS cliente_nome, COUNT(P.pedido_id) AS quantidade_pedidos FROM Clientes C INNER JOIN Pedidos P ON C.cliente_id = P.cliente_id GROUP BY C.nome;')
        
        tabela = comandosql.fetchall()
    
       
        if comandosql.rowcount > 0:

            for registro in tabela:
      
                grid.add_row([registro[0],registro[1]])
         
            print(grid)
       
    except Exception as erro:
        print(f'Ocorreu erro: {erro}')    

def join10():
    
    grid = PrettyTable(['produto_nome', "quantidade_pedidos"])
    try:
        comandosql = conexao.cursor()
        comandosql.execute(f'SELECT Pr.nome AS produto_nome, COUNT(P.pedido_id) AS quantidade_pedidos FROM Produtos Pr INNER JOIN Pedidos P ON Pr.produto_id = P.pedido_id GROUP BY Pr.nome ORDER BY quantidade_pedidos DESC;')
        
        tabela = comandosql.fetchall()
    
       
        if comandosql.rowcount > 0:

            for registro in tabela:
      
                grid.add_row([registro[0],registro[1]])
         
            print(grid)
       
    except Exception as erro:
        print(f'Ocorreu erro: {erro}') 
                       
    
#'''
#========================================= MÓDULO PRINCIPAL DO PROGRAMA
#===============================================
#'''



if abrebanco() == 1:
    resp = input('Deseja entrar no módulo de Ecomerce? (1-Sim, ou qualquer tecla para sair) ==> ')

    while resp =='1':
        print('='*80)
        print('{:^80}'.format('LOJA ECOMMERCE - SISTEMA ADMINISTRATIVO'))
        print('='*80)
        

        cd = input('( 0- Mostra Todas Tabelas ) ou ( Digite qualquer numero para prosseguir ) ')
        while cd.isnumeric() == False:
            cd = input("Deve ser digitado obrigatoriamente um numero!! Digite novamente:")
        if cd.isnumeric():
                    cd = int(cd)
        op = input("Escolha: [I]- Inserir   [C] - Consultar   [U] - Atualizar [E]- Excluir [J]-JOIN [CO]- Cancelar Operações ==> ")
        while op!='I' and op!= 'C' and op!='U' and op!='E' and op!='J' and op!='CO':
            op = input("Escolha: [I]- Inserir   [C] - Consultar   [U] - Atualizar [E]- Excluir [J]-JOIN [CO]- Cancelar Operações ==> ")
        
        if op =='J':
            operacao = input("Deseja utilizar qual join [1 a 10]:")
            while operacao != '1' and operacao != '2' and operacao != '3' and operacao !='4' and operacao != '5' and operacao != '6' and operacao != '7' and operacao != '8' and operacao != '9' and operacao !='10':
                operacao = input(" Operação Inválida !!! Deseja utilizar qual join [1 a 10]:")   
            #join1
            if operacao == '1':
                id_pedido = input("Informe o ID do pedido: ")
                while id_pedido.isnumeric() == False or int(id_pedido) < 0:
                    id_pedido = input("ID invalido!! Digite novamente:")
                if id_pedido.isnumeric():
                        id_pedido = int(id_pedido)
                join1(id_pedido)       
            
            elif operacao == '2':
                id_categoria = input("informe o ID de uma categoria:")
                while id_categoria.isnumeric() == False or int(id_categoria) < 0:
                    id_categoria = input("ID invalido !!! Digite novamente:")
                if id_categoria.isnumeric():
                    id_categoria = int(id_categoria)
                join2(id_categoria)    

            elif operacao == '3':
                id_cliente = input("informe o ID de um cliente:")
                while id_cliente.isnumeric() == False or int(id_cliente) < 0:
                    id_cliente = input("ID invalido !!! Digite novamente:")
                if id_cliente.isnumeric():
                    id_cliente = int(id_cliente)
                join3(id_cliente)    

            elif operacao == '4':
                id_categoria = input("informe o ID de uma categoria:")
                while id_categoria.isnumeric() == False or int(id_categoria) < 0:
                    id_categoria = input("ID invalido !!! Digite novamente:")
                if id_categoria.isnumeric():
                    id_categoria = int(id_categoria)
                join4(id_categoria)      
            elif operacao == '5':                
                join5() 
            elif operacao == '6':                
                join6()  

            elif operacao == '7':
                data = input("informe a data do pedido:")                 
                join7(data) 

            elif operacao == '8':                                
                join8() 

            elif operacao == '9':                                
                join9()  

            elif operacao == '10':                                
                join10()                 
        if op == 'I':

            operacao = input("Deseja inserir em qual tabela  [CL] - Clientes   [P] - Produtos   [CA] - Categoria   [PED] - Pedidos:")
            while operacao != 'CL' and operacao != 'P' and operacao != 'CA' and operacao !='PED':
                 operacao = input(" Operação Inválida !!! Deseja inserir em qual tabela  [CL] - Clientes   [P] - Produtos   [CA] - Categoria   [PED] - Pedidos:")
            
            
            if operacao == 'CL':

                idcliente = input ("Informe o ID do cliente: ")
                while idcliente.isnumeric() == False or int(idcliente) <= 0 :
                    idcliente = input("ID Inválido!! Digite novamente:")

                nome = input("Informe o nome: ")
                while nome.isnumeric() == True:
                    nome = input("O nome do cliente deve conter apenas caracteres!! Digite novamente:")

                email = input ("Informe o email: ")
                while email.isnumeric() == True:
                    email = input("Email Inválido!! Digite novamente:")


                endereco = input("Informe o endereço : ")
                while endereco.isnumeric() == True:
                    endereco = input("Endereço Inválido!! Digite novamente:")
                
                telefone = input("Informe o telefone : ")
                while telefone.isnumeric() == False or len(telefone) != 11:
                    telefone = input("Telefone inválido!! Digite novamente:")
                
                msg = cadastrarCliente(idcliente, nome, email, endereco, telefone)
                print(msg)



            elif operacao == 'CA':

                idcategoria = input ("Informe o ID da Categoria : ")
                while idcategoria.isnumeric() == False or int(idcategoria) <= 0 :
                    idcategoria = input("ID Inválido!! Digite novamente:")

                nomecategoria = input("Informe o nome da categoria: ")
                while nomecategoria.isnumeric() == True:
                    nomecategoria = input("O nome da categoria deve conter apenas caracteres!! Digite novamente:")

                descricao = input ("Informe a descrição: ")
                while descricao.isnumeric() == True:
                    preco = input("Descrição Inválida!! Digite novamente:")

                msg = cadastrarCategoria(idcategoria, nomecategoria, descricao)
                print(msg)
                    
            



            elif operacao == 'P':

                idproduto = input ("Informe o ID do Produto : ")
                while idproduto.isnumeric() == False or int(idproduto) <= 0 :
                    idproduto = input("ID Inválido!! Digite novamente:")

                nomeproduto = input("Informe o nome: ")
                while nomeproduto.isnumeric() == True:
                    nomeproduto = input("O nome do produto deve conter apenas caracteres!! Digite novamente:")

                preco = input ("Informe o preço: ")
                while preco.isnumeric() == False or float(preco) < 0.0:
                    preco = input("Preço Inválido!! Digite novamente:")


                qtd = input("Informe a quantidade : ")
                while qtd.isnumeric() == False or int(qtd) < 0:
                    endereco = input("Quantidade Inválida!! Digite novamente:")
                
                idcategoria = input("Informe o ID da Categoria : ")
                while idcategoria.isnumeric() == False or int(idcategoria) <=0:
                    idcategoria = input("Id Inválido!! Digite novamente:")
                
                msg = cadastrarProduto(idproduto, nomeproduto, preco, qtd, idcategoria)
                print(msg)



            elif operacao == 'PED':

                idpedido = input ("Informe o ID do Pedido : ")
                while idpedido.isnumeric() == False or int(idpedido) <= 0 :
                    idpedido = input("ID Inválido!! Digite novamente:")
                

                idcliente = input ("Informe o ID do Cliente : ")
                while idcliente.isnumeric() == False or int(idcliente) <= 0 :
                    idproduto = input("ID Inválido!! Digite novamente:")
                
                data = input ("Informe a data : ")
                
                
                status = input ("Informe o status : ")
                while status.isnumeric() == True:
                    data = input("Status inválido!! Digite novamente:")
                
                msg = cadastrarPedidos(idpedido , idcliente , data , status)
                print (msg)



        
        
        if op == 'C':

            operacao = input("Deseja consultar  qual tabela  [CL] - Clientes   [P] - Produtos   [CA] - Categoria   [PED] - Pedidos:")
            while operacao != 'CL' and operacao != 'P' and operacao != 'CA' and operacao !='PED':
                 operacao = input(" Operação Inválida !!! Deseja inserir em qual tabela  [CL] - Clientes   [P] - Produtos   [CA] - Categoria   [PED] - Pedidos:")

            if operacao == 'CL':

                idcliente = input ("Informe o ID do Cliente que deseja consultar (0 - Mostra toda a tabela) : ")
                while idcliente.isnumeric() == False or int(idcliente) < 0:
                        idcliente = input("ID Inválido!! Digite novamente: ")
                if idcliente.isnumeric():
                        idcliente = int(idcliente)
                    

                if idcliente == 0:
                        mostraCliente()
                else:
                   msg = consultarCliente(idcliente)
                   



            
            elif operacao == 'CA':

                idcategoria = input ("Informe o ID da Categoria que deseja consultar (0 - Mostra toda a tabela) : ")
                while idcategoria.isnumeric() == False or int(idcategoria) < 0 :
                    idcategoria = input("ID Inválido!! Digite novamente:")
                if idcategoria.isnumeric():
                        idcategoria = int(idcategoria)
                        
                if idcategoria == 0:
                        mostraCategoria()
                else:
                   msg = consultarCategoria(idcategoria)
                  



            elif operacao == 'P':

                idproduto = input ("Informe o ID do Produto que deseja consultar: ")
                while idproduto.isnumeric() == False or int(idproduto) < 0 :
                    idproduto = input("ID Inválido!! Digite novamente:")
                if idproduto.isnumeric():
                    idproduto = int(idproduto)
                if idproduto == 0:
                        mostraProdutos()
                else:
                   msg = consultarProdutos(idproduto)
                   
                
            



            elif operacao == 'PED':

                idpedido = input ("Informe o ID do Pedido que deseja consultar : ")
                while idpedido.isnumeric() == False or int(idpedido) < 0 :
                       idpedido = input("ID Inválido!! Digite novamente:")
                if idpedido.isnumeric():
                    idpedido = int(idpedido)
                if idpedido == 0:
                        mostraPedidos()
                else:
                    msg = consultarPedidos(idpedido)
                    



        if op == 'E':
            operacao = input("Deseja excluir de qual tabela  [CL] - Clientes   [P] - Produtos   [CA] - Categoria   [PED] - Pedidos:")
            while operacao != 'CL' and operacao != 'P' and operacao != 'CA' and operacao !='PED':
                 operacao = input(" Operação Inválida !!! Deseja inserir em qual tabela  [CL] - Clientes   [P] - Produtos   [CA] - Categoria   [PED] - Pedidos:")

            if operacao == 'CL':

                idcliente = input(" Qual o ID que pertence ao cliente que deseja excluir? ")
                while idcliente.isnumeric() == False or int(idcliente) <=0 :
                    idcliente = input(" ID !! Digite novamente:")

                
                comandosql = conexao.cursor()
        
                comandosql.execute(f'select * from  clientes  where cliente_id = {idcliente};')
            
                tabelaconsulta = comandosql.fetchall()
                for registro in tabelaconsulta:
                    grid = PrettyTable(['ID do Cliente', "Nome", "Email","Endereço" ,"Telefone" ])
                    grid.add_row([registro[0], registro[1] , registro[2] ,registro [3] , registro[4]])
                
                    print(grid)
                    conexao.commit()
                confirma = input('ATENÇÃO !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                
                while confirma != 'S' and confirma != 'N':
                        confirma = input('RESPOSTA INEXISTENTE !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                        
                msg = excluirCliente(idcliente)
                print (msg)




            elif operacao == 'CA':
                idcategoria = input ("Informe o ID da Categoria que deseja consultar : ")
                while idcategoria.isnumeric() == False or int(idcategoria) <= 0 :
                    idcategoria = input("ID Inválido!! Digite novamente:")
                comandosql = conexao.cursor()
       
                comandosql.execute(f'select * from  categorias  where categoria_id = {idcategoria};')
                
                tabelaconsulta = comandosql.fetchall()
                for registro in tabelaconsulta:
                    grid = PrettyTable(['ID da Categoria', "Nome", " Descrição" ])
                    grid.add_row([registro[0], registro[1] , registro[2]])
                
                    print(grid)
                    conexao.commit()
                confirma = input('ATENÇÃO !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                
                while confirma != 'S' and confirma != 'N':
                        confirma = input('RESPOSTA INEXISTENTE !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                        
                msg = excluirCategoria(idcategoria)
                print (msg)




            elif operacao == 'P':
                  idproduto = input ("Informe o ID do Produto : ")
                  while idproduto.isnumeric() == False or int(idproduto) <= 0 :
                    idproduto = input("ID Inválido!! Digite novamente:")

                  comandosql = conexao.cursor()
       
                  comandosql.execute(f'select * from  produtos  where produto_id = {idproduto};')
                
                  tabelaconsulta = comandosql.fetchall()
                  for registro in tabelaconsulta:
                    grid = PrettyTable(['ID do Produto', "Nome", "Preço", "Quantidade - Estoque" , " ID da Categoria" ])
                    grid.add_row([registro[0], registro[1] , registro[2] , registro[3] , registro[4]])
                
                    print(grid)
                    conexao.commit()
                  confirma = input('ATENÇÃO !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                
                  while confirma != 'S' and confirma != 'N':
                        confirma = input('RESPOSTA INEXISTENTE !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                        
                  msg = excluirProduto(idproduto)
                  print (msg)
                



            elif operacao == 'PED':

                idpedido = input ("Informe o ID do Pedido que deseja consultar : ")
                while idpedido.isnumeric() == False or int(idpedido) <= 0 :
                       idpedido = input("ID Inválido!! Digite novamente:")
                comandosql = conexao.cursor()
       
                comandosql.execute(f'select * from  pedido  where categoria_id = {idpedido};')
                
                tabelaconsulta = comandosql.fetchall()
                for registro in tabelaconsulta:
                    grid = PrettyTable(['ID do Pedido', "ID do Cliente ", "Data" , "Status " ])
                    grid.add_row([registro[0], registro[1] , registro[2]])
                
                    print(grid)
                    conexao.commit()
                confirma = input('ATENÇÃO !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                
                while confirma != 'S' and confirma != 'N':
                        confirma = input('RESPOSTA INEXISTENTE !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ')
                        
                msg = excluirPedidos(idpedido)
                print (msg)
            



        if op == 'U' :

            operacao = input("Deseja atualizar dados de qual tabela  [CL] - Clientes   [P] - Produtos   [CA] - Categoria   [PED] - Pedidos:")
            while operacao != 'CL' and operacao != 'P' and operacao != 'CA' and operacao !='PED':
                 operacao = input(" Operação Inválida !!! Deseja inserir em qual tabela  [CL] - Clientes   [P] - Produtos   [CA] - Categoria   [PED] - Pedidos:")


            if operacao == 'CL':
                print (" ATENÇÃO !!!! ID NAO PODE SER MODIFICADO")
                idcliente = input(" Informe o ID do Cliente que deseja alterar os dados :  ")
                while idcliente.isnumeric() == False or int(idcliente) <=0 :
                    idcliente = input(" ID !! Digite novamente:")
                comandosql = conexao.cursor()
        
                comandosql.execute(f'select * from  clientes  where cliente_id = {idcliente};')
            
                tabelaconsulta = comandosql.fetchall()
                for registro in tabelaconsulta:
                    grid = PrettyTable(["ID do Cliente", "Nome", "Email","Endereco" , "Telefone" ])
                    grid.add_row([registro[0], registro[1] , registro[2] , registro[3], registro[4]])
                
                    print(grid)
                    conexao.commit()
                

                nome = input("Informe o novo nome: ")
                while nome.isnumeric() == True:
                    nome = input("O nome do cliente deve conter apenas caracteres!! Digite novamente:")

                email = input ("Informe o novo email: ")
                while email.isnumeric() == True:
                    email = input("Email Inválido!! Digite novamente:")


                endereco = input("Informe o novo endereço : ")
                while endereco.isnumeric() == True:
                    endereco = input("Endereço Inválido!! Digite novamente:")
                
                telefone = input("Informe o  novo telefone : ")
                while telefone.isnumeric() == False or len(telefone) != 11:
                    telefone = input("Telefone inválido!! Digite novamente:")
                
                msg = alterarCliente(idcliente,nome, email, endereco, telefone)
                print(msg)




            if operacao == 'CA':
                print (" ATENÇÃO !!!! ID NAO PODE SER MODIFICADO")
                idcategoria = input ("Informe o ID da Categoria que deseja alterar os dados : ")
                while idcategoria.isnumeric() == False or int(idcategoria) <= 0 :
                    idcategoria = input("ID Inválido!! Digite novamente:")
                
                comandosql = conexao.cursor()
       
                comandosql.execute(f'select * from  categorias  where categoria_id = {idcategoria};')
                
                tabelaconsulta = comandosql.fetchall()
                for registro in tabelaconsulta:
                    grid = PrettyTable(['ID da Categoria', "Nome", " Descrição" ])
                    grid.add_row([registro[0], registro[1] , registro[2]])
                
                    print(grid)
                    conexao.commit()

                idcategoria = input ("Informe o ID da Categoria : ")
                while idcategoria.isnumeric() == False or int(idcategoria) <= 0 :
                    idcategoria = input("ID Inválido!! Digite novamente:")

                nomecategoria = input("Informe o nome da categoria: ")
                while nomecategoria.isnumeric() == True:
                    nomecategoria = input("O nome da categoria deve conter apenas caracteres!! Digite novamente:")

                descricao = input ("Informe a descrição: ")
                while descricao.isnumeric() == True:
                    preco = input("Descrição Inválida!! Digite novamente:")

                msg = alterarCategoria(idcategoria, nomecategoria, descricao)
                print(msg)

            

            if operacao == 'P':

                print (" ATENÇÃO !!!! ID NAO PODE SER MODIFICADO")
                idproduto = input ("Informe o ID do Produto que deseja alterar os dados : ")
                while idproduto.isnumeric() == False or int(idproduto) <= 0 :
                    idproduto = input("ID Inválido!! Digite novamente:")
                comandosql = conexao.cursor()
       
                comandosql.execute(f'select * from  produtos  where produto_id = {idproduto};')
                
                tabelaconsulta = comandosql.fetchall()
                for registro in tabelaconsulta:
                    grid = PrettyTable(['ID do Produto', "Nome", "Preço", "Quantidade - Estoque" , " ID da Categoria" ])
                    grid.add_row([registro[0], registro[1] , registro[2] , registro[3] , registro[4]])
                
                    print(grid)
                    conexao.commit() 

                nomeproduto = input("Informe o novo nome de produto: ")
                while nomeproduto.isnumeric() == True:
                    nomeproduto = input("O nome do produto deve conter apenas caracteres!! Digite novamente:")

                preco = input ("Informe o  novo preço: ")
                while preco.isnumeric() == False or float(preco) < 0.0:
                    preco = input("Preço Inválido!! Digite novamente:")


                qtd = input("Informe a nova quantidade : ")
                while qtd.isnumeric() == False or int(qtd) < 0:
                    endereco = input("Quantidade Inválida!! Digite novamente:")
                
                idcategoria = input("Informe o novo ID da Categoria : ")
                while idcategoria.isnumeric() == False or int(idcategoria) <=0:
                    idcategoria = input("Id Inválido!! Digite novamente:")
                
                msg = alterarProduto(idproduto, nomeproduto, preco, qtd, idcategoria)
                print(msg)
            



            if operacao == 'PED':

                print (" ATENÇÃO !!!! ID NAO PODE SER MODIFICADO")
                idpedido = input ("Informe o ID do Pedido que deseja alterar os dados : ")
                while idpedido.isnumeric() == False or int(idpedido) <= 0 :
                       idpedido = input("ID Inválido!! Digite novamente:")
                comandosql = conexao.cursor()
       
                comandosql.execute(f'select * from  pedido  where categoria_id = {idpedido};')
                
                tabelaconsulta = comandosql.fetchall()
                for registro in tabelaconsulta:
                    grid = PrettyTable(['ID do Pedido', "ID do Cliente ", "Data" , "Status " ])
                    grid.add_row([registro[0], registro[1] , registro[2]])
                
                    print(grid)
                    conexao.commit()
                idcliente = input ("Informe o novo ID do Cliente : ")
                while idcliente.isnumeric() == False or int(idcliente) <= 0 :
                    idproduto = input("ID Inválido!! Digite novamente:")
                
                data = input ("Informe a nova data : ")
                
                
                status = input ("Informe o novo status : ")
                while status.isnumeric() == True:
                    data = input("Status inválido!! Digite novamente:")
                
                msg = alterarPedidos(idpedido , idcliente , data , status)
                print (msg)

            print('\n\n')
            print('='*80)
            if input('Deseja continuar usando o programa? 1- Sim OU qualquer tecla para sair:') == '1':

                continue
            else:
                
                comandosql.close()
                conexao.close()
    else:
        print('FIM DO PROGRAMA!!! Algum problema existente na conexão com banco de dados.')  
                







                


                

                
                
                


            


        
                


                
                



                








            




                









                



            


            

                
                
                
                
            
    






















