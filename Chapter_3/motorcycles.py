#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#motorcycles[0] = 'ducati'
#print(motorcycles)

#motorcycles.append('ducati')
#print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

last_motorcycle = motorcycles.pop()
print(motorcycles)
print(f"The last motorcycle I owned was a {last_motorcycle.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(3, 'ducati')
print(motorcycles)

too_expensive ='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")