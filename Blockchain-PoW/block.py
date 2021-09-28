import hashlib as h 
    
class Block():
    def __init__(self,timestamp,transactions,previousHash=""):
        self.nonce = 0
        self.timestamp = timestamp
        self.transactions = transactions
        self.previousHash = previousHash
        self.hash =self.blockHash()

    def blockHash(self):
        block_encryption =h.sha256() 
        block_encryption.update((str(self.timestamp)+str(self.transactions)+str(self.previousHash)+str(self.nonce)).encode('utf-8')) 
        return block_encryption.hexdigest()
    def mineblock(self,difficulity):
        difficulity_level = ""
        while(str(self.hash)[0:difficulity]!= (difficulity_level.zfill(difficulity))):
            self.nonce += 1
            self.hash = self.blockHash()
        print("Block mined:" + str(self.hash))
    