import hashlib

def hashgenrator(data):
     result=hashlib.sha256(data.encoded())
     return result.hexdigest

class Block:
    def __init__(self,data,hash,prev_hash):
        self.data=data
        self.hash=hash
        self.prev_hash=prev_hash

class Blockchain:
    def __init__(self):
     hashlast=hashgenrator ('gen_last')
     hashstart=hashgenrator ('gen_hash')


     genesis=Block('gen-data',hashstart,hashlast)
     self.chain=[genesis]

    def add_block(self,data):
        prev_hash=self.chain[-1].hash
        hash=hashgenrator(data+prev_hash)
        block=Block(data,hash,prev_hash)
        self.chain.append(block)


bc=Blockchain()
bc.addblock('1')
bc.addblock('2')
bc.addblock('3')

for blocks in bc.chain:
    print(blocks.__dict__)

    
