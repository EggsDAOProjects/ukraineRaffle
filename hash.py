import hashlib

with open('./raffle_entries.json', 'rb') as f:
    filehash = hashlib.sha256(f.read()).hexdigest()
    print(filehash)
