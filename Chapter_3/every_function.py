from random import random


random_knowledge = []
random_knowledge.append('jack')
random_knowledge.insert(0,'death')
random_knowledge.append('may')
random_knowledge.append('hilda')
random_knowledge.append('ash')
print(random_knowledge)
print(sorted(random_knowledge))

random_knowledge.reverse()
print(random_knowledge)

random_knowledge.sort()
print(random_knowledge)

random_knowledge.sort(reverse = True)
print(random_knowledge)

random_knowledge.remove('death')

random_knowledge.pop()

del random_knowledge[2]

print(random_knowledge)
print(len(random_knowledge))