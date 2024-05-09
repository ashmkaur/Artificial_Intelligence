# depth limited search

import copy

q = []
visited = []
temp_q = []

def generate(t):
    s = t[0]
    length = t[1]
    children = []
    for i in range(len(s)):
        temp = copy.deepcopy(s)
        if temp[i]:  # Check if the stack is not empty
            elem = temp[i].pop()
            for j in range(len(temp)):
                if j != i:
                    temp1 = copy.deepcopy(temp)
                    temp1[j] = temp1[j] + [elem]
                    if temp1 not in visited and temp1 not in temp_q:
                        temp_q.append(temp1)
                        children.append((temp1, length + 1))
    return children

def search(s, g, depth_limit):
    global q
    global visited
    global temp_q

    if s[0] == g:
        print(g)
        print("Total sol:", s[1])
        print("no of states:", len(visited))
        return
    curr=copy.deepcopy(s)
    
    while True:
        depth= curr[1]
        if depth <= depth_limit:
            children = generate(curr)
            print(curr)
            print("-------------")
            if curr[0] == g:
                print(g)
                print("Total sol:", curr[1])
                print("Total", len(visited))
                return
            else:
                q += children
                if len(q) == 0:
                    print("No solution")
                    return
                else:
                    curr = q[len(q)-1]
                    visited.append(curr)
                    del q[len(q)-1]


        else:
            print("Depth limit reached. Aborting further exploration.")
            return

    # If the while loop completes without finding the goal state
    print("No solution found within the depth limit.")

def main():
    global visited
    global q
    global temp_q

    n = 3
    initial = [['A'], ['B', 'C'], []]
    final = [['A', 'B', 'C'], [], []]
    visited = []
    temp_q = []
    visited = visited + [initial]
    q = [(initial, 0)]  # Initialize queue with initial state

    # Set the depth limit
    depth_limit = 17

    # Perform Depth-Limited Search (DLS) with the given depth limit
    search((initial, 0), final, depth_limit)

if __name__ == '__main__':
    main()