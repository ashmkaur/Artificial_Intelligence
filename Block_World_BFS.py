# BFS

import sys
import copy


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
          if temp1  not in visited and temp1 not in temp_q:
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
    return

  while q:
    curr = q.pop(0)
    children = generate(curr)
    print(curr)
    print("-------------")
    if curr[0] == g:
      print(g)
      print("Total sol:", curr[1])
      print("Total", len(visited))
      return
    else:
      q.extend(children)  # Extend the queue with children states
      for child in children:
        visited = visited + child[0]  # Mark children states as visited


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
  search((initial, 0), final)


if __name__ == '__main__':
  main()