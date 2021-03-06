import json
import random
import sys


def pick_winner(tickets, winners=1):
    all_winners = []

    for i in range(winners):
        indices = range(len(tickets))
        winning_index = random.choice(indices)
        all_winners.append(tickets[winning_index])
        tickets.pop(winning_index)

    return all_winners


if __name__ == '__main__':
    seed = sys.argv[1]
    random.seed(seed)

    winners = 1
    if len(sys.argv) > 2:
        winners = int(sys.argv[2])

    with open('./raffle_entries.json') as f:
        tickets = json.loads(f.read())

    all_winners = pick_winner(tickets, winners)

    for i, winner in enumerate(all_winners):
        print(f"{i+1}.", winner)
