import time

print(''
      '_______________________'

      'Bem-vindo(a) à delegacia! '

      '_______________________')
time.sleep(2)
print('\nHoje vamos investigar alguns dos crimes que mais impressionaram '
     'os moradores de Nashville nos últimos anos...\n')

time.sleep(2)

nome_do_jogador = str(input('Antes de iniciar, digite o seu nome: '))
print('Olá,', f'{nome_do_jogador}!')

time.sleep(2)
# Função para escolher o personagem jogador
def inicio_jogo():
    personagem_jogador = ''
    escolhas = ['1', '2', '3']

    while personagem_jogador not in escolhas:
        personagem = input('''
        Escolha com qual personagem você deseja jogar:

        [1] Marie
        [2] Cristian 
        [3] Kate
        ''').upper()
        if personagem == '1':
            narrativa_Marie()
        elif personagem == '2':
            narrativa_Cristian()
        elif personagem == '3':
            narrativa_Kate()
        else:
            print('Opção inválida! Digite novamente:')

# Função acionada ao fim do jogo
def encerra_jogo():
    escolha = input('Deseja continuar a jogar? '
                    '\n[1] SIM '
                    '[2] NÃO \n '
                    ''
                    'Escolha 1 ou 2').lower

        if escolha == "1":
            inicio_jogo()
        elif escolha == "2":
            print("Fim de jogo!")
        else:
            encerra_jogo()


def narrativa_Marie():
    opcaoMarie = input('Você está de plantão na delegacia e foi convocada para investigar o '
          '\ndesaparecimento de uma adolescente. Há suspeitas de que ela pode ter sido assassinada pelo ex namorado..\n'
          '\nVocê, agora:\n '
             
             '\n[1] Vai ao clube onde ela foi vista pela última vez e registra tudo o que encontrou no local\n'
             '\n[2] Acompanha a força de tarefa da polícia na missão de procurar o ex namorado da jovem\n')

    if opcaoMarie == '1':
        clube()

    elif opcaoMarie == '2':
        suspeito_crimes()

    else:
        print('Opção inválida! Digite novamente')

def clube():
    opcao_clube = input('Chegando no clube, você descobre mais informações e então coleta as digitais presentes no banheiro '
             '\npara descobrir exatamente quem esteve com a moça minutos antes dela desaparecer e por onde ela teria passado...\n'
             '\nO que você descobre?\n'
                        
             '\n[1]  Que há vestígios de sangue seco no local\n'
             '\n[2]  Que há dois suspeitos principais até o momento: o ex namorado e a sua melhor amiga.\n')

    if opcao_clube == '1':
        enredo1_clube()

        if opcao_clube == '2':
            suspeito_crimes()

        else:
            print('Opção inválida! Digite novamente')

def enredo1_clube():
    opcao_enredo = input('Após analisar o material recolhido e novas descobertas acontecerem, você foi perseguida'
                  '\ne vai precisar interromper as investigações. Mas, antes disso, precisa revelar um segredo... \n'
                  ''
                  '\n[1] A moça estava grávida e tinha envolvimento com o tráfico internacional de pessoas \n'
                  '\n[2] As provas indicam o surgimento de uma terceira pessoa no crime...\n')

    if opcao_enredo == '1':
        print('Boa investigação! Nem o FBI iria tão longe!')

    elif opcao_enredo == '2':
        print('VOCÊ! E parece que alguns colegas de trabalho estão desconfiando... Fuja enquanto é tempo!!! Fim de jogo')

    else:
        print('Opção inválida! Digite novamente: ')

#enredo1_clube()


def narrativa_Cristian():
    crime_escola = int(input('Na semana passada, um assassinato misterioso aconteceu na Escola Estadual Pablo Iglesias.\n '
                      '\nNo primeiro dia de aula letivo, após o recreio,\n'
                      '\nFoi encontrado em uma das salas, o corpo do professor Nilton, que dava aulas de matemática.\n'
                      '\nNão havia sinais de agressão física e nem sangue no local.\n'
                      '\nConsiderando que você tenha que descobrir a causa e/ou o culpado pelo crime, escolha uma opção: '
                              ''
                              '[1] Investigar os arquivos pessoais do professor Nilton'
                              '[2] Entrevistar os alunos e a comunidade acadêmica para descobrir novas pistas'))

    if crime_escola == '1':
        opcao1_crime_escola()

    elif crime_escola == '2':
        conclui_crime_escola()

    else:
        print('Opção inválida! Digite novamente: ')
        narrativa_Cristian()


def opcao1_crime_escola(celular, biblioteca,carro):
    celular = input('Você descobriu que o professor era uma pessoa de muitos amigos, mas se envolvia com uma mulher casada')
    biblioteca = 'você encontrou um diário pessoal com informações importantes e sigilosas sobre a vítima'
    carro = 'Não havia provas no carro, apenas vestígios de cabelos de outra pessoa. O professor era solteiro e sem filhos. '












                      '\n Com base nos relatos investigados, você passou a suspeitar principalmente de três funcionários:\n'
                      '\no professor de química, a professora de educação física e o jardineiro. \n '
                      '\nTodos disseram que estavam ocupados no momento em que a tragédia aconteceu, mas um deles é o assassino. '
                      '\nQuem matou Nilton? \n'
                      '\nO professor de Química, Roni, que estava aplicando avaliação bimestral.\n'
                      '\nGuilherme, que era professor de educação Física e estava na quadra esportiva'
                      '\nO jardineiro Bento, que estava podando os arbustos no pátio de trás da escola.\n'
                      'Quem matou o professor de Matemática? '
                             ''
                             '\n[1]Roni\n'
                             ' \n[2]Guilherme\n'
                             ' \n[3]Bento\n '))
    if crime_escola == '1':
        print('Renato e James eram muito amigos, ele não seria capaz de fazer isso.')

    elif crime_escola == '2':
        print(
            'Humm, acho que você se equivocou, pois o Guilherme estava na quadra treinando condicionamento físico com os alunos. ')

    elif crime_escola == '3':
        print(
            'Roni é o principal suspeito até o momento, porque mentiu durante o depoimento.\n Era o primeiro dia de aula e não havia possibilidade de avaliar os alunos...\n')

    else:
        print('Opção inválida! Digite novamente!')
        return narrativa_Cristian()

def suspeito_crimes():
    suspeito = input('Você chegou ao principal suspeito do crime e está próximo(a) de desvendar grandes mistérios.'
                     '\nO rapaz está foragido, mas você dá de cara com ele na estação de trem... '
                     'E agora?\n'
                     ''
                     '\n[1] Você disfarça, mas tenta segui-lo o mais longe possível\n'
                     #'[2] Comunica os seguranças para montarem uma força-tarefa para prender o criminoso'
                     '\n[2] Se aproxima como quem não quer nada e pede uma informação, afinal ele não sabe quem é você\n')


    if suspeito == '1' or suspeito == '2':
        print('GAME OVER! Você seguiu o criminoso mas acabou caindo na armadilha dele e foi feita de refém!!')

    else:
        encerra_jogo()



































