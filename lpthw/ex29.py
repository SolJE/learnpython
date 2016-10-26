people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")
	
if people > cats:
    print("Not many cats! The world is saved!")
	
if people < dogs:
    print("The world is drooled on!")
	
if people > dogs:
    print("The world is dry!")
	
dogs +=5 #是 dogs = dogs + 5的缩写

if people >= dogs: # True
    print("People are greater than or equal to dogs.")
	
if people <= dogs: # True
    print("People are less than or equal to dogs.")
	
if people == dogs: # True
    print("People are dogs.")