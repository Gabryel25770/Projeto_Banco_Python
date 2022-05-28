# importações para o código
import os
from datetime import datetime
import os.path
#função para capturar a data
def data():
    ano = datetime.now().strftime("%Y-%m-%d %H:%M")
    return ano
#função para vizualizar o extrato
def extrato():
    print('\n Extrato\n')
    #confirmação da conta
    cpf = input("Digite o CPF: ")
    senha = input("Digite sua senha: ")
    #leitura do arquivo
    if os.path.exists(cpf + ".txt"):
        arquivo = open(cpf + ".txt", "r")
        info = arquivo.read()
        lista = []
        lista = info.split()
        arquivo.close()
        #verificando dados
        if lista[1] == cpf and lista[2] == senha:
            #abrindo o arquivo para capturar o extrato
            arquivo = open(cpf + ".txt", "r")
            for y in arquivo.readlines():
                print(y.strip())
            arquivo.close()
        #caso a senha esteja errada
        else:
            print("\n CPF ou Senha incorreto.")
#função para vizualizar o saldo
def saldo():
    print("\n Saldo\n")
    #confirmação da conta
    cpf = input("Digite o CPF: ")
    senha = input("Digite sua senha: ")
    #leitura do arquivo
    if os.path.exists(cpf + ".txt"):
        arquivo = open(cpf + ".txt", "r")
        info = arquivo .read()
        lista = []
        lista = info.split()
        arquivo.close()
        #verificando dados
        if lista[1] == cpf and lista[2] == senha: 
            #abrindo o arquivo para a atualização do saldo
            arquivo = open(cpf + ".txt", "r")
            saldoatt = (lista[-1])
            arquivo.close()
            print()
            print(f"Seu saldo é igual a: {saldoatt}")
        #caso a senha esteja errada
        else:
            print("\n CPF ou Senha incorreto.")
#função para depositar
def deposito():
    print("\n Depósito\n")
    #confirmação da conta
    cpf = input("Digite o CPF: ")
    #leitura do arquivo
    if os.path.exists(cpf + ".txt"):
        arquivo = open(cpf + ".txt", "r")
        info = arquivo.read()
        lista = []
        lista = info.split()
        arquivo.close()
        #verificando dados
        if lista[1] == cpf:
            arquivo = open(cpf + ".txt", "a")
            taxa = 0
            #recuperação do saldo
            saldao = float(lista[-1])
            print()
            #perguntar ao cliente qual o valor a ser depositado
            valor = float(input("Digite o valor a ser depositado: "))
            #atualizações após a escolha do valor do depósito
            saldao += valor
            dia = data()
            valoratt = str(f"{valor:>+7.2f}")
            saldinho = str(f"{saldao:>7.2f}")
            taxaatt = str(f"{taxa:>7.2f}")
            #atualizações do arquivo
            arquivo.write("%s  %s  %s  %s \n" % (dia, valoratt, taxaatt, saldinho))
            arquivo.close()
        #caso a senha esteja errada
        else:
            print("\n CPF ou Senha incorreto.")
#função para debitar
def debito():
    print("\n Débito\n")
    #confirmação da conta
    cpf = input("Digite o CPF: ")
    senha = input("Digite sua senha: ")
    #leitura do arquivo
    if os.path.exists(cpf + ".txt"):
        arquivo = open(cpf + ".txt", "r")
        info = arquivo.read()
        lista = []
        lista = info.split()
        arquivo.close()
        #requisitando o saque
        saque = float(input("Digite o valor do débito: "))
        #abertura do arquivo para atualização
        arquivo = open(cpf + ".txt", "a")
        dia = data()
        #verificando os dados
        if lista[1] == cpf and lista[2] == senha:
            #condição para conta salario
            if lista[3] == "Salario":
                saldoatt = float(lista[-1])-saque-(saque*0.05)
                if saldoatt < 0:
                    print("Saldo insuficiente.")
                arquivo.write("%s - %.2f  %.2f %.2f \n" % (dia, saque, (saque*0.05), saldoatt))
            #condição para conta comum
            if lista[3] == "Comum":
                saldoatt = float(lista[-1])-saque-(saque*0.03)
                if saldoatt < -500:
                    print("Limite estourado.")
                arquivo.write("%s - %.2f  %.2f %.2f \n" % (dia, saque, (saque*0.03), saldoatt))
            #condição para conta plus
            if lista[3] == "Plus":
                saldoatt = float(lista[-1])-saque-(saque*0.01)
                if saldoatt < -5000:
                    print("Limite estourado.")
                arquivo.write("%s - %.2f  %.2f %.2f \n" % (dia, saque, (saque*0.01), saldoatt))
        #caso a senha esteja errada
        else:
            print("\n CPF ou Senha incorreto.")
        arquivo.close

