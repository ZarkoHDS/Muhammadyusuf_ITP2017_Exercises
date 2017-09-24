things='bottle'
print("\nis things == 'bottle'? i predict true")
print(things == 'bottle')
print("\nis things == 'box'? i predict true")
print(things == 'box')

car='BMW'
print(car == 'BMW')
print(car != 'ferrari')

print(car.lower()== 'bmw' )

age='15'
print(age == '15')
print(age <= '20')
print(age >= '19')
print(age != '20')

for i in range(0,5):
    if i %2 == 0 and i %3 != 0:
        print(i)
    if i %2 == 0 or i %2 != 0:
        print(i)

favorite_fruit=input("choose your fruits :")
if 'banana' in favorite_fruit:
    print("You really like bananas")

