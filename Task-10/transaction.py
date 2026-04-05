import time
import hashlib
import json

class Transaction:
    def __init__(self, sender, receiver, amount, signature=None, public_key=None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()
        self.signature = signature
        self.public_key = public_key
        self.tx_id = self.calculate_hash()

    def calculate_hash(self):
        tx_data = json.dumps({
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "timestamp": self.timestamp
        }, sort_keys=True)

        return hashlib.sha256(tx_data.encode()).hexdigest()

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "timestamp": self.timestamp,
            "tx_id": self.tx_id,
            "signature": self.signature.hex() if self.signature else None,
            "public_key": self.public_key   # 👈 THIS LINE YOU ADD
        }

    def is_valid(self):
        if self.sender == self.receiver:
            return False
        if self.amount <= 0:
            return False
        if not self.sender or not self.receiver:
            return False
        return True