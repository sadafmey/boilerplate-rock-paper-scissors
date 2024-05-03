def player(prev_play):
    # Initialize an empty list to store the opponent's history
    opponent_history = []

    # Append the previous play to the opponent's history
    opponent_history.append(prev_play)

    # If this is the first move, return a random move
    if not opponent_history:
        import random
        moves = ['R', 'P', 'S']
        return random.choice(moves)

    # If the opponent's last move is the same as the move before that, play the move that beats it
    if len(opponent_history) > 1 and opponent_history[-1] == opponent_history[-2]:
        if opponent_history[-1] == 'R':
            return 'P'
        elif opponent_history[-1] == 'P':
            return 'S'
        else:
            return 'R'

    # Otherwise, play the same move as the opponent's last move
    else:
        return opponent_history[-1]