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

