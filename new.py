mapa = []
pontos = 0

def _repr_(mapa):
    if len(mapa) == 8:
        return (f'{mapa[0]} | {mapa[1]} | {mapa[2]}\n'
                f'{mapa[3]} | {mapa[4]} | {mapa[5]}\n'
                f'{mapa[6]} | {mapa[7]} | {mapa[8]}\n')
    else:
        return ("lista Vazia!")

espada2 = {'Espada de Fogo': 5}
espada1 = {'Espada de Gelo' : 4}
espada = {"Espada" : 2}

monstro2 = {"Zumbi" : 10}
monstro1 = {"Esqueleto": 4}
monstro = {'Fantasma': 7}

personagem = {'Aventureiro': 5}

listArmas = ["Espada", 'Espada de Gelo', 'Espada de Fogo']
listMonstros = ["Zumbi", "Esqueleto", 'Fantasma']

objetos = [espada, espada1, espada2, monstro, monstro1, monstro2]


def calcularPontos(monstroNome):
    global pontos
    if monstroNome == 'Zumbi':
        pontos = pontos + 5
    elif monstroNome == 'Esqueleto':
        pontos += 1
    elif monstroNome == 'Fantasma':
        pontos += 3
    return pontos

def elementoAleatorio():
    from random import randint
    a1 = (randint(0, len(objetos)-1))
    return objetos[a1]

def formarTabuleiro():
    a = '\033[0;30;41m'
    b = '\033[m'
    while len(mapa) < 9:
        mapa.append(elementoAleatorio())
        if len(mapa) ==4:
            mapa.append(personagem)
    print(f'{mapa[0]} | {mapa[1]} | {mapa[2]}\n'
                f'{mapa[3]} | {a}{mapa[4]}{b} | {mapa[5]}\n'
                f'{mapa[6]} | {mapa[7]} | {mapa[8]}\n')


def mostrarTablueiro():
    vez = acharJogador()
    a = '\033[0;30;41m'
    b = '\033[m'
    print("\n")

    print(f'Pontuação: {pontos}')

    if vez == 0:
        print(f'{a}{mapa[0]}{b} | {mapa[1]} | {mapa[2]}\n'
              f'{mapa[3]} | {mapa[4]} | {mapa[5]}\n'
              f'{mapa[6]} | {mapa[7]} | {mapa[8]}\n')

    if vez == 1:
        print(f'\n{mapa[0]} | {a}{mapa[1]}{b} | {mapa[2]}\n'
              f'{mapa[3]} | {mapa[4]} | {mapa[5]}\n'
              f'{mapa[6]} | {mapa[7]} | {mapa[8]}\n')

    if vez == 2:
        print(f'\n{mapa[0]} | {mapa[1]} | {a}{mapa[2]}{b}\n'
              f'{mapa[3]} | {mapa[4]} | {mapa[5]}\n'
              f'{mapa[6]} | {mapa[7]} | {mapa[8]}\n')

    if vez == 3:
        print(f'\n{mapa[0]} | {mapa[1]} | {mapa[2]}\n'
              f'{a}{mapa[3]}{b} | {mapa[4]} | {mapa[5]}\n'
              f'{mapa[6]} | {mapa[7]} | {mapa[8]}\n')

    if vez == 4:
        print(f'\n{mapa[0]} | {mapa[1]} | {mapa[2]}\n'
              f'{mapa[3]} | {a}{mapa[4]}{b} | {mapa[5]}\n'
              f'{mapa[6]} | {mapa[7]} | {mapa[8]}\n')

    if vez == 5:
        print(f'\n{mapa[0]} | {mapa[1]} | {mapa[2]}\n'
              f'{mapa[3]} | {mapa[4]} | {a}{mapa[5]}{b}\n'
              f'{mapa[6]} | {mapa[7]} | {mapa[8]}\n')

    if vez == 6:
        print(f'\n{mapa[0]} | {mapa[1]} | {mapa[2]}\n'
              f'{mapa[3]} | {mapa[4]} | {mapa[5]}\n'
              f'{a}{mapa[6]}{b} | {mapa[7]} | {mapa[8]}\n')

    if vez == 7:
        print(f'\n{mapa[0]} | {mapa[1]} | {mapa[2]}\n'
              f'{mapa[3]} | {mapa[4]} | {mapa[5]}\n'
              f'{mapa[6]} | {a}{mapa[7]}{b} | {mapa[8]}\n')

    if vez == 8:
        print(f'\n{mapa[0]} | {mapa[1]} | {mapa[2]}\n'
              f'{mapa[3]} | {mapa[4]} | {mapa[5]}\n'
              f'{mapa[6]} | {mapa[7]} | {a}{mapa[8]}{b}\n')

formarTabuleiro()

def acharJogador():
    for x in mapa:
        if x == personagem:
            return mapa.index(x)

def direcionamento():
    direcao = int(input("\nQual direção ir?\n"
                        "1 - pra cima\n"
                        "2 - esquerda\n"
                        "3 - pra baixo\n"
                        "4 - direita\n"
                        "Digite uma opção: "))
    return direcao

def movimetarBaixo():

    localAtual = acharJogador()
    substituir = localAtual + 3

    mapa[substituir] = personagem
    mapa[localAtual] = elementoAleatorio()

def movimetarDireita():

    localAtual = acharJogador()
    substituir = localAtual + 1

    mapa[substituir] = personagem
    mapa[localAtual] = elementoAleatorio()
