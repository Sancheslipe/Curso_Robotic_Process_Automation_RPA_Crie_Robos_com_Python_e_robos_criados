import random
array = []
for l in range(0,10):
    rand = random.randint(0,2000)
    array.append(rand)

result = {num:('par' if num % 2 == 0 else 'impar') for num in array}
print(f'este é o array {array}')
print(result.values())