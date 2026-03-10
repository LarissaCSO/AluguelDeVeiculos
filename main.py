import time

print("Bem-vindo ao CarAccess")

print("Seu site preferido de aluguel de veículos!")

def menu():
    print("Menu:")
    
    print("1. Alugar um veículo")
    print("2. Devolver um veículo")
    print("3. Cadastrar um veículo")
    print("4. Sair")

def veiculos_disponiveis():
    print("Veículos disponíveis para aluguel:")
    print("1. Carro - R$100,00 por dia")
    print("2. Moto - R$50,00 por dia")
    print("3. Bicicleta - R$20,00 por dia")

def quantidade_dias(tipo_veiculo):
    dias = int(input("Digite a quantidade de dias para alugar o veículo: "))
    valor_total = calcular_valor_total(dias, tipo_veiculo)
    print(f"O valor total do aluguel é: R${valor_total:.2f}")
    return dias 

def horario_aluguel():
    horario = input("Digite o horário de início do aluguel (ex: 00:00): ")
    return horario

def cor_veiculo():
    cor = input("Digite a cor do veículo: ")
    return cor

def modelo_veiculo():
    modelo = input("Digite o modelo do veículo: ")
    return modelo

def placa_veiculo():
    placa = input("Digite a placa do veículo: ")
    if placa == "":
        print("Placa não pode ser vazia. Por favor, digite uma placa válida.")
        return placa_veiculo()
    if len(placa) != 7:
        print("Placa deve conter exatamente 7 caracteres. Por favor, digite um número válido.")
        return placa_veiculo()
    return placa

def ano_veiculo():
    ano = int(input("Digite o ano do veículo: "))
    return ano

def tipo_combustivel():
    tipo = input("Digite o tipo de combustível do veículo (Gasolina, Diesel, Elétrico): ")
    return tipo

def horario_devolucao():
    horario = input("Digite o horário de devolução do veículo (ex: 00:00): ")
    return horario

def nome_cliente():
    nome = input("Digite o nome do cliente: ")
    return nome

def CPF_cliente():
    CPF = input("Digite o CPF do cliente: ")
    if CPF == "":
        print("CPF não pode ser vazio. Por favor, digite um CPF válido.")
        if len(CPF) != 11:
            print("CPF deve conter exatamente 11 caracteres. Por favor, digite um número válido.")
        return CPF_cliente()
    return CPF

def Telefone_cliente():
    telefone = int(input("Digite o telefone do cliente: "))
    return telefone

def calcular_valor_total(dias, tipo_veiculo):
    if tipo_veiculo == '1':
        valor_total = dias * 100
    elif tipo_veiculo == '2':
        valor_total = dias * 50
    elif tipo_veiculo == '3':
        valor_total = dias * 20
    else:
        print("Opção de veículo inválida.")
    return valor_total

def cadastrar_veiculo():
    tipo_veiculo = input("Digite o tipo de veículo a ser cadastrado (1.Carro, 2.Moto ou 3.Bicicleta): ")   
    print(f"Tipo de veículo cadastrado: {tipo_veiculo}.")

def gerenciamento_de_conta():
    print("Gerenciamento de conta:")
    print("1. Criar conta")
    print("2. Fazer login")
    print("3. Sair")
    if opcao == '1':
        nome = input("Digite seu nome: ")
        CPF = input("Digite seu CPF: ")
        telefone = input("Digite seu telefone: ")
        print(f"Conta criada com sucesso! Nome: {nome}, CPF: {CPF}, Telefone: {telefone}")
    elif opcao == '2':
        CPF = input("Digite seu CPF para login: ")
        print(f"Login bem-sucedido! Bem-vindo de volta, nome = {nome}")
    elif opcao == '3':
        print("Saindo do gerenciamento de conta. Até a próxima!")
    return menu()

while True:
    menu()
    opcao = input("Escolha uma opção do menu: ")

    if opcao == '1':
        veiculos_disponiveis()
        tipo_veiculo = input("Digite o número do tipo de veículo que deseja alugar: 1, 2 ou 3 ")    
        dias = quantidade_dias(tipo_veiculo)
        horario_inicio = horario_aluguel()
        cor = cor_veiculo()
        modelo = modelo_veiculo()
        placa = placa_veiculo()
        ano = ano_veiculo()
        tipo = tipo_combustivel()
        nome = nome_cliente() 
        CPF = CPF_cliente()
        telefone = Telefone_cliente()
        print(f"Aluguel confirmado! tipo de veículo: {tipo_veiculo}, dias: {dias}, horário de início: {horario_inicio}, cor: {cor}, modelo: {modelo}, placa: {placa}, ano: {ano}, tipo de combustível: {tipo}.")
        print(f"Cliente: {nome}, CPF: {CPF}, Telefone: {telefone}")

    elif opcao == '2':
        horario_fim = horario_devolucao()
        print(f"Nome do cliente: {nome_cliente()}, CPF: {CPF_cliente()}, Telefone: {Telefone_cliente()}")
        print(f"Devolução confirmada! Horário de devolução: {horario_fim}")

    elif opcao == '3':
        cadastrar_veiculo()
        cor = cor_veiculo()
        modelo = modelo_veiculo()
        placa = placa_veiculo()
        ano = ano_veiculo()
        tipo = tipo_combustivel()
        print(f"Veículo cadastrado! Cor: {cor}, Modelo: {modelo}, Placa: {placa}, Ano: {ano}, Tipo de combustível: {tipo}")
        nome = nome_cliente()
        CPF = CPF_cliente() 
        telefone = Telefone_cliente()   
        print(f"Cadastro realizado por: {nome}, CPF: {CPF}, Telefone: {telefone}")

    elif opcao == '4':
        print("Obrigado por usar o CarAccess! Até a próxima!")
        break
