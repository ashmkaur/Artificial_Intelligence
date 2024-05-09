# iterative deepning

import copy

q = []
visited = []

def generate(s):
    t = s[0]
    length = s[1]
    children = []
    for i in range(len(t)):
        temp = copy.deepcopy(t)
        if temp[i]:  # Check if the stack is not empty
            ele = temp[i].pop()
            for j in range(len(temp)):
                if j != i:
                    temp1 = copy.deepcopy(temp)
                    temp1[j] = temp1[j] + [ele]
                    if temp1 not in visited:
                        children.append((temp1, length + 1))
    return children

def dfs(s, g, depth_limit):
    global q
    global visited

    if s[0] == g:
        return True

    depth = s[1]
    if depth > depth_limit:
        return False
    visited+=[s]
    children = generate(s)
    for child in children:
        if dfs(child, g, depth_limit):
            return True

    return False

def iterative_deepening_dfs(s, g):
    depth_limit = 0
    while True:
        result = dfs(s, g, depth_limit)
        if result:
            print("depth:",depth_limit)
            return True
        else:
            depth_limit += 1

def main():
    global visited
    global q

    n = 3
    initial = [['A'], ['B', 'C'], []]
    final = [['A','C'], ['B'], []]
    visited=[]

    # Perform Iterative Deepening DFS
    result = iterative_deepening_dfs((initial, 0), final)
    if result:
        print("Found!")
        print("total sol:", len(visited))
        print(final)
    else:
        print("No solution")

if __name__ == '__main__':
    main()