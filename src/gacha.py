import json, random

with open("data/banners.json") as f:
    BANNER = json.load(f)

def pull(rng=random):
    roll = rng.random()
    total = 0
    for rarity, rate in BANNER["rates"].items():
        total += rate
        if roll <= total:
            return rarity, rng.choice(BANNER["pool"][rarity])
    return "3star", rng.choice(BANNER["pool"]["3star"])

if __name__ == "__main__":
    for i in range(10):
        print(i + 1, *pull())
