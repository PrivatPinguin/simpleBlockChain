class BlockData():
    """
    Data-Block
    ------------
    
    this Dataset is filled with
    'from'
    'to'
    'ammount'

    feel free to extend this funktions

    """
    def __init__(self):
        self.from_ = -1
        self.to_ = -1
        self.ammount = -1
    
    def __Set__(from_=-1, to_=-1, ammount=0):
        self = BlockData()
        self.from_ = from_
        self.to_ = to_
        self.ammount = ammount
        if ( (from_ == -1) | (to_ == -1) | (ammount == 0) ):
            ValueError
        else:
            return self

class Hash():
    def __init__(self):
        self.hash = -1
        self.controllsum = -1

    def __Set__( this_blockdata:BlockData):
        self = Hash()
        if type(this_blockdata) == BlockData:
            self.hash = hash(this_blockdata)
            for char in str(self.hash):
                self.controllsum += int(char) + this_blockdata.ammount
            return self
        else:
            TypeError(this_blockdata)

class Block():
    def __init__(self):
        self.prev = -1
        self.data = -1
        self.hash = -1

    def __NewBlock__(self, prevBlockHash:Hash, data:BlockData, hash:Hash):
        self = Block()
        if type(prevBlockHash) == Hash:
            self.prev = prevBlockHash
        else:
            TypeError(Hash)

        if type(data) == BlockData:
            self.data = data
        else:
            TypeError(BlockData)

        if type(hash) == Hash:
            self.hash = hash
        else:
            TypeError(Hash)
        return self
    
    def __Generate_Block__( previous_block:Hash, from_, to_, ammount):
        self = Block()
        if type(previous_block) == Hash:
            self.prev = previous_block
        else:
            return TypeError(previous_block)
        this_data = BlockData.__Set__(from_,to_,ammount)
        if type(this_data) != BlockData:
            return TypeError(this_data)
        this_hash = Hash.__Set__(this_data)
        if type(this_hash) != Hash:
            return TypeError(this_hash)
        self = self.__NewBlock__(previous_block,this_data,this_hash)
        return self

class BlockChain():
    
    def __init__(self):
        self.__chain__ = []
    
    def check_blockchain_data(self, string:bool=False):
        """
        Prints BlockChain
        ------------
        
        usage:

        set var to True[:bool] to get a string, instead of a console print
        ------
        your_blockchain.check_blockchain_data()
            <Prints to Console>
        or
        data = your_blockchain.check_blockchain_data(True)
        data:str

        Returns notifications for Block with Error.

        """
        log_msg = ''
        try:
            previous_hash = None
            if string:
                for cnt, block in enumerate(self.__chain__):
                    if ( (block.prev.hash == previous_hash) | (previous_hash == None) ):
                        log_msg += '{}\nFrom: {}\tTo: {}\n\tAmmount: {}\nPrevious Hash: {}\tThis Hash: {}\n\tChecksum: {}\n'.format(cnt, block.data.from_, block.data.to_, block.data.ammount, block.prev.hash, block.hash.hash, block.hash.controllsum)
                        
                    else:
                        print('\nFATAL ERROR:\tChain Corrupted at position', str(cnt), '\n')
                    previous_hash = block.hash.hash
                return log_msg
            else:
                for cnt, block in enumerate(self.__chain__):
                    if ( (block.hash.hash == previous_hash) | (previous_hash == None) ):
                        print(cnt, '\nFrom:', block.data.from_, '\tTo:', block.data.to_, '\n\tAmmount:', block.data.ammount,'\nPrevious Hash', block.prev.hash, '\tThis Hash:', block.hash.hash, 'Checksum:', block.hash.controllsum, '\n')
        except Exception as e:
            print('Corrupted BlockNumber:', str(cnt), '\n')
            print(e)
            

    def New_Genisis_Block():
        """
        Creates first block in BlockChain
        ------------
        
        usage:
        ------
        your_blockchain = BlockChain.New_Genisis_Block()

        return a list with starting Genesis-Block

        """
        self = BlockChain()
        Genisis_block = BlockData.__Set__('bao', 'foa', 2.4)
        genesis_hash = Hash.__Set__(Genisis_block)
        self.__chain__.append( Block.__Generate_Block__(genesis_hash, 'foo', 'baa', 4.2) )
        return self

    def New_Block(self, from_, to_, ammount)->Block:
        """
        Appends a new Block to the previous one
        ------------
        
        usage:
        ------
        first implement Genesis Block:
            your_blockchain = BlockChain.New_Genisis_Block()

        after that you can input new Blocks to Chain with {New_Block}:
            your_blockchain.New_Block('from', 'to', 'ammount')

        returns BlockChain

        """
        prev_block_hash = self.__chain__[len(self.__chain__)-1].hash
        self.__chain__.append( Block.__Generate_Block__(prev_block_hash, from_, to_, ammount) )
        return self


#How to implement
your_blockchain = BlockChain.New_Genisis_Block()
your_blockchain.New_Block('this', 'that', 13.37)
your_blockchain.New_Block('from', 'to', 73.13)
# as many blocks as you want.

this = your_blockchain.check_blockchain_data(True)
print(this)
# is mostly same to
your_blockchain.check_blockchain_data()