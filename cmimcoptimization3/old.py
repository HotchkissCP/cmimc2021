# from ast import literal_eval
# edit to the name of the input file
task = "5"

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

dirs = {"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1]}

#print(robots)

total = ""

for rob in robots:
  x = rob
  # move the robot first
  # print(total)
  for i in total:
    d = dirs[i]
    new = [x[0] + d[0],x[1] + d[1]]
    try:
      if maze[new[0]][new[1]] == "X":
        # print("hit a wall")
        # it's a wall
        continue
    except:
      # it's out of bounds FIXME: actually check for this because negative values work in python
      # print("tried to go out of bounds")
      continue
    if new[0] < 0 or new[1] < 0:
      continue
    x = [new[0],new[1]]

  #BFS lmao
  q = []
  visited = [[False for i in range(c)] for j in range(r)]
  shortestpath = [["" for i in range(c)] for j in range(r)]

  print(x)
  visited[x[0]][x[1]] = True
  shortestpath[x[0]][x[1]] = ""
  q.append(x)
  while len(q) != 0:
    s = q[0]
    q.pop(0)
    # process node s
    # print(s)
    if maze[s[0]][s[1]] == "E":
      print("exit reached")
      # print(shortestpath[s[0]][s[1]])
      total += shortestpath[s[0]][s[1]]
      break
    for key in dirs:
      d = dirs[key]
      new = [s[0] + d[0],s[1] + d[1]]
      #print(new)
      #print(d)
      try: 
        if visited[new[0]][new[1]]: 
          continue
        # is it a wall?
        visited[new[0]][new[1]] = True
        if maze[new[0]][new[1]] == "X":
          #print("hit a wall")
          continue
        if new[0] < 0 or new[1] < 0:
          # out of bounds
          continue
        #print("appended")
        shortestpath[new[0]][new[1]] = shortestpath[s[0]][s[1]] + key
        q.append(new)
      except:
        # out of bounds
        pass

    
print(total)

# test it out
# for move in total:
#   d = dirs[move]
#   for i in range(len(robots)):
#     rob = robots[i]
#     if maze[rob[0]][rob[1]] == "E":
#       continue
#     new = [rob[0] + d[0],rob[1] + d[1]]
#     try:
#       if maze[new[0]][new[1]] == "X":
#         # print("hit a wall")
#         # it's a wall
#         continue
#     except:
#       # it's out of bounds
#       # print("tried to go out of bounds")
#       continue
#     robots[i] = [new[0],new[1]]
#     print(robots)

# for i in robots:
#   print(i)


# for row in maze:
#   s = ""
#   for point in row:
#     s += point
#   print(s)

# instructions = ["R", "U"]

# change to whatever you want your output file to be called
out = open('output' + task + '.txt', 'w')
out.write(total)
# for i in instructions:
#     out.write(i)
out.close()