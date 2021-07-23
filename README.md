# Atividade_Q_Learning
Disciplina Agentes Cognitivos e Adaptativos

# Exercicio
* Considere o ambiente 3 x 2 onde a posição 6 é o estado terminal;
* Assuma que as ações UP, DOWN, LEFT e RIGHT são determinísticas.

Recompensas:
* +10 no estado 6;
* -10 se bater na parede;
* -1 nos outros casos.

Aplicar o Q-learning sequencialmente usando as seguintes trajetórias:

* Estado inicial 1, sequência U,U,U,R;
* Estado inicial 5: sequência L,L,U,R. 

Inicialize a matriz Q com zeros e assuma alpha = 0.5 e gamma = 0.8.


## Para rodar
```sh
python3 q_learning.py
```

## Output
```
Estado inicial 1, U,U,U,R (aperte a tecla Enter para Iniciar)

     UP  DOWN  LEFT RIGHT
1     2  wall  wall     4
2     3     1  wall     5
3  wall     2  wall     6
4     5  wall     1  wall
5     6     4     2  wall
6  wall     5     3  wall 

     UP  DOWN  LEFT  RIGHT
1   0.0   0.0   0.0    0.0
2   0.0   0.0   0.0    0.0
3   0.0   0.0   0.0    0.0
4   0.0   0.0   0.0    0.0
5   0.0   0.0   0.0    0.0
6  10.0  10.0  10.0   10.0 

------
Saindo de 1 e indo para 2(UP)
Reward: -1
q_matrix:
      UP  DOWN  LEFT  RIGHT
1  -0.5   0.0   0.0    0.0
2   0.0   0.0   0.0    0.0
3   0.0   0.0   0.0    0.0
4   0.0   0.0   0.0    0.0
5   0.0   0.0   0.0    0.0
6  10.0  10.0  10.0   10.0 

------
Saindo de 2 e indo para 3(UP)
Reward: -1
q_matrix:
      UP  DOWN  LEFT  RIGHT
1  -0.5   0.0   0.0    0.0
2  -0.5   0.0   0.0    0.0
3   0.0   0.0   0.0    0.0
4   0.0   0.0   0.0    0.0
5   0.0   0.0   0.0    0.0
6  10.0  10.0  10.0   10.0 

------
Saindo de 3 e indo para wall(UP)
Reward: -10
q_matrix:
      UP  DOWN  LEFT  RIGHT
1  -0.5   0.0   0.0    0.0
2  -0.5   0.0   0.0    0.0
3  -5.0   0.0   0.0    0.0
4   0.0   0.0   0.0    0.0
5   0.0   0.0   0.0    0.0
6  10.0  10.0  10.0   10.0 

------
Saindo de 3 e indo para 6(RIGHT)
Reward: 10
q_matrix:
      UP  DOWN  LEFT  RIGHT
1  -0.5   0.0   0.0    0.0
2  -0.5   0.0   0.0    0.0
3  -5.0   0.0   0.0    9.0
4   0.0   0.0   0.0    0.0
5   0.0   0.0   0.0    0.0
6  10.0  10.0  10.0   10.0 


--------
Estado inicial 5, L,L,U,R (aperte a tecla Enter para Iniciar)

     UP  DOWN  LEFT RIGHT
1     2  wall  wall     4
2     3     1  wall     5
3  wall     2  wall     6
4     5  wall     1  wall
5     6     4     2  wall
6  wall     5     3  wall 

     UP  DOWN  LEFT  RIGHT
1  -0.5   0.0   0.0    0.0
2  -0.5   0.0   0.0    0.0
3  -5.0   0.0   0.0    9.0
4   0.0   0.0   0.0    0.0
5   0.0   0.0   0.0    0.0
6  10.0  10.0  10.0   10.0 

------
Saindo de 5 e indo para 2(LEFT)
Reward: -1
q_matrix:
      UP  DOWN  LEFT  RIGHT
1  -0.5   0.0   0.0    0.0
2  -0.5   0.0   0.0    0.0
3  -5.0   0.0   0.0    9.0
4   0.0   0.0   0.0    0.0
5   0.0   0.0  -0.5    0.0
6  10.0  10.0  10.0   10.0 

------
Saindo de 2 e indo para wall(LEFT)
Reward: -10
q_matrix:
      UP  DOWN  LEFT  RIGHT
1  -0.5   0.0   0.0    0.0
2  -0.5   0.0  -5.0    0.0
3  -5.0   0.0   0.0    9.0
4   0.0   0.0   0.0    0.0
5   0.0   0.0  -0.5    0.0
6  10.0  10.0  10.0   10.0 

------
Saindo de 2 e indo para 3(UP)
Reward: -1
q_matrix:
       UP  DOWN  LEFT  RIGHT
1  -0.50   0.0   0.0    0.0
2   2.85   0.0  -5.0    0.0
3  -5.00   0.0   0.0    9.0
4   0.00   0.0   0.0    0.0
5   0.00   0.0  -0.5    0.0
6  10.00  10.0  10.0   10.0 

------
Saindo de 3 e indo para 6(RIGHT)
Reward: 10
q_matrix:
       UP  DOWN  LEFT  RIGHT
1  -0.50   0.0   0.0    0.0
2   2.85   0.0  -5.0    0.0
3  -5.00   0.0   0.0   13.5
4   0.00   0.0   0.0    0.0
5   0.00   0.0  -0.5    0.0
6  10.00  10.0  10.0   10.0 

      UP  DOWN  LEFT  RIGHT
1  -0.50   0.0   0.0    0.0
2   2.85   0.0  -5.0    0.0
3  -5.00   0.0   0.0   13.5
4   0.00   0.0   0.0    0.0
5   0.00   0.0  -0.5    0.0
6  10.00  10.0  10.0   10.0

```

## refs
* https://www.youtube.com/watch?v=iKdlKYG78j4
* https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/
* Eu tava muito "enrolado" para entender e escrever o algoritmo. Contei com ajuda do codigo de Mariana Medeiros :D
