pytanie="Django grirls jest fajne? "
czy_prawda = (4 == 3*2)
print(pytanie)
if czy_prawda:	
	print('Jasne, ze jest! ;)')
else:
	print('No niezbyt ;(') 

def welocome_on_django(name):
	print('Hi ' + name + '!')
	print('Welcome on Django Girls!')

django_girls_list = {"Magda", "Kasia", "Ania", "Zuzia"}

for name in django_girls_list:
	welocome_on_django(name)

for i in range(1,50):
	print("Current value stored in i equals" + str(i) )