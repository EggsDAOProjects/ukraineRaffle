# EggsForUkraine Raffle
This repo holds the code and raffle entries for the EggsForUkraine raffle.

The raffle script takes as input a string to be used as the seed entropy for the randomness. This seed will be a block hash for a block decided ahead of time. By using the hash of a future block there is a non-determinism to the randomness which makes it fair for all participants. The added bonus is the results can be externally verified by anyone using the code in this repo.

### Usage
```
python raffle.py <random seed>
```

### Raffle Entries JSON validity
The raffle results are picked from the tickets in `raffle_entires.json`. This JSON file contains all the addresses that are entered into the raffle. Each address is included once per entry ie if a user has 12 entries then their address will be in that JSON array 12 times.

The proof that this file has not been tampered with will be done using `hash.py`. The file will be hashed and the hash will be announced before the seed entropy block is mined. This will allow anyone to verify that the file has not been tampered with after the fact and the results can therefore be trusted.

Running `python hash.py` requires the file `raffle_entries.json` to exist. The script will hash that file and return the hex digest of that hash. This allows users to prove the file they have is identical to the one used to draw the raffle. This plus the usage of future block hash for seed entropy allows the entire raffle to be provably fair.

If/when more people buy tickets into future raffles the `raffle_entries.json` file will be updated. The hash of the new file will be announced before the subsequent raffle is drawn.
