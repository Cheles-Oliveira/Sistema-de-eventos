from colorama import Fore, init, Style, Back  # back não utilizado
from datetime import datetime  # data e hora atuais
import hashlib  # importando hashlib
import os  # importando os para limpar o terminal

# Dicionário para armazenar usuários (login) e senhas criptografadas
admin = {}
usuarios = {}
eventos = {}
inscritos = {}

# função para limpa terminal
os.system("cls" if os.name == "nt" else "clear")


def iniciando_colorama():  # função para iniciar colorama
    init()


def del_tela():  # função para quando for chamada limpar terminal
    os.system("cls" if os.name == "nt" else "clear")


def criptografar_senha(
    senha,
):  # função recebe um texto e gera um hash que transforma a senha em um valor unico
    return hashlib.sha256(
        senha.encode()
    ).hexdigest()  # hexdigest converte esse valor para uma string de caracteres hexadecimais (usando os números de 0-9 e as letras de a-f).


def erro_msg(
    msg,
):  # função com parametro para gera a mensagem de erro visualmente em vermelho
    print(Fore.RED + f"{msg}")


def menu_principal():  # menu principal para chamar as funções representadas por texto dentro dos prints
    while True:  # laço de repetiço até que a condição seja verdadeira
        try:  # definife o codigo que pode gerar o erro
            print(Fore.LIGHTMAGENTA_EX + 40 * "=")
            print(Fore.LIGHTCYAN_EX + "    UniFECAF Eventos")
            print(Fore.LIGHTMAGENTA_EX + 40 * "=")
            print(Fore.CYAN + "1 - Menu Administrador")
            print("2 - Menu Usuário")
            print("3 - feedback eventos")
            print("4 - Saindo do sistema")
            print(Fore.LIGHTMAGENTA_EX + 40 * "=")
            opcao = int(input(Fore.CYAN + "Escolha uma opção: "))

            if opcao == 1:
                del_tela(), menu_admin()
            elif opcao == 2:
                del_tela(), menu_usuario()
            elif opcao == 3:
                del_tela(), feedback_eventos()
            elif opcao == 4:
                print("Saindo do sistema...")
                exit()
            else:  # else validade erro ao tentar digitar um numero inteiro que seja fora da condição
                del_tela()
                print(Fore.RED + "Opção invalida tente novamente!")
        except (
            ValueError
        ):  # trata o erro ao tentar escrever textos ou em conjunto com numeros
            del_tela()
            print(Fore.RED + "Por favor, insira um número válido!")


def menu_admin():  # função menu administrador
    while True:
        try:  # tratamento try
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + 40 * "=")
            print(Fore.YELLOW + "1 - Sign up-Admin")
            print("2 - Login-Admin")
            print("3 - Recuperação De login/senha")
            print("4 - Voltar ao menu principal")
            print(Fore.LIGHTCYAN_EX + 40 * "=")
            opcao = int(input(Fore.YELLOW + "Digite uma opção: "))

            if opcao == 1:
                del_tela(), sign_admin()
            elif opcao == 2:
                del_tela(), login_admin_usuario()
            elif opcao == 3:
                del_tela(), recuperacao_login_senha()
            elif opcao == 4:
                del_tela(), menu_principal()
            else:
                print(Fore.RED + "Opção inválida, tente novamente!")
        except ValueError:  # mdg de error tratada por try except
            print(Fore.RED + "Por favor, insira um número válido!")


def menu_usuario():  # função menu usuário
    while True:  # loop de repetição caso a condição gere um error ou seja falsa
        try:
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + 40 * "=")
            print(Fore.YELLOW + "1 - Sign up-usuário")
            print("2 - Login-usuário")
            print("3 - Recuperação da login/senha")
            print("4 - Voltar ao menu principal")
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + 40 * "=")
            opcao = int(input(Fore.YELLOW + "Digite uma opção: "))

            if opcao == 1:
                del_tela(), sign_usuario()
            elif opcao == 2:
                del_tela(), login_admin_usuario()
            elif opcao == 3:
                del_tela(), recuperacao_login_senha()
            elif opcao == 4:
                del_tela(), menu_principal()
            else:
                print(Fore.RED + "Opção inválida, tente novamente!")
        except ValueError:
            print(Fore.RED + "Por favor, insira um número válido!")


def sign_admin():  # função para armazenar conta dentro do dicionário admin
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + 40 * "=")
    nome_ra = input(Fore.YELLOW + "Digite um email,nome ou RA: ")
    senha = input("Digite uma senha: ")
    senha_criptografada = criptografar_senha(senha)
    admin[nome_ra] = senha_criptografada
    del_tela()
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + 40 * "=")
    print(Fore.GREEN + f"Administrador:{nome_ra} criado com sucesso!")
    print(f"Hash armazenado: {senha_criptografada}")


