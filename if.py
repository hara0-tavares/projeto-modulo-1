print('------------------------------------------------------------------')
print('Bem Vindo a guerra de gregos e troianos pela bela princesa Helena.')
print('------------------------------------------------------------------')

print('Escolha o personagem que você deseja jogar:')
personagem = int(input(' 1 - Aquiles , 2 - Paris , 3 - Heitor:'))


def personagem_1 (personagem_1):
    if personagem == 1 :
        print('Aquiles foi o maior guerreiro grego, ele esta sendo chamado pelo rei Menelau a participar da guerra,você aceita?')
        print(' sim')
        print(' nao')
        resposta= input('Responda:')
    else    :
        print('GAME OVER!!! TENTE NA PROXIMA VEZ.')
    if resposta == 'sim' :
        print('Parabéns, agora vamos a 2 pergunta. Agora que você está participando da guerra, acabou de morrer seu sobrinho, o que fazer?')
        print('1 - Buscar o culpado pela morte.')
        print('2 - Voltar para casa.')
        resposta = input('resposta:')
    else:
        print('GAME OVER!!! TENTE NA PROXIMA VEZ.')
    if resposta== '1' :
        print('Você está quase lá, depois de longas batalhas o rei decidiu um plano surpresa para invasão, qual decisão tomar?')
        print(' a - participar da ideia')
        print(' b - recusar e lutar sua própria batalha.')
    resposta= input('Responda:')
    if resposta == 2:
        print('GAME OVER!!! TENTE NA PROXIMA VEZ.')
    if resposta == 'a' :
        print('PARABÉNS VOCÊ ACABA DE INVADIR TROIA E CONQUISTAR A CIDADE!!!!')

def personagem_2 (personagem_2):
    if personagem == 2 :
        print('Você fez uma viagem a esparta, lá acabou conhecendo uma bela mulher, porém ela é a esposa do rei, o que fazer?')
        print(' sim - Continua a investir nesse romance.')
        print(' nao - deixa isso para lá e segue a viagem.')
        resposta= input('Responda:')
    else    :
        print('GAME OVER!!! TENTE NA PROXIMA VEZ.')
    if resposta == 'sim' :
        print('Parabéns, agora que vocês vivem um romance, você não sabe que decisão tomar , o que fazer?')
        print('1 - Não deixa seu amor escapar, e enfrenta qualquer coisa por ela.')
        print('2 - Acaba aqui e tente evitar uma guerra.')
        resposta = input('resposta:')
    if resposta == 'nao':
        print('GAME OVER!!! TENTE NA PROXIMA VEZ.')
    if resposta== '1' :
        print('Foi descoberto o seu romance, agora Menelau está enviando tropas para pegar Helena, qual decisão tomar?')
        print(' a - Ir a luta pelo amor')
        print(' b - Não arriscar a cidade e devolver Helena')
        resposta= input('Responda:')
    if resposta == '2':
        print('GAME OVER!!! TENTE NA PROXIMA VEZ.')
    if resposta == 'a' :
        print('PARABÉNS VOCÊ CONQUISTOU O AMOR DE HELENA!!!!')

def personagem_3 (personagem_3):
    if personagem == 3 :
        print('Na sua viagem a esparta você viu que seu irmão quer fugir com a princesa, qual sua decisão?')
        print(' sim - Ajudar o irmão com o seu amor. ')
        print(' nao - Impedir essa situação. ')
        resposta= input('Responda:')
    
    else    :
        print('GAME OVER!!! TENTE NA PROXIMA VEZ.')
    
    if resposta == 'sim' :
        print('Agora que Helena chegou na cidade o que você irá fazer?')
        print('1 - Se preparar para guerra.')
        print('2 - Ir descansar.')
        resposta = input('resposta:')

    else:
        print('GAME OVER!!! TENTE NA PROXIMA VEZ.')

    if resposta== '1' :
        print('Menelau com seu exercito está na porta da sua cidade, o que fazer?')
        print(' a - Proteger a cidade')
        print(' b - Fugir.')

    resposta= input('Responda:')

    if resposta == 2:
        print('GAME OVER!!! TENTE NA PROXIMA VEZ.')

    if resposta == 'a' :
        print('PARABÉNS VOCÊ ACABA DE INVADIR TROIA E CONQUISTAR A CIDADE!!!!')



if personagem == 1 :
    personagem_1(personagem)
if personagem == 2 :
    personagem_2(personagem)
if personagem == 3 :
    personagem_3(personagem)


