# MOHIRDEV LESSONS
# lESSON 3 - VARIABLES

name= input("Enter your name")
surname= input("Enter your surname")
print(f"Hello, my name is {name}. \nMy surname is {surname}")

fruit="   apple    "
print("I like " + fruit.strip() + " because it is very useful")

name= 'husnora'
print(name.upper())
name= 'HUSNORA is very gorgeous girl for me'
print(name.lower())
print(name.find('for'))
print(name.replace('gorgeous', 'clever'))

name=input("What's your name? ")
print("hello, ", name.title())

# NUMBERS IN PYTHON
number=int(input('enter the number'))
print(f"{number**2} square of {number}" )
print(f"{number**3} cube of {number}")

age=int(input("How old are you? "))
year= 2024-age
print(f"You were born in {year}.")
year=int(input("When were you born? "))
age= 2024-year
print(f"You are {age} years old .")

number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number:"))
print(number1+ number2)
print(number1 * number2)
print(number1-number2)
print(number1//number2)

# lesson 7 LIST

fruits=['apple', 'grape', 'pomegranate', 'orange']
print(fruits)
print(fruits[2])
fruits[0]='apricot'
print(fruits)
fruits[-1]='peach'
print(fruits)

foods_vegs=['carrot', 'tomato', 'potato', 'cabbage']
foods_vegs.append('cucumber')
print(foods_vegs)
foods_vegs.insert(0, 'garlic')
print(foods_vegs)
del foods_vegs[0]
print(foods_vegs)
foods_vegs.remove("tomato")
print(foods_vegs)

shopping=['flour', 'meat', 'onion', 'garlic', 'carrot', 'pea']
product=shopping.pop(3)
print(product)
print(shopping)
print('I bought a  ' + product)
print("Don't bought yet:", shopping)

fruits=['pear', 'peach', 'grapes', 'apple', 'banana', 'kiwi']
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
print(sorted(fruits))
fruits.reverse()
print(fruits)

numbers=list(range(0,16))
print(numbers)
print(len(numbers))

odd_numbers=list(range(1, 20, 2))
print(odd_numbers)
even_numbers=list(range(0, 20, 2))
print(even_numbers)

prices=[25789, 9087, 564300, 56000, 54321, 76530]
print(max(prices))
print(min(prices))
print(sum(prices))