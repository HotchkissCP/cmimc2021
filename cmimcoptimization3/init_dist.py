# from ast import literal_eval
# edit to the name of the input file
task = "3"

f = open('robotrecovery' + task + '.txt', 'r')
# change this function however you want: it takes in a character representing a cell 
# of the maze and x/y coordinates and returns whatever representation you want
def rep(c,x,y):
    if c == '.':
        return c
    elif c == 'X':
        return c
    elif c == 'R':
        robots.append([y,x]) # this needed to be flipped wtf cmimc
        return c
    elif c == 'E':
        entrance.append([y,x]) # same here
        return c
# you shouldn't need to edit lines 18-25
r,c,n = map(int, f.readline().strip().split())
robots = []
entrance = []
maze = []
instructions = []
for y in range(r):
    s = f.readline().strip()
    maze.append([rep(s[x],x,y) for x in range(c)])

# replace from here to line 30 with your own logic

# print(entrance)
# quit()

rev = {"U":"D","D":"U","L":"R","R":"L"}
dirs = {"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1]}

# switch the direction of a path
def reverse(s):
  new_s = ""
  for char in s:
    new_s = rev[char] + new_s
  return new_s

# get all possible paths of length n
def get_all_paths(n):
  if n == 0:
    return [""]
  else:
    prev = get_all_paths(n - 1)
    new = []
    for i in prev:
      for d in dirs:
        new.append(i + d)
    return new

# find the shortest path from every point to the entrance
# BFS lmao
q = []
visited = [[False for i in range(c)] for j in range(r)]
shortestpath = [["" for i in range(c)] for j in range(r)]
x = entrance[0]

visited[x[0]][x[1]] = True
shortestpath[x[0]][x[1]] = ""
reached = 0
walls = 0
q.append(x)
while len(q) != 0:
  s = q[0]
  q.pop(0)
  # process node s
  # print(s)
  for key in dirs:
    d = dirs[key]
    new = [s[0] + d[0],s[1] + d[1]]
    #print(new)
    #print(d)
    
    if new[0] < 0 or new[1] < 0 or new[0]>=r or new[1]>=c:
      # out of bounds
      continue
    if visited[new[0]][new[1]]: 
      continue
    # is it a wall?
    visited[new[0]][new[1]] = True
    if maze[new[0]][new[1]] == "X":
      #print("hit a wall")
      walls += 1
      continue
    #print("appended")
    shortestpath[new[0]][new[1]] = shortestpath[s[0]][s[1]] + key
    q.append(new)
    reached += 1

for rob in robots:
  print(len(shortestpath[rob[0]][rob[1]]))