#funçao para apagar a conta
def apagar():
    print("\n Apagar a conta\n ")
    #confirmação da conta
    cpf = input("Digite o CPF: ")
    senha = input("Digite sua senha: ")
    #leitura do arquivo
    if os.path.exists(cpf + ".txt"):
        arquivo = open(cpf + ".txt", "r" )
        info = arquivo.read()
        lista = []
        lista = info.split()
        arquivo.close()
        #verificando os dados
        if lista[1] == cpf and lista[2] == senha:
            #remoção
            os.remove(cpf + ".txt")
        else:
            print("\n CPF ou Senha incorreto.")
#funçao para designar o tipo de conta escolhida
def tipo(conta="0"):
    #condição para o funcionamento
    while conta != "1" or conta != "2" or conta != "3":
        conta = input("Escolha um tipo de conta: ")
        #o que acontece caso o usuario escolha cada opção
        if conta == "1":
            print("Conta salario - Tarifa desconto 5% - Cheque especial : 0.00\n")
            return "Salario"
        elif conta == "2":
            print("Conta comum - Tarifa desconto 3% - Cheque especial : 500.00\n")
            return "Comum"
        elif conta == "3":
            print("Conta plus - Trarifa desconto 1% - Cheque especial : 5.000.00\n")
            return "Plus"

    
#função para criar uma conta no banco
def criarNovo():
    taxa = 0
    print("\n Cria nova conta\n")
    #passos iniciais
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    senha = input("Digite a senha: ")
    print("1 - Sálario")
    print("2 - Comum")
    print("3 - Plus")
    conta = tipo()
    inicial = float(input("Digite o valor inicial da conta: "))
    valor = float(f"{inicial:>+12.2f}")
    valor_taxa = float(f"{taxa:>7.2f}")
    dia = data()
    #verificação se o cliente ja existe
    if os.path.isfile(cpf + ".txt"):
        print()
        print("Cliente já registrado!")
    #caso ele ainda não exista
    else:
        arquivo = open(cpf+".txt", "w")
        arquivo.write("%s\n" % nome)
        arquivo.write("%s\n" % cpf)
        arquivo.write("%s\n" % senha)
        arquivo.write("%s\n" % conta)
        arquivo.write("%s   + %.2f   %.2f   %.2f \n" % (dia, inicial, valor_taxa, valor))
        
        arquivo.close()

#função pricipal
def main():
    while True:
        #titulo
        print("\nBANCO QUEM POUPA TEM")
        print()
        #opções de escolha
        print("-----MENU-----")
        print("1 - Criar nova conta")
        print("2 - Apagar conta")
        print("3 - Debitar")
        print("4 - Depositar")
        print("5 - Saldo")
        print("6 - Extrato")
        print()
        print("0 - Sair")

        print()
        opcao = input("Escolha uma das opções: ")
        #o que acontece caso que escolha cada função
        if opcao == "1":
            criarNovo()
        if opcao == "2":
            apagar()
        if opcao == "3":
            debito()
        if opcao == "4":
            deposito()
        if opcao == "5":
            saldo()
        if opcao == "6":
            extrato()
        if opcao == "0":
            break

#chamando a função
main()

#ANOTAÇÕES: arquivo.read().splitlines() serve para tirar o "\n". 