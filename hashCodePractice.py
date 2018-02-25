from enum import Enum

class Ingredient(Enum):
    Empty = 0
    Tomato = 1
    Mushroom = 2

class Pizza:
    def __init__(self, f):
        rows, cols, self.min_ings, self.max_cells = map(
            lambda x: int(x), f.readline().split(' ')
        )
        
        self.layout = [
            [Ingredient.Empty for _ in range(cols)] 
            for _ in range(rows)
        ]
        
        for i, line in enumerate(f):
            for j, ingredient in enumerate(line):
                if "T" in ingredient:
                    self.layout[i][j] = Ingredient.Tomato
                elif "M" in ingredient:
                    self.layout[i][j] = Ingredient.Mushroom
            
        self.slices = []
                        
    def __repr__(self):
        return str(self.layout)
        
    def slice(self, topLeft, bottomRight):
        self.slices.append(Pizza.Slice(topLeft, bottomRight))
        
    def output(self, f):
        f.write("{:d}\n".format(len(self.slices)))
        for slice in self.slices:
            f.write(str(slice) + "\n")
            
    
    class Slice:
        def __init__(self, topLeft, bottomRight):
            self.topLeft = topLeft
            self.bottomRight = bottomRight
            
        def __repr__(self):
            return "{:d} {:d} {:d} {:d}".format(
                self.topLeft[0], self.topLeft[1], 
                self.bottomRight[0], self.bottomRight[1]
            )
            

def main():
    i_f = open('input/example.in', 'r')
    pizza = Pizza(i_f)
    i_f.close()
    
    # Insert logic to slice up pizza here:
    #pizza.slice((0,0), (2,2))
    
    outname = i_f.name.replace("input/", "").replace(".in", "")
    o_f = open('output/'+outname+'.out', 'w')
    pizza.output(o_f)
    
main()
