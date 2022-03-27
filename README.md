# EggsForUkraine Raffle
This repo holds the code and raffle entries for the EggsForUkraine raffle.

The raffle script takes as input a string to be used as the seed entropy for the randomness. This seed will be a block hash for a block decided ahead of time. By using the hash of a future block there is a non-determinism to the randomness which makes it fair for all participants. The added bonus is the results can be externally verified by anyone using the code in this repo.

### Usage
```
python raffle.py <random seed>
```

If/when more people buy tickets into future raffles the `raffle_entries.json` file will be updated.
