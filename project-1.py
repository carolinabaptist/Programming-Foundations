from queue import Queue

def eh_labirinto(uni):

    '''

    A funcao eh_labirinto devolve True se o seu argumento corresponde a um
    labirinto e False caso contrario.

    eh_labirinto: universal -> booleano

    '''

    if not isinstance(uni, tuple):
        return False

    for i in range(len(uni)):
        if not isinstance(uni[i],tuple):
            return False

    if len(uni) < 3 or len(uni[0]) < 3:
        return False

    col = len(uni)
    lin = len(uni[0])

    for i in range(col):
        if len(uni[i]) != lin:
            return False
        for j in range(lin):
            if (i == 0 or i == len(uni)-1) and uni[i][j] != 1 or (i != 0 or i != len(uni)-1) and (uni[i][0] != 1 or uni[i][lin-1] != 1):
                return False
            if uni[i][j] != 1 and uni[i][j] != 0:
                return False
    return True


def eh_posicao(uni):

    '''

    A funcao eh_posicao devolve True se o seu argumento corresponde a uma posicao e
    False caso contrario

    eh_posicao: universal -> booleano

    '''


    if not isinstance(uni, tuple) or len(uni)!=2 or not isinstance(uni[0], int) or uni[0]<0 or not isinstance(uni[1], int) or uni[1]<0:
        return False
    return True

def eh_conj_posicoes(uni):

    """

    A funcao conj_posicoes devolve True se o seu argumento corresponde a um conjunto de
    posicoes unicas e False caso contrario

    conj_posicoes: universal -> booleano


    """

    if not isinstance(uni, tuple):
        return False
    for i in range(len(uni)):
        if not eh_posicao(uni[i]):
            return False
        if i!=len(uni)-1 and uni[i][0] == uni[i+1][0] and uni[i][1] == uni[i+1][1]:
            return False
    return True

def tamanho_labirinto(lab):

    """

    A funcao tamanho_labirinto devolve um tuplo de dois valores inteiros correspondendo
    o primeiro deles a dimensao Nx e o segundo a dimensao Ny do labirinto

    tamanho_labirinto: labirinto -> tuplo


    """
    if not eh_labirinto(lab):
        raise ValueError ('tamanho_labirinto: argumento invalido')
    else:
        return ((len(lab), len(lab[0])))

def eh_mapa_valido(lab, conj):

    """

    A funcao eh_mapa_valido devolve True se o segundo argumento corresponde a um
    conjunto de posicoes compativeis (nao ocupadas por paredes) dentro do labirinto
    e False caso contrario

    eh_mapa_valido: labirinto x conj_posicoes -> booleano


    """
    if not eh_labirinto(lab) or not eh_conj_posicoes(conj):
        raise ValueError ('eh_mapa_valido: algum dos argumentos e invalido')

    n_col, n_linhas = len(lab), len(lab[0])
    num = len(conj)

    for j in range(num):
        if conj[j][0] >= n_col or conj[j][1] >=n_linhas or conj[j][0] == 0 or conj[j][0] == n_col-1 or conj[j][1] == 0 or conj[j][1] == n_linhas-1:
            return False
    return True

def eh_posicao_livre(lab, conj, pos):

    """

    A funcao eh_posicao_livre devolve True se a posicao corresponde a uma posicao livre
    (nao ocupada nem por paredes, nem por unidades) dentro do labirinto e False caso
    contrario

    eh_posicao_livre: labirinto x conj_posicoes x posicao -> booleano


    """

    if not eh_mapa_valido(lab, conj) or not eh_posicao(pos):
        raise ValueError ('eh_posicao_livre: algum dos argumentos e invalido')

    if pos[0] == 0 or pos[0] == len(lab)-1 or pos[1] == 0 or pos[1] == len(lab[0])-1 or pos in conj:
        return False

    return True

def posicoes_adjacentes(pos):

    """

    A funcao posicoes_adjacentes devolve o conjunto de posicoes adjacentes da posicao
    em ordem de leitura de um labirinto.

    posicoes_adjacentes: posicao -> conj_posicoes


    """

    if not eh_posicao(pos):
        raise ValueError ('posicao_adjacentes: argumento invalido')

    candidates = ((pos[0], pos[1]-1), (pos[0]-1, pos[1]), ((pos[0]+1, pos[1])), (pos[0], pos[1]+1))
    res = ()

    for i in range(len(candidates)):
        if eh_posicao(candidates[i]):
            res = res + (candidates[i],)
    return res

def mapa_str(lab, conj):

    """

    A funcao mapa_str devolve a cadeia de caracteres que as representa.

    mapa_str: labirinto x conj_posicoes -> cad. carateres


    """

    if not eh_mapa_valido(lab, conj):
        raise ValueError ('eh_posicao_livre: algum dos argumentos e invalido')

    map = ''

    for j in range(len(lab[0])):
        for i in range(len(lab)):

            if lab[i][j] == 1:
                map = map + '#'
            flag = True
            if lab[i][j] == 0:
                for k in range(len(conj)):
                    if conj[k][0] == i and conj[k][1] == j:
                        map = map + '0'
                        flag = False
                if (flag):
                    map = map + '.'
        map = map + '\n'

    return map

