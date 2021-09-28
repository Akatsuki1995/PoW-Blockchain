from block import Block as block
from transactions import Transaction as tra
import datetime as d 


class Blockchain():
    def __init__(self):
        self.chain = [self.genesisBlock()]
        self.difficulity=4
        self.pendingTransactions = []
        self.Reward = 100;
    @staticmethod
    def genesisBlock():
        return block("01/01/2021","Genesis Block"," ")
    def getLatestBlock(self):
        return self.chain[-1]
    def minePendingTransactions(self,miningRewardAddress):
        newblock = block(d.datetime.now,self.pendingTransactions)
        newblock.mineblock(self.difficulity)
        print("Block seccessfully mined!")
        self.chain.append(newblock)
        self.pendingTransactions = tra(None,miningRewardAddress,self.Reward),
    def createTransaction(self,transaction):
        self.pendingTransactions.append(transaction)
    def getBalanceOfAddress(self,address):
        balance = 0
        for b in range(1,len(self.chain)):
            hh = self.chain[b].transactions
            print("this is what I need",hh)
            for number in hh:
                if(number.fromAddress == address):
                    balance -= number.amount
                if(number.toaddress == address):
                    balance += number.amount
        return balance
    def verifyBlockchain(self):
        for i in range(1,len(self.chain)):
            this_block = self.chain[i]
            previous_block = self.chain[i-1]
            if (this_block.hash != this_block.blockHash()):
                return False
            if (previous_block.hash != this_block.previousHash):
                return False
        return True

bb = Blockchain()
bb.createTransaction(tra("address1","address2",100))
bb.createTransaction(tra("address2","address1",10))

print("Starting the miner...")
bb.minePendingTransactions("hakamaddress")

print("balance of hakam is", bb.getBalanceOfAddress("hakamaddress"))
print("Starting the miner again ....")
bb.minePendingTransactions("hakamaddress")
print("balance of hakam is", bb.getBalanceOfAddress("hakamaddress"))


