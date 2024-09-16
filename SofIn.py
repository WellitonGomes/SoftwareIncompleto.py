import re
import os

def exibir_menu():
    print("Selecione uma opção:")
    print("1. Verificar Dados do Cliente")
    print("2. Adicionar Novos Dados do Cliente")
    print("3. Verificar Dados do Usuário")
    print("4. Adicionar Novos Dados do Usuário")
    print("5. Adicionar Dados de Produto")
    print("6. Sair")

def limpar_linhas(num_linhas):
    os.system('cls' if os.name == 'nt' else 'clear')
    for _ in range(num_linhas):
        print()

def obter_dadosUsuario():
    def obter_emailUS():
        r = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
        emailUS = input('Por favor, digite um e-mail: ')
        if r.match(emailUS):
            print(f'E-mail válido: {emailUS}')
        else:
            print('E-mail inválido.')

    def obter_nomeUS():
        while True:
            try:
                nomeUS = input("Por favor, digite seu nome: ")
                if not nomeUS.strip():
                    raise ValueError("Nome não pode estar vazio.")
                print(f"Nome válido: {nomeUS}")
                return nomeUS
            except ValueError as e:
                print(e)

    def obter_senhaUS():
        while True:
            try:
                senha_str = input("Por favor, digite sua senha (somente números): ")
                if not senha_str.strip():
                    raise ValueError("Senha não pode estar vazia.")
                senhaUS = int(senha_str)
                print(f"Senha válida: {senhaUS}")
                return senhaUS
            except ValueError:
                print("Erro: A senha deve conter apenas números. Tente novamente.")

    def obter_telefoneUS():
        while True:
            try:
                telefone_str = input("Por favor, digite seu número de telefone (apenas números, 8 dígitos): ")
                if not telefone_str.strip():
                    raise ValueError("Telefone não pode estar vazio.")
                if not telefone_str.isdigit():
                    raise ValueError("Telefone deve conter apenas números.")
                if len(telefone_str) != 8:
                    raise ValueError("Telefone deve conter exatamente 8 dígitos.")
                telefoneUS = int(telefone_str)
                print(f"Telefone válido: {telefoneUS}")
                return telefoneUS
            except ValueError as e:
                print(f"Erro: {e}. Tente novamente.")

    obter_nomeUS()
    obter_emailUS()
    obter_senhaUS()
    obter_telefoneUS()

def obter_dadosCliente():
    def obter_emailC():
        r = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
        emailC = input('Por favor, digite um e-mail: ')
        if r.match(emailC):
            print(f'E-mail válido: {emailC}')
        else:
            print('E-mail inválido.')

    def obter_nomeC():
        while True:
            try:
                nomeC = input("Por favor, digite seu nome: ")
                if not nomeC.strip():
                    raise ValueError("Nome não pode estar vazio.")
                print(f"Nome válido: {nomeC}")
                return nomeC
            except ValueError as e:
                print(e)

    def obter_cpfC():
        while True:
            try:
                cpf = input("Por favor, digite 11 dígitos do seu CPF: ")
                if len(cpf) != 11 or not cpf.isdigit():
                    raise ValueError("Por favor, digite exatamente 11 dígitos do seu CPF.")
                print(f"CPF válido: {cpf}")
                return cpf
            except ValueError as e:
                print(e)

    def obter_telefoneC():
        while True:
            try:
                telefone_str = input("Por favor, digite seu número de telefone (apenas números, 8 dígitos): ")
                if not telefone_str.strip():
                    raise ValueError("Telefone não pode estar vazio.")
                if not telefone_str.isdigit():
                    raise ValueError("Telefone deve conter apenas números.")
                if len(telefone_str) != 8:
                    raise ValueError("Telefone deve conter exatamente 8 dígitos.")
                telefoneC = int(telefone_str)
                print(f"Telefone válido: {telefoneC}")
                return telefoneC
            except ValueError as e:
                print(f"Erro: {e}. Tente novamente.")

    def obter_comprasC():
        while True:
            compras_str = input("Por favor, digite a quantidade de compras: ")

            if not compras_str.strip():
                print("Número de compras não pode estar vazio. Tente novamente.")
                continue

            if not compras_str.isdigit():
                print("Entrada inválida. Por favor, digite apenas números inteiros.")
                continue

            compras = int(compras_str)

            if compras < 0:
                print("A quantidade de compras não pode ser negativa. Tente novamente.")
                continue

            print(f"Quantidade de compras válida: {compras}")
            return compras

    def verificar_compras_anteriores():
        while True:
            resposta = input("O cliente já fez compras anteriores? (sim ou não): ").strip().lower()

            if resposta == "sim":
                compras_anteriores = obter_comprasC()  # Obtém a quantidade de compras realizadas
                print(f"Quantidade de compras anteriores: {compras_anteriores}")
                return True
            elif resposta == "não":
                print("Primeira compra.")
                return False
            else:
                print("Entrada inválida. Por favor, responda com 'sim' ou 'não'.")

    def obter_enderecoC():
        while True:
            try:
                enderecoC = input("Por favor, digite seu endereço completo: ")
                if not enderecoC.strip():
                    raise ValueError("Endereço não pode estar vazio.")
                print(f"Endereço válido: {enderecoC}")
                return enderecoC
            except ValueError as e:
                print(e)

    def obter_dataC():
        while True:
            try:
                data = input("Por favor, digite sua data de nascimento (dd/mm/aaaa): ")
                if re.match(r'^\d{2}/\d{2}/\d{4}$', data):
                    print(f"Data válida: {data}")
                    return data
                else:
                    raise ValueError("Formato de data inválido. Use dd/mm/aaaa.")
            except ValueError as e:
                print(e)

    obter_nomeC()
    obter_emailC()
    obter_cpfC()
    obter_telefoneC()
    verificar_compras_anteriores()
    obter_enderecoC()
    obter_dataC()