def sign_usuario():  # função para armazena conta dentro do dicionário usuarios
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + 40 * "=")
    nome_ra = input(Fore.YELLOW + "Digite um email,nome ou RA: ")
    senha = input("Digite uma senha: ")
    senha_criptografada = criptografar_senha(senha)
    usuarios[nome_ra] = senha_criptografada
    del_tela()
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + 40 * "=")
    print(Fore.GREEN + f"Usuário:{nome_ra} criado com sucesso!")
    print(f"Hash armazenado: {senha_criptografada}")


def login_admin_usuario():  # função compartilhada login admin e usuario
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + 40 * "=")
    nome_ra = input(Fore.YELLOW + "Digite seu nome ou RA: ")
    senha = input("Digite sua senha: ")
    senha_criptografada = criptografar_senha(senha)

    if (
        nome_ra in admin and admin[nome_ra] == senha_criptografada
    ):  # if nome + senha for igual a dicionário admin loga na def login admin
        del_tela()
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 40 * "=")
        print(Fore.GREEN + "Login realizado com sucesso!")
        login_admin()
    elif nome_ra in usuarios and usuarios[nome_ra] == senha_criptografada:
        del_tela()  # elif nome + senha for igual a dicionário usuários loga na def login usuario
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 40 * "=")
        print(Fore.GREEN + "Login realizado com sucesso!")
        login_usuario()
    else:  # else não encontrada as info dentro dos dicionários
        del_tela()
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + 40 * "=")
        print(Fore.RED + "Email,nome RA ou senha incorretos!")


def recuperacao_login_senha():  # função para recuperar a senha atraves do nome
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + 40 * "=")
    nome_ra = input("Digite um email, nome ou RA: ")

    if nome_ra in admin:  # Verifica se o nome_ra está no dicionário admin
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + 40 * "=")
        print(Fore.GREEN + f"Identificado: {nome_ra}, digite uma nova senha!")
        senha_criptografada = input(Fore.CYAN + "Nova senha: ")
        senha_criptografada = criptografar_senha(senha_criptografada)
        admin[nome_ra] = senha_criptografada  # Atualiza a senha no dicionário admin
        print(Fore.GREEN + "Senha atualizada para o administrador!")
    elif nome_ra in usuarios:  # Verifica se o nome_ra está no dicionário usuarios
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + 40 * "=")
        print(Fore.GREEN + f"Identificado: {nome_ra}, digite uma nova senha!")
        senha_criptografada = input(Fore.CYAN + "Nova senha: ")
        senha_criptografada = criptografar_senha(senha_criptografada)
        usuarios[nome_ra] = (
            senha_criptografada  # Atualiza a senha no dicionário usuarios
        )
        print(Fore.GREEN + "Senha atualizada para o usuário!")
    else:
        print(Fore.RED + "Email, nome ou RA não existente. Tente novamente!")


def login_admin():  # # função administrador
    while True:
        try:
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 40 * "=")
            print(Fore.CYAN + "1 - Cadastrar eventos")
            print("2 - Atualizar eventos")
            print("3 - Visualizar eventos")  # cria def para usuario e admin
            print("4 - visualizar inscrições")
            print("5 - Excluir evento")
            print("6 - Voltar ao menu administrador")
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 40 * "=")
            opcao = int(input(Fore.CYAN + "Digite uma opção: "))

            if opcao == 1:
                del_tela(), cadastrar()
            elif opcao == 2:
                del_tela(), atualizar()
            elif opcao == 3:
                del_tela(), visualizar_eventos()
            elif opcao == 4:
                del_tela(), visualizar_inscritos()
            elif opcao == 5:
                del_tela(), excluir_eventos()
            elif opcao == 6:
                del_tela(), menu_admin()
            else:
                print(Fore.RED + "Opção invalida tente novamente!")
        except ValueError:
            print(Fore.RED + "Por favor, insira um número válido!")


