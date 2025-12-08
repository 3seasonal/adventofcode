## notes for day 




parse into a 2d list "map"





classes:
- parse

- process
    - 
process initialised on a map
case zero function: 
Looks for S in start row of map
calls tacheon function on second row where the S (or ses) will go

tracks:
no 


tacheon (row, col)
 function checks what the proposed cell is and based on that marks the recurses to the where the tacheon beam should go next
    excape: when last row is reached, when a tacheon beam is alreandy discovered in map
 checks for splitter or tacheon beam
 updates map with tacheon beam (if approarite eg not a splitter)
 update count
 calls next 
 

print function:
pretty prints the output


IN ORDER TREE TRAVERSAL:
from node:


traversals = start_traverse( 0 )

def start_traverse( row ):
    for col in range(len(self.map[row])):
        # expect only one
        if self.map[row][col] == "S":
            return traverse (row+2, col, 0)


def traverse(row, col, count):
    # exit cases
    if (row > len(self.map)):
        return 0
    if (col >= len(self.map[0])):
        return 0

    # complete traversal
    if (col == len(self.map)):
        return count +1 

    tree_char = self.map[row][col]

    # if there is no splitter:
    if tree_char == "|"
        return traverse(row+2, col, count)

    # if there is a splitter:
    if tree_char == "^":
        return traverse(row+2, col-1, count) # left branch
        return traverse(row+2, col+1, count) # right branch

 
    




# traverse left
traverse()

# traverse right