def obter_objetivos(lab, conj, pos):

    '''
    A funcao obter_objetivos devolve o conjunto de posicoes (em qualquer ordem)
    nao ocupadas dentro do labirinto correspondente a todos os possiveis objetivos
    da unidade correspondente a posicao dada.

    obter_objetivos: labirinto x conj_posicoes x posicao -> conj_posicoes
    '''

    if not eh_mapa_valido(lab, conj) or not eh_posicao(pos) or pos not in conj:
        raise ValueError ('obter_objetivos: algum dos argumentos e invalido')

    # retiro a posicao da lista de unidades
    remaining_units = ()
    for i in range(len(conj)):
        if conj[i] != pos:
            remaining_units = remaining_units + (conj[i],)

    res = ()
    for j in range(len(remaining_units)):
        # descubro qual as posicoes adjacentes de cada tuplo na lista de unidades restantes
        pos_adj = posicoes_adjacentes(remaining_units[j])

        for i in range(len(pos_adj)):
            # retiro as posicoes repetidas
            if pos_adj[i] not in res:
                res = res + (pos_adj[i],)

    n_cols, n_linhas = len(lab), len(lab[0])
    num = len(res)

    tuplos_a_remover = ()
    for j in range(num):
        # seleciono as posicoes que sao paredes ou invalidas
        if res[j] == pos or res[j][0] == 0 or res[j][0] == n_cols-1 or res[j][0] >= n_cols or res[j][1] == 0 or res[j][1] == n_linhas-1 or res[j][1] >=n_linhas:
            tuplos_a_remover = tuplos_a_remover + (res[j],)

    sem_paredes = ()
    for i in range(num):
        # retiro as posicoes que sao paredes ou invalidas
        if res[i] not in tuplos_a_remover:
            sem_paredes = sem_paredes + (res[i],)

    return sem_paredes

def eh_parede(lab, conj):
    n_cols, n_linhas = len(lab), len(lab[0])
    num = len(conj)

    for j in range(num):
        if conj[j][0] == 0 or conj[j][0] == n_cols-1 or conj[j][0] >= n_cols or conj[j][1] == 0 or conj[j][1] == n_linhas-1 or conj[j][1] >=n_linhas:
            return True

    return False

def pos_preferencial(lab, conj):

    menor_x = len(lab)
    for i in range(len(conj)-1):
        if conj[i][0] < menor_x:
           menor_x = conj[i][0]

    menor_y = len(lab[0])
    for i in range(len(conj)-1):
        if conj[i][1] < menor_y and conj[i][0] == menor_x:
           menor_y = conj[i][1]

    return (menor_x,menor_y)

def caminho_pra_tras(pos_final, anterior):

    caminho = []
    pos = pos_final

    while pos in anterior:
        caminho.append(pos)
        pos = anterior[pos]

    caminho.append(pos) # isso eh a primeira posicao

    return tuple(reversed(caminho))

def obter_caminho(lab, conj, pos):
    '''
    A funcao obter_caminho devolve um conjunto de posicoes correspondente ao caminho de
    numero minimo de passos desde a posicao dada ate a posicao objetivo.

    obter_caminho: labirinto x conj_posicoes x posicao -> conj_posicoes
    '''
    if not eh_mapa_valido(lab, conj) or not eh_posicao(pos) or pos not in conj:
        raise ValueError ('obter_caminho: algum dos argumentos e invalido')

    #a fila contem apenas a posicao inicial
    fila_de_exploracao = [pos]
    posicoes_visitadas = []
    anterior = {}

    objetivos = obter_objetivos(lab,conj,pos)

    while len(fila_de_exploracao) != 0:
        pos_atual = fila_de_exploracao[0]
        #a posicao n foi visitada
        if pos_atual not in posicoes_visitadas:
            #adiciono a lista posicoes_visitadas
            posicoes_visitadas.append(pos_atual)

            if pos_atual in objetivos:
                return caminho_pra_tras(pos_atual, anterior)
            else:
                #posicoes adjacentes a posicao atual
                pos_adj = posicoes_adjacentes(pos_atual)

                for i in range(len(pos_adj)):
                    if pos_adj[i] not in conj and not eh_parede(lab, (pos_adj[i], )):
                        fila_de_exploracao.append(pos_adj[i])
                        if not pos_adj[i] in anterior:
                            anterior[pos_adj[i]] = pos_atual

        fila_de_exploracao.remove(fila_de_exploracao[0])

    return ()



def mover_unidade(lab, conj, pos):

    '''
    A funcao mover_unidade devolve o conjunto de posicoes actualizado correspondente
    as unidades presentes no labirinto apos a unidade dada ter realizado um unico movimento.

    mover_unidade: labirinto x conj_posicoes x posicao -> conj_posicoes
    '''

    if not eh_mapa_valido(lab, conj) or not eh_posicao(pos) or pos not in conj:
        raise ValueError ('mover_unidade: algum dos argumentos e invalido')

    adj = ()
    adj = adj + posicoes_adjacentes(pos)

    n_cols, n_linhas = len(lab), len(lab[0])
    num = len(adj)

    tuplos_a_remover = ()
    for j in range(num):
        if adj[j] == pos or adj[j][0] == 0 or adj[j][0] == n_cols-1 or adj[j][0] >= n_cols or adj[j][1] == 0 or adj[j][1] == n_linhas-1 or adj[j][1] >=n_linhas:
            tuplos_a_remover = tuplos_a_remover + (adj[j],)

    sem_paredes = ()
    for i in range(num):
        if adj[i] not in tuplos_a_remover:
            sem_paredes = sem_paredes + (adj[i],)

    res = ()
    for i in range(len(conj)):
        if not conj[i] == pos:
            res = res + (conj[i],)
        else:
            res = res + (sem_paredes[0],)

    return res