def obter_dadosProdutos():
    def obter_nomeP():
        while True:
            try:
                nomeP = input("Por favor, digite o nome do produto: ")
                if not nomeP.strip():
                    raise ValueError("Nome não pode estar vazio.")
                print(f"Nome válido: {nomeP}")
                return nomeP
            except ValueError as e:
                print(e)

    def obter_descricaoP():
        while True:
            try:
                descricaoP = input("Por favor, digite uma descrição do produto: ")
                if not descricaoP.strip():
                    raise ValueError("Descrição não pode estar vazio.")
                print(f"Descrição válida: {descricaoP}")
                return descricaoP
            except ValueError as e:
                print(e)

    def obter_precoP():
        while True:
            preco_str = input("Por favor, digite o valor do produto (use vírgula para decimais): ")

            if not preco_str.strip():
                print("Valor do produto não pode estar vazio. Tente novamente.")
                continue

            preco_str = preco_str.replace(',', '.')

            try:
                precoP = float(preco_str)
                if precoP < 0:
                    print("O preço do produto não pode ser negativo. Tente novamente.")
                    continue

                print(f"Preço válido: {precoP:.2f}")
                return precoP
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido com vírgula para decimais.")

    def obter_quantidadeP():
        while True:
            quantidade_str = input("Por favor, digite a quantidade de produtos no estoque: ")

            if not quantidade_str.strip():
                print("Quantidade não pode estar vazio. Tente novamente.")
                continue

            if not quantidade_str.isdigit():
                print("Entrada inválida. Por favor, digite apenas números inteiros.")
                continue

            quantidadeP = int(quantidade_str)

            if quantidadeP < 0:
                print("A quantidade em estoque não pode ser negativa. Tente novamente.")
                continue

            print(f"Quantidade em estoque válida: {quantidadeP}")
            return quantidadeP

    def obter_nomeFornecedorP():
        while True:
            try:
                nomeFP = input("Por favor, digite o nome do fornecedor do produto: ")
                if not nomeFP.strip():
                    raise ValueError("O nome do fornecedor não pode estar vazio.")
                print(f"Nome do fornecedor válido: {nomeFP}")
                return nomeFP
            except ValueError as e:
                print(e)

    def obter_dataDAdmicaoP():
        while True:
            try:
                dataAP = input("Por favor, digite a data de vencimento deste produto (dd/mm/aaaa): ")
                if re.match(r'^\d{2}/\d{2}/\d{4}$', dataAP):
                    print(f"Data de vencimento válida: {dataAP}")
                    return dataAP
                else:
                    raise ValueError("Formato de data inválido. Use dd/mm/aaaa.")
            except ValueError as e:
                print(e)

    def obter_dataVencimentoP():
        while True:
            try:
                dataVP = input("Por favor, digite a data de vencimento deste produto (dd/mm/aaaa): ")
                if re.match(r'^\d{2}/\d{2}/\d{4}$', dataVP):
                    print(f"Data de vencimento válida: {dataVP}")
                    return dataVP
                else:
                    raise ValueError("Formato de data inválido. Use dd/mm/aaaa.")
            except ValueError as e:
                print(e)

    obter_nomeP()
    obter_descricaoP()
    obter_precoP()
    obter_quantidadeP()
    obter_nomeFornecedorP()
    obter_dataDAdmicaoP()
    obter_dataVencimentoP()

