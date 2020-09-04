import questions
data = questions.Data

def ask():
    wallet_points = 0

    for key, value in data.items():
        #Informa a chave da pergunta e o seu valor
        question = '{0}: {1}'.format(key ,value['question'])
        print(question)
        print('Respostas:')

        for optionKey, optionValue in value['options'].items():
            # Informa a chave e o valor das opções
            options = '[{0}]: {1}'.format(optionKey, optionValue)
            print(options)
        
        print()
        user_input = input('Sua resposta: ')
        user_response = user_input.upper()

        # Verificações da resposta
        if user_response == value['answer']:
            print('Resposta correta!!')
        else:
            if value['difficulty'] == 'Fácil':
                print('Você errou uma pergunta muito fácil, +3 pontos na carteira!')
                wallet_points += 3
            elif value['difficulty'] == 'Médio':
                print('Você errou uma pergunta de dificuldade média, +2 pontos na carteira!')
                wallet_points += 2
            elif value['difficulty'] == 'Difícil':
                print('Essa pergunta realmente era difícil, ganhará apenas 1 ponto na carteira!')
                wallet_points += 1
        print()

    print('Seus pontos: ', wallet_points)

ask()