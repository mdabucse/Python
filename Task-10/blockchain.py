from block import Block
from utils import verify_transaction

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]   # First block
        self.difficulty = 4                          # Mining difficulty
        self.mempool = []                            # Pending transactions

    def create_genesis_block(self):
        """
        First block in the chain
        """
        return Block(0, [], "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        """
        Add transaction to mempool
        """
        self.mempool.append(transaction)

    def mine_block(self, miner_address):
        """
        Mine all transactions in mempool
        """

        # Reward transaction (miner gets coins)
        reward_tx = {
            "sender": "SYSTEM",
            "receiver": miner_address,
            "amount": 1.0
        }

        self.mempool.append(reward_tx)

        new_block = Block(
            index=len(self.chain),
            transactions=self.mempool,
            prev_hash=self.get_last_block().hash
        )

        # Proof of Work
        while not new_block.hash.startswith("0" * self.difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        print(f" Block mined: {new_block.hash}")

        self.chain.append(new_block)
        self.mempool = []   # Clear transactions
    


    def add_transaction(self, transaction):
        if not transaction.is_valid():
            print(" Invalid transaction structure")
            return False

        if not verify_transaction(transaction):
            print(" Invalid signature")
            return False

        self.mempool.append(transaction.to_dict())
        return True