def obter_dadosFuncionarios():
    def obter_nomeF():
        while True:
            try:
                nomeF = input("Por favor, digite seu nome: ")
                if not nomeF.strip():
                    raise ValueError("Nome não pode estar vazio.")
                return nomeF
            except ValueError as e:
                print(e)

    def obter_emailF():
        r = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
        emailF = input('Por favor, digite um e-mail: ')
        if r.match(emailF):
            return emailF
        else:
            print('E-mail inválido.')
            return None

    def obter_cpfF():
        while True:
            try:
                cpf = input("Por favor, digite 11 dígitos do seu CPF: ")
                if len(cpf) != 11 or not cpf.isdigit():
                    raise ValueError("Por favor, digite exatamente 11 dígitos do seu CPF.")
                return cpf
            except ValueError as e:
                print(e)

    def obter_telefoneF():
        while True:
            try:
                telefone_str = input("Por favor, digite seu número de telefone (apenas números, 8 dígitos): ")
                if not telefone_str.strip():
                    raise ValueError("Telefone não pode estar vazio.")
                if not telefone_str.isdigit():
                    raise ValueError("Telefone deve conter apenas números.")
                if len(telefone_str) != 8:
                    raise ValueError("Telefone deve conter exatamente 8 dígitos.")
                telefoneF = int(telefone_str)
                return telefoneF
            except ValueError as e:
                print(f"Erro: {e}. Tente novamente.")

    def obter_enderecoF():
        while True:
            try:
                enderecoF = input("Por favor, digite seu endereço completo: ")
                if not enderecoF.strip():
                    raise ValueError("Endereço não pode estar vazio.")
                return enderecoF
            except ValueError as e:
                print(e)

    def obter_dataF():
        while True:
            try:
                data = input("Por favor, digite sua data de nascimento (dd/mm/aaaa): ")
                if re.match(r'^\d{2}/\d{2}/\d{4}$', data):
                    return data
                else:
                    raise ValueError("Formato de data inválido. Use dd/mm/aaaa.")
            except ValueError as e:
                print(e)

    def obter_RGF():
        while True:
            try:
                rg = input("Por favor, digite 9 dígitos do seu RG: ")
                if len(rg) != 9 or not rg.isdigit():
                    raise ValueError("Por favor, digite exatamente 9 dígitos do seu RG.")
                return rg
            except ValueError as e:
                print(e)

    def obter_EsCiviF():
        while True:
            try:
                EsCiviF = input("Por favor, digite seu estado civil: ")
                if not EsCiviF.strip():
                    raise ValueError("Estado civil não pode estar vazio.")
                return EsCiviF
            except ValueError as e:
                print(e)

    # Chamar todas as funções para obter as informações do funcionário
    nome = obter_nomeF()
    email = obter_emailF()
    cpf = obter_cpfF()
    telefone = obter_telefoneF()
    endereco = obter_enderecoF()
    data_nascimento = obter_dataF()
    rg = obter_RGF()
    estado_civil = obter_EsCiviF()

def exibir_menu():
    print("Menu:")
    print("1 - Verificar dados do cliente")
    print("2 - Adicionar novos dados do cliente")
    print("3 - Verificar dados do usuário")
    print("4 - Adicionar novos dados do usuário")
    print("5 - Adicionar novos dados de Produto")
    print("6 - Obter dados dos funcionários")
    print("7 - Sair")

def menu():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("Verificando dados do cliente...")
            obter_dadosCliente()

        elif escolha == "2":
            print("Adicionando novos dados do cliente...")
            obter_dadosCliente()

        elif escolha == "3":
            print("Verificando dados do usuário...")
            obter_dadosUsuario()

        elif escolha == "4":
            print("Adicionando novos dados do usuário...")
            obter_dadosUsuario()

        elif escolha == "5":
            print("Adicionando novos dados de Produto...")
            obter_dadosProdutos()

        elif escolha == "6":
            while True:
                print("Obter dados dos funcionários:")
                print("1 - Adicionar dados pessoais dos funcionários")
                print("2 - Voltar ao menu principal")

                escolha_funcionario = input("Escolha uma opção: ")

                if escolha_funcionario == "1":
                    print("Adicionando dados pessoais dos funcionários...")
                    obter_dadosFuncionarios()

                elif escolha_funcionario == "2":
                    break

                else:
                    print("Opção inválida. Tente novamente.")

        elif escolha == "7":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Chamar a função do menu para iniciar o programa
menu()
