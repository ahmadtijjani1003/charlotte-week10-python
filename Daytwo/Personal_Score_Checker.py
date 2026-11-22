
name = input('Enter your name: ')

score = int(input('Enter your score: '))

if score < 0 or score > 100:
    print('Invalid score')

else:
    remaining = 100 - score
    passed = score >= 50
    result = 'Pass' if passed else 'Try again'

    print('Hello', name)
    print('Your score is', score)
    print('Marks to reach 100:', remaining)
    print('Passed:', passed)
    print('Result:', result)

#membership operators.
Foods = ['Mandi rice & Chicken',
         'Jollof Rice & Plantain',
         'Pasta, stew & smoked Fish',
         'Beans Porridge',
         'Chips & Ketchup']

print('rice' in Foods)
print('pizza' not in Foods)

#Tenary operator
Temperature = 30
Status = 'Hot' if Temperature >= 25 else 'Cool'
print(Status)

#Bitwise operators
#The binary representation of 6 is 110
#The binary representation of 3 is 011
6&3
#Then the & operator compares the bits and returns 0010, which is 2 in decimal.
6 | 3 
#The binary representation of 6 is 110
#The binary representation of 3 is 011
#Then the | operator compares the bits and returns 0111, which is 7 in decimal.
6 ^ 3 
#The binary representation of 6 is 110
#The binary representation of 3 is 011
#Then the ^ operator compares the bits and returns 0101, which is 5 in decimal.
6 << 1
#The binary representation of 6 is 110
#The binary representation of 1 is 000
#By adding the 0 to right.
#The the << operator compares the bits and return 1100
6 >> 1 
#The binary representation of 6 is 110
#By removing the bit (0) from its. 110
#The the >> operator compares the bits and return 11.

print(6&3)
print(6|3)
print(6^3)
print(6<<1)
print(6>>1)

#identity operator
first = [10, 20]
second = first
third = [10, 20]
print (first is second)
print (first is not second)
print (first is third)
print (first is not third)
print (first == third)

#logical operators
##logical and
Age = 19
has_ticket = True
print (Age >= 18 and has_ticket)

# logical or
day = 'Saturday'
if day == 'Saturday' or day == 'Sunday':
    print (True)

#logical not
is_raining = False
print (not is_raining)

#assignment operators
Points=20
Points +=5
Points -=3
Points *=2
print (Points)

#comparison operators
score = 65
print(score > 50)
print(score < 50)
print(score == 65)
print(score != 65)

#arithmetic operators
print(24 - 6)
print(24 + 6)
print(24 * 6)
print(24 / 6)
print(25 // 4)
print(25 % 4)
print(3 ** 2)