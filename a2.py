import hashlib
import json
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):  # Corrected __init__
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):  # Corrected __init__
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.previous_hash != previous_block.hash:
                return False

            if current_block.calculate_hash() != current_block.hash:
                return False

        return True

# Example usage:
blockchain = Blockchain()

# Add patient data to the blockchain
patient_data = {
    "name": "John Doe",
    "age": 30,
    "medical_history": "Hypertension"
}
blockchain.add_block(Block(1, time.time(), patient_data, blockchain.get_latest_block().hash))

# Verify chain integrity
if blockchain.is_chain_valid():
    print("Blockchain is valid.")
else:
    print("Blockchain is invalid.")