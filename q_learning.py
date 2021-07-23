# refs:
# https://www.youtube.com/watch?v=iKdlKYG78j4
# https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/
# Eu tava muito "enrolado" para entender e escrever o algoritmo. Contei com ajuda do codigo de Mariana Medeiros :D

import pandas as pd
import numpy as np


def q_update(current_state_action_q, next_state_action_q, action_reward):
    alpha = 0.5
    gamma = 0.8

    error = action_reward + gamma*next_state_action_q - current_state_action_q

    return current_state_action_q + alpha*error


def run(current_state, sequence, matrix, rewards, q_matrix):
    q_matrix = q_matrix.copy()
    for action in sequence:
        next_state = matrix.loc[current_state, action]
        print(
            f"------\nSaindo de {current_state} e indo para {next_state}({action})")

        if next_state == "wall" or next_state == "6":
            rw = next_state
        else:
            rw = "any"
        action_reward = rewards[rw]
        print(f"Reward: {action_reward}")
        current_state_action_q = q_matrix.loc[current_state, action]

        # if next_state == "6":
        #

        if next_state != "wall":
            next_state = int(next_state)
        else:
            next_state = current_state

        next_state_action_q = max(q_matrix.loc[next_state, :])

        current_state_action_q_updated = q_update(
            current_state_action_q=current_state_action_q,
            next_state_action_q=next_state_action_q,
            action_reward=action_reward,
        )

        q_matrix.loc[current_state, action] = current_state_action_q_updated

        print(f"q_matrix:\n", q_matrix, "\n")

        current_state = next_state

    return q_matrix


if __name__ == "__main__":
    actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    states = 6

    matrix = pd.DataFrame(
        {
            "UP": ["2", "3", "wall", "5", "6", "wall"],
            "DOWN": ["wall", "1", "2", "wall", "4", "5"],
            "LEFT": ["wall", "wall", "wall", "1", "2", "3"],
            "RIGHT": ["4", "5", "6", "wall", "wall", "wall"]
        },
        index=range(1, states+1)
    )

    rewards = {
        "6": 10,
        "wall": -10,
        "any": -1
    }

    # matrix zerada
    q_matrix = pd.DataFrame(
        np.zeros((states, len(actions))),
        columns=actions,
        index=range(1, states+1)
    )
    # UTILIDADE NO ESTADO 6 (para qualquer ação) SERIA JÁ A RECOMPENSA? SE SIM, DESCOMENTAR ESTA LINHA!
    q_matrix.loc[6, :] = rewards["6"]

    ##

    # Estado inicial 1, U,U,U,R
    print("Estado inicial 1, U,U,U,R (aperte a tecla Enter para Iniciar)")
    input()
    current_state = 1
    sequence = ["UP", "UP", "UP", "RIGHT"]

    print(matrix, "\n")
    print(q_matrix, "\n")
    final_q_matrix_1 = run(
        current_state=current_state,
        sequence=sequence,
        matrix=matrix,
        rewards=rewards,
        q_matrix=q_matrix,
    )

    # Estado inicial 5, L,L,U,R
    print("\n--------\nEstado inicial 5, L,L,U,R (aperte a tecla Enter para Iniciar)")
    input()

    current_state = 5
    sequence = ["LEFT", "LEFT", "UP", "RIGHT"]

    print(matrix, "\n")
    print(final_q_matrix_1, "\n")
    final_q_matrix_2 = run(
        current_state=current_state,
        sequence=sequence,
        matrix=matrix,
        rewards=rewards,
        q_matrix=final_q_matrix_1,
    )
    print(final_q_matrix_2)
