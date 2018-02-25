from enum import Enum

class Ingredient(Enum):
    Empty = 0
    Tomato = 1
    Mushroom = 2

def main():
    f = open('input/example.in', 'r')
    text = f.readline()
    rows, cols, min, max = map(lambda x: int(x), text.split(' '))
    
    pizza = [[Ingredient.Empty for _ in range(cols)] for _ in range(rows)]
    
    for i, line in enumerate(f):
        for j, ingredient in enumerate(line):
            if "T" in ingredient:
                pizza[i][j] = Ingredient.Tomato
            elif "M" in ingredient:
                pizza[i][j] = Ingredient.Mushroom
    
    f.close()
    
main()
