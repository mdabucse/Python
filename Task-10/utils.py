from ecdsa import VerifyingKey
import hashlib
import json
def verify_transaction(transaction):
    if transaction.sender == "SYSTEM":
        return True  # mining reward

    try:
        public_key = VerifyingKey.from_string(
            bytes.fromhex(transaction.public_key)
        )

        return public_key.verify(
            bytes.fromhex(transaction.signature),
            transaction.tx_id.encode()
        )

    except:
        return False

def calculate_merkle_root(transactions):
    """
    Generate Merkle Root from transactions
    """

    if not transactions:
        return None

    # Step 1: hash all transactions
    hashes = [
        hashlib.sha256(json.dumps(tx, sort_keys=True).encode()).hexdigest()
        for tx in transactions
    ]

    # Step 2: build tree
    while len(hashes) > 1:
        temp = []

        for i in range(0, len(hashes), 2):
            left = hashes[i]
            right = hashes[i+1] if i+1 < len(hashes) else left

            combined = left + right
            new_hash = hashlib.sha256(combined.encode()).hexdigest()

            temp.append(new_hash)

        hashes = temp

    return hashes[0]