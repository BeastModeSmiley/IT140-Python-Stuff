import datetime

name = input('What is your name?')
age = int(input('How old are you?'))
x = datetime.datetime.now()
year = x.year - age
final = str(year)
print('Hello ' + name + '! You were born in ' + final + '.')
