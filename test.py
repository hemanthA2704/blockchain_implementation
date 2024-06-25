from blockchain import Blockchain
btc = Blockchain()
btc.createNewTransaction("0xBcd4042DE499D14e55001CcbB24a551F3b954096","0xa0Ee7A142d267C1f36714E4a8F75612F20a79720","100")
btc.createNewTransaction("0xa0Ee7A142d267C1f36714E4a8F75612F20a79720","0xBcd4042DE499D14e55001CcbB24a551F3b954096","100")
btc.createNewBlock()
print(btc.blocks)