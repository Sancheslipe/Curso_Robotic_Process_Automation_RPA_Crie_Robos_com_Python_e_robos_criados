#list comprehensions
array = [numero * 3 for numero in range(1,7+1)]
print(array)
#dict comprehensions
chaves = 'feliph'
valores = [0,1,2,3,4,5]
mist = {chaves[i]: valores[i] for i in range(0,6)}
print(mist)
#logica usando list comprehensions e if comprehensions
numeros = [i for i in range(1,6)]
res = {num:('par' if num % 2 == 0 else 'impar')for num in numeros}
print(res.values())