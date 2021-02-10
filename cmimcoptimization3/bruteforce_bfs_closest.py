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

#print(entrance)

dirs = {"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1]}

total = ""
next_path = ""

for _ in range(n):
  print(_)
  # move all the robots first
  for move in next_path:
    d = dirs[move]
    to_remove = []
    for i in range(len(robots)):
      rob = robots[i]
      # print("rob is",rob)
      # if rob[0] == entrance[0][0] and rob[1] == entrance[0][1]:
      #   # made it to the entrance
      #   continue
      
      new = [rob[0] + d[0],rob[1] + d[1]]
      try:
        if maze[new[0]][new[1]] == "X":
          # print("hit a wall")
          # it's a wall
          continue
      except:
        # it's out of bounds
        # print("tried to go out of bounds")
        continue
      if new[0] < 0 or new[1] < 0:
        continue
      robots[i] = [new[0],new[1]]
      if new[0] == entrance[0][0] and new[1] == entrance[0][1]:
        # made it to the entrance
        # remove it?
        to_remove.append(i)
        print(i,"made it to the entrance")
        continue
      #print(robots)
    for i in range(len(to_remove) - 1, -1, -1):
      #print(to_remove[i], "is being removed now")
      del robots[to_remove[i]]
  #print(robots)
  # find the one with the shortest path
  actual_shortest = "init"
  for i in range(len(robots)):
    x = robots[i]

    #BFS lmao
    q = []
    visited = [[False for i in range(c)] for j in range(r)]
    shortestpath = [["" for i in range(c)] for j in range(r)]

    #print("trying",x)
    visited[x[0]][x[1]] = True
    shortestpath[x[0]][x[1]] = ""
    q.append(x)
    while len(q) != 0:
      s = q[0]
      q.pop(0)
      # process node s
      # print(s)
      if maze[s[0]][s[1]] == "E":
        # print("exit reached")
        # print(shortestpath[s[0]][s[1]])
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
    if actual_shortest == "init":
      actual_shortest = shortestpath[s[0]][s[1]]
    if len(shortestpath[s[0]][s[1]]) < len(actual_shortest):
      #print(x, "is closer")
      actual_shortest = shortestpath[s[0]][s[1]]
  if actual_shortest == "init":
    #we're done?
    break
  next_path = actual_shortest
  total += actual_shortest

    
print(total)
print(len(total))

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
