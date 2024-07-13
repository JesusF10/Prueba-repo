
content = []

with open('hola.txt') as file:
    for line in file:
        content.append(line.rstrip())

for con in content:
    print(con)
    