def validar_input(prompt, tipo, campo):
    while True:
        valor = input(prompt).strip()
        if tipo == "data":
            try:
                data = datetime.strptime(valor, "%d/%m/%Y").date()
                if data < datetime.today().date():
                    erro_msg(f"A data do evento não pode ser anterior à data atual.")
                    continue  # Retorna para o input
                return data
            except ValueError:
                erro_msg("Data inválida. Use o formato (DD/MM/AAAA).")
        elif tipo == "hora":
            try:
                hora = datetime.strptime(valor, "%H:%M").time()
                return hora
            except ValueError:
                erro_msg("Hora inválida. Use o formato (HH:MM).")
        elif tipo == "numero":
            try:
                numero = int(valor)
                if numero <= 0:
                    erro_msg(f"O campo '{campo}' não pode ser zero ou negativo.")
                    continue  # Retorna para o input
                return numero
            except ValueError:
                erro_msg(f"Insira um número válido para o campo '{campo}'.")
        elif tipo == "texto":
            if not valor:
                erro_msg(f"O campo '{campo}' não pode ser vazio.")
                continue  # Retorna para o input
            return valor


def cadastrar():  # função para cadastrar eventos coletando dados como nome,descrição,data,local,hora,endereço
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 40 * "=")
    nome = input(Fore.CYAN + "Digite o nome do evento: ")

    if nome not in eventos:
        # if o nome do evento existe!

        # Usando a função validar_input para validar a data
        descreva = validar_input(
            Fore.CYAN + "Descrição do evento: ", "texto", "Descrição do evento"
        )
        data = validar_input(
            Fore.CYAN + "Digite a data do evento (formato DD/MM/AAAA): ",
            "data",
            "Data do evento",
        )

        local = validar_input(
            Fore.CYAN + "Digite o local do evento: ", "texto", "Local"
        )
        hora = validar_input(
            Fore.CYAN + "Digite a hora do evento (formato HH:MM): ", "hora", "Hora"
        )
        vagas = validar_input(
            Fore.CYAN + "Digite o número de vagas: ", "numero", "Vagas"
        )

        # Cadastrando o evento no dicionário
        eventos[nome] = {
            "descreva": descreva,
            "data": data.strftime("%d/%m/%Y"),
            "local": local,
            "hora": hora.strftime("%H:%M"),
            "vagas": vagas,
        }
        del_tela()
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 40 * "=")
        print(
            Fore.GREEN
            + f"Evento '{nome}' cadastrado com sucesso para a data {eventos[nome]['data']}"
        )
    else:
        print(
            Fore.RED
            + f"O evento '{nome}' já existe e não pode ser cadastrado novamente."
        )


def atualizar():  # função atualizar eventos reaproveitando codigos da def cadastro,alterando basicamente os textos das prints
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 40 * "=")
    nome = input(Fore.CYAN + "Digite o nome do evento: ")

    if nome in eventos:
        # if o nome do evento existe!
        descreva = validar_input(
            Fore.CYAN + "Descrição do evento: ", "texto", "Descrição do evento"
        )
        # Usando a função validar_input para validar a data
        data = validar_input(
            Fore.CYAN + "Digite nova data do evento (formato DD/MM/AAAA): ",
            "data",
            "Data do evento",
        )

        local = validar_input(
            Fore.CYAN + "Digite novo local do evento: ", "texto", "Local"
        )
        hora = validar_input(
            Fore.CYAN + "Digite nova hora do evento (formato HH:MM): ", "hora", "Hora"
        )
        vagas = validar_input(
            Fore.CYAN + "Digite novo número de vagas: ", "numero", "Vagas"
        )

        # Cadastrando o evento no dicionário
        eventos[nome] = {
            "descreva": descreva,
            "data": data.strftime("%d/%m/%Y"),
            "local": local,
            "hora": hora.strftime("%H:%M"),
            "vagas": vagas,
        }
        del_tela()
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 40 * "=")
        print(
            Fore.GREEN
            + f"Evento '{nome}' atualizado com sucesso para a data {eventos[nome]['data']}"
        )
    else:
        print(Fore.RED + f"O evento não existe!")


def visualizar_eventos():  # função visualizar eventos

    if eventos:
        del_tela()
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 40 * "=")
        print("Lista De Eventos: ")
        for nome, info in eventos.items():  # laço for
            print(
                Fore.LIGHTWHITE_EX
                + f"Nome: {nome} | Descrição: {info['descreva']} | Data: {info['data']} | local: {info['local']} | hora: {info['hora']} | vagas: {info['vagas']}"
            )
    else:
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 40 * "=")
        print("Eventos vazios!")


def excluir_eventos():  # função excluir eventos
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 40 * "=")
    nome = input(Fore.CYAN + "Digite o nome do eventos que deseja excluir: ")

    if nome in eventos:
        del eventos[nome]
        del_tela()
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 40 * "=")
        print(Fore.GREEN + "Evento excluido com sucesso!")
    else:
        del_tela()
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 40 * "=")
        print(Fore.RED + "Evento não encontrado na lista de eventos!")


