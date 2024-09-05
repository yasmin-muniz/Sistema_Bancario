# Atribuindo data da transação e limite de transacao diaria

menu = """


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[u] Usuário
[c] Conta Corrente


=> """
 
from datetime import datetime
lista_extrato = []
lista_cad_cliente = []
lista_cad_conta = []

saldo = 1000
limite = 500
extrato = ""

num_conta = 0
numero_saques = 0
numero_transacoes = 0
valor_saque = 0
valor_deposito = 0

LIMITE_SAQUES = 3
LIMITE_TRANS_DIARIA = 10

# ################### SAQUE ###################
def saque(saldo, valor_saque, limite, numero_saques, LIMITE_SAQUES, numero_transacoes, data_formatada, lista_extrato):
    valor_saque = float(input('Qual valor a ser sacado?'))
    if valor_saque > limite:
        print ("O limite para saque é de R$500,00 reais") 
    elif valor_saque > saldo:
        print("Não há saldo suficiente na conta!")
    elif numero_saques >= LIMITE_SAQUES:
        print("Você atingiu o limite de saques diários!") 
    else:
        saldo -= valor_saque
        lista_extrato.append(f'Saque: R$ {valor_saque} / Data da transação: {data_formatada}')  
        numero_saques += 1
        numero_transacoes +=1
        print(f"Saque de R${valor_saque} realizado com sucesso!") 
        return saldo, numero_saques, numero_transacoes, lista_extrato

# ################### DEPOSITO ###################
def deposito(saldo,lista_extrato,numero_transacoes):
    valor_deposito =  float(input ('Qual valor a ser depositado?')) 
    saldo += valor_deposito 
    lista_extrato.append(f'Depósito: R$ {valor_deposito} / Data da transação: {data_formatada}')
    numero_transacoes += 1 
    return saldo, lista_extrato, numero_transacoes


# ################### EXTRATO ###################
def extrato(lista_extrato):
    for transacao in lista_extrato:
        print(transacao)
    print(f"Saldo: R${saldo}")

# ############### VERIFICA CPF #################
def verificar_cpf_existente(cpf):
    for cliente in lista_cad_cliente:
        if cliente['cpf'] == cpf:
            return True
    return False    

# ################ USUARIO #################
def usuario(nome, data_nasc, cpf, logradouro, numero, bairro, cidade, estado):    
    cliente = {
        'nome': nome,
        'data_nasc': data_nasc,
        'cpf': cpf,
        'endereco': {
            'logradouro': logradouro,
            'numero': numero,
            'bairro': bairro,
            'cidade': cidade,
            'estado': estado
        }
    }
    lista_cad_cliente.append(cliente)

 # ################ CONTA CORRENTE #################
def conta_corrente(num_conta, cpf_usuario, agencia = '0001'):    
    conta_corrente = {
        'agencia': agencia,
        'num_conta': num_conta,
        'cpf_usuario': cpf_usuario 
    }
    lista_cad_conta.append(conta_corrente)   



while True:
    

    opcao = input (menu)
    data_atual = datetime.now()
    data_formatada = data_atual.strftime("%d-%m-%Y %H:%M:%S")

    if opcao in ("d","s"):
        if numero_transacoes == LIMITE_TRANS_DIARIA:
            print("Você atingiu o limite de transações diárias!") 
        else: 
            if opcao == "d": 
                saldo, lista_extrato, numero_transacoes = deposito(saldo = saldo,
                                            lista_extrato=lista_extrato,
                                            numero_transacoes=numero_transacoes)    
            
            elif opcao == "s":
                saldo, numero_saques, numero_transacoes, lista_extrato = saque(
                    saldo=saldo,
                    valor_saque=valor_saque,
                    limite=limite,
                    numero_saques=numero_saques,
                    LIMITE_SAQUES=LIMITE_SAQUES,
                    numero_transacoes=numero_transacoes,
                    data_formatada=data_formatada,
                    lista_extrato=lista_extrato
                )

    elif opcao == "e": 
        extrato(lista_extrato=lista_extrato)

    elif opcao == "u": 
        cpf = input('Digite o CPF do Usuário: ')
        cpf = cpf.replace('.', '').replace('-', '')
        #print(cpf)

        if verificar_cpf_existente(cpf):
            print("Erro: CPF já cadastrado!")
        else:
            nome = input ('Digite o nome do Usuário: ')
            data_nasc = input ('Digite o data de nascimento do Usuário: ') 
            logradouro = input ('Digite o logradouro do Usuário: ')
            numero = input ('Digite o numero do Usuário: ')   
            bairro = input ('Digite o bairro do Usuário: ') 
            cidade = input ('Digite o cidade do Usuário: ') 
            estado = input ('Digite o estado do Usuário: ') 
            usuario(nome, data_nasc, cpf, logradouro, numero, bairro, cidade, estado)
            print(f"Usuario {nome} cadastrado(a) com sucesso!") 

    elif opcao == 'c':
        cpf_usuario = input('Digite o CPF do Usuário para a criação da conta corrente: ')
        cpf_usuario = cpf_usuario.replace('.', '').replace('-', '')
        if verificar_cpf_existente(cpf_usuario):
            num_conta += 1
            conta_corrente(num_conta, cpf_usuario)
            print(f"Conta corrente cadastrada com sucesso para o usuario {nome}!") 
        else:
            print("Erro: CPF não encontrado!")    

    elif opcao == "q":
        break

    else:
        print ("Operação Inválida, por favor selecione novamente a operação desejada.")