def movimetarEsquerda():

    localAtual = acharJogador()
    substituir = localAtual - 1

    mapa[substituir] = personagem
    mapa[localAtual] = elementoAleatorio()

def movimetarCima():

    localAtual = acharJogador()
    substituir = localAtual -3

    mapa[substituir] = personagem
    mapa[localAtual] = elementoAleatorio()


def lutar(direcionamentoMapa):
    localAtual = acharJogador()

    tipoDeOperacao = 0
    # 1 == adicao
    # 2 == subtracao
    #print(mapa[localAtual]["Aventureiro"])
    nomeProximoObjeto = (mapa[localAtual + direcionamentoMapa].keys())
    valorProximoObjeto = (mapa[localAtual + direcionamentoMapa].values())

    for x in nomeProximoObjeto:
        chave = x

    for y in valorProximoObjeto:
        value = y

    print(chave, value)

    for h in listMonstros:
        if chave == h:
            #print("monstro")
            tipoDeOperacao = 2


    for z in listArmas:
        if chave == z:
            #print("Arma")
            tipoDeOperacao = 1

    if tipoDeOperacao == 1:
        personagem["Aventureiro"] += value
        print(f'\nVocê pegou uma {chave} - valor:{value}')
    elif tipoDeOperacao == 2:
        personagem["Aventureiro"] -= value
        print(f'\nVocê lutou contra um {chave} - valor:{value}')
        calcularPontos(chave)

def movimentar():
    proximoLocal = direcionamento()
    localAtual = acharJogador()

# Canto Superior Esquerdo
    if localAtual == 0:

        if proximoLocal == 3:
            lutar(3)
            movimetarBaixo()
        elif proximoLocal == 4:
            lutar(1)
            movimetarDireita()
        else:
            print("\n <<<<<<<<<<<<<<<< Se mova para outra direção!!! >>>>>>>>>>>>>>>>>>>")

# Meio Superiror
    if localAtual == 1:

        if proximoLocal == 2:
            lutar(-1)
            movimetarEsquerda()
        elif proximoLocal == 3:
            lutar(3)
            movimetarBaixo()
        elif proximoLocal == 4:
            lutar(1)
            movimetarDireita()
        else:
            print("\n <<<<<<<<<<<<<<<< Se mova para outra direção!!! >>>>>>>>>>>>>>>>>>>")

# Canto Superior Direito
    if localAtual == 2:

        if proximoLocal == 2:
            lutar(-1)
            movimetarEsquerda()
        elif proximoLocal == 3:
            lutar(3)
            movimetarBaixo()
        else:
            print("\n <<<<<<<<<<<<<<<< Se mova para outra direção!!! >>>>>>>>>>>>>>>>>>>")

# Canto do meio Esquerdo
    if localAtual == 3:

        if proximoLocal == 1:
            lutar(-3)
            movimetarCima()
        elif proximoLocal == 3:
            lutar(3)
            movimetarBaixo()
        elif proximoLocal == 4:
            lutar(1)
            movimetarDireita()
        else:
            print("\n <<<<<<<<<<<<<<<< Se mova para outra direção!!! >>>>>>>>>>>>>>>>>>>")

# Meião
    if localAtual == 4:
        if proximoLocal == 1:
            lutar(-3)
            movimetarCima()
        elif proximoLocal == 2:
            lutar(-1)
            movimetarEsquerda()
        elif proximoLocal == 3:
            lutar(3)
            movimetarBaixo()
        elif proximoLocal == 4:
            lutar(1)
            movimetarDireita()
        else:
            print("\n <<<<<<<<<<<<<<<< Se mova para outra direção!!! >>>>>>>>>>>>>>>>>>>")

# Canto do meio Direito
    if localAtual == 5:

        if proximoLocal == 1:
            lutar(-3)
            movimetarCima()

        elif proximoLocal == 2:
            lutar(-1)
            movimetarEsquerda()

        elif proximoLocal == 3:
            lutar(3)
            movimetarBaixo()
        else:
            print("\n <<<<<<<<<<<<<<<< Se mova para outra direção!!! >>>>>>>>>>>>>>>>>>>")

# Canto Inferior Esquerdo
    if localAtual == 6:

        if proximoLocal == 1:
            lutar(-3)
            movimetarCima()
        if proximoLocal == 4:
            lutar(1)
            movimetarDireita()
        else:
            print("\n <<<<<<<<<<<<<<<< Se mova para outra direção!!! >>>>>>>>>>>>>>>>>>>")

# Meio inferior
    if localAtual == 7:

        if proximoLocal == 1:
            lutar(-3)
            movimetarCima()
        elif proximoLocal == 2:
            lutar(-1)
            movimetarEsquerda()
        elif proximoLocal == 4:
            lutar(1)
            movimetarDireita()
        else:
            print("\n <<<<<<<<<<<<<<<< Se mova para outra direção!!! >>>>>>>>>>>>>>>>>>>")

# Canto Inferior Direito
    if localAtual == 8:


        if proximoLocal == 1:
            lutar(-3)
            movimetarCima()
        elif proximoLocal == 2:
            lutar(-1)
            movimetarEsquerda()
        else:
            print("\n <<<<<<<<<<<<<<<< Se mova para outra direção!!! >>>>>>>>>>>>>>>>>>>")


    mostrarTablueiro()

while True:
    movimentar()
    vida = (mapa[acharJogador()].values())
    for y in vida:
        vidaJogador = y
    if vidaJogador <= 0:
        print(f'Você Morreu! \nPontuação Total: {pontos}')
        break


#print(acharJogador())