def login_usuario():  # menu login usuário
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 40 * "=")
    print(Fore.CYAN + "1 - Inscrever-se em eventos")
    print("2 - Visualizar eventos disponiveis")
    print("3 - Voltar ao menu usuário")
    opcao = int(input("Digite uma opção: "))
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 40 * "=")

    if opcao == 1:
        del_tela(), inscrever_evento()
    elif opcao == 2:
        del_tela(), visualizar_eventos()
    elif opcao == 3:
        del_tela(), menu_usuario()


def inscrever_evento():  # função para usuários se inscrever em eventos
    nome_ra = input(Fore.CYAN + "Digite seu nome ou RA para inscrição: ")
    if nome_ra not in usuarios:  # Verifica se o usuário está registrado
        erro_msg(Fore.RED + "Usuário não encontrado! Por favor, faça o login primeiro.")
        return

    nome_evento = input(Fore.CYAN + "Digite o nome do evento para inscrição: ")

    if nome_evento not in eventos:
        erro_msg(f"O evento '{nome_evento}' não existe!")
        return

    # Verifica se o usuário já está inscrito
    if nome_evento in inscritos and nome_ra in inscritos[nome_evento]:
        erro_msg(f"Você já está inscrito no evento '{nome_evento}'.")
        return

    # Verifica se ainda há vagas
    vagas_disponiveis = eventos[nome_evento]["vagas"]
    if vagas_disponiveis <= 0:
        erro_msg(f"Não há vagas disponíveis para o evento '{nome_evento}'.")
        return

    # Inscreve o usuário no evento
    if nome_evento not in inscritos:
        inscritos[nome_evento] = []

    inscritos[nome_evento].append(nome_ra)

    # Decrementa a vaga disponível
    eventos[nome_evento]["vagas"] -= 1

    print(Fore.GREEN + f"Você foi inscrito com sucesso no evento '{nome_evento}'!")
    print(Fore.YELLOW + f"Vagas restantes: {eventos[nome_evento]['vagas']}")


def visualizar_inscritos():  # função para visualizar inscritos
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 40 * "=")
    nome_evento = input(
        Fore.CYAN + "Digite o nome do evento para visualizar os inscritos: "
    )

    if nome_evento not in eventos:
        erro_msg(Fore.RED + f"O evento '{nome_evento}' não existe!")
        return

    elif nome_evento not in inscritos or not inscritos[nome_evento]:
        print(Fore.RED + f"Não há inscritos no evento '{nome_evento}'.")
        return

    else:
        print(Fore.GREEN + f"Lista de inscritos no evento '{nome_evento}':")
        for nome_ra in inscritos[nome_evento]:
            print(Fore.LIGHTWHITE_EX + f"- {nome_ra}")


def feedback_eventos():  # função para relizar comentarios em eventos já ocorridos
    print("1 - Criar feedback")
    print("2 - Ver feedbacks")
    opcao = int(input("Digite uma opção: "))
    chave_feedback = "feedback"  # Definindo a chave feedback em uma variável dinanica com aspas se torna uma variavel do tipo "string"

    if opcao == 1:
        del_tela()
        nome_evento = input("Digite nome do evento para o feedback: ")
        del_tela()
        if nome_evento in eventos:
            # Se o evento já existe, adiciona o novo feedback à lista
            feedback = input("Dê seu feedback aqui: ")

            # Verifica se já existe a chave "feedback" e a inicializa como lista vazia se necessário
            if chave_feedback not in eventos[nome_evento]:
                eventos[nome_evento][chave_feedback] = []

            # Adiciona o novo feedback à lista
            eventos[nome_evento][chave_feedback].append({"feedback": feedback})
            print(
                Fore.GREEN
                + "Obrigado pelo seu feedback! Ele foi registrado com sucesso."
            )
        else:
            print("Evento não encontrado!")

    elif opcao == 2:
        del_tela()
        nome_evento = input("Digite nome do evento para visualizar comentários: ")
        if nome_evento in eventos and chave_feedback in eventos[nome_evento]:
            if eventos[nome_evento][
                chave_feedback
            ]:  # Verifica se a lista de feedbacks não está vazia
                print(f"Feedbacks para o evento '{nome_evento}':")
                for i, feedback in enumerate(eventos[nome_evento][chave_feedback], 1):
                    print(f"{i}. {feedback['feedback']}")
                    input(Fore.LIGHTMAGENTA_EX + "\nPressione qualquer tecla: ")
                    del_tela()
                    menu_principal()
            else:
                erro_msg("Ainda não há feedbacks para este evento.")
        else:
            erro_msg("Evento não encontrado ou sem feedbacks.")
    else:
        erro_msg("Opção inválida.")


menu_principal()  # função menu principal
