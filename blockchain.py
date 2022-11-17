import hmac
import pickle

block = [{'account1': 57634564765, 'account2': 654836594, 'amount': 674.50},
         {'account1': 57634564765, 'account2': 654836594, 'amount': 674.50},
         {'account1': 57634564765, 'account2': 654836594, 'amount': 674.50}]

key = bytes('542354387254573', encoding='utf8')

block_prepared = pickle.dumps(block)
print(block_prepared)
block_bytes = bytes(block_prepared)
print(block_bytes)

obj = hmac.new(key=key, msg=block_bytes, digestmod='md5')

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
