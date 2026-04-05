from utils import calculate_merkle_root

txs = [
    {"a": 1},
    {"b": 2},
    {"c": 3}
]

root1 = calculate_merkle_root(txs)

# Modify one transaction
txs[0]["a"] = 999

root2 = calculate_merkle_root(txs)

print("Root before:", root1)
print("Root after :", root2)