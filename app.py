import os
from datetime import datetime


def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    # respostas com if/elif (linhas 7-22 originais, agora em comentário)
    # if comando in ('olá', 'boa tarde', 'bom dia'):
    #     return 'Olá tudo bem!'
    # if comando == 'como estás':
    #     return 'Estou bem, obrigado!'
    # if comando == 'como te chamas?':
    #     return 'O meu nome é: Bot :)'
    # if comando == 'tempo':
    #     return 'Está um dia de sol!'
    # if comando in ('bye', 'adeus', 'tchau'):
    #     return 'Gostei de falar contigo! Até breve...'
    # if 'horas' in comando:
    #     return f'São: {datetime.now():%H:%M} horas'
    # if 'data' in comando:
    #     return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    # respostas com dicionário (linhas 24-37 descomentadas)
    respostas = {
        ('olá', 'boa tarde', 'bom dia'):        'Olá tudo bem!',
        'como estás':                            'Estou bem, obrigado!',
        'como te chamas?':                       'O meu nome é: Bot :)',
        'tempo':                                 'Está um dia de sol!',
        ('bye', 'adeus', 'tchau'):               'Gostei de falar contigo! Até breve...',
        'horas':                                 f'São: {datetime.now():%H:%M} horas',
        'data':                                  f'Hoje é dia: {datetime.now():%d-%m-%Y}',
        # 5 novas interações
        'qual é a tua cor favorita?':            'A minha cor favorita é o azul!',
        ('obrigado', 'obrigada'):                'De nada, foi um prazer ajudar!',
        'conta uma piada':                       'Por que o livro de matemática estava triste? Tinha muitos problemas!',
        'qual é a capital de portugal?':         'A capital de Portugal é Lisboa!',
        'ajuda':                                 'Podes perguntar-me: horas, data, tempo, como estás, ou simplesmente conversar!',
    }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta

    return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}!\nComo te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta = obter_resposta(user_input)  # bug corrigido
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()