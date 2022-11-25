import hmac
import pickle
import random

def account_generator():
    return random.randint(111111111,999999999)

def block_generator():
    block = []
    for i in range(0,5):
        transakcia = dict()
        transakcia['account1'] = account_generator()
        transakcia['account2'] = account_generator()
        transakcia['amount'] = random.randint(1,1000000)
        block.append(transakcia)
    return block


block = block_generator()

key = bytes('542354387254573', encoding='utf8')

block_prepared = pickle.dumps(block)
print(block_prepared)
block_bytes = bytes(block_prepared)
print(block_bytes)

obj = hmac.new(key=key, msg=block_bytes, digestmod='md5')  # Vytvarame si HMAC object

# vypocitavame Valid block

c = 1
while True:
    print(obj.hexdigest())
    obj.update(bytes(c))  # prihadzujeme do mixera
    if obj.hexdigest()[:2] == '00':
        print('VALID BLOCK', obj.hexdigest())
        print(pickle.loads(block_bytes))
        c = 1
        input()
    else:
        c += 1

# JSON, lokalne
# JSON, webserver cez urllib
# Cloud - DATABAZA