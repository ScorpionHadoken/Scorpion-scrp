import sys
from collections import deque

filename = sys.argv[1]
file = open(filename, "r")
contents = file.read()


hold_msg = "Press Eneter to exit this program..."
i = 0

q = deque()

while i < len(contents):
    if (contents[i] == "/"):
        j = i
        while (contents[j] != "\_"):
            j += 1
        q.appendleft(contents[i+1:j])
        i = j
        
    elif (contents[i] == "..."):
        input(hold_msg)
        
    elif (contents[i] == ","):
        print(q[0])
    i+=1
