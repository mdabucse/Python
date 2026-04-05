from ecdsa import SigningKey, SECP256k1
import hashlib

class Wallet:
    def __init__(self):
        # Generate private key
        self.private_key = SigningKey.generate(curve=SECP256k1)

        # Generate public key
        self.public_key = self.private_key.get_verifying_key()

        # Wallet address (shortened hash of public key)
        self.address = self.generate_address()

    def generate_address(self):
        """
        Create wallet address from public key
        """
        pub_key_bytes = self.public_key.to_string()
        return hashlib.sha256(pub_key_bytes).hexdigest()

    def sign_transaction(self, message):
        """
        Sign a message (transaction)
        """
        return self.private_key.sign(message.encode())

    def get_public_key(self):
        return self.public_key