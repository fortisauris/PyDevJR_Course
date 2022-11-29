import hmac
import pickle
import random


class BlockGenerator(object):
    """
    Class generates random blocks in Blockchain and stores them to 3 separate destinations.
    1. Local copy in .json format
    2. http vesrion in json version
    3 Cloud based copy ???
    """

    def __init__(self):
        self.block = self.block_generator()
        self.key = bytes('542354387254573', encoding='utf8')
        self.block_prepared = pickle.dumps(self.block)
        # print(block_prepared)
        self.block_bytes = bytes(self.block_prepared)
        self.hmac_obj = hmac.new(key=self.key, msg=self.block_bytes, digestmod='md5')  # Vytvarame si HMAC object
        # H L A V N  Y    P R O G R A M
        self.main_procedure()

    def main_procedure(self):
        '''
        Main loop of generator.
        '''
        c = 1
        while True:
            print(self.hmac_obj.hexdigest())
            self.hmac_obj.update(bytes(c))  # prihadzujeme do mixera
            if self.hmac_obj.hexdigest()[:2] == '00':
                print('VALID BLOCK', self.hmac_obj.hexdigest())
                raw_block = pickle.loads(self.block_bytes)
                [print(i) for i in raw_block]  # LIST COMPREHENSION
                c = 1
                input()  # TU TO ZASTAVUJE A CAKA NA POVEL
            else:
                c += 1

    def account_generator(self):
        """
        Generates random content of block. Our blockchain is filled with Transaction info
        """
        return random.randint(111111111, 999999999)

    def block_generator(self, length: int):
        '''
        Generates Block content
        '''
        empty_block = []
        for i in range(0, length):
            transakcia = dict()
            transakcia['account1'] = self.account_generator()
            transakcia['account2'] = self.account_generator()
            transakcia['amount'] = random.randint(1,1000)
            empty_block.append(transakcia)
        return empty_block


if __name__ == '__main__':
    obj = BlockGenerator()  # construct object of Blockchain generator


