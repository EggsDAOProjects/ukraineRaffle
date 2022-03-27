import json
import random
import sys


def pick_winner(tickets):
    return random.choice(tickets)


if __name__ == '__main__':
    seed = sys.argv[1]
    random.seed(seed)

    with open('./raffle_entries.json') as f:
        tickets = json.loads(f.read())

    winner = pick_winner(tickets)
    print(winner)
