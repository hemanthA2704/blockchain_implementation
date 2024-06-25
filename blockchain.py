from datetime import datetime
from hashlib import sha256
class Blockchain:
    def __init__(self):
        self.blocks = [self.createGenesisBlock()]
        self.pendingTransactions = []

    def createGenesisBlock(self):
        return {
            "timestamp" : datetime.now() ,
            "hash" : "hash" ,
            "prevBlockHash" : "prevblockhash" ,
            "nonce" : "nonce" ,
            "transactions" : []
        }
    
    def getLastBlockHash(self):
        lastBlock = self.blocks[-1]
        return lastBlock["hash"]

    def createNewTransaction(self,sender,reciever,amount):
        newTransaction = {
            "sender" : sender ,
            "reciever" : reciever ,
            "amount" : amount
        }
        self.pendingTransactions.append(newTransaction)

    def generateHash(self,prevBlockHash,timestamp,pendingTransactions):
        hash=""
        nonce=0
        while hash[:3] != "000" :
            nonce+=1
            data = prevBlockHash + str(timestamp) + str(pendingTransactions) + str(nonce)
            hash = sha256(data.encode())
            hash = hash.hexdigest()
            hash = str(hash)
        return {"hash" : hash , "nonce" : nonce}
    
    def createNewBlock(self):
        timestamp = datetime.now()
        prevBlockHash = self.getLastBlockHash()
        pendingTransactions = self.pendingTransactions
        newHash = self.generateHash(prevBlockHash,timestamp,pendingTransactions)
        newBlock = {
            "timestamp" : timestamp ,
            "hash" : newHash["hash"] ,
            "prevBlockHash" : prevBlockHash ,
            "nonce" : newHash["nonce"] ,
            "transactions" : pendingTransactions
        }
        self.pendingTransactions = []
        self.blocks.append(newBlock)
        return newBlock

