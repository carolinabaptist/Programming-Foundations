from FP_proj1_1920 import *

#representação do labirinto e das unidades

#eh_labirinto

maze = ((1,1,1,1),(1,0,0,1),(1,0,0,1),(1,0,0,1),(1,1,1,1))
assert eh_labirinto(maze) == True

maze = ((1,1,1,1),(1,0,0,1),(1,0,0,1),(1,0,0,1),(1,1,1))
assert eh_labirinto(maze) == False

maze = ((0,0,0,0),(1,0,0,1),(1,0,0,1),(1,0,0,1),(1,1,1,1))
assert eh_labirinto(maze) == False

maze = 1
assert eh_labirinto(maze) == False

maze = 'Oi'
assert eh_labirinto(maze) == False

maze = ()
assert eh_labirinto(maze) == False

maze = ((1, 1, 1, 1), (1, 0, 1), (1, 0, 0, 1), (1, 1, 1, 1))
assert eh_labirinto(maze) == False

maze = ((1, 1, 1, 1), (1, 0, 0, 1), (1, 0, 1), (1, 0, 0, 1), (1, 1, 1, 1))
assert eh_labirinto(maze) == False

maze = ((1, 1, 1, 1), (1, 0, 2, 1), (1, 0, 0, 1), (1, 1, 1, 1))
assert eh_labirinto(maze) == False

maze = ((1, 1, 1, 1), (1, 'a', 0, 1), (1, 0, 0, 1), (1, 1, 1, 1))
assert eh_labirinto(maze) == False

maze = (1, (1, 1, 0, 1), (1, 0, 0, 1), (1, 1, 1, 1))
assert eh_labirinto(maze) == False

#eh_posicao
assert eh_posicao((0,2)) == True
assert eh_posicao((1,-2)) == False
assert eh_posicao((1,1,2)) == False
assert eh_posicao('a') == False
assert eh_posicao((1,'a')) == False
assert eh_posicao(()) == False
assert eh_posicao((1.5, 2)) == False
assert eh_posicao((1.5, 2.5)) == False
assert eh_posicao((-1, -2)) == False
assert eh_posicao((0, 0)) == True

#eh_conj_posicoes
assert eh_conj_posicoes(((1,1),(2,2))) == True
assert eh_conj_posicoes((())) == True
assert eh_conj_posicoes(((1,1),)) == True
assert eh_conj_posicoes(((1,1),(-5,5))) == False
assert eh_conj_posicoes(((1,1),(2,2),(2,2))) == False
assert eh_conj_posicoes(((1, 1), (2, 2), (2, 2), (3, 3))) == False
assert eh_conj_posicoes(((1, 1), (1, 1), (2, 2), (3, 3))) == False
assert eh_conj_posicoes(((1, 1), (2, 2), (3, 3), (4, 4), (4, 4))) == False
assert eh_conj_posicoes(('a', 'b', 'c')) == False
assert eh_conj_posicoes([(1, 1), (2, 2), (3, 3)]) == False

#tamanho_labirinto

maze = ((1,1,1,1),(1,0,0,1),(1,0,0,1),(1,0,0,1),(1,1,1,1))
assert  tamanho_labirinto(maze) == (5, 4)
maze = ((1,1,1,1),(1,0,0,1),(1,0,0,1),(1,1,1,1))
assert  tamanho_labirinto(maze) == (4, 4)


#eh_mapa_valido
maze = ((1,1,1,1),(1,0,0,1),(1,0,0,1),(1,0,0,1),(1,1,1,1))
assert eh_mapa_valido(maze, ((1,1),(2,2))) == True
assert eh_mapa_valido(maze, ((1,1),(5,5))) == False
assert eh_mapa_valido(maze, ((0,1),(2,2))) == False

#1 parede vertical
assert eh_mapa_valido(maze, ((1,1),(0,2))) == False
assert eh_mapa_valido(maze, ((1,1),(0,1))) == False
assert eh_mapa_valido(maze, ((1,1),(0,0))) == False

#1 parede horizontal
assert eh_mapa_valido(maze, ((1,1),(1,0))) == False
assert eh_mapa_valido(maze, ((1,1),(2,0))) == False
assert eh_mapa_valido(maze, ((1,1),(4,0))) == False

#2 parede vertical
assert eh_mapa_valido(maze, ((1,1),(4,1))) == False
assert eh_mapa_valido(maze, ((1,1),(4,2))) == False
assert eh_mapa_valido(maze, ((1,1),(4,3))) == False

#2 parede horizontal
assert eh_mapa_valido(maze, ((1,1),(1,3))) == False
assert eh_mapa_valido(maze, ((1,1),(2,3))) == False

#eh_posicao_livre
maze = ((1,1,1,1,1),(1,0,0,0,1),(1,0,0,0,1),(1,0,0,0,1),
(1,0,0,0,1),(1,0,0,0,1),(1,1,1,1,1))
unidades = ((2,1),(4,3))
assert  eh_posicao_livre(maze, unidades, (2,2)) == True

#1 parede vertical
assert  eh_posicao_livre(maze, unidades, (0,0)) == False
assert  eh_posicao_livre(maze, unidades, (0,1)) == False
assert  eh_posicao_livre(maze, unidades, (0,2)) == False
assert  eh_posicao_livre(maze, unidades, (0,3)) == False

#1 parede horizontal
assert  eh_posicao_livre(maze, unidades, (1,0)) == False
assert  eh_posicao_livre(maze, unidades, (2,0)) == False
assert  eh_posicao_livre(maze, unidades, (3,0)) == False
assert  eh_posicao_livre(maze, unidades, (4,0)) == False

#2 parede vertical
assert  eh_posicao_livre(maze, unidades, (6,0)) == False
assert  eh_posicao_livre(maze, unidades, (6,1)) == False
assert  eh_posicao_livre(maze, unidades, (6,2)) == False
assert  eh_posicao_livre(maze, unidades, (6,3)) == False

#2 parede horizontal
assert  eh_posicao_livre(maze, unidades, (0,4)) == False
assert  eh_posicao_livre(maze, unidades, (1,4)) == False
assert  eh_posicao_livre(maze, unidades, (2,4)) == False

assert  eh_posicao_livre(maze, unidades, (4,3)) == False

#posicoes_adjacentes
assert posicoes_adjacentes((2,1)) == ((2, 0), (1, 1), (3, 1), (2, 2))
assert posicoes_adjacentes((3,2)) == ((3, 1), (2, 2), (4, 2), (3, 3))
assert posicoes_adjacentes((0,0)) == ((1, 0), (0, 1))


#funcoes de movimento

#obter_objetivos

maze = ((1,1,1,1,1),(1,0,0,0,1),(1,0,0,0,1),(1,0,0,0,1),(1,0,0,0,1),(1,0,0,0,1),(1,1,1,1,1))
unidades = ((2,1),(4,3))
assert obter_objetivos(maze, unidades, (2,1)) == ((4, 2), (3, 3), (5, 3))
assert obter_objetivos(maze, unidades[:1], (2,1)) == ()

unidades = ((2,1),(5,2),(4,3))
assert obter_objetivos(maze, unidades, (2,1)) == ((5, 1), (4, 2), (5, 3), (3, 3))

unidades = ((4,2),(4,3))
assert obter_objetivos(maze, unidades, (4,2)) == ((3, 3), (5, 3))

