import hashlib
import time
import json
from utils import calculate_merkle_root

class Block:
    def __init__(self, index, transactions, prev_hash):
        self.index = index                    # Block number
        self.timestamp = time.time()          # Creation time
        self.transactions = transactions      # List of transactions
        self.prev_hash = prev_hash            # Previous block hash
        self.nonce = 0                        # Used for mining
        self.hash = self.calculate_hash()     # Current block hash

    def calculate_hash(self):
        """
        Convert block data → string → SHA256 hash
        """

        block_data = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "prev_hash": self.prev_hash,
            "nonce": self.nonce,
            "merkle_root": self.merkle_root
        }, sort_keys=True)

        return hashlib.sha256(block_data.encode()).hexdigest()