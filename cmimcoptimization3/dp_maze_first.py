# from ast import literal_eval
# edit to the name of the input file
task = "6"

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
    
    

# # print(visited[197][151])
# print("spaces",reached,"walls",walls,"total", reached + walls,"out of", c * r)
# for i in range(r):
#   for j in range(c):
#     if (not visited[i][j]) and maze[i][j] != "X":
#       print(i,j)
#       for key in dirs:
#         d = dirs[key]
#         try:
#           print("umm", i + d[0], j + d[1])
#           print(shortestpath[i + d[0]][j + d[1]])
#         except:
#           pass
# quit()

total = ""
next_path = ""

for _ in range(n):
  print("turn",_)
  # move all the robots first
  for move in next_path:
    d = dirs[move]
    to_remove = []
    for i in range(len(robots)):
      rob = robots[i]
      # print("rob is",rob)
      # don't need this below
      # if rob[0] == entrance[0][0] and rob[1] == entrance[0][1]: 
      #   # made it to the entrance
      #   continue
      
      new = [rob[0] + d[0],rob[1] + d[1]]
      if new[0] < 0 or new[1] < 0 or new[0]>=r or new[1]>=c:
        # out of bounds
        # print("tried to go out of bounds")
        continue
      if maze[new[0]][new[1]] == "X":
        # print("hit a wall")
        # it's a wall
        continue
      robots[i] = [new[0],new[1]]
      if new[0] == entrance[0][0] and new[1] == entrance[0][1]:
        # made it to the entrance
        # remove it?
        to_remove.append(i)
        print(i,"made it to the entrance")
        continue
    
    for i in range(len(to_remove) - 1, -1, -1):
      print(to_remove[i], "is being removed now")
      del robots[to_remove[i]]
  #print(robots)

  # find the one with the shortest path / or the longest path?
  # actual_longest = ""
  # for i in range(len(robots)):
  #   x = robots[i]
  #   path = reverse(shortestpath[x[0]][x[1]])
  #   #print(path)
  #   if len(path) > len(actual_longest):
  #     #print(x, "is closer")
  #     actual_longest = path
  #   if path == "":
  #     print("bruh",x,maze[x[0]][x[1]])
  # if actual_longest == "":
  #   #we're done?
  #   break
  # next_path = actual_longest
  # total += actual_longest

  actual_shortest = "init"
  for i in range(len(robots)):
    x = robots[i]
    path = reverse(shortestpath[x[0]][x[1]])
    #print(path)
    if actual_shortest == "init":
      actual_shortest = path
    if len(path) < len(actual_shortest):
      #print(x, "is closer")
      actual_shortest = path
    if path == "":
      print("bruh",x,maze[x[0]][x[1]])
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

# change to whatever you want your output file to be called
out = open('output' + task + '.txt', 'w')
out.write(total)
# for i in instructions:
#     out.write(i)
out.close()