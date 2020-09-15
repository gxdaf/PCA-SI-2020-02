import questions, teste
data = questions.Data

def ask():

    for key, value in data.items():
        #Informa a chave da pergunta e o seu valor
        while mens_pos != 'Ponte' or mens_pos != 'Buraco!':
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
            if value['difficulty'] == 'Fácil' and escolha == "Amarelo":
                print('Você errou uma pergunta muito fácil, +3 pontos na carteira!')
                pontos_am += 3
                escolha = 'Azul'
            elif value['difficulty'] == 'Médio' and escolha == "Amarelo":
                print('Você errou uma pergunta de dificuldade média, +2 pontos na carteira!')
                pontos_am += 4
                escolha = 'Azul'
            elif value['difficulty'] == 'Difícil' and escolha == "Amarelo":
                print('Essa pergunta realmente era difícil, ganhará apenas 1 ponto na carteira!')
                pontos_am += 5
                escolha = 'Azul'
            elif value['difficulty'] == 'Muito difícil' and escolha == "Amarelo":
                print('Essa pergunta era praticamente impossível! +4 pontos na carteira!')
                pontos_am += 7
                escolha = 'Azul'
            if value['difficulty'] == 'Fácil' and escolha == "Azul":
                print('Você errou uma pergunta muito fácil, +3 pontos na carteira!')
                pontos_az += 3
                escolha = 'Amarelo'
            elif value['difficulty'] == 'Médio' and escolha == "Azul":
                print('Você errou uma pergunta de dificuldade média, +2 pontos na carteira!')
                pontos_az += 4
                escolha = 'Amarelo'
            elif value['difficulty'] == 'Difícil' and escolha == "Azul":
                print('Essa pergunta realmente era difícil, ganhará apenas 1 ponto na carteira!')
                pontos_az += 5
                escolha = 'Amarelo'
            elif value['difficulty'] == 'Muito difícil' and escolha == "Azul":
                print('Essa pergunta era praticamente impossível! +4 pontos na carteira!')
                pontos_az += 7
                escolha = 'Amarelo'

        print()
ask()