file = open("names.txt", "r")

data = file.read()

vyskyt1 = data.count("Lea")


file = open("names.txt", "r")

data = file.read()
vyskyt2 = data.count("Luke")


file = open("names.txt", "r")
data = file.read()
vyskyt3 = data.count("Darth")

print('Výskyt jména Lea', vyskyt1)

print('Výskyt jména Luke', vyskyt2)

print('Výskyt jména Darth', vyskyt3)