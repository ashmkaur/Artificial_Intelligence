# DFS

import sys
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
        if temp[i]:
            elem = temp[i].pop()
            for j in range(len(temp)):
                if j != i:
                    temp1 = copy.deepcopy(temp)
                    temp1[j] = temp1[j] + [elem]
                    if temp1 not in visited and temp1 not in temp_q:
                        temp_q.append(temp1)
                        children.append((temp1, length + 1))
    return children

def search(s, g):
    global q
    global visited
    global temp_q

    if s[0] == g:
        print(g)
        print("Total sol:", s[1])
        print("no of states:", len(visited))

    curr = copy.deepcopy(s)
    while True:
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

def main():
    global visited
    n = 3
    initial = [['A'], ['B', 'C'], []]
    final = [['A', 'B', 'C'], [], []]
    visited = visited + [initial]
    search((initial,0), final)

if __name__ == '_main_':
    main()